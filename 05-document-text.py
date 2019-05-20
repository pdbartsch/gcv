# set GOOGLE_APPLICATION_CREDENTIALS=C:\Projects\cloud_vision_ocr\my_gcv.json
    
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
path = os.path.join(
    os.path.dirname(__file__),
    'resources/assemble.JPG')

def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    output = []

    for word in response.full_text_annotation.pages:

        word_text = ''.join([
            symbol.text for symbol in word.symbols
        ])

        output.append(word_text)

    print(" ".join(output))

detect_document(path)