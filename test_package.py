#!/usr/bin/env python3
"""
Simple test script to verify the package works correctly.
"""

from pval_corrections import correction

def test_package():
    """Test the pval_corrections package."""
    print("Testing pval_corrections package...")
    
    # Test data
    p_values = [0.01, 0.02, 0.03, 0.04, 0.05]
    
    # Test Bonferroni correction
    print("\n1. Testing Bonferroni correction:")
    bonferroni_result = correction(p_values, 'bonferroni')
    print(f"Original p-values: {bonferroni_result['p originals']}")
    print(f"Bonferroni adjusted: {bonferroni_result['padj']}")
    
    # Test Benjamini-Hochberg correction
    print("\n2. Testing Benjamini-Hochberg correction:")
    bh_result = correction(p_values, 'benjamini_hochberg')
    print(f"Original p-values: {bh_result['p originals']}")
    print(f"BH adjusted: {bh_result['padj']}")
    
    print("\n✅ Package test completed successfully!")

if __name__ == "__main__":
    test_package()
