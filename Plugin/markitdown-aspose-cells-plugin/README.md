# MarkItDown markitdown_aspose_cells_plugin


The native MarkItdown tool supports limited file conversions to Markdown. By integrating the markitdown_aspose_cells_plugin, you can extend compatibility to include ODS, XLSB, and other spreadsheet formats.

This project shows how to create an markitdown_aspose_cells_plugin for MarkItDown. The most important parts are as follows:

## Installation

To use the plugin with MarkItDown, it must be installed. To install the plugin from the current directory use:

```bash
pip install -e .
```

Once the plugin package is installed, verify that it is available to MarkItDown by running:

```bash
markitdown --list-plugins
```

To use the plugin for a conversion use the `--use-plugins` flag. For example, to convert an XLSX file:

```bash
markitdown --use-plugins test.xlsx
```

In Python, plugins can be enabled as follows:

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=True) 
result = md.convert("path-to-file.xlsx")
print(result.text_content)
```

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

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
