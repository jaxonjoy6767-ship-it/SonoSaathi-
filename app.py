import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import io
import base64

st.set_page_config(page_title="SonoSaathi - Global Health AI", page_icon="🩺", layout="wide")

# --- CSS for Premium Look ---
st.markdown("""
<style>
    .stDownloadButton button { background-color: #0E76A8; color: white; width: 100%; }
    .share-box { background: #e8f5e9; padding: 20px; border-radius: 15px; text-align: center; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("SonoSaathi 🩺")
    st.markdown("**From Rural Punjab to WHO**")
    st.markdown("---")
    st.markdown("### 👨‍💻 Founder")
    st.markdown("**Hassan Raza**")
    st.markdown("Lahore, Pakistan")
    st.markdown("---")
    st.markdown("### 🎯 Vision")
    st.markdown("Low-cost AI for every rural clinic in the world.")
    st.markdown("---")
    st.link_button("💬 Contact on WhatsApp", "https://wa.me/923000000000")
    st.markdown("📧 hassanraza050074@gmail.com")
    st.markdown("---")
    st.caption("© 2026 SonoSaathi Global")

st.markdown("<h1 style='text-align:center;'>🩺 SonoSaathi</h1><h4 style='text-align:center; color:grey;'>AI that makes a $500 machine work like a $5000 machine</h4>", unsafe_allow_html=True)
st.markdown("---")

uploaded_file = st.file_uploader("📤 اپنی الٹراساؤنڈ تصویر اپلوڈ کریں (Low Quality)", type=["jpg","jpeg","png"])

if uploaded_file is None:
    st.info("👆 اوپر تصویر اپلوڈ کریں اور جادو دیکھیں - تصویر صاف، ڈاؤن لوڈ اور شیئر کے قابل ہو جائے گی۔")
    col1, col2, col3 = st.columns(3)
    col1.metric("Clinics Target", "1000+", "Punjab")
    col2.metric("Cost Saved", "$4500", "Per Machine")
    col3.metric("Goal", "WHO Partnership", "2027")
else:
    original = Image.open(uploaded_file).convert("RGB")
    
    # AI Enhancement
    img1 = ImageOps.autocontrast(original, cutoff=2)
    img2 = ImageEnhance.Contrast(img1).enhance(1.8)
    img3 = ImageEnhance.Sharpness(img2).enhance(2.5)
    final = ImageEnhance.Brightness(img3).enhance(1.1)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Original Image")
        st.image(original, use_container_width=True)
    with c2:
        st.markdown("#### ✨ AI Enhanced by SonoSaathi")
        st.image(final, use_container_width=True)

    st.success("✅ تصویر تیار ہے!")

    # Convert to bytes for download/share
    buf = io.BytesIO()
    final.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.markdown("### 📥 Download & Share")
    d1, d2, d3 = st.columns(3)
    
    with d1:
        st.download_button("📥 Download HD Image", byte_im, "SonoSaathi_Enhanced.png", "image/png", use_container_width=True)
    
    with d2:
        # WhatsApp Share Link
        wa_text = "SonoSaathi se enhanced ki gayi image dekhein - Low cost AI for doctors"
        st.link_button("🟢 WhatsApp پر بھیجیں", f"https://wa.me/?text={wa_text}", use_container_width=True)
    
    with d3:
        # This will copy link - user can share anywhere
        st.link_button("🔗 App کا لنک شیئر کریں", "https://x6ph49lrsbp2fgbybvaryt.streamlit.app/", use_container_width=True)

    st.markdown("---")
    st.markdown("<div class='share-box'><h3>🌍 اس کو بڑا کیسے بنانا ہے؟</h3><p>اگر آپ ڈاکٹر ہیں اور یہ ٹول پسند آیا ہے تو اس کو دوسرے کلینک سے شیئر کریں۔ ہر شیئر سے ہمارا مشن WHO تک پہنچے گا۔</p></div>", unsafe_allow_html=True)

# Earning / Future Plan
st.markdown("---")
st.markdown("### 💰 Earning Model (تمہارے لیے پلان)")
st.markdown("""
1.  **Freemium:** روز کی 5 تصویریں فری، اس کے بعد 500 روپے ماہانہ سبسکرپشن کلینک کے لیے
2.  **NGO / WHO Pitch:** اس ویب سائٹ کو پورٹ فولیو بنا کر WHO, UNICEF کو ایمیل کرو - وہ اس طرح کے low-cost حل کے لیے فنڈنگ دیتے ہیں
3.  **API:** بعد میں اس کو دوسری ہیلتھ ایپس کو کرائے پر دے سکتے ہو
""")
