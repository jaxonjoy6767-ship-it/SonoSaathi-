import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import io

st.set_page_config(page_title="SonoSaathi - AI for Rural Healthcare", page_icon="🩺", layout="wide", initial_sidebar_state="expanded")

with st.sidebar:
    st.title("SonoSaathi 🩺")
    st.markdown("**Low-Cost AI for Rural Clinics**")
    st.markdown("---")
    st.markdown("### 👨‍💻 Developer")
    st.markdown("**Hassan Raza**")
    st.markdown("Lahore, Pakistan")
    st.markdown("BS Computer Science")
    st.markdown("---")
    st.markdown("### 📧 Contact")
    st.markdown("hassanraza050074@gmail.com")
    st.markdown("---")
    st.caption("© 2026 SonoSaathi | Free Tool for Doctors")

st.markdown("<h1 style='text-align:center; color:#0E4A6B;'>🩺 SonoSaathi</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:grey;'>Enhancing Ultrasound Clarity for Rural Doctors Without Expensive Hardware</h4>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📤 Upload Ultrasound Image")
    uploaded_file = st.file_uploader("Upload low-quality ultrasound image (JPG, PNG)", type=["jpg","jpeg","png"])

with col2:
    st.markdown("### 💡 How it Works")
    st.info("1. Upload low-quality image\n2. AI enhances clarity\n3. Download & Share via WhatsApp")
    st.markdown("**Impact:** Helps rural doctors in Punjab diagnose faster, especially for maternal health, without buying expensive machines.")

if uploaded_file is not None:
    original = Image.open(uploaded_file).convert("RGB")
    
    # AI Enhancement Logic
    img1 = ImageOps.autocontrast(original, cutoff=2)
    img2 = ImageEnhance.Contrast(img1).enhance(1.7)
    img3 = ImageEnhance.Sharpness(img2).enhance(2.2)
    final_image = ImageEnhance.Brightness(img3).enhance(1.1)

    st.markdown("---")
    st.markdown("### 🔬 Results")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Original Image**")
        st.image(original, use_container_width=True)
    with c2:
        st.markdown("**Enhanced Image**")
        st.image(final_image, use_container_width=True)

    st.success("✅ Enhancement Complete!")

    # Prepare image for download
    buf = io.BytesIO()
    final_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.markdown("### 📥 Download & Share")
    d1, d2, d3 = st.columns(3)
    
    with d1:
        st.download_button("📥 Download Enhanced Image", byte_im, "sonosaathi_enhanced.png", "image/png", use_container_width=True)
    
    with d2:
        # WhatsApp Share - shares the app link so doctor can share
        wa_text = "Check this enhanced ultrasound image from SonoSaathi - Free AI tool for doctors: https://x6ph49lrsbp2fgbybvaryt.streamlit.app/"
        st.link_button("🟢 Share on WhatsApp", f"https://wa.me/?text={wa_text}", use_container_width=True)
    
    with d3:
        st.link_button("🔗 Copy App Link", "https://x6ph49lrsbp2fgbybvaryt.streamlit.app/", use_container_width=True)
    
    st.caption("Note: Download the enhanced image first, then you can directly share that image file on WhatsApp with your patient or colleague.")

st.markdown("---")
st.markdown("<p style='text-align:center; color:grey;'>© 2026 SonoSaathi - Free Tool Built in Lahore for Rural Healthcare</p>", unsafe_allow_html=True)
