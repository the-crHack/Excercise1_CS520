#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path
import shutil
from datetime import datetime

# Configuration
VARIANTS = {
    "QWEN_COT": {
        "test_dir": "Solutions/QWEN_COT/TestCases",
        "solution_dir": "Solutions/QWEN_COT",
        "name": "QWEN with Chain of Thought"
    },
    "QWEN_SCOT": {
        "test_dir": "Solutions/QWEN_SCOT/TestCases", 
        "solution_dir": "Solutions/QWEN_SCOT",
        "name": "QWEN with Step-wise COT"
    },
    "CLAUDE_COT": {
        "test_dir": "Solutions/CLAUDE_COT/TestCases",
        "solution_dir": "Solutions/CLAUDE_COT", 
        "name": "Claude with Chain of Thought"
    },
    "CLAUDE_SCOT": {
        "test_dir": "Solutions/CLAUDE_SCOT/TestCases",
        "solution_dir": "Solutions/CLAUDE_SCOT",
        "name": "Claude with Step-wise COT"
    }
}

def run_coverage_for_variant(variant_key, config):
    """Generate comprehensive coverage reports for a variant."""
    test_dir = config["test_dir"]
    solution_dir = config["solution_dir"]
    name = config["name"]
    
    # Create output directories
    html_dir = f"coverage_reports/html/{variant_key.lower()}"
    xml_file = f"coverage_reports/xml/coverage_{variant_key.lower()}.xml"
    
    # Ensure directories exist
    Path("coverage_reports/html").mkdir(parents=True, exist_ok=True)
    Path("coverage_reports/xml").mkdir(parents=True, exist_ok=True)
    
    print(f"\n{'='*80}")
    print(f"Generating coverage reports for: {name}")
    print(f"{'='*80}")
    print(f"Test Directory:     {test_dir}")
    print(f"Solution Directory: {solution_dir}")
    print(f"HTML Report:        {html_dir}/index.html")
    print(f"XML Report:         {xml_file}")
    
    # Check if directories exist
    if not Path(test_dir).exists():
        print(f"Test directory not found: {test_dir}")
        return False
    
    if not Path(solution_dir).exists():
        print(f"Solution directory not found: {solution_dir}")
        return False
    
    # Run pytest with comprehensive coverage
    cmd = [
        "python", "-m", "pytest",
        test_dir,
        f"--cov={solution_dir}",
        f"--cov-report=html:{html_dir}",
        f"--cov-report=xml:{xml_file}",
        "--cov-report=term-missing",
        "--cov-branch",
        "-v",
        "--tb=short"
    ]
    
    print(f"\nRunning: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(" Coverage reports generated successfully!")
    else:
        print(" Coverage reports generated with test failures")
    
    # Print summary from output
    output_lines = result.stdout.split('\n')
    for line in output_lines:
        if 'passed' in line or 'failed' in line or 'TOTAL' in line:
            print(f"   {line}")
    
    return True

def create_index_html():
    """Create a simple index.html file linking to all coverage reports."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Coverage Reports</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #333; }}
        .info {{ color: #666; margin-bottom: 30px; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        a {{ color: #0066cc; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; color: #666; font-size: 0.9em; }}
    </style>
</head>
<body>
    <h1>Coverage Reports</h1>
    <div class="info">
        <p><strong>Generated:</strong> {timestamp}</p>
        <p><strong>Project:</strong> LLM Code Generation Analysis</p>
    </div>
    
    <table>
        <tr>
            <th>Variant</th>
            <th>Description</th>
            <th>HTML Report</th>
            <th>XML Report</th>
        </tr>
        <tr>
            <td><strong>QWEN_COT</strong></td>
            <td>QWEN with Chain of Thought</td>
            <td><a href="html/qwen_cot/index.html">View HTML</a></td>
            <td><a href="xml/coverage_qwen_cot.xml">Download XML</a></td>
        </tr>
        <tr>
            <td><strong>QWEN_SCOT</strong></td>
            <td>QWEN with Step-wise COT</td>
            <td><a href="html/qwen_scot/index.html">View HTML</a></td>
            <td><a href="xml/coverage_qwen_scot.xml">Download XML</a></td>
        </tr>
        <tr>
            <td><strong>CLAUDE_COT</strong></td>
            <td>Claude with Chain of Thought</td>
            <td><a href="html/claude_cot/index.html">View HTML</a></td>
            <td><a href="xml/coverage_claude_cot.xml">Download XML</a></td>
        </tr>
        <tr>
            <td><strong>CLAUDE_SCOT</strong></td>
            <td>Claude with Step-wise COT</td>
            <td><a href="html/claude_scot/index.html">View HTML</a></td>
            <td><a href="xml/coverage_claude_scot.xml">Download XML</a></td>
        </tr>
    </table>
    
    <div class="footer">
        <p><strong>Regenerate reports:</strong> python generate_all_coverage_reports.py</p>
        <p><strong>Quick analysis:</strong> python analyze_coverage.py Solutions/VARIANT/TestCases Solutions/VARIANT</p>
    </div>
</body>
</html>"""
    
    with open("coverage_reports/index.html", "w") as f:
        f.write(html_content)
    
    print(f"\n Index page created: coverage_reports/index.html")

def main():
    """Main function to generate all coverage reports."""
    print("🧪 LLM Code Generation - Coverage Report Generator")
    print("="*80)
    
    # Clean up old reports
    if Path("coverage_reports").exists():
        print(" Cleaning up old reports...")
        shutil.rmtree("coverage_reports")
    
    success_count = 0
    total_count = len(VARIANTS)
    
    # Generate reports for each variant
    for variant_key, config in VARIANTS.items():
        success = run_coverage_for_variant(variant_key, config)
        if success:
            success_count += 1
    
    # Create index page
    create_index_html()
    
    # Print final summary
    print(f"\n{'='*80}")
    print("COVERAGE REPORT GENERATION COMPLETE")
    print(f"{'='*80}")
    print(f"Successfully generated: {success_count}/{total_count} reports")
    print(f"Reports location: coverage_reports/")
    print(f"Open index: coverage_reports/index.html")
    
    if success_count == total_count:
        print("\n All coverage reports generated successfully!")
        print("\nNext steps:")
        print("1. Open coverage_reports/index.html in your browser")
        print("2. Review HTML reports for detailed line-by-line coverage")
        print("3. Use XML/JSON reports for automated analysis")
        return 0
    else:
        print(f"\n  {total_count - success_count} reports failed to generate")
        print("Check the error messages above and ensure all directories exist")
        return 1

if __name__ == "__main__":
    sys.exit(main())
