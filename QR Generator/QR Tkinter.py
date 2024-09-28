import qrcode  # type: ignore
from PIL import Image, ImageTk  # type: ignore
import tkinter as tk
from tkinter import messagebox

def generate_qr():
    url = entry_url.get()
    filename = entry_filename.get() or "qrcode"  # Default filename if none is provided

    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{filename}.png")

    # Display the generated QR code in the Tkinter window
    img = Image.open(f"{filename}.png")
    img = img.resize((250, 250))  # Resize for better display
    img_tk = ImageTk.PhotoImage(img)

    label_qr.config(image=img_tk)
    label_qr.image = img_tk  # Keep a reference to avoid garbage collection

    messagebox.showinfo("Success", f"QR code saved as {filename}.png")

def clear_fields():
    entry_url.delete(0, tk.END)
    entry_filename.delete(0, tk.END)
    label_qr.config(image='')  # Clear the displayed image

# Set up the main application window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x400")
root.config(bg="#f0f0f0")

# Frame for inputs
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=20)

# Input field for URL
label_instruction = tk.Label(frame_input, text="Enter your URL:", bg="#f0f0f0", font=("Arial", 12))
label_instruction.grid(row=0, column=0, padx=5)

entry_url = tk.Entry(frame_input, width=30, font=("Arial", 12))
entry_url.grid(row=0, column=1, padx=5)

# Input field for filename
label_filename = tk.Label(frame_input, text="Enter filename (optional):", bg="#f0f0f0", font=("Arial", 12))
label_filename.grid(row=1, column=0, padx=5)

entry_filename = tk.Entry(frame_input, width=30, font=("Arial", 12))
entry_filename.grid(row=1, column=1, padx=5)

# Generate button
button_generate = tk.Button(root, text="Generate QR Code", command=generate_qr, bg="#4CAF50", fg="white", font=("Arial", 12))
button_generate.pack(pady=10)

# Clear button
button_clear = tk.Button(root, text="Clear", command=clear_fields, bg="#f44336", fg="white", font=("Arial", 12))
button_clear.pack(pady=5)

# Label to display the QR code
label_qr = tk.Label(root, bg="#f0f0f0")
label_qr.pack(pady=10)

# Start the application
root.mainloop()
