import os
from aspose.cells import Workbook

def get_source_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "01_SourceDirectory")

def get_output_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "02_OutputDirectory")

def read_ods_background():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook = Workbook(os.path.join(source_dir, "GraphicBackground.ods"))

    worksheet = workbook.worksheets[0]

    background = worksheet.page_setup.ods_page_background

    print("Background Type: " + str(background.type))
    print("Background Position: " + str(background.graphic_position_type))

    import io
    from PIL import Image
    
    image_data = background.graphic_data
    image_stream = io.BytesIO(image_data)
    image = Image.open(image_stream)
    
    # Convert RGBA to RGB to avoid JPEG save error
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    output_path = os.path.join(output_dir, "background.jpg")
    image.save(output_path, "JPEG")

    print("ReadODSBackground executed successfully.")

if __name__ == "__main__":
    read_ods_background()