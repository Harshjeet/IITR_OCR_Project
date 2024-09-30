# Use a base image with Python
FROM python:3.9-slim

# Install system dependencies (including Tesseract)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-hin \
    libgl1-mesa-glx

# Set the working directory
WORKDIR /app

# Copy your app files into the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the Streamlit port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py"]
