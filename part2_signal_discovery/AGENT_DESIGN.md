## 📊 AGENT.md – Signal Extractor Agent

### 🎯 Purpose

This agent analyzes a list of F&O trades, groups them by strategy, calculates PnL per trade, and uses an LLM to summarize signals, risks, and performance in natural language.

### 🔁 Agent Workflow

#### ✅ Input

A list of trade dictionaries with keys like strategy, symbol, type, entry_price, exit_price, etc.

#### 🧠 Step-by-Step Flow

1. Group by Strategy (group_by_strategy)
   Groups all trades under their respective strategies.

Stores a mapping like:

```
{
  "Straddle": [trade1, trade2],
  "Momentum": [trade3],
  ...
}
```

#### ➡️ Output: strategy_map added to agent state.

2. Compute PnL (calculate_pnl)
   For each trade in each strategy:

```
if type == SELL:
PnL = (entry_price - exit_price) * quantity

else:
PnL = (exit_price - entry_price) * quantity
```

#### ➡️ Output: trade_pnl dictionary added to state with trade_id as key and PnL as value.

3. Generate LLM Summary (summarizer)

   Sends both strategy_map and trade_pnl to an LLM.

Prompts the model to analyze risks, strategies, and performance.

#### ➡️ Output: A detailed natural language summary stored in response.

```
📤 Output

✅ response (text summary from LLM)

✅ strategy_map (grouped trades)

✅ trade_pnl (calculated PnLs)

-----------------------------------------------

📦 Example Output
{
  "strategy_map": {
    "Straddle": [...],
    "Momentum": [...],
    ...
  },
  "trade_pnl": {
    "T001": -2020.0,
    "T002": -1550.0,
    ...
  },
  "response": "The Straddle strategy resulted in consistent small losses... Momentum performed well..."
}
```

### 🛠️ Built With

- LangGraph

- OpenAI-compatible LLM (via A4F)

- Python 3.8+
