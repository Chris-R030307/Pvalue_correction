"""
P-value Corrections Package

A Python package for statistical p-value corrections including:
- Bonferroni correction
- Benjamini-Hochberg correction

Author: Your Name
Version: 0.1.0
"""

from .correction import (
    bonferroni_correction,
    benjamini_hochberg_correction,
    correction_engine
)

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

__all__ = [
    "bonferroni_correction",
    "benjamini_hochberg_correction", 
    "correction_engine"
]
