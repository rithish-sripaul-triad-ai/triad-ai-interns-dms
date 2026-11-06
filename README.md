# Triad AI \- DMS Take-Home Assignment Test Suite

Welcome to the automated test repository for the Triad AI Document Management System (DMS) internship assignment. This repository contains the test script (`test_api.py`) used to evaluate your backend REST API.

## Expected Project Structure

To keep submissions consistent and clean, we expect your project to broadly follow this structure:

```
your_submission/
├── app/
│   ├── __init__.py
│   ├── routes.py          # REST API endpoints (auth, documents, search, access)
│   ├── models.py          # MongoDB schemas/models
│   ├── ocr.py             # OCR processing logic
│   └── utils.py           # Helpers and RBAC logic
├── test_api.py            # The provided test script
├── test_sample.pdf        # Auto-generated or provided dummy PDF for testing
├── requirements.txt       # Python dependencies (Flask, PyMongo, etc.)
├── Dockerfile             # (Optional but recommended) Docker configuration
├── docker-compose.yml     # (Optional) To spin up the Flask app and MongoDB together
└── README.md              # Setup instructions for your project
```

## How to Run the Tests

You can use the provided `test_api.py` script to validate your endpoints locally before submitting. The script acts as a client, making HTTP requests to your Flask server to evaluate functionality, metadata handling, and RBAC isolation rules.

### Prerequisites

1. Ensure your backend Flask server is running locally (the test script defaults to `http://localhost:5000/api`).  
2. Ensure your MongoDB instance (local or Docker container) is running and accessible to your backend.  
3. Install the required `requests` library in your local environment if you haven't already:

```sh
pip install requests
```

### Execution Steps

1. Open your terminal and navigate to the directory containing `test_api.py`.  
2. Run the test script:

```sh
python test_api.py
```

3. The script will automatically ping your endpoints (e.g., `POST /api/documents/upload`), simulate file uploads with dynamic metadata, and verify the status codes and responses.  
4. Upon completion, a `test_report.txt` file will be generated in the same directory.

### Understanding the Output

Open `test_report.txt` to review your results. It will display:

* The total number of endpoints tested.  
* The number of passed and failed tests.  
* Specific error logs and response codes for any failed assertions to help you debug before your final submission.