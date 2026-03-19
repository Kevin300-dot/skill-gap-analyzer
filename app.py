import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="SkillBridge TN", page_icon="🎓", layout="wide")

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1a1a2e, #16213e);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .metric-card {
        background: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    .skill-gap-item {
        background: #fff3cd;
        padding: 10px;
        border-radius: 8px;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='main-header'>
    <h1 style='color: white; text-align: center;'>🎓 SkillBridge TN</h1>
    <p style='color: #a0aec0; text-align: center; font-size: 18px;'>AI-Powered Workforce Skill Gap Analyzer for Tamil Nadu</p>
</div>
""", unsafe_allow_html=True)

job_skills = {
    "EV Technician (Ola Electric / Ather)": [
        "Battery Management Systems", "Motor Control", "CAN Bus Protocol",
        "EV Charging Systems", "Electrical Wiring", "Python Basic"
    ],
    "Automobile Manufacturing (TVS / Ashok Leyland)": [
        "Engine Repair", "Manual Transmission", "Quality Control",
        "Welding", "CNC Operation", "Safety Standards"
    ],
    "Auto Components MSME Worker": [
        "Metal Fabrication", "Lathe Operation", "Quality Inspection",
        "Blueprint Reading", "Basic Hydraulics", "Safety Standards"
    ],
    "EV Battery Assembly (Exide / Amara Raja)": [
        "Battery Cell Assembly", "Electrical Safety", "Quality Control",
        "Battery Testing", "Soldering", "EV Charging Systems"
    ]
}

course_recommendations = {
    "Battery Management Systems": {
        "course": "Naan Mudhalvan - EV Battery Module 3",
        "duration": "6 weeks",
        "provider": "Naan Mudhalvan",
        "priority": "High"
    },
    "Motor Control": {
        "course": "TN AUTO Skills - Motor Control Course",
        "duration": "4 weeks",
        "provider": "TN AUTO Skills",
        "priority": "High"
    },
    "CAN Bus Protocol": {
        "course": "Naan Mudhalvan - Automotive Networking",
        "duration": "3 weeks",
        "provider": "Naan Mudhalvan",
        "priority": "Medium"
    },
    "EV Charging Systems": {
        "course": "TN AUTO Skills - EV Charging Infrastructure",
        "duration": "2 weeks",
        "provider": "TN AUTO Skills",
        "priority": "High"
    },
    "Electrical Wiring": {
        "course": "Government ITI - Electrical Technician Course",
        "duration": "8 weeks",
        "provider": "Government ITI",
        "priority": "Medium"
    },
    "Python Basic": {
        "course": "Naan Mudhalvan - Python for Automation",
        "duration": "4 weeks",
        "provider": "Naan Mudhalvan",
        "priority": "Low"
    },
    "Engine Repair": {
        "course": "TN AUTO Skills - Engine Overhaul Program",
        "duration": "6 weeks",
        "provider": "TN AUTO Skills",
        "priority": "High"
    },
    "Manual Transmission": {
        "course": "Government ITI - Automobile Engineering",
        "duration": "4 weeks",
        "provider": "Government ITI",
        "priority": "High"
    },
    "Quality Control": {
        "course": "Naan Mudhalvan - Manufacturing Quality Module",
        "duration": "3 weeks",
        "provider": "Naan Mudhalvan",
        "priority": "Medium"
    },
    "Welding": {
        "course": "Government ITI - Welding Technology",
        "duration": "6 weeks",
        "provider": "Government ITI",
        "priority": "High"
    },
    "CNC Operation": {
        "course": "TANCAM - CNC Machining Course",
        "duration": "8 weeks",
        "provider": "TANCAM",
        "priority": "High"
    },
    "Safety Standards": {
        "course": "TN AUTO Skills - Industrial Safety Program",
        "duration": "2 weeks",
        "provider": "TN AUTO Skills",
        "priority": "Medium"
    },
    "Metal Fabrication": {
        "course": "Government ITI - Fabrication Technology",
        "duration": "6 weeks",
        "provider": "Government ITI",
        "priority": "High"
    },
    "Lathe Operation": {
        "course": "TANCAM - Lathe & Turning Operations",
        "duration": "4 weeks",
        "provider": "TANCAM",
        "priority": "High"
    },
    "Quality Inspection": {
        "course": "Naan Mudhalvan - Quality Assurance Module",
        "duration": "3 weeks",
        "provider": "Naan Mudhalvan",
        "priority": "Medium"
    },
    "Blueprint Reading": {
        "course": "TN AUTO Skills - Technical Drawing Course",
        "duration": "2 weeks",
        "provider": "TN AUTO Skills",
        "priority": "Medium"
    },
    "Basic Hydraulics": {
        "course": "Government ITI - Hydraulics & Pneumatics",
        "duration": "4 weeks",
        "provider": "Government ITI",
        "priority": "Medium"
    },
    "Battery Cell Assembly": {
        "course": "TN AUTO Skills - EV Battery Assembly",
        "duration": "4 weeks",
        "provider": "TN AUTO Skills",
        "priority": "High"
    },
    "Electrical Safety": {
        "course": "Naan Mudhalvan - Electrical Safety Module",
        "duration": "2 weeks",
        "provider": "Naan Mudhalvan",
        "priority": "High"
    },
    "Battery Testing": {
        "course": "TN AUTO Skills - Battery Diagnostics",
        "duration": "3 weeks",
        "provider": "TN AUTO Skills",
        "priority": "High"
    },
    "Soldering": {
        "course": "Government ITI - Electronics & Soldering",
        "duration": "2 weeks",
        "provider": "Government ITI",
        "priority": "Low"
    },
}

def generate_smart_recommendation(name, course, target_job, skill_gaps, readiness):
    if readiness == 100:
        return f"🎉 Excellent! {name} is fully job-ready for {target_job.split('(')[0]}. We recommend applying immediately to companies like {target_job.split('(')[1].replace(')', '')} and registering on the TN AUTO Skills job portal."

    high_priority = [s for s in skill_gaps if course_recommendations.get(s, {}).get("priority") == "High"]
    medium_priority = [s for s in skill_gaps if course_recommendations.get(s, {}).get("priority") == "Medium"]
    total_weeks = sum(int(course_recommendations[s]["duration"].split()[0]) for s in skill_gaps if s in course_recommendations)

    if readiness >= 60:
        urgency = "You are close to job-ready!"
    elif readiness >= 30:
        urgency = "You have a moderate skill gap to bridge."
    else:
        urgency = "You need significant upskilling — but it is achievable!"

    recommendation = f"""
📊 **AI Skill Gap Analysis for {name}**

{urgency} Your current readiness for **{target_job.split('(')[0]}** is **{readiness}%**.

🔴 **Start immediately with these High Priority skills:**
{chr(10).join(f"• {s} → {course_recommendations[s]['course']}" for s in high_priority) if high_priority else "• None — great foundation!"}

🟡 **Then focus on these Medium Priority skills:**
{chr(10).join(f"• {s} → {course_recommendations[s]['course']}" for s in medium_priority) if medium_priority else "• None — well covered!"}

⏱️ **Estimated total training time:** {total_weeks} weeks

🏆 **Recommended Action Plan:**
1. Register on Naan Mudhalvan portal immediately
2. Enroll in High Priority courses first
3. Complete Medium Priority courses in parallel
4. Apply to TN AUTO Skills job placement program upon completion

💡 **Career Insight:** Tamil Nadu's EV sector is growing at 34% annually. Students who complete this skill gap training have 3x higher placement rates in companies like Ola Electric, Ather Energy, and TVS Motor.
"""
    return recommendation

st.sidebar.header("👤 Student Profile")
student_name = st.sidebar.text_input("Your Name", placeholder="Enter your name")
course = st.sidebar.selectbox("Your Current Course", [
    "Diploma in Automobile Engineering",
    "ITI - Mechanic Motor Vehicle",
    "ITI - Electrician",
    "B.Tech Mechanical Engineering",
    "Polytechnic - Mechanical",
    "Polytechnic - Electrical"
])

district = st.sidebar.selectbox("Your District", [
    "Chennai", "Hosur", "Coimbatore", "Madurai",
    "Tiruchirappalli", "Salem", "Vellore", "Erode"
])

target_job = st.sidebar.selectbox("Target Job Role", list(job_skills.keys()))

st.sidebar.markdown("---")
st.sidebar.subheader("✅ Your Current Skills")
all_skills = list(course_recommendations.keys())
current_skills = st.sidebar.multiselect("Select skills you already have", all_skills)

analyze = st.sidebar.button("🔍 Analyze My Skill Gap", type="primary")

if analyze:
    if not student_name:
        st.warning("Please enter your name!")
    else:
        required_skills = job_skills[target_job]
        skill_gaps = [s for s in required_skills if s not in current_skills]
        matched_skills = [s for s in required_skills if s in current_skills]
        readiness = int((len(matched_skills) / len(required_skills)) * 100)

        st.success(f"✅ Analysis complete for **{student_name}** from **{district}**!")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("🎯 Target Role", target_job.split("(")[0].strip())
        with col2:
            st.metric("✅ Skills Matched", f"{len(matched_skills)} / {len(required_skills)}")
        with col3:
            st.metric("⚠️ Skill Gaps", len(skill_gaps))
        with col4:
            st.metric("📊 Readiness Score", f"{readiness}%")

        st.markdown("---")

        col_chart1, col_chart2 = st.columns(2)

        with col_chart1:
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=readiness,
                title={"text": "Job Readiness Score"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#2ecc71" if readiness >= 60 else "#e74c3c"},
                    "steps": [
                        {"range": [0, 40], "color": "#fadbd8"},
                        {"range": [40, 70], "color": "#fdebd0"},
                        {"range": [70, 100], "color": "#d5f5e3"},
                    ],
                }
            ))
            fig_gauge.update_layout(height=300)
            st.plotly_chart(fig_gauge, use_container_width=True)

        with col_chart2:
            if skill_gaps or matched_skills:
                fig_pie = go.Figure(go.Pie(
                    labels=["Skills You Have", "Skills You Need"],
                    values=[len(matched_skills), len(skill_gaps)],
                    hole=0.4,
                    marker_colors=["#2ecc71", "#e74c3c"]
                ))
                fig_pie.update_layout(
                    title="Your Skill Coverage",
                    height=300
                )
                st.plotly_chart(fig_pie, use_container_width=True)

        st.markdown("---")

        st.subheader("🤖 AI-Powered Recommendation")
        recommendation = generate_smart_recommendation(
            student_name, course, target_job, skill_gaps, readiness
        )
        st.markdown(recommendation)

        st.markdown("---")

        if skill_gaps:
            st.subheader("📚 Your Personalized Training Roadmap")
            for skill in skill_gaps:
                if skill in course_recommendations:
                    info = course_recommendations[skill]
                    priority_color = "🔴" if info["priority"] == "High" else "🟡" if info["priority"] == "Medium" else "🟢"
                    with st.expander(f"{priority_color} {skill} — {info['provider']} ({info['duration']})"):
                        st.write(f"**Course:** {info['course']}")
                        st.write(f"**Provider:** {info['provider']}")
                        st.write(f"**Duration:** {info['duration']}")
                        st.write(f"**Priority:** {info['priority']}")
        else:
            st.balloons()
            st.success("🎉 You have all required skills! You are 100% job ready!")

else:
    st.markdown("### 👋 Welcome to SkillBridge TN")
    st.markdown("The AI-powered platform helping Tamil Nadu students bridge the gap between education and industry.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Step 1️⃣**\n\nEnter your profile — name, course, district and target job role")
    with col2:
        st.warning("**Step 2️⃣**\n\nSelect the skills you already have from your training")
    with col3:
        st.success("**Step 3️⃣**\n\nGet your AI-powered skill gap report and training roadmap!")

    st.markdown("---")
    st.markdown("### 🏭 Supported Industry Partners")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("🏢 **Ola Electric**\nHosur, Tamil Nadu")
    with col2:
        st.markdown("🏢 **TVS Motor**\nHosur, Tamil Nadu")
    with col3:
        st.markdown("🏢 **Ashok Leyland**\nChennai, Tamil Nadu")
    with col4:
        st.markdown("🏢 **Ather Energy**\nHosur, Tamil Nadu")