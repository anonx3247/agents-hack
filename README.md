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

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. The application will open in your default web browser
2. Use the sidebar to upload lesson and exercise documents
3. Chat with the assistant in the main interface
4. Uploaded files are automatically categorized and stored in the `uploads` directory

## File Structure

- `app.py`: Main application file
- `requirements.txt`: Project dependencies
- `uploads/`: Directory for uploaded files
  - `cours/`: Lesson documents
  - `exos/`: Exercise documents