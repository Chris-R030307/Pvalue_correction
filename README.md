# P-value Corrections

[![PyPI version](https://badge.fury.io/py/pval-corrections.svg)](https://badge.fury.io/py/pval-corrections)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A Python package for statistical p-value corrections including Bonferroni and Benjamini-Hochberg corrections.

**Available on PyPI**: https://pypi.org/project/pval-corrections/

## Features

- **Bonferroni Correction**: Controls family-wise error rate (FWER)
- **Benjamini-Hochberg Correction**: Controls false discovery rate (FDR)
- **Python API**: Simple programmatic interface

## Installation

### From PyPI (Recommended)

```bash
pip install pval-corrections
```

### From Source

```bash
git clone https://github.com/Chris-R030307/Pvalue_correction.git
cd pval-corrections
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/Chris-R030307/Pvalue_correction.git
cd pval-corrections
pip install -e ".[dev]"
```

## Usage

### Python API

```python
from pval_corrections import correction

# Example p-values
p_values = [0.01, 0.02, 0.03, 0.04, 0.05]

# Bonferroni correction
bonferroni_result = correction(p_values, 'bonferroni')
print("Bonferroni adjusted p-values:", bonferroni_result['padj'])

# Benjamini-Hochberg correction
bh_result = correction(p_values, 'benjamini_hochberg')
print("BH adjusted p-values:", bh_result['padj'])
```


## Methods

### Bonferroni Correction

The Bonferroni correction is a conservative method that controls the family-wise error rate (FWER). It ensures that the probability of making at least one Type I error across all tests remains below the chosen significance level. This method is most appropriate when you want to be very confident that none of your significant results are false positives, even if it means missing some true effects.

**When to use**: When you need to be very conservative and can afford to miss some true effects to avoid false discoveries.

### Benjamini-Hochberg Correction

The Benjamini-Hochberg (BH) correction controls the false discovery rate (FDR), which is the expected proportion of false positives among all rejected hypotheses. Unlike Bonferroni, BH is less conservative and allows for a controlled proportion of false discoveries while maintaining good statistical power to detect true effects.

**When to use**: When you want to balance between detecting true effects and controlling false discoveries, especially in exploratory research or when testing many hypotheses.

## Requirements

- Python >= 3.8
- pandas >= 2.1.3
- numpy >= 2.1.3
- matplotlib >= 3.10.0
- seaborn >= 0.13.2
- scipy >= 1.13.0
- scikit-learn >= 1.3.0
- statsmodels >= 0.14.0

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black pval_corrections/
```

### Type Checking

```bash
mypy pval_corrections/
```

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Citation

If you use this package in your research, please cite:

```bibtex
@software{pval_corrections,
  title={P-value Corrections},
  author={Chris-R030307},
  year={2024},
  url={https://github.com/Chris-R030307/Pvalue_correction}
}
```
