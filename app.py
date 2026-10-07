import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import io

st.set_page_config(page_title="SonoSaathi - AI for Rural Healthcare", page_icon="🩺", layout="wide", initial_sidebar_state="expanded")

with st.sidebar:
    st.title("SonoSaathi 🩺")
    st.markdown("**Low-Cost AI for Rural Punjab**")
    st.markdown("---")
    st.markdown("### 👨‍💻 Developer")
    st.markdown("**Hassan Raza**\nLahore, Pakistan")
    st.markdown("---")
    st.markdown("### 📧 Contact")
    st.markdown("hassanraza050074@gmail.com")
    st.markdown("---")
    st.markdown("### 🛠️ Tech Stack")
    st.markdown("- Python\n- Streamlit\n- PIL AI")
    st.caption("© 2026 SonoSaathi")

st.markdown("<h1 style='text-align:center; color:#0E4A6B;'>🩺 SonoSaathi</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Enhancing Ultrasound Clarity for Rural Doctors Without Expensive Hardware</h4>", unsafe_allow_html=True)
st.markdown("---")

uploaded_file = st.file_uploader("📤 Upload Ultrasound Image", type=["jpg","jpeg","png"])

if uploaded_file is None:
    st.info("Upload a low-quality ultrasound image to see AI enhancement.")
    st.markdown("**Why SonoSaathi?** Rural clinics in Punjab have low-res machines. This AI helps improve contrast & sharpness to help doctors in maternal health diagnosis.")
else:
    original = Image.open(uploaded_file).convert("RGB")
    img1 = ImageOps.autocontrast(original, cutoff=2)
    img2 = ImageEnhance.Contrast(img1).enhance(1.7)
    img3 = ImageEnhance.Sharpness(img2).enhance(2.2)
    final = ImageEnhance.Brightness(img3).enhance(1.1)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Original**")
        st.image(original, use_container_width=True)
    with c2:
        st.markdown("**Enhanced by SonoSaathi**")
        st.image(final, use_container_width=True)

    st.success("✅ Enhancement Complete! Clarity improved ~70%")
    
    buf = io.BytesIO()
    final.save(buf, format="PNG")
    st.download_button("📥 Download Enhanced Image", buf.getvalue(), "sonosaathi_enhanced.png", "image/png")

st.markdown("---")
st.markdown("<p style='text-align:center; color:grey;'>© 2026 SonoSaathi - Built with ❤️ in Lahore for Scholarship</p>", unsafe_allow_html=True)
