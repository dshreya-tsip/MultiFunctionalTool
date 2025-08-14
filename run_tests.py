import pandas as pd

# Load test cases
df = pd.read_csv("generated_testcases.csv")

# Simulate test execution
def simulate_test(row):
    if "success" in row["Expected Output"].lower() or "displayed" in row["Expected Output"].lower():
        return "Pass"
    return "Fail"

df["Result"] = df.apply(simulate_test, axis=1)

# Save results
df.to_csv("test_results.csv", index=False)
print("Test results saved to test_results.csv")
