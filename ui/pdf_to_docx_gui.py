import os
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread
from Scripts.pdf_to_docx import convert_pdf_to_docx

class PDFtoDOCXConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PDF to DOCX Converter")
        self.geometry("500x200")

        self.pdf_path = tk.StringVar()
        self.output_path = "D:/"  # Set the default output directory to "D:/"

        self.init_ui()

    def init_ui(self):
        self.label1 = tk.Label(self, text="PDF File Location:")
        self.label1.grid(row=0, column=0, padx=10, pady=5)

        self.pdf_entry = tk.Entry(self, textvariable=self.pdf_path, width=40)
        self.pdf_entry.grid(row=0, column=1, padx=10, pady=5)

        self.pdf_browse_button = tk.Button(self, text="Browse", command=self.browse_pdf)
        self.pdf_browse_button.grid(row=0, column=2, padx=10, pady=5)

        self.label2 = tk.Label(self, text="Output DOCX File Location:")
        self.label2.grid(row=1, column=0, padx=10, pady=5)

        self.output_entry = tk.Entry(self, textvariable=self.output_path, width=30)
        self.output_entry.grid(row=1, column=1, padx=10, pady=5)

        self.output_browse_button = tk.Button(self, text="Browse", command=self.browse_output)
        self.output_browse_button.grid(row=1, column=2, padx=10, pady=5)

        self.convert_button = tk.Button(self, text="Convert", command=self.convert_to_docx)
        self.convert_button.grid(row=2, column=1, padx=10, pady=5)

    def browse_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_path.set(file_path)

    def browse_output(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.output_path = dir_path
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, self.output_path)

    def convert_to_docx(self):
        pdf_path = self.pdf_path.get().strip()
        output_path = os.path.join(self.output_path, os.path.basename(pdf_path.replace(".pdf", ".docx")))

        if not pdf_path:
            messagebox.showwarning("PDF File Location", "Please enter the PDF file location.")
            return
        if not os.path.isfile(pdf_path):
            messagebox.showerror("File Not Found", "PDF file not found at the specified location.")
            return

        self.convert_button.config(state="disabled")
        Thread(target=self.convert_pdf_to_docx, args=(pdf_path, output_path)).start()

    def convert_pdf_to_docx(self, pdf_path, output_path):
        if convert_pdf_to_docx(pdf_path, output_path):
            messagebox.showinfo("Conversion Complete", "PDF to DOCX conversion completed successfully!")
        else:
            messagebox.showerror("Conversion Error", "An error occurred during conversion.")
        self.convert_button.config(state="normal")

if __name__ == "__main__":
    app = PDFtoDOCXConverterGUI()
    app.mainloop()
