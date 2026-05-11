# Excel Scientific Analysis Agent

This project combines:

- Aspose.Cells for Python via .NET
- NumPy
- SciPy
- OpenAI

The system can:

- Read Excel files
- Detect numeric columns
- Run scientific analysis
- Generate charts
- Highlight anomalies
- Export analysis reports

## Run

```bash
pip install -r requirements.txt
python app/main.py
````

````

---

# app/config.py

```python
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
````
