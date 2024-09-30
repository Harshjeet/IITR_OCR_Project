import pytesseract
from PIL import Image
import cv2
import numpy as np

# Preprocessing Function to improve OCR accuracy
def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    
    # Apply binary thresholding
    _, binary_img = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Denoise the image
    denoised_img = cv2.GaussianBlur(binary_img, (5, 5), 0)
    
    return Image.fromarray(denoised_img)

# Tesseract OCR Function to extract text
def extract_text_from_image(image):
    # Preprocess the image for better accuracy
    processed_image = preprocess_image(image)
    
    # Perform OCR using Tesseract for both Hindi and English
    extracted_text = pytesseract.image_to_string(processed_image, lang='eng+hin')
    
    return extracted_text
