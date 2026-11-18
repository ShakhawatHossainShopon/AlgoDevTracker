"""
Topic 01: Python Fundamentals - Practical Lab
Project: High-Precision Market Tick Stream Validator & Memory Profiler

Instructions:
Complete the functions marked with TODO below following the specifications
in instructions.md. You can test your solution anytime by running:
    python test_project.py
"""

import sys
import json
from typing import Dict, Any, Tuple, List

# ==============================================================================
# Task 1: Bitwise Flag Constants
# ==============================================================================
# TODO: Define the bitwise constants as specified:
FLAG_VALID = 1 << 0             # Decimal 1
FLAG_ANOMALOUS_SPREAD = 1 << 1  # Decimal 2
FLAG_ZERO_VOLUME = 1 << 2       # Decimal 4
FLAG_STALE_TIMESTAMP = 1 << 3   # Decimal 8


# ==============================================================================
# Task 2: Validate Tick
# ==============================================================================
def validate_tick(raw_tick: Dict[str, Any], prev_timestamp: int = 0) -> Tuple[Dict[str, Any], int]:
    """
    Validates, casts and computes bitwise status flags for a single tick packet.

    Args:
        raw_tick: Raw dictionary with keys: 'symbol', 'bid', 'ask', 'volume', 'timestamp'
        prev_timestamp: Timestamp of the previous valid tick (for staleness check)

    Returns:
        Tuple of:
          - cleaned_tick (Dict): normalized and strongly-typed dictionary with 'spread'
          - status_code (int): bitwise combination of flags
    """
    # TODO 1: Clean and uppercase symbol (as string)
    # TODO 2: Cast bid and ask to float rounded to 2 decimal places
    # TODO 3: Cast volume and timestamp to int
    # TODO 4: Calculate spread = round(ask - bid, 2)
    # TODO 5: Evaluate bitwise flags:
    #         - If ask <= bid OR spread > 50.0 -> add FLAG_ANOMALOUS_SPREAD
    #         - If volume <= 0 -> add FLAG_ZERO_VOLUME
    #         - If timestamp <= prev_timestamp -> add FLAG_STALE_TIMESTAMP
    #         - If no error flags triggered -> add FLAG_VALID
    
    # Placeholder return (Replace with your implementation):
    cleaned_tick = {}
    status_code = 0
    return cleaned_tick, status_code


# ==============================================================================
# Task 3: Profile Object Memory
# ==============================================================================
def profile_object_memory(obj: Any, label: str) -> Dict[str, Any]:
    """
    Inspects object memory address, reference count, and mutability classification.

    Args:
        obj: Any Python object
        label: Descriptive label for the object

    Returns:
        Dict containing: 'label', 'type', 'memory_id_hex', 'ref_count', 'is_mutable'
    """
    # TODO:
    # 1. Obtain hex representation of id(obj) -> hex(id(obj))
    # 2. Get type name -> type(obj).__name__
    # 3. Reference count -> sys.getrefcount(obj) - 1
    # 4. Check if type is mutable (list, dict, set, bytearray) -> bool
    
    # Placeholder return (Replace with your implementation):
    return {
        "label": label,
        "type": type(obj).__name__,
        "memory_id_hex": hex(id(obj)),
        "ref_count": 0,
        "is_mutable": False
    }


# ==============================================================================
# Task 4: Format Terminal Summary Table
# ==============================================================================
def format_terminal_summary(cleaned_ticks: List[Dict[str, Any]], status_codes: List[int]) -> str:
    """
    Formats an aligned fixed-width ASCII table using modern Python f-strings.

    Columns:
    | Symbol | Timestamp  | Bid       | Ask       | Spread  | Flags |
    """
    # TODO: Construct formatted string with headers, separators, and data rows
    # Ensure prices are aligned right with 2 decimal places.
    # Format spread with a '+' or '-' sign (e.g. +1.50).
    return ""


# ==============================================================================
# Main Demonstration Runner
# ==============================================================================
if __name__ == "__main__":
    print("=== Market Tick Stream Validator & Memory Profiler ===")
    try:
        with open("sample_ticks.json", "r", encoding="utf-8") as f:
            raw_stream = json.load(f)
    except FileNotFoundError:
        print("Error: sample_ticks.json not found.")
        sys.exit(1)

    cleaned_list = []
    status_list = []
    last_ts = 0

    for raw in raw_stream:
        cleaned, status = validate_tick(raw, prev_timestamp=last_ts)
        cleaned_list.append(cleaned)
        status_list.append(status)
        if cleaned.get("timestamp"):
            last_ts = cleaned["timestamp"]

    print("\nProcessed Ticks:")
    print(format_terminal_summary(cleaned_list, status_list))
    
    # Profile a sample object
    print("\nMemory Profile of First Cleaned Tick:")
    if cleaned_list:
        print(profile_object_memory(cleaned_list[0], "First Processed Tick"))
