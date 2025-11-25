# Coverage Reports

## Quick Start

```bash
# View the reports
open coverage_reports/index.html
```

## What's Included


### File Structure
```
coverage_reports/
├── index.html                          # Main dashboard (all variants)
├── html/                               # HTML reports
│   ├── qwen_cot/index.html
│   ├── qwen_scot/index.html
│   ├── claude_cot/index.html
│   └── claude_scot/index.html
└── xml/                                # XML reports
    ├── coverage_qwen_cot.xml
    ├── coverage_qwen_scot.xml
    ├── coverage_claude_cot.xml
    └── coverage_claude_scot.xml

coverage_comparison/                    # Before/After comparison (Assignment 3)
├── index.html                          # Main comparison page
├── README.md                           # Documentation
├── month_season_before/                # Original test coverage
│   └── index.html
├── month_season_after/                 # With spec-guided tests
│   └── index.html
├── bell_number_before/                 # Original test coverage
│   └── index.html
└── bell_number_after/                  # With spec-guided tests
    └── index.html
```

## Results Summary

| Variant | Tests Passed | Pass Rate | Coverage |
|---------|--------------|-----------|----------|
| QWEN_SCOT | 761/1020 | 74.6% | 97% |
| CLAUDE_SCOT | 760/1020 | 74.5% | 98% |
| CLAUDE_COT | 661/1020 | 64.8% | 97% |
| QWEN_COT | 658/1020 | 64.5% | 98% |

## Regenerate Reports

```bash
# All variants
python generate_all_coverage_reports.py

# Single variant
python -m pytest Solutions/QWEN_SCOT/TestCases \
  --cov=Solutions/QWEN_SCOT \
  --cov-report=html:htmlcov \
  --cov-branch -v
```


```bash
# View main dashboard (all variants)
open coverage_reports/index.html

# View before/after comparison (Assignment 2)
open coverage_comparison/index.html

# View specific variant
open coverage_reports/html/qwen_scot/index.html

# Quick terminal analysis
python analyze_coverage.py Solutions/QWEN_SCOT/TestCases Solutions/QWEN_SCOT
```

## Generate Before/After Comparison (Assignment 3)

To create the coverage comparison page showing improvements from spec-guided tests:

### Step 1: Generate BEFORE reports (original tests only)

```bash
# month_season - baseline
python -m pytest Solutions/QWEN_SCOT/TestCases/test_month_season.py \
  --cov=Solutions.QWEN_SCOT.month_season \
  --cov-report=html:coverage_comparison/month_season_before \
  --cov-branch -v

# bell_number - baseline
python -m pytest Solutions/QWEN_SCOT/TestCases/test_bell_number.py \
  --cov=Solutions.QWEN_SCOT.bell_number \
  --cov-report=html:coverage_comparison/bell_number_before \
  --cov-branch -v
```

### Step 2: Generate AFTER reports (original + spec-guided tests)

```bash
# month_season - with spec-guided tests
python -m pytest Solutions/QWEN_SCOT/TestCases/test_month_season.py \
  Solutions/QWEN_SCOT/spec_guided_tests/test_month_season.py \
  --cov=Solutions.QWEN_SCOT.month_season \
  --cov-report=html:coverage_comparison/month_season_after \
  --cov-branch -v

# bell_number - with spec-guided tests
python -m pytest Solutions/QWEN_SCOT/TestCases/test_bell_number.py \
  Solutions/QWEN_SCOT/spec_guided_tests/test_bell_number.py \
  --cov=Solutions.QWEN_SCOT.bell_number \
  --cov-report=html:coverage_comparison/bell_number_after \
  --cov-branch -v
```

### Step 3: View the comparison

```bash
open coverage_comparison/index.html
```

### Results:

**month_season:**
- Before: 80% stmt, 75% branch (102 tests)
- After: 100% stmt, 100% branch (122 tests = 102 + 20 spec-guided)
- Improvement: +20% stmt, +25% branch

**bell_number:**
- Before: 83% stmt, 80% branch (102 tests)
- After: 100% stmt, 100% branch (112 tests = 102 + 10 spec-guided)
- Improvement: +17% stmt, +20% branch
```

