## **OCR Web Application (Hindi + English) with Keyword Search**

### **Overview**
This app allows you to upload an image with text in Hindi or English, extract the text using **Tesseract OCR**, and search for keywords within the extracted text. The keywords are highlighted in **red**.

### **Access the Deployed App**
Visit the deployed app on Streamlit:  
[Access the OCR Web App Here](https://iitroorke)

---

### **Running the App Locally**

#### **For Windows:**

1. **Clone the Project**:
   ```bash
   git clone https://github.com/your-repository/ocr_web_app.git
   cd ocr_web_app
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv ocr_env
   ocr_env\Scripts\activate
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tesseract** from [here](https://github.com/UB-Mannheim/tesseract/wiki), and ensure it's added to your system’s PATH.

5. **Run the App**:
   ```bash
   streamlit run app.py
   ```

#### **For Mac:**

1. **Clone the Project**:
   ```bash
   git clone https://github.com/your-repository/ocr_web_app.git
   cd ocr_web_app
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python3 -m venv ocr_env
   source ocr_env/bin/activate
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tesseract**:
   ```bash
   brew install tesseract
   ```

5. **Run the App**:
   ```bash
   streamlit run app.py
   ```

---

### **File Structure**

```
ocr_web_app/
│
├── app.py            # Main app script
├── ocr.py            # OCR utility functions
├── requirements.txt  # List of dependencies

```

---

### **How to Use the App**

1. **Upload an Image**: Upload an image with Hindi or English text.
2. **View Extracted Text**: The extracted text will appear below the image.
3. **Keyword Search**: Enter a keyword to search, and the matches will be highlighted in **red**.

---

### **Contact**

For any issues or questions, contact [email@example.com].

---

This simple version includes the key steps for deploying and running the OCR app locally or on Streamlit. Let me know if it fits your needs!
