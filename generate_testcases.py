import sys
import docx
import pandas as pd

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)

def generate_test_cases(text):
    # Placeholder logic for generating test cases
    # In a real scenario, integrate with an AI model or use NLP techniques
    test_cases = [
        {
            "Test Case ID": "TC001",
            "Description": "Verify application launch",
            "Input": "Double-click application icon",
            "Expected Output": "Application launches successfully",
            "Test Type": "Functional",
            "Result": ""
        },
        {
            "Test Case ID": "TC002",
            "Description": "Check protocol configuration window",
            "Input": "Open protocol configuration",
            "Expected Output": "Protocol values are displayed",
            "Test Type": "Functional",
            "Result": ""
        },
        {
            "Test Case ID": "TC003",
            "Description": "Verify debug log collection",
            "Input": "Click Run button",
            "Expected Output": "Logs are copied to shared folder",
            "Test Type": "Functional",
            "Result": ""
        },
        {
            "Test Case ID": "TC004",
            "Description": "Check memory leak comparison table",
            "Input": "Run memory leak check",
            "Expected Output": "Comparison table is displayed",
            "Test Type": "Functional",
            "Result": ""
        },
        {
            "Test Case ID": "TC005",
            "Description": "Verify application compatibility on desktop",
            "Input": "Run app on desktop",
            "Expected Output": "App runs without errors",
            "Test Type": "Non-Functional",
            "Result": ""
        }
    ]
    return pd.DataFrame(test_cases)

if __name__ == "__main__":
    srs_file = sys.argv[1]
    text = extract_text_from_docx(srs_file)
    df = generate_test_cases(text)
    df.to_csv("generated_testcases.csv", index=False)
    print("Test cases generated and saved to generated_testcases.csv")
