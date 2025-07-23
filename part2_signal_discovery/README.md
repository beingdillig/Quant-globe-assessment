# Signal Discovery Agent 🧠📈

## Overview

This LangGraph-powered agent analyzes structured trade data, groups it by trading strategy, computes P&L, and uses GPT-4.1 to summarize signals, risks, and performance insights.

---

## 🛠️ Files

- `signal_extractor.py` — Main agent pipeline using LangGraph
- `agent.md` — Design and flow documentation
- `output.json` — Final insights generated from trade data
- `requirements.txt` — Python dependencies
- `research.md` — Tool comparison and model justification

---

## 🔁 Agent Workflow

1. **Input**: List of executed trades
2. **Step 1**: Group trades by strategy
3. **Step 2**: Compute PnL for each trade
4. **Step 3**: GPT-4.1 summarizes performance
5. **Output**: JSON file with full strategy mapping, PnL, and insights

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
```

#### Update your OpenAI API key in signal_extractor.py.
And You are ready to execute the agent, Output will be saved in output.json .

## Sample Output
```
{
  "strategy_map": {
    "Straddle": [
      {
        "trade_id": "T001",
        "strategy": "Straddle",
        "symbol": "NIFTY",
        "type": "SELL",
        "instrument": "CE",
        "strike_price": 19500,
        "expiry": "2024-07-25",
        "quantity": 100,
        "entry_price": 120.5,
        "exit_price": 100.2,
        "timestamp": "2024-07-18T09:30:00Z"
      },
      {
        "trade_id": "T002",
        "strategy": "Straddle",
        "symbol": "NIFTY",
        "type": "SELL",
        "instrument": "PE",
        "strike_price": 19500,
        "expiry": "2024-07-25",
        "quantity": 100,
        "entry_price": 110.5,
        "exit_price": 95.0,
        "timestamp": "2024-07-18T09:35:00Z"
      },
      {
        "trade_id": "T011",
        "strategy": "Straddle",
        "symbol": "BANKNIFTY",
        "type": "SELL",
        "instrument": "CE",
        "strike_price": 49000,
        "expiry": "2024-07-25",
        "quantity": 100,
        "entry_price": 110,
        "exit_price": 95,
        "timestamp": "2024-07-18T12:15:00Z"
      },
      {
        "trade_id": "T012",
        "strategy": "Straddle",
        "symbol": "BANKNIFTY",
        "type": "SELL",
        "instrument": "PE",
        "strike_price": 49000,
        "expiry": "2024-07-25",
        "quantity": 100,
        "entry_price": 105,
        "exit_price": 88,
        "timestamp": "2024-07-18T12:20:00Z"
      }
    ],
    "Momentum": [
      {
        "trade_id": "T003",
        "strategy": "Momentum",
        "symbol": "BANKNIFTY",
        "type": "BUY",
        "instrument": "FUT",
        "strike_price": null,
        "expiry": "2024-07-25",
        "quantity": 25,
        "entry_price": 49000,
        "exit_price": 49300,
        "timestamp": "2024-07-18T10:00:00Z"
      },
      {
        "trade_id": "T008",
        "strategy": "Momentum",
        "symbol": "TCS",
        "type": "BUY",
        "instrument": "FUT",
        "strike_price": null,
        "expiry": "2024-07-25",
        "quantity": 30,
        "entry_price": 3650,
        "exit_price": 3680,
        "timestamp": "2024-07-18T11:45:00Z"
      }
    ],
    "Mean Reversion": [
      {
        "trade_id": "T004",
        "strategy": "Mean Reversion",
        "symbol": "RELIANCE",
        "type": "SELL",
        "instrument": "FUT",
        "strike_price": null,
        "expiry": "2024-07-25",
        "quantity": 50,
        "entry_price": 2800,
        "exit_price": 2825,
        "timestamp": "2024-07-18T11:00:00Z"
      },
      {
        "trade_id": "T013",
        "strategy": "Mean Reversion",
        "symbol": "SBIN",
        "type": "BUY",
        "instrument": "FUT",
        "strike_price": null,
        "expiry": "2024-07-25",
        "quantity": 80,
        "entry_price": 580,
        "exit_price": 590,
        "timestamp": "2024-07-18T12:30:00Z"
      }
    ],
    "Breakout": [
      {
        "trade_id": "T005",
        "strategy": "Breakout",
        "symbol": "INFY",
        "type": "BUY",
        "instrument": "FUT",
        "strike_price": null,
        "expiry": "2024-07-25",
        "quantity": 40,
        "entry_price": 1520,
        "exit_price": 1555,
        "timestamp": "2024-07-18T11:15:00Z"
      },
      {
        "trade_id": "T010",
        "strategy": "Breakout",
        "symbol": "NIFTY",
        "type": "BUY",
        "instrument": "CE",
        "strike_price": 19700,
        "expiry": "2024-07-25",
        "quantity": 75,
        "entry_price": 95,
        "exit_price": 120,
        "timestamp": "2024-07-18T12:10:00Z"
      }
    ],
    "Strangle": [
      {
        "trade_id": "T006",
        "strategy": "Strangle",
        "symbol": "BANKNIFTY",
        "type": "SELL",
        "instrument": "PE",
        "strike_price": 48200,
        "expiry": "2024-07-25",
        "quantity": 50,
        "entry_price": 125,
        "exit_price": 100,
        "timestamp": "2024-07-18T11:30:00Z"
      },
      {
        "trade_id": "T007",
        "strategy": "Strangle",
        "symbol": "BANKNIFTY",
        "type": "SELL",
        "instrument": "CE",
        "strike_price": 49500,
        "expiry": "2024-07-25",
        "quantity": 50,
        "entry_price": 135,
        "exit_price": 110,
        "timestamp": "2024-07-18T11:32:00Z"
      }
    ],
    "Reversal": [
      {
        "trade_id": "T009",
        "strategy": "Reversal",
        "symbol": "HDFCBANK",
        "type": "SELL",
        "instrument": "FUT",
        "strike_price": null,
        "expiry": "2024-07-25",
        "quantity": 60,
        "entry_price": 1620,
        "exit_price": 1605,
        "timestamp": "2024-07-18T12:00:00Z"
      },
      {
        "trade_id": "T014",
        "strategy": "Reversal",
        "symbol": "ITC",
        "type": "SELL",
        "instrument": "FUT",
        "strike_price": null,
        "expiry": "2024-07-25",
        "quantity": 150,
        "entry_price": 450,
        "exit_price": 440,
        "timestamp": "2024-07-18T12:45:00Z"
      }
    ]
  },
  "trade_pnl": {
    "T001": 2029.9999999999998,
    "T002": 1550.0,
    "T011": 1500,
    "T012": 1700,
    "T003": 7500,
    "T008": 900,
    "T004": -1250,
    "T013": 800,
    "T005": 1400,
    "T010": 1875,
    "T006": 1250,
    "T007": 1250,
    "T009": 900,
    "T014": 1500
  },
  "summary": "Certainly! Let's break down the analysis into clearly delineated sections: **performance**, **signals**, and **risks** based on the provided trade data and PnL.\n\n---\n\n### 1. **Performance Analysis by Strategy**\n\n#### **PnL by Strategy**\nLet's aggregate the PnL for each strategy:\n\n#### **Straddle**  \n- Trades: T001, T002, T011, T012  \n- Total PnL: 2029.99 (T001) + 1550.0 (T002) + 1500 (T011) + 1700 (T012) = **6779.99**\n\n#### **Momentum**  \n- Trades: T003, T008  \n- Total PnL: 7500 (T003) + 900 (T008) = **8400**\n\n#### **Mean Reversion**  \n- Trades: T004, T013  \n- Total PnL: -1250 (T004) + 800 (T013) = **-450**\n\n#### **Breakout**  \n- Trades: T005, T010  \n- Total PnL: 1400 (T005) + 1875 (T010) = **3275**\n\n#### **Strangle**  \n- Trades: T006, T007  \n- Total PnL: 1250 (T006) + 1250 (T007) = **2500**\n\n#### **Reversal**  \n- Trades: T009, T014  \n- Total PnL: 900 (T009) + 1500 (T014) = **2400**\n\n#### **Overall Performance**\n- **Net PnL (All trades):**  \n6779.99 + 8400 + (-450) + 3275 + 2500 + 2400 = **22,904.99**\n\n- **Profitable Strategies:**  \n  - Momentum (8400) was the best performer, followed by Straddle (6779.99), Breakout (3275), Strangle (2500), Reversal (2400).\n- **Losing Strategy:**  \n  - Mean Reversion (-450).\n\n---\n\n### 2. **Signals Observed**\n\n#### **Winning Signals**\n- **Momentum and Breakout Strategies:**\n    - Both generated consistently high profits, suggesting strong, tradable trends in the market.\n    - All trades under Momentum and Breakout were profitable.\n- **Straddle and Strangle (Option Selling):**\n    - Both index option-selling strategies (Straddle and Strangle) have positive PnL, indicating the market likely exhibited rangebound or low volatility behavior after trades were placed.\n- **Reversal:**\n    - Both reversal trades (short futures) were profitable, indicating well-timed entries against prevailing trends.\n\n#### **Losing/Weak Signals**\n- **Mean Reversion:**\n    - One trade (sell Reliance fut) was a significant loser (-1250), only partly offset by a modest winner (+800). This might indicate mean reversion was ineffective, possibly due to trending phase in underlying.\n\n#### **General Signal Insights:**\n- **Option Selling (Straddle, Strangle):** Favorable, likely due to time decay/expiry proximity.\n- **Directional Futures Trading:** Profitable when aligned with trending market (Momentum, Breakout, Reversal).\n- **Poor performance on contrarian plays (Mean Reversion).**\n\n---\n\n### 3. **Risks Identified**\n\n#### **Strategy Risk**\n- **Mean Reversion Risk:**\n    - Stands out as a net drag (-450), highlighting the potential pitfalls of contrarian strategies in trending markets.\n- **Concentration:** \n    - Momentum strategy\u2019s large profit is from one trade (T003: +7500) \u2014 high concentration risk.\n\n#### **Instrument-specific/Market Risk**\n- **Index Option Selling (Straddle, Strangle):**\n    - Works well in rangebound/low volatility. However, these are subject to sharp losses during sudden breakout moves. The current data shows only profit; future positions may incur large, sudden drawdowns.\n- **Futures:** \n    - Trades with leverage \u2014 multiplication of losses possible in volatile/illiquid markets.\n\n#### **General Risk/Market Regime Dependence**\n- **Market Regime Dependency:** \n    - Strong performance of momentum/breakout and option selling may indicate the market was rangebound with sporadic trends. If the market regime shifts (more volatility, sustained trends), the performance could swing significantly.\n- **Short Gamma/Option Selling:** \n    - Though currently profitable, short volatility trades (straddle, strangle sells) carry \u201ctail risk\u201d as losses can be uncapped if large moves occur.\n- **Lack of Diversification:** \n    - Some strategies only have a couple of trades. Greater diversification (across symbols, approaches) reduces risk.\n\n---\n\n### 4. **Summary Table**\n\n| Strategy        | Num. Trades | Net PnL | Signal Strength  | Key Risk                           |\n|-----------------|-------------|---------|------------------|-------------------------------------|\n| Straddle        | 4           | 6779.99 | Medium-Strong    | Breakout risk (sharp move losses)   |\n| Momentum        | 2           | 8400    | Very Strong      | Large position risk                 |\n| Mean Reversion  | 2           | -450    | Poor             | Ineffectiveness in trends           |\n| Breakout        | 2           | 3275    | Strong           | False breakout (whipsaw)            |\n| Strangle        | 2           | 2500    | Good             | Tail risk, sudden volatility spike  |\n| Reversal        | 2           | 2400    | Good             | Trend continuation risk             |\n\n---\n\n## **Executive Summary**\n\n- **Signals:**  \n    - Strongest performance from **Momentum** and **Breakout** (trend following).\n    - **Option selling** strategies (Straddle, Strangle) are working well in the current regime, indicating rangebound/low volatility.\n    - **Mean Reversion** is under-performing; signals likely not aligning with prevailing market conditions.\n\n- **Risks:**  \n    - Significant **tail risk** in short options strategies if volatility expands or market breaks out.\n    - **Concentration risk** if relying too much on a single big trade (Momentum).\n    - **Trend regime risk:** If market switches from rangebound to trending or volatile, both option sellers and mean reversion could face steep losses.\n\n- **Performance:**  \n    - **Overall PnL is strong (22,904.99) and most strategies are profitable.**\n    - Strategies are **not equally robust**; continued outperformance depends on correct alignment of strategy to market regime.\n\n---\n\n## **Recommendations**\n- **Monitor market volatility and trends closely; adjust options exposure if signs of breakout appear.**\n- **Consider reducing mean reversion risk or incorporating stop-loss mechanisms.**\n- **Diversify across more trades and symbols to reduce concentration risk.**\n- **Constantly revalidate signals, especially for option selling and mean reversion, as their performance is regime-dependent.**"
}
```


