# Use aspose-cells-python as a Docling plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Docling converts XLSX documents to markdown, JSON, and HTML quickly and accurately.  

We can replace **openpyxl** with **aspose-cells-python** in `docling\docling\backend\msexcel_backend.py` to achieve the same functionality.  

Docling only supports the XLSX format.

## Features

* 🗂️  Parsing of [multiple document formats][supported_formats] incl. PDF, DOCX, PPTX, XLSX, HTML, WAV, MP3, images (PNG, TIFF, JPEG, ...), and more
* 📑 Advanced PDF understanding incl. page layout, reading order, table structure, code, formulas, image classification, and more
* 🧬 Unified, expressive [DoclingDocument][docling_document] representation format
* ↪️  Various [export formats][supported_formats] and options, including Markdown, HTML, [DocTags](https://arxiv.org/abs/2503.11576) and lossless JSON
* 🔒 Local execution capabilities for sensitive data and air-gapped environments
* 🤖 Plug-and-play [integrations][integrations] incl. LangChain, LlamaIndex, Crew AI & Haystack for agentic AI
* 🔍 Extensive OCR support for scanned PDFs and images
* 👓 Support of several Visual Language Models ([SmolDocling](https://huggingface.co/ds4sd/SmolDocling-256M-preview))
* 🎙️  Support for Audio with Automatic Speech Recognition (ASR) models
* 💻 Simple and convenient CLI

 
## Installation

To use Docling, simply install `docling` from your package manager, e.g. pip:
```bash
pip install -e .
```

Works on macOS, Linux and Windows environments. Both x86_64 and arm64 architectures.

More [detailed installation instructions](https://docling-project.github.io/docling/installation/) are available in the docs.

## Getting started

```python
docling  /path/test.xlsx --to html
docling  /path/test.xlsx --to md
docling  /path/test.xlsx --to json
```

More [advanced usage options](https://docling-project.github.io/docling/usage/) are available in
the docs.


## Set License

### Environment Variables
To activate your Aspose License, set the corresponding environment variable. Refer to the OS-specific instructions below:

**Windows (PowerShell):**

```powershell
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

**Windows (CMD):**

```powershell
set ASPOSE_LICENSE_PATH = C:\path\to\license
```

**Unix-based systems:**

```bash
export ASPOSE_LICENSE_PATH="/path/to/license"
```


