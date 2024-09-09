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
    st.markdown(f"<h1 class='main-title'>{NAME}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='sub-title'>{姓名}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='description'>{DESCRIPTION}</p>", unsafe_allow_html=True)

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
    "LinkedIn": r"C:/Users/HP/Documents/Digital CV/assets/LinkedIn Logo.webp",
    "GitHub": r"C:/Users/HP/Documents/Digital CV/assets/GitHub Logo.png",
    "Instagram": r"C:/Users/HP/Documents/Digital CV/assets/Instagram Logo.webp",
    "X": r"C:/Users/HP/Documents/Digital CV/assets/X Logo.jpg"
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
- ✔️ Well-trained in writing and public speaking, understanding of statistical principles and applications
- ✔️ Excellent team player and displaying a strong sense of initiative on tasks
- ✔️ Life-long Learner, with focus area in Science-Technology Innovation Policy, Smart City, and AI. 
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

# --- lANGUAGE ---
st.write('\n')
st.subheader("Language Proficiency")
st.write("""
- 👩‍💻 Indonesian: Native
- 📊 English: Fluent (IELTS Band 8, TOEFL IBT 104/120)
- 📚 Chinese: Advance (HSK 6)
- 🗄️ French: Intermediate (DELF B2)
""")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write("""
- ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
""")

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write("""
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales efforts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
""")

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write("""
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traffic
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
""")

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
