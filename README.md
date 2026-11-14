# 📄 PDF ToolX

**Your PDFs. Your Control.**

PDF ToolX is a web-based PDF utility application built with Python and Django. It provides a simple, modern interface for merging, splitting, converting, securing and extracting content from PDF documents.

## ✨ Features

PDF ToolX provides eight useful PDF operations:

| Feature | Description |
|---|---|
| ➕ Merge PDF | Combine multiple PDF files into one document. |
| ✂️ Split PDF | Extract selected pages from a PDF. |
| 🖼️ Images to PDF | Convert multiple images into a single PDF. |
| 📄 PDF to Images | Convert PDF pages into images and download them as a ZIP file. |
| 🖼️ Extract Images | Extract embedded images from PDF documents. |
| 🔒 Lock PDF | Protect PDF files with a password. |
| 🔓 Unlock PDF | Remove password protection using the correct password. |
| 📝 PDF to DOCX | Convert PDF documents into editable Word files. |

## 🎨 Interface

PDF ToolX features a dark interface with emerald-green accents, designed for a clean and straightforward user experience.

<!-- Add your application screenshots here -->

## 🛠️ Technology Stack

**Backend**
- Python 3.14
- Django 5.2

**Frontend**
- HTML5
- CSS3
- Bootstrap

**PDF and Document Processing**
- PyMuPDF
- PyPDF2
- pdf2docx
- Pillow
- python-docx

**Deployment Preparation**
- WhiteNoise
- Vercel

## 📁 Project Structure

```text
PDF-Utility-Toolkit/
│
├── pdf_toolkit/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── tools/
│   ├── templates/
│   │   └── tools/
│   ├── forms.py
│   ├── utils.py
│   ├── views.py
│   └── urls.py
│
├── static/
├── manage.py
├── requirements.txt
├── .python-version
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AbdulAhad166/PDF-Utility-Toolkit.git
cd PDF-Utility-Toolkit
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside the `pdf_toolkit/` directory.

Add:

```env
SECRET_KEY=your-private-django-secret-key
DEBUG=True
```

Generate your own Django secret key. Never publish your actual secret key or commit your `.env` file to GitHub.

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Collect static files

```bash
python manage.py collectstatic --noinput
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application:

http://127.0.0.1:8000/

## 🚀 Deployment

PDF ToolX is being prepared for deployment on Vercel.

Deployment requires appropriate environment variables, static-file configuration and a compatible strategy for PDF uploads, processing and downloads.

Large file uploads require special consideration because of serverless platform request and response limits.

## 🔮 Future Enhancements

- 📌 PDF Compression
- 📌 Reorder PDF Pages
- 📌 Add Watermarks
- 📌 Additional PDF editing tools
- 📌 Improved file-handling and cloud-storage support

## 🙌 Acknowledgements

This project is based on the original Django-based PDF Tools project by **Malavika Suresh**.

Thanks to the original developer and the open-source communities behind:

- [Django](https://www.djangoproject.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [pdf2docx](https://pypi.org/project/pdf2docx/)
- [Pillow](https://pypi.org/project/pillow/)
- [Bootstrap](https://getbootstrap.com/)

## 📜 License

This project retains the original MIT License and copyright attribution.

Copyright (c) 2025 Malavika Suresh.

See the [LICENSE](LICENSE) file for details.
