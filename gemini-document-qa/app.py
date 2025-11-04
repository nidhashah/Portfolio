import gradio as gr
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("GENAI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Function to upload and store file
def upload_file(file_obj):
    if file_obj is None:
        return None, "⚠️ Please upload a PDF file."
    uploaded_file = client.files.upload(file=file_obj.name)
    return uploaded_file.name, f"✅ File '{file_obj.name}' uploaded successfully."

# Function to generate response using the uploaded file
def generate_response(question, file_name):
    if not file_name:
        return "⚠️ Please upload a document first."
    if not question:
        return "⚠️ Please enter a question."

    # Retrieve file reference
    file_ref = client.files.get(name=file_name)
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[question, file_ref],
        config=types.GenerateContentConfig(
            system_instruction="""
You are a Document Intelligence Engine. Answer questions or summarize content using ONLY the information in the uploaded file.
RULES:
  1. Ground all responses strictly in the uploaded document.
  2. If information is not in the document, respond: "Information not found in the document."
  3. Do not use external knowledge or make inferences beyond what's explicitly stated.
RESPONSE TYPES:
  - For specific questions: Provide direct, concise answers.
  - For summary requests: Provide a 3-5 sentence overview of main points.
  - Maintain a professional, clear tone.
If the query is ambiguous, interpret it reasonably based on document context.
"""
        ),
    )
    return response.text


# Gradio UI setup
with gr.Blocks(title="Document Q&A with Gemini") as demo:
    gr.Markdown("## 📄 Document Q&A using Google Gemini")
    gr.Markdown("Upload a PDF and ask a question about its content.")

    with gr.Row():
        file_input = gr.File(label="Upload your PDF", file_types=[".pdf"])
        upload_btn = gr.Button("Upload")

    upload_output = gr.Textbox(label="Upload Status", interactive=False)
    file_name_state = gr.State()

    with gr.Row():
        question_input = gr.Textbox(label="Enter your question", placeholder="Ask something about the document...")
        submit_btn = gr.Button("Get Answer")

    answer_output = gr.Textbox(label="Answer", lines=6, interactive=False)

    # Button actions
    upload_btn.click(upload_file, inputs=[file_input], outputs=[file_name_state, upload_output])
    submit_btn.click(generate_response, inputs=[question_input, file_name_state], outputs=answer_output)


# Run the app
if __name__ == "__main__":
    demo.launch()
