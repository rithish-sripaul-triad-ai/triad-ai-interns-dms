import requests
import os
import json

BASE_URL = "http://localhost:5000/api"
REPORT_FILE = "test_report.txt"

results = {"total": 0, "passed": 0, "failed": 0, "errors": []}

def log_result(test_name, success, error_msg=""):
    results["total"] += 1
    if success:
        results["passed"] += 1
    else:
        results["failed"] += 1
        results["errors"].append(f"[{test_name}] FAILED: {error_msg}")

def test_document_upload():
    url = f"{BASE_URL}/documents/upload"
    
    # Generate a simple 1KB dummy PDF for the test if it doesn't exist
    if not os.path.exists("test_sample.pdf"):
        with open("test_sample.pdf", "wb") as f:
            f.write(b"%PDF-1.4\n%" + b"A" * 1024 + b"\n%%EOF")

    try:
        with open("test_sample.pdf", "rb") as f:
            files = {"file": ("test_sample.pdf", f, "application/pdf")}
            # Simulating dynamic metadata extraction
            data = {"metadata": json.dumps({"Division": "Division A", "Report Type": "Financial"})}
            
            response = requests.post(url, files=files, data=data)
            
            if response.status_code in [200, 201]:
                log_result("POST /api/documents/upload", True)
            else:
                log_result("POST /api/documents/upload", False, f"Expected 200/201, got {response.status_code}. Response: {response.text}")
    except requests.exceptions.ConnectionError:
        log_result("POST /api/documents/upload", False, "Connection Refused. Is the Flask server running on port 5000?")
    except Exception as e:
        log_result("POST /api/documents/upload", False, str(e))

def generate_report():
    with open(REPORT_FILE, "w") as f:
        f.write("=== BACKEND API TEST REPORT ===\n")
        f.write(f"Total Endpoints Tested: {results['total']}\n")
        f.write(f"Passed: {results['passed']}\n")
        f.write(f"Failed: {results['failed']}\n\n")
        
        if results["failed"] > 0:
            f.write("=== FAILURE DETAILS ===\n")
            for error in results["errors"]:
                f.write(f"{error}\n")

if __name__ == "__main__":
    print(f"Running automated API tests against {BASE_URL}...")
    
    # Run tests
    test_document_upload()
    # TODO: Add test_authentication(), test_rbac_isolation(), test_search()
    
    # Output report
    generate_report()
    print(f"Testing complete. Summary written to {REPORT_FILE}.")