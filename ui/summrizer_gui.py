import tkinter as tk
from tkinter import filedialog, messagebox
from Scripts.sumrizer import summarize_pdf

class PDFSummarizerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.title("PDF Summarizer")
        self.geometry("300x100")
        
        upload_button = tk.Button(self, text="Upload PDF", command=self.upload_pdf)
        upload_button.pack(pady=20)

    def upload_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            summarized_text = summarize_pdf(file_path)
            messagebox.showinfo("PDF Summary", summarized_text)

if __name__ == "__main__":
    app = PDFSummarizerGUI()
    app.mainloop()
