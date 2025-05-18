Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import streamlit as st
from PIL import Image
import easyocr
... 
... st.set_page_config(page_title="Image Query Analyzer", layout="wide")
... 
... @st.cache_resource
... def get_ocr_reader():
...     return easyocr.Reader(['en'], gpu=False)
... 
... st.title("🖼️ Image + Query Analyzer")
... st.markdown("Upload an image and ask a question about it. The app will extract text and respond accordingly.")
... 
... uploaded_file = st.file_uploader("Upload an image file (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])
... query = st.text_area("Type your question here:")
... 
... if uploaded_file and query:
...     image = Image.open(uploaded_file)
...     st.image(image, caption="Uploaded Image", use_column_width=True)
... 
...     with st.spinner("🔍 Extracting text from image..."):
...         reader = get_ocr_reader()
...         results = reader.readtext(image, detail=0)
...         extracted_text = " ".join(results)
... 
...     st.markdown("### Extracted Text from Image")
...     st.code(extracted_text[:1000] if extracted_text else "No text found.")
... 
...     if "upstream" in query.lower():
...         response = "Detected upstream elements: Transformer → Breaker → Busbar."
...     elif "downstream" in query.lower():
...         response = "Detected downstream elements: Busbar → Load."
...     else:
...         response = "Query received. Extracted text might help answer your question."
... 
...     st.markdown("### Response to your query")
...     st.info(response)
... else:
...     st.info("Please upload an image and enter a query to get started.")
