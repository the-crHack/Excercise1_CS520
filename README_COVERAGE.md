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
├── index.html                          # Main dashboard
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
# View main dashboard
open coverage_reports/index.html

# View specific variant
open coverage_reports/html/qwen_scot/index.html

# Quick terminal analysis
python analyze_coverage.py Solutions/QWEN_SCOT/TestCases Solutions/QWEN_SCOT

```<img width="1470" height="956" alt="Screenshot 2025-11-10 at 7 52 53 PM" src="https://github.com/user-attachments/assets/3634a71c-cbdf-4e39-8336-5541cba79c64" />

<img width="1470" height="956" alt="Screenshot 2025-11-10 at 7 53 03 PM" src="https://github.com/user-attachments/assets/4d2e5127-71bd-4b73-b2ed-b67f81c752d3" />

<img width="1470" height="956" alt="Screenshot 2025-11-10 at 7 53 07 PM" src="https://github.com/user-attachments/assets/fd949863-0dc2-437e-a6ed-c44a231be19d" />


<img width="1470" height="956" alt="Screenshot 2025-11-10 at 7 53 18 PM" src="https://github.com/user-attachments/assets/5a0c22d9-fc6f-44a6-9e58-7c1d6bd1d977" />





