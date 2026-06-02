

# 1. Define 5 test results as variables (test name, duration in ms, status).

# Test data
test1_name = "test_login"
test1_duration = 1200
test1_status = "✅ PASS"

test2_name = "test_search"
test2_duration = 850
test2_status = "✅ PASS"

test3_name = "test_checkout"
test3_duration = 2300
test3_status = "❌ FAIL"

test4_name = "test_profile"
test4_duration = 450
test4_status = "✅ PASS"

test5_name = "test_logout"
test5_duration = 180
test5_status = "✅ PASS"

total_duration =  test1_duration+ test2_duration + test3_duration + test4_duration + test5_duration

passed_tests = 4
total_tests = 5

#2. Print a formatted table using f-strings with alignment
print("┌──────────────────┬────────────────┬────────────────┐") 
print("│ Test Name        │ Duration       │ Status         │")
print("├──────────────────┼────────────────┼────────────────┤")

print(f"│ {test1_name:<16} │ {test1_duration:>10,} ms  │ {test1_status:>10}    │")
print(f"│ {test2_name:<16} │ {test2_duration:>10,} ms  │ {test2_status:>10}    │")
print(f"│ {test3_name:<16} │ {test3_duration:>10,} ms  │ {test3_status:>10}    │ ")
print(f"│ {test4_name:<16} │ {test4_duration:>10,} ms  │ {test4_status:>10}    │")
print(f"│ {test5_name:<16} │ {test5_duration:>10,} ms  │ {test5_status:>10}    │")

print("├──────────────────┼────────────────┼────────────────┤")
print(f"│ {'TOTAL':<16} │ {total_duration:>10,} ms  │ {passed_tests}/{total_tests} Pass       │")
print("└──────────────────┴────────────────┴────────────────┘")