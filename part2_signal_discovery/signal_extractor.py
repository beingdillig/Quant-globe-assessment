from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, START, END
from collections import defaultdict
from openai import AzureOpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
azure_endpoint = os.getenv("OPENAI_API_BASE")
deployment_name = os.getenv("OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("OPENAI_API_VERSION")

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
    azure_deployment=deployment_name
)

class AgentState(TypedDict):
  trades: List[Dict[str, Any]]
  strategy_map: Dict[str,List[Dict[str,Any]]]
  trade_pnl: Dict[str,float]
  response: str


with open("trade_book.json", "r") as f:
    trades_data = json.load(f)

def group_by_strategy(state:AgentState) -> AgentState:
  print("Grouping By Strategy.....")
  trades = state['trades']

  strategy_map = defaultdict(list)
  for trade in trades:
    strategy_map[trade['strategy']].append(trade)

  state['strategy_map'] = strategy_map
  print("Grouping Completed!!")
  return state

def calculate_pnl(state:AgentState) -> AgentState:
  print("Calculating PNL of Trades....")
  strategy_map = state['strategy_map']
  trade_pnl = {}

  for strategy, trades in strategy_map.items():
    for trade in trades:
      if trade['type'] == 'SELL':
        pnl = (trade['entry_price'] - trade['exit_price']) * trade['quantity']
      else:
        pnl = (trade['exit_price'] - trade['entry_price']) * trade['quantity']
      trade_pnl[trade['trade_id']] = pnl

  state['trade_pnl'] = trade_pnl
  print("PNL Calculated!!")
  return state

def summarizer(state:AgentState) -> AgentState:
  print("Summarizing Output And Getting Insights....")
  strategy_map = state['strategy_map']
  trade_pnl = state['trade_pnl']

  messages = [
        {"role": "system", "content": f"""
        You are an F&O Expert. You have been provided the trade data grouped by strategy
        and PnL per trade: \n\nStrategy Map: {strategy_map}\n\nPnL Map: {trade_pnl}\n
        Analyze this and summarize signals, risks, and performance.
        """},
        {"role": "user", "content": "Analyze the given data and summarize signals, risks and performance."}
    ]

  completion = client.chat.completions.create(
      model="gpt4-o",
      messages=messages,
  )

  response = completion.choices[0].message.content
  state['response'] = response
  print(response)
  return state


def output(state:AgentState) -> AgentState:
    output_data = {
        "strategy_map": state["strategy_map"],
        "trade_pnl": state["trade_pnl"],
        "summary": state["response"]
    }

    with open("output.json", "w") as f:
        json.dump(output_data, f, indent=2)

    print("✅ Output saved to output.json")
    return state

graph = StateGraph(AgentState)

graph.add_node('group_by_strategy', group_by_strategy)
graph.add_node('calculate_pnl', calculate_pnl)
graph.add_node('summarizer', summarizer)
graph.add_node('output',output)

graph.add_edge(START, 'group_by_strategy')
graph.add_edge('group_by_strategy', 'calculate_pnl')
graph.add_edge('calculate_pnl', 'summarizer')
graph.add_edge('summarizer', 'output')
graph.add_edge('output',END)

app = graph.compile()


#----------------------------------------Running The Graph (Agent)---------------------------------------
initial_state = trades_data

result = app.invoke(initial_state)
