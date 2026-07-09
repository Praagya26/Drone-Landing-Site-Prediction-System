# Drone Landing Site Prediction System

A deep learning-based image classification system built using **TensorFlow/Keras** to identify potential drone landing environments from aerial images. The application features an interactive **Streamlit** interface that predicts the landing category, displays the confidence score, and provides a landing recommendation.

> **Runs Completely Offline:** Once the dependencies and trained model are available locally, the application runs entirely offline without requiring an internet connection or external APIs.

---

## Features

- Predicts drone landing environments from aerial images
- Classifies images into:
  - 🛬 Runway
  - ⚽ Football Field
  - 🏙️ City
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

![Home Page](assets/home_page.png)

---

### Prediction Result

![Prediction Result](assets/prediction_result 1.png)
![Prediction Result](assets/prediction_result 2.png)
![Prediction Result](assets/prediction_result 3.png)
