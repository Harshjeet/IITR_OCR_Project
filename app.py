import streamlit as st
from PIL import Image  # Importing the Image module from Pillow
from ocr import extract_text_from_image

# Title and description of the app
st.title("OCR Web Application")
st.write("""
Upload an image that contains text in Hindi or English, and the app will extract the text. 
Also search for keywords in the extracted text.
""")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Extract text from the image using OCR
    extracted_text = extract_text_from_image(image)
    
    # Display the extracted text
    st.write("### Extracted Text:")
    st.write(extracted_text)
    
    # Keyword search functionality
    keyword = st.text_input("Enter a keyword to search:")
    
    if keyword:
        # Highlight the keyword in red color
        highlighted_text = extracted_text.replace(
            keyword, f'<span style="color:red;">{keyword}</span>'
        )
        st.write("### Search Results:")
        st.markdown(highlighted_text, unsafe_allow_html=True) 
