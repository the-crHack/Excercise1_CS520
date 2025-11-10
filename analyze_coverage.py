#!/usr/bin/env python3


import sys
import subprocess
import json
import re
from pathlib import Path

def get_test_results(test_file):
    """Get test pass/fail counts for a test file."""
    if not Path(test_file).exists():
        return 0, 0
    
    cmd = ["python", "-m", "pytest", test_file, "-v", "--tb=no"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout + result.stderr
    
    # Count PASSED and FAILED in output
    passed = output.count(' PASSED')
    failed = output.count(' FAILED')
    
    return passed, failed

def get_coverage_data(test_folder, solution_folder):
    """Run coverage analysis and return results."""
    json_file = "temp_coverage.json"
    
    # Run pytest with coverage
    cmd = [
        "python", "-m", "pytest",
        test_folder,
        f"--cov={solution_folder}",
        f"--cov-report=json:{json_file}",
        "--cov-branch",
        "-q"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Parse coverage data
    coverage_by_file = {}
    try:
        with open(json_file, 'r') as f:
            cov_json = json.load(f)
            files = cov_json.get('files', {})
            
            for file_path, file_data in files.items():
                filename = Path(file_path).stem
                summary = file_data.get('summary', {})
                
                # Calculate branch coverage percentage
                branches_covered = summary.get('covered_branches', 0)
                branches_total = summary.get('num_branches', 0)
                branch_pct = round((branches_covered / branches_total * 100) if branches_total > 0 else 100)
                
                coverage_by_file[filename] = {
                    'line_pct': round(summary.get('percent_covered', 0)),
                    'lines_covered': summary.get('covered_lines', 0),
                    'lines_total': summary.get('num_statements', 0),
                    'branch_pct': branch_pct,
                    'branches_covered': branches_covered,
                    'branches_total': branches_total
                }
    except Exception as e:
        print(f"Error reading coverage data: {e}")
    
    # Clean up temp file
    if Path(json_file).exists():
        Path(json_file).unlink()
    
    return coverage_by_file

def interpret_coverage(line_pct, branch_pct, passed, failed):
    """Generate interpretation for coverage results."""
    total = passed + failed
    pass_rate = (passed / total * 100) if total > 0 else 0
    
    if line_pct == 100 and branch_pct == 100 and failed == 0:
        return "Perfect: 100% coverage, all tests pass"
    elif line_pct == 100 and failed > 0:
        return f"Full coverage but {failed} test(s) fail - logic errors"
    elif line_pct < 20:
        return "Critical: Very low coverage, function signature issues"
    elif line_pct < 50:
        return "Low coverage: Missing edge case handling"
    elif line_pct < 85:
        return "Good coverage: Some edge cases untested"
    elif pass_rate < 50:
        return f"High coverage but many failures ({failed}/{total})"
    else:
        return "Excellent: High coverage with most tests passing"

def main():
    """Main function."""
    if len(sys.argv) != 3:
        print("Usage: python analyze_coverage.py <test_folder> <solution_folder>")
        print("\nExamples:")
        print("  python analyze_coverage.py TestCases Solutions")
        print("  python analyze_coverage.py TestCases_QWEN_COT Solutions/QWEN/COT")
        print("  python analyze_coverage.py TestCases_CLAUDE_SCOT Solutions/CLAUDE_SCOT")
        sys.exit(1)
    
    test_folder = sys.argv[1]
    solution_folder = sys.argv[2]
    
    # Validate folders exist
    if not Path(test_folder).exists():
        print(f"Error: Test folder '{test_folder}' does not exist")
        sys.exit(1)
    
    if not Path(solution_folder).exists():
        print(f"Error: Solution folder '{solution_folder}' does not exist")
        sys.exit(1)
    
    print("="*80)
    print(f"Coverage Analysis")
    print("="*80)
    print(f"Test Folder:     {test_folder}")
    print(f"Solution Folder: {solution_folder}")
    print("="*80)
    print()
    
    # Get coverage data
    print("Running coverage analysis...")
    coverage_data = get_coverage_data(test_folder, solution_folder)
    
    if not coverage_data:
        print("No coverage data found. Make sure the folders contain valid Python files.")
        sys.exit(1)
    
    # Get test results for each problem
    print("Analyzing test results...")
    test_results = {}
    for problem in coverage_data.keys():
        test_file = f"{test_folder}/test_{problem}.py"
        passed, failed = get_test_results(test_file)
        test_results[problem] = {'passed': passed, 'failed': failed}
    
    # Print results table
    print()
    print("="*80)
    print("COVERAGE ANALYSIS RESULTS")
    print("="*80)
    print()
    
    # Print header
    print(f"{'#':<3} {'Problem':<22} {'Tests Passed':<15} {'Line Cov':<15} {'Branch':<8}")
    print("-" * 80)
    
    total_passed = 0
    total_failed = 0
    total_line_pct = 0
    total_branch_pct = 0
    count = 0
    
    for idx, (problem, cov) in enumerate(sorted(coverage_data.items()), 1):
        # Skip __init__ files and test files
        if problem == '__init__' or problem.startswith('test_'):
            continue
            
        tests = test_results.get(problem, {'passed': 0, 'failed': 0})
        passed = tests['passed']
        failed = tests['failed']
        total_tests_for_problem = passed + failed
        
        line_pct = cov['line_pct']
        lines_covered = cov['lines_covered']
        lines_total = cov['lines_total']
        branch_pct = cov['branch_pct']
        
        # Truncate problem name if too long
        problem_display = problem if len(problem) <= 22 else problem[:19] + "..."
        
        tests_str = f"{passed}/{total_tests_for_problem}"
        line_cov_str = f"{line_pct}% ({lines_covered}/{lines_total})"
        branch_str = f"{branch_pct}%"
        
        print(f"{idx:<3} {problem_display:<22} {tests_str:<15} {line_cov_str:<15} {branch_str:<8}")
        
        total_passed += passed
        total_failed += failed
        total_line_pct += line_pct
        total_branch_pct += branch_pct
        count += 1
    
    # Print summary
    total_tests = total_passed + total_failed
    pass_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
    avg_line_pct = total_line_pct / count if count > 0 else 0
    avg_branch_pct = total_branch_pct / count if count > 0 else 0
    
    print()
    print("="*80)
    print("SUMMARY STATISTICS")
    print("="*80)
    print(f"Total Tests:              {total_tests} ({total_passed} passed, {total_failed} failed)")
    print(f"Pass Rate:                {pass_rate:.1f}%")
    print(f"Average Line Coverage:    {avg_line_pct:.1f}%")
    print(f"Average Branch Coverage:  {avg_branch_pct:.1f}%")
    print(f"Functions Analyzed:       {count}")
    print("="*80)
    
    # Return exit code based on pass rate
    if pass_rate >= 90:
        print("\n✅ Excellent: 90%+ tests passing")
        return 0
    elif pass_rate >= 70:
        print("\n  Good: 70-90% tests passing")
        return 0
    elif pass_rate >= 50:
        print("\n  Fair: 50-70% tests passing")
        return 0
    else:
        print("\n Poor: <50% tests passing - review implementations")
        return 1

if __name__ == "__main__":
    sys.exit(main())
