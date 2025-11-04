# 📄 Gemini Document Q&A

A mini web app that allows users to **upload a PDF** and ask **questions about its contents** using **Google Gemini (`google-genai`)**.

---

## 🚀 Features

- Upload a PDF document
- Ask a question about the document
- Get AI-generated answers grounded **only** in the uploaded file
- Clean and simple web interface using **Gradio**

---

## 🛠️ Technologies Used

- Python 3.x
- Google Gemini 
- Gradio (for web UI)
- python-dotenv (for environment variables)

---

## ⚙️ Setup & Run

1. **Clone the repository**
```bash
   git clone https://github.com/nidhashah/Portfolio.git
   cd gemini-document-qa
```
2. **Install dependencies**
  ```bash
   pip install -r requirements.txt
```
3. **Create a .env file in the folder:**
  ```bash
   GENAI_API_KEY=your_api_key_herec
```
4. **Run the app**
  ```bash
   python app.py
```
5. Open your browser at http://localhost:7860

**🖥️ Usage**

1. Upload a PDF file
2. Enter a question in the text box
3. Click Get Answer
4. The AI will respond with information strictly from the uploaded docume

**⚠️ Notes**
- The app does not use external knowledge, only the uploaded PDF.
- Make sure your API key has proper access to Google Gemini.

**📈 Future Improvements**
- 💬 Add a chat-style interface for multiple queries
- 📄 Support multiple document uploads
- ✨ Display summaries and highlights from the PD
 
