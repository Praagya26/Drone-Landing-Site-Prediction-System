import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

# ---------------- CONFIG ----------------
IMG_SIZE = 128
CLASSES = ['runway', 'football_field', 'city']

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_my_model():
    return load_model("runway_landing_model.keras")

model = load_my_model()

# ---------------- UI ----------------
st.set_page_config(page_title="Landing Zone Detection", layout="centered")

st.title("✈️ Safe Landing Zone Detection System")
st.write("Upload aerial image to check if aircraft can land safely.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

# ---------------- PREDICTION ----------------
if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = np.array(image)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)[0]

    class_id = np.argmax(pred)
    confidence = pred[class_id] * 100

    st.subheader("📊 Class Probabilities")
    for i, c in enumerate(CLASSES):
        st.write(f"{c}: {pred[i]*100:.2f}%")

    st.subheader("🛬 Final Decision")

    if class_id == 0 and confidence > 80:
        st.success(f"✅ RUNWAY — SAFE TO LAND ({confidence:.2f}%)")

    elif class_id == 1 and confidence > 70:
        st.warning(f"⚠️ FOOTBALL FIELD — EMERGENCY LANDING ONLY ({confidence:.2f}%)")

    else:
        st.error(f"❌ CITY / UNSAFE — DO NOT LAND ({confidence:.2f}%)")