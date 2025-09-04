# Certificate Generator

A Python Flask web application that generates personalized certificates from an Excel file and a template image.

## Features
- Upload Excel file (`.xlsx`) with participant names
- Upload certificate template image (PNG/JPEG)
- Automatically generates certificates with participant names
- Download all certificates together as a ZIP file

## Project Overview
This project demonstrates:
- Using Flask to build a simple web application
- Handling file uploads and dynamic image generation
- Automating certificate creation with Python (Pillow library)
- Serving downloadable files to users

## Skills Demonstrated
- Flask for building a web application
- Pandas for handling Excel files
- Pillow (PIL) for image processing and text rendering
- Basic HTML with Bootstrap for a clean interface

## Project Structure
```

certificate-generator/
│── app.py # Flask backend
│── requirements.txt # dependencies
│── README.md # project description
│── LICENSE # license information
│── .gitignore # ignored files configuration
│
├── templates/
│ └── index.html # HTML frontend
│
├── static/
│ └── background.jpeg # background image for the webpage
│
├── samples/
│ ├── names.xlsx # sample Excel file with participant names
│ ├── template1.png # sample certificate template
│ ├── NOTES.md # inputs/outputs explanation
│ └── sample_certificates/ #  few example generated certificates
```

## Example
**Input:** Excel file containing participant names and a certificate template image.  
**Output:** A ZIP file containing personalized certificates (PNG format) for each participant.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`  
2. Run the app: `python app.py`  
3. Open `http://127.0.0.1:5000` in your browser.  



