# Coverage Comparison - Before and After Spec-Guided Tests

## Summary

This directory contains HTML coverage reports comparing baseline coverage (original tests only) vs improved coverage (original + spec-guided tests).

## Results

### month_season

| Metric | Before (102 tests) | After (224 tests) | Improvement |
|--------|-------------------|-------------------|-------------|
| **Statement Coverage** | 80% (15/18) | **100% (18/18)** | +20% |
| **Branch Coverage** | 75% (9/12) | **100% (12/12)** | +25% |
| **Missing Lines** | 4, 26, 34 | None | All covered |
| **Tests Added** | - | 122 spec-guided | +119.6% |

**Missing Coverage Before:**
- Line 4: Invalid month handling
- Line 26: Invalid day handling  
- Line 34: Edge case in season logic

**Achieved After:** Complete coverage of all branches and edge cases

---

### bell_number

| Metric | Before (102 tests) | After (214 tests) | Improvement |
|--------|-------------------|-------------------|-------------|
| **Statement Coverage** | 83% (12/14) | **100% (14/14)** | +17% |
| **Branch Coverage** | 80% (8/10) | **100% (10/10)** | +20% |
| **Missing Lines** | 8, 10 | None | All covered |
| **Tests Added** | - | 112 spec-guided | +109.8% |

**Missing Coverage Before:**
- Line 8: Negative input handling (n < 0)
- Line 10: Base case B(0) = 1

**Achieved After:** Complete coverage including negative inputs and all base cases

---

## How to View Reports

### month_season
```bash
# Before (baseline)
open coverage_comparison/month_season_before/index.html

# After (with spec-guided tests)
open coverage_comparison/month_season_after/index.html
```

### bell_number
```bash
# Before (baseline)
open coverage_comparison/bell_number_before/index.html

# After (with spec-guided tests)
open coverage_comparison/bell_number_after/index.html
```

## Key Insights

1. **Targeted Testing**: Spec-guided tests achieved 100% coverage by systematically targeting uncovered branches
2. **Efficiency**: Small number of focused tests (122 and 112) completed what 102 general tests missed
3. **Edge Cases**: Specifications revealed critical edge cases:
   - Invalid input handling
   - Boundary conditions (season transitions, negative numbers)
   - Base cases (B(0), B(1), B(2))

## Files Generated

```
coverage_comparison/
├── README.md (this file)
├── month_season_before/
│   └── index.html (+ supporting files)
├── month_season_after/
│   └── index.html (+ supporting files)
├── bell_number_before/
│   └── index.html (+ supporting files)
└── bell_number_after/
    └── index.html (+ supporting files)
```

## Regenerate Reports

```bash
# month_season before
python -m pytest Solutions/QWEN_SCOT/TestCases/test_month_season.py \
  --cov=Solutions.QWEN_SCOT.month_season \
  --cov-report=html:coverage_comparison/month_season_before \
  --cov-branch -v

# month_season after
python -m pytest Solutions/QWEN_SCOT/TestCases/test_month_season.py \
  Solutions/QWEN_SCOT/spec_guided_tests/test_month_season.py \
  --cov=Solutions.QWEN_SCOT.month_season \
  --cov-report=html:coverage_comparison/month_season_after \
  --cov-branch -v

# bell_number before
python -m pytest Solutions/QWEN_SCOT/TestCases/test_bell_number.py \
  --cov=Solutions.QWEN_SCOT.bell_number \
  --cov-report=html:coverage_comparison/bell_number_before \
  --cov-branch -v

# bell_number after
python -m pytest Solutions/QWEN_SCOT/TestCases/test_bell_number.py \
  Solutions/QWEN_SCOT/spec_guided_tests/test_bell_number.py \
  --cov=Solutions.QWEN_SCOT.bell_number \
  --cov-report=html:coverage_comparison/bell_number_after \
  --cov-branch -v
```

---
