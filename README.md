# Math Study Assistant

A Streamlit-based application that helps students study mathematics through an interactive chat interface and document management system.

## Features

- Interactive chat interface for asking questions about mathematics
- Document management system for organizing lessons and exercises
- Support for multiple file formats (PDF, TXT, DOCX)
- Persistent storage of uploaded documents

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the ingestion process to prepare the documents:
```bash
python -m ingestion.ingest_pipeline --source pb-solution
python -m ingestion.ingest_pipeline --source clas-notes
```

4. Run the application:
```bash
python app.py
```

## Usage

1. First, ensure you've run the ingestion process (`python -m ingest.ingest`) to prepare your documents
2. The application will open in your default web browser
3. Use the sidebar to upload lesson and exercise documents
4. Chat with the assistant in the main interface
5. Uploaded files are automatically categorized and stored in the `uploads` directory

## File Structure

- `app.py`: Main application file
- `requirements.txt`: Project dependencies
- `uploads/`: Directory for uploaded files
  - `cours/`: Lesson documents
  - `exos/`: Exercise documents
