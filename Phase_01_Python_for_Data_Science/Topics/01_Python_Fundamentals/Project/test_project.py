"""
Automated Test Suite for Topic 01 Practical Lab:
High-Precision Market Tick Stream Validator & Memory Profiler
"""

import unittest
import sys
from main import (
    FLAG_VALID,
    FLAG_ANOMALOUS_SPREAD,
    FLAG_ZERO_VOLUME,
    FLAG_STALE_TIMESTAMP,
    validate_tick,
    profile_object_memory,
    format_terminal_summary
)

class TestPythonFundamentalsProject(unittest.TestCase):

    def test_bitwise_constants(self):
        """Verify bitwise flags are distinct powers of two."""
        self.assertEqual(FLAG_VALID, 1)
        self.assertEqual(FLAG_ANOMALOUS_SPREAD, 2)
        self.assertEqual(FLAG_ZERO_VOLUME, 4)
        self.assertEqual(FLAG_STALE_TIMESTAMP, 8)

    def test_validate_valid_tick(self):
        """Test a clean tick with valid spread and volume."""
        raw = {
            "symbol": "us30",
            "bid": "39500.20",
            "ask": "39501.70",
            "volume": "150",
            "timestamp": 1700000010
        }
        cleaned, status = validate_tick(raw, prev_timestamp=1700000005)
        
        self.assertEqual(cleaned["symbol"], "US30")
        self.assertEqual(cleaned["bid"], 39500.20)
        self.assertEqual(cleaned["ask"], 39501.70)
        self.assertEqual(cleaned["volume"], 150)
        self.assertEqual(cleaned["timestamp"], 1700000010)
        self.assertAlmostEqual(cleaned["spread"], 1.50, places=2)
        
        # Must have FLAG_VALID and no errors
        self.assertTrue(bool(status & FLAG_VALID))
        self.assertFalse(bool(status & FLAG_ANOMALOUS_SPREAD))
        self.assertFalse(bool(status & FLAG_ZERO_VOLUME))
        self.assertFalse(bool(status & FLAG_STALE_TIMESTAMP))

    def test_validate_inverted_spread(self):
        """Test tick where ask <= bid (crossed market)."""
        raw = {
            "symbol": "US30",
            "bid": 39500.0,
            "ask": 39499.0,
            "volume": 100,
            "timestamp": 1700000010
        }
        cleaned, status = validate_tick(raw, prev_timestamp=1700000000)
        self.assertTrue(bool(status & FLAG_ANOMALOUS_SPREAD))
        self.assertFalse(bool(status & FLAG_VALID))

    def test_validate_excessive_spread(self):
        """Test tick where spread > 50.0."""
        raw = {
            "symbol": "US30",
            "bid": 39500.0,
            "ask": 39560.0,
            "volume": 100,
            "timestamp": 1700000010
        }
        cleaned, status = validate_tick(raw, prev_timestamp=1700000000)
        self.assertTrue(bool(status & FLAG_ANOMALOUS_SPREAD))
        self.assertFalse(bool(status & FLAG_VALID))

    def test_validate_zero_volume_and_stale_ts(self):
        """Test multiple error flags triggered simultaneously."""
        raw = {
            "symbol": "US30",
            "bid": 39500.0,
            "ask": 39502.0,
            "volume": 0,
            "timestamp": 1700000000
        }
        cleaned, status = validate_tick(raw, prev_timestamp=1700000000)
        self.assertTrue(bool(status & FLAG_ZERO_VOLUME))
        self.assertTrue(bool(status & FLAG_STALE_TIMESTAMP))
        self.assertFalse(bool(status & FLAG_VALID))

    def test_profile_memory(self):
        """Test memory profiler on mutable and immutable objects."""
        mutable_obj = [1, 2, 3]
        prof_mut = profile_object_memory(mutable_obj, "Test List")
        self.assertEqual(prof_mut["type"], "list")
        self.assertTrue(prof_mut["is_mutable"])
        self.assertTrue(prof_mut["memory_id_hex"].startswith("0x"))

        immutable_obj = "US30_TICK"
        prof_imm = profile_object_memory(immutable_obj, "Test String")
        self.assertEqual(prof_imm["type"], "str")
        self.assertFalse(prof_imm["is_mutable"])

    def test_format_terminal_summary(self):
        """Test that table string formats with expected headers."""
        sample_cleaned = [{
            "symbol": "US30",
            "timestamp": 1700000001,
            "bid": 39500.50,
            "ask": 39502.00,
            "spread": 1.50,
            "volume": 100
        }]
        sample_status = [FLAG_VALID]
        output = format_terminal_summary(sample_cleaned, sample_status)
        self.assertIsInstance(output, str)
        self.assertIn("US30", output)
        self.assertIn("39500.50", output)
        self.assertIn("39502.00", output)


if __name__ == "__main__":
    unittest.main()
