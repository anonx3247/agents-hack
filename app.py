import streamlit as st
import os
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Math Study Assistant",
    page_icon="📚",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize session state for uploaded files
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = {
        "cours": [],
        "exos": []
    }

# Create directories if they don't exist
os.makedirs("uploads/cours", exist_ok=True)
os.makedirs("uploads/exos", exist_ok=True)

# Sidebar for file upload
with st.sidebar:
    st.title("📚 Document Management")
    
    # File upload section for lessons
    st.subheader("Upload Lessons")
    cours_files = st.file_uploader(
        "Upload lesson documents",
        type=["pdf", "txt", "docx"],
        key="cours_uploader",
        accept_multiple_files=True
    )
    
    # File upload section for exercises
    st.subheader("Upload Exercises")
    exos_files = st.file_uploader(
        "Upload exercise documents",
        type=["pdf", "txt", "docx"],
        key="exos_uploader",
        accept_multiple_files=True
    )
    
    # Display uploaded files
    st.subheader("Uploaded Files")
    
    st.write("**Lessons:**")
    for file in st.session_state.uploaded_files["cours"]:
        st.write(f"- {file}")
    
    st.write("**Exercises:**")
    for file in st.session_state.uploaded_files["exos"]:
        st.write(f"- {file}")

# Main chat interface
st.title("🤖 Math Study Assistant")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Ask your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Display assistant response (placeholder for now)
    with st.chat_message("assistant"):
        response = "I'm your math study assistant! I can help you with your questions and analyze your uploaded documents. What would you like to know?"
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Handle file uploads
def save_uploaded_files(uploaded_files, category):
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            # Create a unique filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}_{uploaded_file.name}"
            
            # Save the file
            file_path = os.path.join("uploads", category, filename)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Add to session state
            if filename not in st.session_state.uploaded_files[category]:
                st.session_state.uploaded_files[category].append(filename)

# Process new file uploads
if cours_files:
    save_uploaded_files(cours_files, "cours")
    st.rerun()

if exos_files:
    save_uploaded_files(exos_files, "exos")
    st.rerun() 