import streamlit as st
from PIL import Image
from pathlib import Path
import base64

# Page configuration
st.set_page_config(page_title="Linguistic to Logic - About us", page_icon=":anchor:", layout="wide")
st.markdown('<h1 style="text-align: center;">LINGUISTIC TO LOGIC - THE SQL CONVERTER (LTL-SQL)</h1>', unsafe_allow_html=True)
st.markdown('')
st.markdown('')

# Team section
st.markdown('<h2>TEAM - CODE SYNDICATE</h2>', unsafe_allow_html=True)
st.markdown('<h3>About Us</h3>', unsafe_allow_html=True)
st.markdown("**Code Syndicate** is an innovative and dynamic team of three 3rd-year B.Tech students from Amrita Vishwa Vidyapeetham, Coimbatore. Driven by our passion for technology and problem-solving, we have come together to push the boundaries of what's possible in the realm of software development and data processing.")
st.markdown("<hr>", unsafe_allow_html=True)

# Team member profiles (replace with your actual images and descriptions)
st.markdown('<h3>Our Team</h3>', unsafe_allow_html=True)
st.markdown('')
col1, col2, col3, col4 = st.columns(4)

with col1:
    img_bytes = Path('Media\Images\ganesh.png').read_bytes()
    image = base64.b64encode(img_bytes).decode()
    st.markdown(f"""
    <div style="text-align: center; margin-left: 16%; margin-right: 16%;">
        <div style="margin-bottom: 25px;">
            <img src="data:image/png;base64,{image}" width="300" style="border-radius: 10px;" alt="Ganesh Sundhar S">
        </div>
        <div style="margin-bottom: 10px;">
            <strong>Ganesh Sundhar S</strong>
        </div>
        <div style="margin-bottom: 10px;">
            CSE(AI) AVV Coimbatore
        </div>
        <div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
            <span>Contact :</span>
            <a href="https://www.linkedin.com/in/ganesh2609/" target="_blank">
                <img src="https://static.vecteezy.com/system/resources/previews/023/986/970/non_2x/linkedin-logo-linkedin-logo-transparent-linkedin-icon-transparent-free-free-png.png" width="32" alt="LinkedIn">
            </a>
            <a href="https://github.com/Ganesh2609" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="32" alt="GitHub">
            </a>
            <a href="https://leetcode.com/u/Ganesh2609/" target="_blank">
                <img src="https://media.dev.to/cdn-cgi/image/width=320,height=320,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1139481%2Ff5ce3759-1e67-44a6-8041-9599b8148e50.png" width="32" alt="LeetCode">
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    img_bytes = Path('Media\Images\hari.png').read_bytes()
    image = base64.b64encode(img_bytes).decode()
    st.markdown(f"""
    <div style="text-align: center; margin-left: 16%; margin-right: 16%;">
        <div style="margin-bottom: 25px;">
            <img src="data:image/png;base64,{image}" width="300" style="border-radius: 10px;" alt="Ganesh Sundhar S">
        </div>
        <div style="margin-bottom: 10px;">
            <strong>Hari Krishnan N</strong>
        </div>
        <div style="margin-bottom: 10px;">
            CSE(AI) AVV Coimbatore
        </div>
        <div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
            <span>Contact :</span>
            <a href="https://www.linkedin.com/in/ganesh2609/" target="_blank">
                <img src="https://static.vecteezy.com/system/resources/previews/023/986/970/non_2x/linkedin-logo-linkedin-logo-transparent-linkedin-icon-transparent-free-free-png.png" width="32" alt="LinkedIn">
            </a>
            <a href="https://github.com/Ganesh2609" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="32" alt="GitHub">
            </a>
            <a href="https://leetcode.com/u/Ganesh2609/" target="_blank">
                <img src="https://media.dev.to/cdn-cgi/image/width=320,height=320,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1139481%2Ff5ce3759-1e67-44a6-8041-9599b8148e50.png" width="32" alt="LeetCode">
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    img_bytes = Path('Media\Images\dhanush.png').read_bytes()
    image = base64.b64encode(img_bytes).decode()
    st.markdown(f"""
    <div style="text-align: center; margin-left: 16%; margin-right: 16%;">
        <div style="margin-bottom: 25px;">
            <img src="data:image/png;base64,{image}" width="300" style="border-radius: 10px;" alt="Ganesh Sundhar S">
        </div>
        <div style="margin-bottom: 10px;">
            <strong>Dhanush MC</strong>
        </div>
        <div style="margin-bottom: 10px;">
            CSE(AI) AVV Coimbatore
        </div>
        <div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
            <span>Contact :</span>
            <a href="https://www.linkedin.com/in/dhanush-m-c-668055258/" target="_blank">
                <img src="https://static.vecteezy.com/system/resources/previews/023/986/970/non_2x/linkedin-logo-linkedin-logo-transparent-linkedin-icon-transparent-free-free-png.png" width="32" alt="LinkedIn">
            </a>
            <a href="https://github.com/DhanushMC" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="32" alt="GitHub">
            </a>
            <a href="https://leetcode.com/u/Ganesh2609/" target="_blank">
                <img src="https://media.dev.to/cdn-cgi/image/width=320,height=320,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1139481%2Ff5ce3759-1e67-44a6-8041-9599b8148e50.png" width="32" alt="LeetCode">
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    
with col4:
    img_bytes = Path('Media\Images\premjith_sir.png').read_bytes()
    image = base64.b64encode(img_bytes).decode()
    st.markdown(f"""
    <div style="text-align: center; margin-left: 16%; margin-right: 16%;">
        <div style="margin-bottom: 25px;">
            <img src="data:image/png;base64,{image}" width="300" style="border-radius: 10px;" alt="Ganesh Sundhar S">
        </div>
        <div style="margin-bottom: 10px;">
            <strong>Dr.Premjith B</strong>
        </div>
        <div style="margin-bottom: 10px;">
            Mentor
        </div>
        <div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
            Asst. Professor (AVV Coimbatore)
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<hr>", unsafe_allow_html=True)
    
# Contact Us Section
st.markdown('<h2>📱Contact Us</h2>', unsafe_allow_html=True)
st.markdown("""
We would love to hear from you! Whether you have a question about our project, want to collaborate, or just want to say hi, feel free to reach out to us.

 **📨 Email:** 
  - Ganesh Sundhar S: [ganeshsundhar007@gmail.com](mailto:ganeshsundhar007@gmail.com)
  - Hari Krishnan N: [hariprabha1979@gmail.com](mailto:hariprabha1979@gmail.com)
  - Dhanush MC: [mcdhanush1122@outlook.com](mailto:mcdhanush1122@outlook.com)

 **📞 Phone:** 
  - Ganesh Sundhar S: [9677236828](tel:9677236828)
  - Hari Krishnan N: [6379266196](tel:6379266196)
  - Dhanush MC: [6383269837](tel:6383269837)
""")