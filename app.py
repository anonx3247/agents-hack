from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
import json
from pathlib import Path
from ingestion.ingest_pipeline import Pipeline
from dotenv import load_dotenv
from agents.main_agent import STEMLearningAgent, save_memories
# Load environment variables

agent = STEMLearningAgent()

load_dotenv()

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)))
COURS_FOLDER = os.path.join(UPLOAD_FOLDER, 'cours')
EXOS_FOLDER = os.path.join(UPLOAD_FOLDER, 'exos')
MARKDOWN_DIR = os.path.join(UPLOAD_FOLDER, 'markdown')
CHROMA_DB_DIR = os.path.join(UPLOAD_FOLDER, 'chroma_db')

# Ensure directories exist
os.makedirs(COURS_FOLDER, exist_ok=True)
os.makedirs(EXOS_FOLDER, exist_ok=True)
os.makedirs(MARKDOWN_DIR, exist_ok=True)
os.makedirs(CHROMA_DB_DIR, exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'md', 'docx', 'doc'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def vectorize_file(file_path, file_type):
    """Vectorize a file based on its type and location."""
    try:
        # Determine source type based on file extension and location
        if file_path.endswith('.pdf'):
            source_type = 'pdf'
        elif os.path.dirname(file_path) == EXOS_FOLDER:
            source_type = 'exos'
        else:
            source_type = 'class-notes'

        # Create pipeline instance with default values if env vars are not set
        pipeline = Pipeline(
            source_type=source_type,
            source_dir=os.path.dirname(file_path),
            md_dir=MARKDOWN_DIR,
            db_dir=CHROMA_DB_DIR,
            embedding_model=os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"),
            chunk_size=int(os.getenv("CHUNK_SIZE", "512")),
            chunk_overlap=int(os.getenv("CHUNK_OVERLAP", "50"))
        )

        # Run pipeline
        pipeline.run()
        return True
    except Exception as e:
        print(f"Error vectorizing file {file_path}: {str(e)}")
        return False

def vectorize_existing_files():
    """Vectorize all existing files in cours and exos directories."""
    print("Vectorizing existing files...")
    
    # Vectorize files in cours directory
    for filename in os.listdir(COURS_FOLDER):
        if allowed_file(filename):
            file_path = os.path.join(COURS_FOLDER, filename)
            vectorize_file(file_path, 'cours')
    
    # Vectorize files in exos directory
    for filename in os.listdir(EXOS_FOLDER):
        if allowed_file(filename):
            file_path = os.path.join(EXOS_FOLDER, filename)
            vectorize_file(file_path, 'exos')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Determine which folder to save to based on the upload type
        folder = COURS_FOLDER if request.form.get('type') == 'cours' else EXOS_FOLDER
        file_path = os.path.join(folder, filename)
        file.save(file_path)
        
        # Vectorize the uploaded file
        success = vectorize_file(file_path, request.form.get('type'))
        if not success:
            return jsonify({'error': 'Error vectorizing file'}), 500
            
        return jsonify({'message': 'File uploaded and vectorized successfully', 'filename': filename})
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/files/<type>')
def list_files(type):
    folder = COURS_FOLDER if type == 'cours' else EXOS_FOLDER
    files = []
    for filename in os.listdir(folder):
        if allowed_file(filename):
            files.append({
                'name': filename,
                'size': os.path.getsize(os.path.join(folder, filename)),
                'modified': os.path.getmtime(os.path.join(folder, filename))
            })
    return jsonify(files)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    # Here you would integrate with your AI agent
    # For now, we'll just echo back
    response = agent.run(message)
    return jsonify({'response': response})

# Vectorize existing files on startup
vectorize_existing_files()

if __name__ == '__main__':
    app.run(debug=True) 
