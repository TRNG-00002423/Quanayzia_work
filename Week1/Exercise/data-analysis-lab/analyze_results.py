
#TASK 1 
# "Question: How many dependencies did pandas install? Write the answer in a comment."
# 3, numpy, python-dateutil, tzdata

# TASK 3 

import pandas as pd
import os
df = pd.read_csv("test_data.csv")


#2. Print basic info:
print("Total tests:", len(df))
print("\nColumns and dtypes:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

# 3. Calculate aggregate metrics
   #Overall Pass Rate
pass_rate = (df["status"] == "pass").mean()
print("Overall pass rate:", pass_rate)

   #Avg duration
avg_ms = df["duration_ms"].mean()
avg_sec = avg_ms / 1000

print("Average duration (ms):", avg_ms)
print("Average duration (sec):", avg_sec)

   #Test speeds
slowest = df.loc[df["duration_ms"].idxmax()]
fastest = df.loc[df["duration_ms"].idxmin()]

print("\nSlowest test:")
print(slowest[["test_name", "duration_ms"]])

print("\nFastest test:")
print(fastest[["test_name", "duration_ms"]])

#4. Group by module
   # Pass rate per module
group = df.groupby("module")

    # Pass per rate module
pass_rate_module = (df["status"] == "pass").groupby(df["module"]).mean()
print(pass_rate_module)

    # number of tests per module 
test_per_mod= group.size()
#5 Filter

    # All failed tests (name, module, duration)
failed_tests = df[df["status"] == "fail"][["test_name", "module", "duration_ms"]]
print(failed_tests)

    #Tests slower than 1500ms
slow_tests = df[df["duration_ms"] > 1500]
print(slow_tests)


auth_tests = df[df["module"] == "auth"]
print(auth_tests)

#6. Add a column
df["duration_sec"] = df["duration_ms"] / 1000


# 7. Sort and Export
sorted=df.sort_values(by="duration_ms", ascending=False)
print(sorted)

os.makedirs("output", exist_ok=True)
sorted.to_csv("output/results_sorted.csv",index=False)



#Task 4 Pip Freeze 