# test_curvefinance.py
"""
Tests for CurveFinance module.
"""

import unittest
from curvefinance import CurveFinance

class TestCurveFinance(unittest.TestCase):
    """Test cases for CurveFinance class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CurveFinance()
        self.assertIsInstance(instance, CurveFinance)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CurveFinance()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
