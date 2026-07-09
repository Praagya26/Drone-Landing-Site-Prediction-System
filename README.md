# Drone Landing Site Prediction System

A deep learning-based image classification system built using **TensorFlow/Keras** to identify potential drone landing environments from aerial images. The application features an interactive **Streamlit** interface that predicts the landing category, displays the confidence score, and provides a landing recommendation.

> **Runs Completely Offline:** Once the dependencies and trained model are available locally, the application runs entirely offline without requiring an internet connection or external APIs.

---

## Features

- Predicts drone landing environments from aerial images
- Classifies images into:
  -  Runway
  -  Football Field
  -  City
- Displays prediction confidence
- Provides landing recommendation
- Interactive Streamlit interface
- Supports JPEG and PNG image uploads
- Fully offline inference
- Achieves approximately **90–95% classification accuracy**

---

## Tech Stack

- Python
- TensorFlow
- Keras
- Streamlit
- OpenCV
- NumPy
- Pillow
- Matplotlib

---

## Project Structure

```text
Drone-Landing-Site-Prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── runway_landing_model.keras
├── model_training.ipynb
├── assets/
└── test images/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Praagya26/Drone-Landing-Site-Prediction-System.git
cd Drone-Landing-Site-Prediction-System
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Usage

1. Launch the Streamlit application.
2. Upload an aerial image (`.jpg` or `.png`).
3. View the predicted landing category.
4. Check the confidence score.
5. Read the landing recommendation.

---

## Screenshots

### Home Page
<img width="1917" height="1023" alt="home_page" src="https://github.com/user-attachments/assets/bbc19917-d3f3-424b-9e44-3ee26800ce37" />

---

### Prediction Result
<img width="1917" height="1028" alt="prediction_result 1" src="https://github.com/user-attachments/assets/34e24ce6-18c5-450b-b989-6c244ede32d3" />
<img width="1918" height="1007" alt="prediction_result 2" src="https://github.com/user-attachments/assets/5e4c776c-9d34-4ef3-b42f-92884dcc528a" />
<img width="1918" height="952" alt="prediction_result 3" src="https://github.com/user-attachments/assets/32f913f4-05c9-4a6f-be84-23efd9a73231" />

---

