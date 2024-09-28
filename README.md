# QR Code Generator

This repository contains two QR code generator implementations in Python: one with a graphical user interface (GUI) using `tkinter` and another command-line version. Both projects allow users to generate QR codes from input URLs.

## Project Overview

### 1. QR Tkinter
- **Description**: A user-friendly QR code generator built using the `tkinter` library. Users can input a URL and generate a QR code, which can be saved with a custom filename. The application features a clean interface and provides success messages upon code generation.
- **Technologies Used**: 
  - Python
  - Tkinter
  - `qrcode`
  - `PIL` (Pillow)

- **Features**:
  - Input field for the URL and optional filename.
  - Generates a scannable QR code.
  - Displays the generated QR code within the GUI.
  - Clear button to reset inputs and output.
  
### 2. QR
- **Description**: A simple command-line QR code generator that allows users to enter a URL and generates a QR code image saved as `qrcode.png`.
- **Technologies Used**:
  - Python
  - `qrcode`
  - `PIL` (Pillow)

- **Features**:
  - Input prompt for the URL.
  - Generates a QR code saved as an image file.
  - Displays error messages for invalid inputs.

## Installation

To run the projects, you will need to have Python installed on your machine. You can install the required libraries using `pip`:

```bash
pip install qrcode[pil]
pip install Pillow
