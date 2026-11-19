# Phase 1 Capstone Project: MT5 Historical Market Data Collector & Parquet Engine

> **Notice / Capstone Reservation Policy:**
> This capstone project is reserved exclusively for the student to build and code directly on PC. Do not place auto-generated scripts here. Follow the specifications below to implement the engine.

---

## 🎯 Project Overview
In quantitative algorithmic trading, raw market data from brokers (like MetaTrader 5) is the bedrock of backtesting and signal generation. However, retrieving streaming ticks or multi-timeframe candles over network sockets introduces latency, disconnections, missing bars, and memory bloat.

In this capstone project, you will build an **Industrial-Grade Historical Market Data Collector** in Python connecting to MetaTrader 5 (MT5), transforming raw market ticks and candlesticks into partitioned, compressed Apache Parquet archives for ultra-fast vector backtesting.

---

## 📋 Architecture & Core Requirements

### 1. MT5 Connector & Authentication
- Initialize and authenticate the `MetaTrader5` terminal (`mt5.initialize()`).
- Implement health-check diagnostics (account currency, leverage, broker connection ping).
- Graceful shutdown handling (`mt5.shutdown()`) on termination or critical socket failure.

### 2. Multi-Timeframe Candle Extraction
- Extract OHLCV bar series for key trading instruments:
  - Forex: `EURUSD`, `GBPUSD`, `USDJPY`
  - Commodities: `XAUUSD` (Gold), `USOUSD` (Oil)
  - Indices/Crypto: `BTCUSD`, `SP500`
- Support timeframes: `TIMEFRAME_M1`, `TIMEFRAME_M5`, `TIMEFRAME_H1`, `TIMEFRAME_D1`.
- Convert broker Unix timestamps into UTC `pd.DatetimeIndex`.

### 3. High-Frequency Tick Harvester
- Stream and fetch full tick histories (`mt5.copy_ticks_range()`).
- Parse Bid, Ask, Spread (in points), and Volume.
- Compute Bid-Ask Imbalance: $\text{Imbalance} = \frac{\text{BidVol} - \text{AskVol}}{\text{BidVol} + \text{AskVol}}$.

### 4. Data Validation & Integrity Engine
- Check for zero volume or flatlined price quotes.
- Detect missing bars in regular market trading hours.
- Verify price boundaries ($\text{High} \ge \text{Low}$, $\text{High} \ge \text{Open}$, $\text{High} \ge \text{Close}$).

### 5. High-Performance Partitioned Storage
- Save historical datasets in partitioned Apache Parquet (`pyarrow` or `fastparquet` engine with Snappy compression).
- Partition directory format: `data/equity/symbol=EURUSD/year=2024/month=11/data.parquet`.
- Implement incremental appending: avoid redownloading existing bars.

---

## 🛠️ Recommended Project Directory Structure
```
Project_Trading_MT5_Historical_Market_Data_Collector/
├── README.md              # Project Blueprint (This file)
├── config.yaml            # Symbols, timeframes, date ranges
├── requirements.txt       # MetaTrader5, pandas, pyarrow, pyyaml
├── mt5_collector/
│   ├── __init__.py
│   ├── connector.py       # MT5 login & session manager
│   ├── extractor.py       # OHLCV & Tick fetch logic
│   ├── validator.py       # Integrity checks
│   └── storage.py         # Partitioned Parquet writer
├── data/                  # Output directory (gitignored)
└── main.py                # CLI runner
```

---

## 🚀 Execution & Verification
1. Run MT5 terminal on your local Windows PC.
2. Install dependencies: `pip install MetaTrader5 pandas pyarrow pyyaml`.
3. Execute `python main.py --symbol EURUSD --timeframe M1 --days 30`.
4. Verify parquet data files load cleanly into pandas in under 50ms.
