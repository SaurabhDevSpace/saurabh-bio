import streamlit as st
import json
import os

# Load JSON configuration
with open('config.json') as f:
    data = json.load(f)

# Set page configuration (sidebar remains collapsed)
st.set_page_config(page_title="Saurabh Brahmankar - Job Profile", layout="wide", initial_sidebar_state="collapsed", page_icon="🙂")

# Header section with profile picture, name, and tagline
col1, col2 = st.columns([1, 3])
with col1:
    st.image(data["header"]["profile_picture"], width=150, caption="Be Curious!")
with col2:
    st.title(data["header"]["name"])
    st.subheader(data["header"]["tagline"])
st.write("---")

# About Me
with st.container():
    st.header("About Me 👋")
    st.write(data["job"]["about_me"])
    st.write("---")

# Patents
with st.container():
    st.header("Patents 📜")
    for patent in data["job"]["patents"]:
        st.write(f"- {patent}")
    st.write("---")
    
# Work Experience
with st.container():
    st.header("Work Experience 💼")
    for exp in data["job"]["work_experience"]:
        with st.expander(f"{exp['company']} - {exp['role']}", expanded=False):
            st.write(f"**Duration:** {exp['duration']}")
            st.write(exp["description"])
    st.write("---")

# Internships
with st.container():
    st.header("Internships & Trainings 🛠️")
    for internship in data["job"]["internships"]:
        with st.expander(internship["company"]):
            st.write(f"**Role:** {internship['role']}")
            st.write(f"**Technologies:** {internship['technologies']}")
            st.write(f"**Duration:** {internship['duration']}")
    st.write("---")

# Technical Skills
with st.container():
    st.header("Technical Skills 💻")
    for category, skills in data["job"]["skills"]["technical"].items():
        st.subheader(category)
        st.write(", ".join(skills))
    
    st.header("Soft Skills 🤝")
    st.write(", ".join(data["job"]["skills"]["soft"]))
    st.write("---")


# Education
with st.container():
    st.header("Education 🎓")
    for edu in data["job"]["education"]:
        st.write(f"**{edu['degree']}** - {edu.get('institution', '')} ({edu.get('year', '')})")
        if "cgpa" in edu:
            st.write(f"CGPA: {edu['cgpa']}")
        if "marks" in edu:
            st.write(f"Marks: {edu['marks']}")
    st.write("---")

# Awards
with st.container():
    st.header("Awards & Honors 🏆")
    for award in data["job"]["awards"]:
        st.write(f"- {award}")
    st.write("---")

# Contact
with st.container():
    st.header("Contact 📞")
    st.write(f"**Phone:** {data['job']['contact']['phone']}")
    st.write(f"**Email:** [{data['job']['contact']['email']}](mailto:{data['job']['contact']['email']})")
    st.write(f"**Personal Website:** [{data['job']['contact']['website']}]({data['job']['contact']['website']})")
    st.write(f"**LinkedIn:** [{data['job']['contact']['linkedin']}]({data['job']['contact']['linkedin']})")
    st.write(f"**Medium:** [{data['job']['contact']['medium']}]({data['job']['contact']['medium']})")
    st.write(f"**Instagram:** [{data['job']['contact']['instagram']}]({data['job']['contact']['instagram']})")

    st.write("---")

# Photos
with st.container():
    st.header("Me 🙂")
    cols = st.columns(3)
    for i, photo in enumerate(data["photos"]):
        cols[i % 3].image(photo, use_container_width=True)
    st.write("---")

# Footer section with visitor counter
def footer_section():
    """App Footer section with visitor counter"""
    visitor_file = 'visitor_count.json'
    
    if 'visitor_counted' not in st.session_state:
        st.session_state.visitor_counted = False
        
        if os.path.exists(visitor_file):
            try:
                with open(visitor_file, 'r') as f:
                    visitor_data = json.load(f)
                    visitor_count = visitor_data.get('count', 0)
            except (json.JSONDecodeError, FileNotFoundError):
                visitor_count = 0
        else:
            visitor_count = 0
        
        visitor_count += 1
        
        with open(visitor_file, 'w') as f:
            json.dump({'count': visitor_count}, f)
        
        st.session_state.visitor_counted = True
    else:
        if os.path.exists(visitor_file):
            try:
                with open(visitor_file, 'r') as f:
                    visitor_data = json.load(f)
                    visitor_count = visitor_data.get('count', 0)
            except (json.JSONDecodeError, FileNotFoundError):
                visitor_count = 0
        else:
            visitor_count = 0
    
    st.markdown(
        f"""
        <style>
            #footer {{
                position: fixed;
                bottom: 10px;
                left: 50%;
                transform: translateX(-50%);
                font-size: 14px;
                color: gray;
                text-align: center;
                z-index: 1000;
            }}
        </style>
        <div id="footer">
            Built by <b>XploreMe@Sports</b> with 🫰〔Visits: {visitor_count}〕
        </div>
        """,
        unsafe_allow_html=True
    )
# footer_section()