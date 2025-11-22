import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from PIL import Image
import pytesseract
import os

class ImageTextExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Extractor")
        self.root.geometry("900x700")
        self.root.configure(bg="#f5f6fa")
        
        # Configure tesseract path
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        # Main container with padding
        main_frame = tk.Frame(root, bg="#f5f6fa")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Title with icon effect
        title_frame = tk.Frame(main_frame, bg="#f5f6fa")
        title_frame.pack(pady=(0, 30))
        
        title_label = tk.Label(title_frame, text="📸 Image Text Extractor", 
                              font=("Segoe UI", 24, "bold"), 
                              bg="#f5f6fa", fg="#2c3e50")
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Extract text from images instantly", 
                                 font=("Segoe UI", 11), 
                                 bg="#f5f6fa", fg="#7f8c8d")
        subtitle_label.pack()
        
        # Button container with modern style
        button_container = tk.Frame(main_frame, bg="#ffffff", relief=tk.FLAT)
        button_container.pack(pady=(0, 20), fill=tk.X, ipady=15)
        
        # Create modern buttons
        btn_frame = tk.Frame(button_container, bg="#ffffff")
        btn_frame.pack(pady=10)
        
        # Select images button - primary action
        self.select_btn = tk.Button(btn_frame, text="📁 Select Images", 
                                    command=self.select_image,
                                    bg="#3498db", fg="white", 
                                    font=("Segoe UI", 11, "bold"),
                                    bd=0, padx=30, pady=12,
                                    cursor="hand2",
                                    activebackground="#2980b9",
                                    activeforeground="white")
        self.select_btn.pack(side=tk.LEFT, padx=5)
        
        # Copy button
        self.copy_btn = tk.Button(btn_frame, text="📋 Copy Text", 
                                 command=self.copy_to_clipboard,
                                 bg="#2ecc71", fg="white", 
                                 font=("Segoe UI", 11),
                                 bd=0, padx=25, pady=12,
                                 cursor="hand2",
                                 activebackground="#27ae60",
                                 activeforeground="white")
        self.copy_btn.pack(side=tk.LEFT, padx=5)
        
        # Save button
        self.save_btn = tk.Button(btn_frame, text="💾 Save File", 
                                 command=self.save_to_file,
                                 bg="#e67e22", fg="white", 
                                 font=("Segoe UI", 11),
                                 bd=0, padx=25, pady=12,
                                 cursor="hand2",
                                 activebackground="#d35400",
                                 activeforeground="white")
        self.save_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        self.clear_btn = tk.Button(btn_frame, text="🗑️ Clear", 
                                  command=self.clear_text,
                                  bg="#95a5a6", fg="white", 
                                  font=("Segoe UI", 11),
                                  bd=0, padx=25, pady=12,
                                  cursor="hand2",
                                  activebackground="#7f8c8d",
                                  activeforeground="white")
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # File info label
        self.file_label = tk.Label(main_frame, text="No images selected", 
                                  font=("Segoe UI", 10), 
                                  bg="#f5f6fa", fg="#95a5a6")
        self.file_label.pack(pady=(0, 15))
        
        # Text area container
        text_container = tk.Frame(main_frame, bg="#ffffff", relief=tk.FLAT)
        text_container.pack(fill=tk.BOTH, expand=True)
        
        # Text area header
        text_header = tk.Frame(text_container, bg="#ffffff")
        text_header.pack(fill=tk.X, padx=20, pady=(15, 5))
        
        tk.Label(text_header, text="Extracted Text", 
                font=("Segoe UI", 12, "bold"), 
                bg="#ffffff", fg="#2c3e50").pack(side=tk.LEFT)
        
        # Text area with modern styling
        text_frame = tk.Frame(text_container, bg="#ffffff")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 15))
        
        self.text_area = scrolledtext.ScrolledText(text_frame, 
                                                   wrap=tk.WORD,
                                                   font=("Consolas", 10),
                                                   bg="#fafafa",
                                                   fg="#2c3e50",
                                                   relief=tk.FLAT,
                                                   padx=15, pady=15,
                                                   insertbackground="#3498db",
                                                   selectbackground="#3498db",
                                                   selectforeground="white",
                                                   bd=1,
                                                   highlightthickness=1,
                                                   highlightbackground="#dfe6e9",
                                                   highlightcolor="#3498db")
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Status bar with modern design
        status_container = tk.Frame(root, bg="#34495e", height=35)
        status_container.pack(side=tk.BOTTOM, fill=tk.X)
        status_container.pack_propagate(False)
        
        self.status_label = tk.Label(status_container, text="Ready to extract text", 
                                    font=("Segoe UI", 9),
                                    bg="#34495e", fg="#ecf0f1",
                                    anchor=tk.W, padx=15)
        self.status_label.pack(fill=tk.BOTH, expand=True)
        
        # Add hover effects to buttons
        self._add_hover_effect(self.select_btn, "#3498db", "#2980b9")
        self._add_hover_effect(self.copy_btn, "#2ecc71", "#27ae60")
        self._add_hover_effect(self.save_btn, "#e67e22", "#d35400")
        self._add_hover_effect(self.clear_btn, "#95a5a6", "#7f8c8d")
    
    def _add_hover_effect(self, button, normal_color, hover_color):
        """Add hover effect to button"""
        button.bind("<Enter>", lambda e: button.config(bg=hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=normal_color))
        
    def select_image(self):
        """Open file dialog to select multiple images"""
        file_paths = filedialog.askopenfilenames(
            title="Select Images (can select multiple)",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.tif"),
                ("All Files", "*.*")
            ]
        )
        
        if file_paths:
            num_files = len(file_paths)
            self.file_label.config(text=f"Selected: {num_files} image(s)")
            self.extract_text_from_multiple(file_paths)
    
    def extract_text_from_multiple(self, image_paths):
        """Extract text from multiple images"""
        try:
            total = len(image_paths)
            self.text_area.delete(1.0, tk.END)
            
            for idx, image_path in enumerate(image_paths, 1):
                self.status_label.config(text=f"Extracting text... ({idx}/{total})")
                self.root.update()
                
                # Open image
                image = Image.open(image_path)
                
                # Extract text using OCR
                extracted_text = pytesseract.image_to_string(image)
                
                # Add separator and filename
                separator = f"\n{'='*60}\n"
                header = f"IMAGE {idx}: {os.path.basename(image_path)}\n{separator}"
                
                # Append extracted text
                self.text_area.insert(tk.END, header)
                self.text_area.insert(tk.END, extracted_text)
                self.text_area.insert(tk.END, "\n")
            
            self.status_label.config(text=f"Successfully extracted text from {total} image(s)!")
            
        except pytesseract.TesseractNotFoundError:
            messagebox.showerror("Error", 
                               "Tesseract OCR is not installed or not found in PATH.\n\n"
                               "Please install Tesseract OCR:\n"
                               "1. Download from: https://github.com/UB-Mannheim/tesseract/wiki\n"
                               "2. Install it\n"
                               "3. Add to PATH or update tesseract_cmd in the code")
            self.status_label.config(text="Error: Tesseract not found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract text:\n{str(e)}")
            self.status_label.config(text="Error occurred")
    
    def copy_to_clipboard(self):
        """Copy extracted text to clipboard"""
        text = self.text_area.get(1.0, tk.END).strip()
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.status_label.config(text="Text copied to clipboard!")
            messagebox.showinfo("Success", "Text copied to clipboard!\nYou can now paste it in Word.")
        else:
            messagebox.showwarning("Warning", "No text to copy!")
    
    def save_to_file(self):
        """Save extracted text to a file"""
        text = self.text_area.get(1.0, tk.END).strip()
        if text:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[
                    ("Text Files", "*.txt"),
                    ("Word Documents", "*.docx"),
                    ("All Files", "*.*")
                ]
            )
            if file_path:
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(text)
                    self.status_label.config(text=f"Saved to {os.path.basename(file_path)}")
                    messagebox.showinfo("Success", f"Text saved to {os.path.basename(file_path)}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save file:\n{str(e)}")
        else:
            messagebox.showwarning("Warning", "No text to save!")
    
    def clear_text(self):
        """Clear the text area"""
        self.text_area.delete(1.0, tk.END)
        self.file_label.config(text="No file selected")
        self.status_label.config(text="Cleared")

def main():
    root = tk.Tk()
    app = ImageTextExtractor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
