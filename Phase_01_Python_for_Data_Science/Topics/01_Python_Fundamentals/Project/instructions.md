# Practical Project: Market Tick Stream Validator & Memory Profiler

**Topic 01:** Python Fundamentals  
**Phase 01:** Python for Data Science  
**Type:** Hands-On Implementation Lab  

---

## 🎯 Project Overview
In financial data systems, automated trading infrastructure receives millions of raw market data packets every second. Before feeding these quotes to machine learning models or backtesting engines, the system must:
1. **Validate and cast** incoming raw data types strictly.
2. **Encode anomaly flags** efficiently using **bitwise masks** (e.g. invalid spread, zero volume, negative price).
3. **Inspect memory identity (`id()`) and reference counts (`sys.getrefcount`)** to ensure immutable objects are not repeatedly copied unnecessarily and mutable data structures are protected from unintentional side-effects.
4. **Format structured telemetry reports** using modern Python f-strings with precise column alignment and scientific/currency format specifiers.

In this project, you will implement this core tick validator and profiler from scratch using **pure Python fundamentals** (no external libraries).

---

## 📂 Project Structure
```text
Project/
├── instructions.md       # This file (Specifications & Guide)
├── main.py               # Your implementation workspace (starter template provided)
├── sample_ticks.json     # Test input market quote stream
└── test_project.py       # Automated test suite to verify your solution
```

---

## 📋 Requirements & Technical Specifications

### Task 1: Bitwise Status Flags Definition
Define the following integer bitwise flag constants:
- `FLAG_VALID` = `1 << 0` (Bit 0: Decimal 1)
- `FLAG_ANOMALOUS_SPREAD` = `1 << 1` (Bit 1: Decimal 2) - Triggered when `ask <= bid` or `spread > 50.0`.
- `FLAG_ZERO_VOLUME` = `1 << 2` (Bit 2: Decimal 4) - Triggered when `volume <= 0`.
- `FLAG_STALE_TIMESTAMP` = `1 << 3` (Bit 3: Decimal 8) - Triggered when `timestamp <= previous_timestamp`.

### Task 2: Implement `validate_tick(raw_tick, prev_timestamp)`
A function that accepts a raw dictionary representing a tick:
```python
{
    "symbol": "US30",
    "bid": "39500.50",     # note: may come as str or float
    "ask": "39502.00",
    "volume": 120,
    "timestamp": 1700000001
}
```
**Specifications:**
- Cast `bid` and `ask` to `float`. Round both to 2 decimal places.
- Cast `volume` and `timestamp` to `int`.
- Clean and uppercase `symbol` as an immutable `str`.
- Calculate `spread = ask - bid`.
- Evaluate condition flags using bitwise operations (`|`).
- If no error flags are triggered, include `FLAG_VALID`.
- Return a tuple: `(cleaned_tick_dict, status_code_int)`.

### Task 3: Implement `profile_object_memory(obj, label)`
A function that inspects the memory characteristics of any Python object:
- Returns a dictionary with:
  - `"label"`: label string
  - `"type"`: string name of `type(obj)`
  - `"memory_id_hex"`: `hex(id(obj))`
  - `"ref_count"`: `sys.getrefcount(obj) - 1` (accounting for the inspection overhead)
  - `"is_mutable"`: `True` if `obj` is `list`, `dict`, `set`, else `False` if `str`, `int`, `float`, `tuple`.

### Task 4: Implement `format_terminal_summary(cleaned_ticks, status_codes)`
Using modern Python **f-strings**, format a clean, fixed-width ASCII table showing:
- Columns: `| Symbol | Timestamp | Bid | Ask | Spread | Status Flags |`
- Floating-point prices must be right-aligned with 2 decimal places.
- Spread formatted with `+` sign and 2 decimal places.
- Return the full formatted string.

---

## 🧪 Verification & Automated Testing
Run the automated test runner in your terminal:
```bash
python test_project.py
```
When all test assertions pass, you have successfully completed this topic project!

---

## 🏁 Completion Step
Once all tests pass:
1. Open your master [index.html](../../../index.html) in your browser.
2. Toggle the radio button for **Topic 01: Python Fundamentals** to **🟢 Done**.
3. Let me know: *"I have finished Topic 1, generate next!"*
