"""
QA Test Metrics Calculator
Fill in the code below where you see # TODO comments.
"""

def main():
    print("═" * 40)
    print("  QA Test Metrics Calculator")
    print("═" * 40)

    # TODO 1: Get user input
    # - Total test cases (convert to int)
    # - Passed tests (convert to int)
    # - Total execution time in seconds (convert to float)
    total_tests = int(input("Enter total number of test cases: "))
    passed_tests = int(input("Enter in number of passed test cases: "))
    total_time = float(input("Enter in the total execution time in seconds: "))

    # TODO 2: Calculate metrics
    # - failed tests
    # - pass rate (as percentage)
    # - fail rate (as percentage)
    # - average time per test
    failed_tests = total_tests-passed_tests
    pass_rate = (passed_tests/total_tests) * 100
    fail_rate = (failed_tests/total_tests)*100
    avg_time = total_time/total_tests

    # TODO 3: Print the results summary using f-strings
    # Use the format shown in the README

    print()
    print("───────────────────────────────────────")
    print("  Test Results Summary")
    print("───────────────────────────────────────")
    print(f"  Total Tests:   {total_tests:>8}")
    print(f"  Passed:        {passed_tests:>8}")
    print(f"  Failed:        {failed_tests:>8}")
    print(f"  Pass Rate:     {pass_rate:>7.1f}%")
    print(f"  Fail Rate:     {fail_rate:>7.1f}%")
    print(f"  Avg Time/Test: {avg_time:>7.2f}s")
    print(f"  Total Time:    {total_time:>7.2f}s")
 

    # TODO 4: Determine and print the verdict
    # >= 95% → RELEASE APPROVED
    # >= 80% → CONDITIONAL RELEASE
    # else   → RELEASE BLOCKED


    if pass_rate >= 95:
        verdict = "✅ RELEASE APPROVED"
    elif pass_rate >= 80:
        verdict = "⚠️ CONDITIONAL RELEASE — review failures"
    else:
        verdict = "❌RELEASE BLOCKED — too many failures"


    print()
    print(f"  Verdict: {verdict}")
    print("═══════════════════════════════════════")


if __name__ == "__main__":
    main()