import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Functions from your original script
def detect_circles(input_img):
    # ... [Your original function here]

def detect_material(input_img, x, y, box_size):
    # ... [Your original function here]

def get_coin_value(c_radius, c_mat):
    # ... [Your original function here]

# Streamlit app begins here
st.title("Coin Detection App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    input_img = np.array(image)  # Convert PIL image to numpy array
    input_img = cv2.cvtColor(input_img, cv2.COLOR_RGB2BGR)  # Streamlit uses RGB, while OpenCV uses BGR

    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Detecting...")

    # Convert to grayscale and blur it slightly
    gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 1.5)

    # Detect circles in the image
    detected_circles = detect_circles(gray)

    if detected_circles is not None:
        # Convert the (x, y) coordinates and radius of the circles to integers
        output = input_img.copy()
        count = 1
        for (x, y, r) in detected_circles[0, :]:
            cv2.circle(output, (x, y), r, (0, 255, 0), 3)
            cv2.circle(output, (x, y), 2, (0, 0, 255), 5)
            c_mat = detect_material(gray, x, y, 15)
            c_value = get_coin_value(r, c_mat)
            cv2.putText(output, f"c:{count}/v:{c_value}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            count += 1

        st.image(output, caption='Processed Image.', use_column_width=True)
    else:
        st.write("No coins detected in the image.")
