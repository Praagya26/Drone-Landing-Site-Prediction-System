🚁 Drone Landing Site Prediction System

A deep learning-based image classification system built using TensorFlow/Keras to identify potential drone landing environments from aerial images. The application features an interactive Streamlit interface that predicts the landing category, displays the confidence score, and provides a landing recommendation.

Runs Completely Offline: Once the dependencies and trained model are available locally, the application runs entirely offline without requiring an internet connection or external APIs.

Features
Predicts drone landing environments from aerial images
Classifies images into:
 Runway
 Football Field
 City
Displays prediction confidence
Provides landing recommendation
Interactive Streamlit interface
Supports JPEG and PNG image uploads
Fully offline inference
Achieves approximately 90–95% classification accuracy
Tech Stack
Python
TensorFlow
Keras
Streamlit
OpenCV
NumPy
Pillow
Matplotlib

Project Structure:

Drone-Landing-Site-Prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── model/
├── sample_images/
├── assets/
└── utils/

Installation:

Clone the repository:

git clone https://github.com/<your-username>/drone-landing-site-prediction.git
cd drone-landing-site-prediction

Create a virtual environment:

python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Linux/macOS

source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Run the application:

streamlit run app.py

Usage:

Launch the Streamlit application.
Upload an aerial image (JPEG or PNG).
The model predicts the landing category.
View the confidence score and landing recommendation.

Screenshots:

Home Page

(Add screenshot here)

Prediction Result

(Add screenshot here)