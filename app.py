import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="SonoSaathi - by Hassan Raza", layout="centered")

st.title("SonoSaathi 🩺")
st.subheader("Low-Cost Ultrasound Image Enhancement for Rural Clinics")

st.markdown("**Developed by: Hassan Raza | Lahore, Pakistan**")
st.markdown("---")

uploaded_file = st.file_uploader("Upload Ultrasound Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)
    
    # Enhancement
    img_array = np.array(image.convert('L'))
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    enhanced = clahe.apply(img_array)
    
    st.image(enhanced, caption="Enhanced Image - SonoSaathi Result", use_container_width=True, clamp=True)
    
    st.success("Enhancement Complete! Image quality improved for better diagnosis.")
    st.download_button("Download Enhanced Image", data=Image.fromarray(enhanced).tobytes(), file_name="enhanced.png")
else:
    st.info("Please upload an ultrasound image to see the enhancement.")

st.markdown("---")
st.markdown("### About Project")
st.write("SonoSaathi helps doctors in rural areas of Punjab to get clearer ultrasound images using AI enhancement, without expensive hardware.")
st.write("**Mission: Quality healthcare for every village.**")
st.caption("Created for Scholarship Application 2026 | Hassan Raza")
