# Use aspose-cells-python as a Marker plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Marker converts XLSX documents to markdown, JSON, and HTML quickly and accurately.  

We can replace **openpyxl** with **aspose-cells-python** in `marker\marker\providers\spreadsheet.py` to achieve the same functionality.  

Marker always converts XLSX files to PDF first, and then to other formats. Marker only supports the XLSX format.

# Installation

You'll need python 3.10+ and [PyTorch](https://pytorch.org/get-started/locally/).

Install with:

```shell
pip install marker-pdf
```

If you want to use marker on documents other than PDFs, you will need to install additional dependencies with:

```shell
pip install marker-pdf[full]
```
When you run the above command in a virtual Python environment, you will find that there are many executable programs in `.venv\Scripts`, such as `marker_single`.  
You can use it to convert a single file, as shown below:

## Convert a single file

```shell
marker_single /path/to/test.xlsx 

marker_single /path/to/test.xlsx  --output_format html
```

Options:
- `--output_format [markdown|json|html|chunks]`: Specify the format for the output results.
- `--output_dir PATH`: Directory where output files will be saved. Defaults to the value specified in settings.OUTPUT_DIR.
- `--debug`: Enable debug mode for additional logging and diagnostic information.
- `--config_json PATH`: Path to a JSON configuration file containing additional settings.
- `config --help`: List all available builders, processors, and converters, and their associated configuration.  These values can be used to build a JSON configuration file for additional tweaking of marker defaults.
- `--help`: see all of the flags that can be passed into marker.  (it supports many more options then are listed above)

## Convert multiple files

```shell
marker /path/to/input/folder
```

- `marker` supports all the same options from `marker_single` above.
- `--workers` is the number of conversion workers to run simultaneously.  This is automatically set by default, but you can increase it to increase throughput, at the cost of more CPU/GPU usage.  Marker will use 5GB of VRAM per worker at the peak, and 3.5GB average.

## Convert multiple files on multiple GPUs

```shell
NUM_DEVICES=4 NUM_WORKERS=15 marker_chunk_convert ../pdf_in ../md_out
```

- `NUM_DEVICES` is the number of GPUs to use.  Should be `2` or greater.
- `NUM_WORKERS` is the number of parallel processes to run on each GPU.

## Use from python

See the `PdfConverter` class at `marker/converters/pdf.py` function for additional arguments that can be passed.

```python
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

converter = PdfConverter(
    artifact_dict=create_model_dict(),
)
rendered = converter("FILEPATH")
text, _, images = text_from_rendered(rendered)
```

`rendered` will be a pydantic basemodel with different properties depending on the output type requested.  With markdown output (default), you'll have the properties `markdown`, `metadata`, and `images`.  For json output, you'll have `children`, `block_type`, and `metadata`.

### Custom configuration

You can pass configuration using the `ConfigParser`.  To see all available options, do `marker_single --help`.

```python
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.config.parser import ConfigParser

config = {
    "output_format": "json",
    "ADDITIONAL_KEY": "VALUE"
}
config_parser = ConfigParser(config)

converter = PdfConverter(
    config=config_parser.generate_config_dict(),
    artifact_dict=create_model_dict(),
    processor_list=config_parser.get_processors(),
    renderer=config_parser.get_renderer(),
    llm_service=config_parser.get_llm_service()
)
rendered = converter("FILEPATH")
```

### Extract blocks

Each document consists of one or more pages.  Pages contain blocks, which can themselves contain other blocks.  It's possible to programmatically manipulate these blocks.  

Here's an example of extracting all forms from a document:

```python
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.schema import BlockTypes

converter = PdfConverter(
    artifact_dict=create_model_dict(),
)
document = converter.build_document("FILEPATH")
forms = document.contained_blocks((BlockTypes.Form,))
```

Look at the processors for more examples of extracting and manipulating blocks.

# Output Formats

## Markdown

Markdown output will include:

- image links (images will be saved in the same folder)
- formatted tables
- embedded LaTeX equations (fenced with `$$`)
- Code is fenced with triple backticks
- Superscripts for footnotes

## HTML

HTML output is similar to markdown output:

- Images are included via `img` tags
- equations are fenced with `<math>` tags
- code is in `pre` tags

## JSON

JSON output will be organized in a tree-like structure, with the leaf nodes being blocks.  Examples of leaf nodes are a single list item, a paragraph of text, or an image.

The output will be a list, with each list item representing a page.  Each page is considered a block in the internal marker schema.  There are different types of blocks to represent different elements.  

Pages have the keys:

- `id` - unique id for the block.
- `block_type` - the type of block. The possible block types can be seen in `marker/schema/__init__.py`.  As of this writing, they are ["Line", "Span", "FigureGroup", "TableGroup", "ListGroup", "PictureGroup", "Page", "Caption", "Code", "Figure", "Footnote", "Form", "Equation", "Handwriting", "TextInlineMath", "ListItem", "PageFooter", "PageHeader", "Picture", "SectionHeader", "Table", "Text", "TableOfContents", "Document"]
- `html` - the HTML for the page.  Note that this will have recursive references to children.  The `content-ref` tags must be replaced with the child content if you want the full html.  You can see an example of this at `marker/output.py:json_to_html`.  That function will take in a single block from the json output, and turn it into HTML.
- `polygon` - the 4-corner polygon of the page, in (x1,y1), (x2,y2), (x3, y3), (x4, y4) format.  (x1,y1) is the top left, and coordinates go clockwise.
- `children` - the child blocks.

The child blocks have two additional keys:

- `section_hierarchy` - indicates the sections that the block is part of.  `1` indicates an h1 tag, `2` an h2, and so on.
- `images` - base64 encoded images.  The key will be the block id, and the data will be the encoded image.

Note that child blocks of pages can have their own children as well (a tree structure).

```json
{
      "id": "/page/10/Page/366",
      "block_type": "Page",
      "html": "<content-ref src='/page/10/SectionHeader/0'></content-ref><content-ref src='/page/10/SectionHeader/1'></content-ref><content-ref src='/page/10/Text/2'></content-ref><content-ref src='/page/10/Text/3'></content-ref><content-ref src='/page/10/Figure/4'></content-ref><content-ref src='/page/10/SectionHeader/5'></content-ref><content-ref src='/page/10/SectionHeader/6'></content-ref><content-ref src='/page/10/TextInlineMath/7'></content-ref><content-ref src='/page/10/TextInlineMath/8'></content-ref><content-ref src='/page/10/Table/9'></content-ref><content-ref src='/page/10/SectionHeader/10'></content-ref><content-ref src='/page/10/Text/11'></content-ref>",
      "polygon": [[0.0, 0.0], [612.0, 0.0], [612.0, 792.0], [0.0, 792.0]],
      "children": [
        {
          "id": "/page/10/SectionHeader/0",
          "block_type": "SectionHeader",
          "html": "<h1>Supplementary Material for <i>Subspace Adversarial Training</i> </h1>",
          "polygon": [
            [217.845703125, 80.630859375], [374.73046875, 80.630859375],
            [374.73046875, 107.0],
            [217.845703125, 107.0]
          ],
          "children": null,
          "section_hierarchy": {
            "1": "/page/10/SectionHeader/1"
          },
          "images": {}
        },
        ...
        ]
    }


```

## Metadata

All output formats will return a metadata dictionary, with the following fields:

```json
{
    "table_of_contents": [
      {
        "title": "Introduction",
        "heading_level": 1,
        "page_id": 0,
        "polygon": [...]
      }
    ], // computed PDF table of contents
    "page_stats": [
      {
        "page_id":  0, 
        "text_extraction_method": "pdftext",
        "block_counts": [("Span", 200), ...]
      },
      ...
    ]
}
```
