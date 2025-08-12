from markitdown import MarkItDown

md = MarkItDown(enable_plugins=True) 
result = md.convert("test.xlsx")
print(result.text_content)