from flask import Flask, render_template, request, send_file
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import zipfile
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")  

@app.route('/generate', methods=['POST'])
def generate():
    # Getting uploaded files
    excel_file = request.files['excel']
    template_file = request.files['template']

    # Reading names from Excel
    df = pd.read_excel(excel_file)

    # Loading template
    base_template = Image.open(template_file.stream)

  
    name_x = 950   # horizontal pixel position
    name_y = 780   # vertical pixel position

   
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zipf:
        for name in df['Name']:
           
            template = base_template.copy()
            draw = ImageDraw.Draw(template)

           
            font = ImageFont.truetype("arial.ttf", 60)

           
            draw.text((name_x, name_y), name, fill="black", font=font, anchor="mm")

            # Saving certificate 
            img_bytes = BytesIO()
            template.save(img_bytes, format="PNG")
            img_bytes.seek(0)

            # Add to ZIP
            zipf.writestr(f"{name}.png", img_bytes.getvalue())

    
    zip_buffer.seek(0)

    # Sending ZIP to user
    return send_file(
        zip_buffer,
        as_attachment=True,
        download_name="certificates.zip",
        mimetype="application/zip"
    )

if __name__ == "__main__":
    app.run(debug=True)
