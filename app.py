# IMPORTING LIBRARIES
from pathlib import Path
import streamlit as st
from PIL import Image
import base64

# --- PATH SETTINGS ---
current_dir = Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV简历 - Albertus Erwin Susanto 阎余文 - EN中文.pdf"
profile_pic = current_dir / "assets" / "Profile Picture.png"
# Logos
linkedin_logo = current_dir / "assets" / "LinkedIn Logo.png"
github_logo = current_dir / "assets" / "GitHub Logo.png"
instagram_logo = current_dir / "assets" / "Instagram Logo.png"
x_logo = current_dir / "assets" / "X Logo.jpg"
kompas_logo = current_dir / "assets" / "Litbang Kompas Logo.png"
kemenko_logo = current_dir / "assets" / "Kemenko Marves Logo.png"
hdcm_logo = current_dir / "assets" / "hdcm logo.png"
xavier_logo = current_dir / "assets" / "Xavier High School Logo.png"

# Function to convert images to base64
def img_to_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Convert logos to base64
linkedin_img_base64 = img_to_base64(linkedin_logo)
github_img_base64 = img_to_base64(github_logo)
instagram_img_base64 = img_to_base64(instagram_logo)
x_img_base64 = img_to_base64(x_logo)
kompas_logo_base64 = img_to_base64(kompas_logo)
kemenko_logo_base64 = img_to_base64(kemenko_logo)
hdcm_logo_base64 = img_to_base64(hdcm_logo)
xavier_logo_base64 = img_to_base64(xavier_logo)

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

# --- CONTACTS SECTION ---
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

# --- SOCIAL MEDIA SECTION --- 
st.markdown(
    f"""
    <div style="display: flex; justify-content: space-evenly; align-items: center;">
        <a href="https://www.linkedin.com/in/albertus-erwin-s/" target="_blank" style="text-decoration: none;">
            <img src="data:image/webp;base64,{linkedin_img_base64}" width="20" style="vertical-align:middle; margin-right: 10px;">
            LinkedIn
        </a>
        <a href="https://github.com/aerwins-yyw" target="_blank" style="text-decoration: none; margin-left: 20px;">
            <img src="data:image/png;base64,{github_img_base64}" width="20" style="vertical-align:middle; margin-right: 10px;">
            GitHub
        </a>
        <a href="https://www.instagram.com/aubert_erwin/" target="_blank" style="text-decoration: none; margin-left: 20px;">
            <img src="data:image/webp;base64,{instagram_img_base64}" width="20" style="vertical-align:middle; margin-right: 10px;">
            Instagram
        </a>
        <a href="https://x.com/A_Erwin_S" target="_blank" style="text-decoration: none; margin-left: 20px;">
            <img src="data:image/jpg;base64,{x_img_base64}" width="20" style="vertical-align:middle; margin-right: 10px;">
            X
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)
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
# Display the logo with base64 and the text using st.write()
st.markdown(f"""
    <div style="text-align: left; margin-bottom: 20px;">
        <img src="data:image/png;base64,{kompas_logo_base64}" style="width:200px;">
    </div>
""", unsafe_allow_html=True)

st.write("💡", "**Assistant Researcher, Data Analyst, Illustrator | KOMPAS Research & Development**")
st.write("03/2020 - Present")
st.write("""
- ⁜ Doing research on various fields, particularly Indonesia's industrial upstreaming policy, energy transition, AI and Big Data regulation. 
- ⁜ Regular writer to Kompaspedia platform
- ⁜ Research report illustrator
""")
st.write('\n')

# --- JOB 2 ---
# Display both logos side by side using base64
st.markdown(f"""
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <img src="data:image/png;base64,{kemenko_logo_base64}" style="width:70px; margin-right: 10px;">
        <img src="data:image/png;base64,{hdcm_logo_base64}" style="width:50px;">
    </div>
""", unsafe_allow_html=True)

st.write("📊", "**Consultant | Coordinating Ministry for Maritime Affairs and Investment, Indonesia**")
st.write("08/2021 - 09/2022")
st.write("""
- ⁜ Consultant for Secretariat of High-level Dialogue and Cooperation Mechanism between Republic of Indonesia and People's Republic of China
- ⁜ Coordinating inter-ministerial works and bilateral meetings, supervising investment projects, and hosting business matching forums and focus group discussions
- ⁜ Chinese interpreter and document translations
""")
st.write('\n')

# --- JOB 3 ---
# Display both logos side by side using base64
st.markdown(f"""
    <div style="text-align: left; margin-bottom: 20px;">
        <img src="data:image/png;base64,{xavier_logo_base64}" style="width:50px;">
    </div>
""", unsafe_allow_html=True)

st.write("🇫🇲", "**Teacher | Xavier High School, Federated States of Micronesia**")
st.write("08/2019 - 03/2020")
st.write("""
- ⁜ Teaching Ethics, Latin Language, French A1 and Chinese HSK 1-2
- ⁜ Coordinating campus ministry and social service programs
""")

# --- EDUCATION & PROFESSIONAL TRAINING ---
st.write('\n')
st.subheader("Education & Professional Training")
st.write("---")

# Education Section
st.write("🎓", "**Master of Public Administration**")
st.write("Tsinghua University, Beijing, China | 2022 - Present")
st.write("""
- ⁜ Focus Areas: Data Science, Policy Analysis, AI in Business Strategy
- ⁜ GPA: 3.91 (4.00)
- ⁜ Thesis: Impact of ASEAN-Smart City Network on Urban Developments
- ⁜ Center for Science, Technology, and Education Policy Research Team Member
""")

st.write('\n')
st.write("🎓", "**Bachelor of Engineering**")
st.write("Universitas Yuppentek Indonesia | 2022 - Present")
st.write("""
- ⁜ Major: Electrical Engineering
- ⁜ GPA: 4.00 (4.00)
- ⁜ Thesis: -
""")

st.write('\n')
st.write("🎓", "**Bachelor of Arts**")
st.write("Driyarkara School of Philosophy, Jakarta, Indonesia | 2015 - 2019")
st.write("""
- ⁜ Major: Philosophy
- ⁜ GPA: 3.99 (4.00)
- ⁜ Thesis: Struggle for Recognition - Axel Honnet's Critical Theory
- ⁜ Driyarkara Journal Coordinator in Chief & Head of Editors 2016-2017
- ⁜ MaGis Community Coordinator 2016-2018 
- ⁜ Hermanum College International Students Tutor
""")

# Professional Training Section
st.write('\n')
st.subheader("Professional Training & Certifications")
st.write("""
- 🏅 **Data Science with R Professional Certificate** – Harvard University 
- 🏅 **Data Science Professional Certificate** – IBM 
- 🏅 **[Project Management Professional Certificate](https://credentials.edx.org/credentials/c7cad5d671ef48e48e9dbdee429acfa1/)** – University of Adelaide ([details](https://cloud.tsinghua.edu.cn/f/762e4ba360344e7682a0/?dl=1)) 
- 🏅 **[Becoming an Entrepreneur](https://courses.edx.org/certificates/a36b3607414441198b9f3878d771a597)** – Massachusetts Institute of Technology
- 🏅 **[Macroeconomics Professional Certificate](https://credentials.edx.org/credentials/b97f11b39f394159bbbcb6107ac66251/)** – University of Queensland ([details](https://cloud.tsinghua.edu.cn/f/b9b0da3770dd4fcfb4ad/?dl=1)) 
- 🏅 **French B2** – l’Institut Français d’Indonésie, Jakarta
""")

# Academic Training Section
st.write('\n')
st.subheader("Theoretical Courses & Certifications")
st.write("""
- 📜 **Statistics: [Concepts](https://courses.edx.org/certificates/63fcb9b0112a437b94918250f1d303d8), [Methods](https://courses.edx.org/certificates/e217a3299de74a4aaf6bb0ff647ad2d4)** – London School of Economics
- 📜 **[Policy for Science, Technology and Innovation](https://courses.edx.org/certificates/1d3502bd20184aa0988548efc9ed1203)** – MIT
- 📜 **[Smart City](https://courses.edx.org/certificates/231973dc7a3a4d49bb2f65cc21b66061)** – World Bank
""")

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
PROJECTS = {
    "🏙️ Indonesia Public Services & Urban Development Research Database (in progress --please email for further information)": "https://example.com",
    "🤖 Data & AI Policy Analysis (in progress --please email for further information)": "https://example.com"
}

for project, link in PROJECTS.items():
    st.markdown(f"- [{project}]({link})")

# --- ARTICLES & PUBLICATIONS ---
st.write('\n')
st.subheader("Articles & Publications")
st.write("---")
st.markdown('<p style="font-size: small;"><em>Note: writings published on Kompas platforms are attributed to the editor (as corporate policy requires), but the author\'s name appears at the end of the page under the title \'Contributor\'.</em></p>', unsafe_allow_html=True)

# Data & AI Policy
st.markdown("#### Data & AI Policy")
ARTICLES_DATA_AI = {
    "Efforts to Strengthen Personal Data Protection": "https://kompaspedia.kompas.id/baca/paparan-topik/upaya-memperkuat-perlindungan-data-pribadi",
    "The Development of Artificial Intelligence and Its Impact": "https://kompaspedia.kompas.id/baca/paparan-topik/perkembangan-kecerdasan-buatan-dan-dampaknya"
}
for article, link in ARTICLES_DATA_AI.items():
    st.markdown(f"- :page_facing_up: [{article}]({link})")

# Science-Technology Innovation Policy & Industrial Policy
st.markdown("#### Science-Technology Innovation Policy & Industrial Policy")
ARTICLES_SCI_TECH = {
    "Realizing the National Semiconductor Industry": "https://kompaspedia.kompas.id/baca/paparan-topik/membangkitkan-kembali-pariwisata-indonesia",
    "The Development of Indonesia's Aluminum Industry": "https://kompaspedia.kompas.id/baca/paparan-topik/pengembangan-industri-aluminium-indonesia",
    "History, Production, and Downstream Policy of Bauxite and Aluminum": "https://kompaspedia.kompas.id/baca/paparan-topik/sejarah-produksi-dan-kebijakan-hilirisasi-bauksit-dan-aluminium",
    "Indonesia's Nickel Industry: History, Production, Policy, and Challenges": "https://kompaspedia.kompas.id/baca/paparan-topik/industri-nikel-indonesia-sejarah-produksi-kebijakan-dan-tantangan",
    "Tin Mining: History, Production, and Tin Exports from Indonesia": "https://kompaspedia.kompas.id/baca/paparan-topik/pertambangan-timah-sejarah-produksi-dan-ekspor-timah-indonesia",
    "The Development of the National Copper Industry": "https://kompaspedia.kompas.id/baca/paparan-topik/perkembangan-industri-tembaga-nasional",
    "Efforts to Accelerate Technological Sovereignty": "https://kompaspedia.kompas.id/baca/paparan-topik/upaya-mempercepat-kedaulatan-teknologi"
}
for article, link in ARTICLES_SCI_TECH.items():
    st.markdown(f"- :page_facing_up: [{article}]({link})")

# Development & Climate Policy
st.markdown("#### Development & Climate Policy")
ARTICLES_CLIMATE_POLICY = {
    "Carbon Trading Mechanism": "https://kompaspedia.kompas.id/baca/paparan-topik/mekanisme-perdagangan-karbon",
    "The Ins and Outs of Carbon Trading in Indonesia": "https://kompaspedia.kompas.id/baca/paparan-topik/seluk-beluk-perdagangan-karbon-di-indonesia"
}
for article, link in ARTICLES_CLIMATE_POLICY.items():
    st.markdown(f"- :page_facing_up: [{article}]({link})")