import tkinter as tk
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

def translate_text():
    """Fetches translated text and updates the output field."""
    input_text = input_text_area.get("1.0", tk.END).strip()
    selected_lang = language_var.get()
    target_lang = lang_name_to_code[selected_lang]  # Convert full name to code
    
    if not input_text:
        messagebox.showwarning("Warning", "Please enter text to translate!")
        return
    
    try:
        translator = Translator()
        translated = translator.translate(input_text, dest=target_lang)
        output_text_area.delete("1.0", tk.END)
        output_text_area.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation Failed: {e}")

# Initialize main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x400")
root.resizable(False, False)

# Available languages
languages = googletrans.LANGUAGES
lang_name_to_code = {languages[code].capitalize(): code for code in languages}
lang_names = list(lang_name_to_code.keys())

# UI Elements
tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack(pady=5)
input_text_area = tk.Text(root, height=5, width=50)
input_text_area.pack(pady=5)

# Dropdown for target language
tk.Label(root, text="Select Target Language:", font=("Arial", 12)).pack(pady=5)
language_var = tk.StringVar()
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=lang_names, state="readonly")
language_dropdown.pack(pady=5)
language_dropdown.current(0)  # Default selection

# Translate Button
translate_button = tk.Button(root, text="Translate", font=("Arial", 12), command=translate_text)
translate_button.pack(pady=10)

# Output Area
tk.Label(root, text="Translated Text:", font=("Arial", 12)).pack(pady=5)
output_text_area = tk.Text(root, height=5, width=50, state="normal")
output_text_area.pack(pady=5)

# Run the application
root.mainloop()