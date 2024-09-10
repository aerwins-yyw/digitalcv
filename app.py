# IMPORTING LIBRARIES
from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV简历 - Albertus Erwin Susanto 阎余文 - EN中文.pdf"
profile_pic = current_dir / "assets" / "Profile Picture.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "CURRICULUM VITAE"
PAGE_ICON = ":wave:"
NAME = "ALBERTUS ERWIN SUSANTO"
姓名 = "閻余文"
DESCRIPTION = """
Aspiring data scientist and policy analyst, assisting public sectors and enterprises by supporting data-driven decision-making.
"""
EMAIL = "altusersanto@gmail.com | yanyw22@mails.tsinghua.edu.cn"
PHONE_WhatsApp = "+62-812-8433-3331"
微信 = "+82-159-1077-2512"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/albertus-erwin-s/",
    "GitHub": "https://github.com/aerwins-yyw",
    "Instagram": "https://www.instagram.com/aubert_erwin/",
    "X": "https://x.com/A_Erwin_S"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2])  # Adjusted column ratio for better layout
with col1:
    # Add some padding around the image to prevent overlap
    st.markdown(
        """
        <style>
        .profile-pic {
            margin-top: 10px;
            margin-bottom: 10px;
            padding-right: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.image(profile_pic, width=230, use_column_width=False, output_format="auto")

with col2:
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 36px; /* Adjust font size as needed */
            white-space: nowrap; /* Prevent wrapping */
            text-align: center; /* Center the text */
        }
        .sub-title {
            font-size: 24px; /* Adjust the subtitle font size */
            white-space: nowrap; /* Prevent wrapping */
            text-align: center; /* Center the text */
        }
        .description {
            font-size: 18px; /* Adjust the description font size */
            text-align: left; /* Center the text */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(f"<h1 class='main-title'>{NAME}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='sub-title'>{姓名}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='description'>{DESCRIPTION}</p>", unsafe_allow_html=True)
# Three Main Principles in Professional Life
st.write('\n')
st.markdown(
    """
    <div style="text-align: left; margin-top: -10px; margin-bottom: 20px;">
        <em>Sincerity, Grit, Innovation</em><br>
    </div>
    """,
    unsafe_allow_html=True
)

# Download Resume Button
st.download_button(
    label=" 📄 Download Résumé",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
)

# --- CONTACTS & SOCIAL MEDIA SECTION ---
st.markdown(f"""
    <style>
    .small-text {{
        font-size: 15px;
        color: #B0B0B0;
    }}
    .social-icon {{
        width: 20px;  /* Size of the social media icon */
        vertical-align: middle;
        margin-right: 10px;  /* Space between icon and text */
    }}
    </style>
    <p class='small-text'>
        📫 Email: {EMAIL}<br>
        📱 WhatsApp: {PHONE_WhatsApp}<br>
        📨 微信: {微信}
    </p>
    """, unsafe_allow_html=True)

# --- SOCIAL MEDIA LINKS WITH ICONS ---
SOCIAL_MEDIA_ICONS = {
    "LinkedIn": "C:/Users/HP/Documents/Digital CV/assets/LinkedIn Logo.webp",
    "GitHub": "C:/Users/HP/Documents/Digital CV/assets/GitHub Logo.png",
    "Instagram": "C:/Users/HP/Documents/Digital CV/assets/Instagram Logo.webp",
    "X": "C:/Users/HP/Documents/Digital CV/assets/X Logo.jpg"
}

# Display social media links with icons
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    icon_url = SOCIAL_MEDIA_ICONS[platform]
    cols[index].markdown(f"""
        <a href="{link}" target="_blank">
            <img src="{icon_url}" class="social-icon"/> {platform}
        </a>
        """, unsafe_allow_html=True)

st.write('\n')

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write("""
- ✔️ 3 Years of Working Experience in Education, Research, and Government Relations
- ✔️ Well-trained in writing and public speaking 
- ✔️ Understanding of statistical principles and applications
- ✔️ Excellent team player and displaying a strong sense of initiative on tasks
- ✔️ Life-long Learner, with focus in public policy, data and AI, enterpreneurship 
""")

# --- SKILLS ---
st.write('\n')
st.subheader("Specific Skills")
st.write("""
- 👩‍💻 Programming: R, Python, SQL
- 📊 Data Visualization: Flourish, R, Plotly, MS Excel, MS Powerpoint, Canva 
- 📚 Modeling: Linear Regression, Logistic Regression, Decision Trees, Combination
- 🗄️ Databases: MySQL, IBM DB2
""")

# --- LANGUAGE ---
st.write('\n')
st.subheader("Language Proficiency")
st.write("""
- 🇮🇩 Indonesian: Native
- 🇬🇧 English: Fluent (IELTS Band 8, TOEFL IBT 104/120)
- 🇨🇳 Chinese: Advance (HSK 6)
- 🇫🇷 French: Intermediate (DELF B2)
""")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---
st.image("C:/Users/HP/Documents/Digital CV/assets/Litbang Kompas Logo.png", width=200)  # Add logo here
st.write("💡", "**Assistant Researcher, Data Analyst, Illustrator | KOMPAS Research & Development**")
st.write("03/2020 - Present")
st.write("""
- ► Doing research on various fields, particularly Indonesia's industrial upstreaming policy, energy transition, AI and Big Data regulation. 
- ► Regular writer to Kompaspedia platform
- ► Research Report Illustrator
""")

# --- JOB 2 ---
st.write('\n')
st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <img src='C:/Users/HP/Documents/Digital CV/assets/Kemenko Marves Logo.png' style='width:50px;'/>
        <img src='C:/Users/HP/Documents/Digital CV/assets/hdcm Logo.png' style='width:50px; margin-right: 10px;'/>
    </div>
    """, 
    unsafe_allow_html=True
)

st.write('\n')
st.write("📊", "**Consultant | Coordinating Ministry for Maritime Affairs and Investment, Republic of Indonesia**")
st.write("08/2021 - 09/2022")
st.write("""
- ► Consultant for Secretariat of High-level Dialogue and Cooperation Mechanism between Republic of Indonesia and People's Republic of China
- ► Coordinating inter-ministerial works and bilateral meetings, supervising investment projects, and hosting business matching forums and focus group discussions
- ► Chinese interpreter and document translations
""")

# --- JOB 3 ---
st.write('\n')
st.image("C:/Users/HP/Documents/Digital CV/assets/Xavier High School Logo.png", width=50)  # Add logo here
st.write("🇫🇲", "**Teacher | Xavier High School, Federated States of Micronesia**")
st.write("08/2019 - 03/2020")
st.write("""
- ► Teaching Ethics, Latin Language, French A1 and Chinese HSK 1-2
- ► Coordinating campus ministry and social service programs
""")

# --- EDUCATION & PROFESSIONAL TRAINING ---
st.write('\n')
st.subheader("Education & Professional Training")
st.write("---")

# Education Section
st.write("🎓", "**Master of Public Administration**")
st.write("Tsinghua University, Beijing, China | 2022 - Present")
st.write("""
- ► Focus Areas: Data Science, Policy Analysis, AI in Business Strategy
- ► GPA: 3.91 (4.00)
- ► Thesis: Impact of ASEAN-Smart City Network on Urban Developments 
""")

st.write('\n')
st.write("🎓", "**Bachelor of Engineering**")
st.write("Universitas Yuppentek Indonesia | 2022 - Present")
st.write("""
- ► Major: Electrical Engineering
- ► GPA: 4.00 (4.00)
- ► Thesis: -
""")

st.write('\n')
st.write("🎓", "**Bachelor of Arts**")
st.write("Driyarkara School of Philosophy, Jakarta, Indonesia | 2015 - 2019")
st.write("""
- ► Major: Philosophy
- ► GPA: 3.99 (4.00)
- ► Thesis: Struggle for Recognition - Axel Honnet's Critical Theory
- ► Driyarkara Journal Coordinator in Chief & Head of Editors 2016-2017; MaGis Community Coordinator 2016-2018; Hermanum College International Students Tutor
""")

# Professional Training Section
st.write('\n')
st.subheader("Professional Training & Certifications")
st.write("""
- 🏅 **Data Science with R Professional Certificate** – Harvard University
- 🏅 **Data Science Professional Certificate** – IBM
- 🏅 **Science and Technology Policy Course** – Massachusetts Institute of Technology
- 🏅 **Project Management Professional Certificate** – University of Adelaide
- 🏅 **French B2** - l’Institut Français d’Indonésie, Jakarta  
""")

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
PROJECTS = {
    "Smart City Research": "https://example.com",
    "AI Policy Analysis": "https://example.com"
}

for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- ARTICLES & PUBLICATIONS ---
st.write('\n')
st.subheader("Articles & Publications")
st.write("---")

ARTICLES = {
    "The Future of Smart Cities: Harnessing AI for Public Policy": "https://example.com/article1",
    "Data-Driven Decision Making in the Public Sector": "https://example.com/article2",
    "The Impact of AI on Science-Technology Innovation Policy": "https://example.com/article3"
}

for article, link in ARTICLES.items():
    st.write(f"[{article}]({link})")
