"""
Cialfo.ai — Next-Gen Global College & Career Readiness (CCR) & Direct Admissions Platform
Entrypoint application built with Streamlit.
Fulfills all requirements from prd.md and design/ specifications.
"""
import streamlit as st
from config import CUSTOM_CSS, DEFAULT_PORT
from modules.views.view_home_roadmap import render_home_roadmap_view
from modules.views.view_universities_courses import render_universities_courses_view
from modules.views.view_lor_studio import render_lor_studio_view
from modules.views.view_direct_apply import render_direct_apply_view
from modules.views.view_counselor_cdocs import render_counselor_cdocs_view
from modules.views.view_explore_visits import render_explore_visits_view
from modules.views.view_data_architecture import render_data_architecture_view
from modules.ai_copilot import SaigeAICopilot
from modules.ui_utils import render_html

# Streamlit Page Configuration
st.set_page_config(
    page_title="Cialfo.ai | Global CCR & Direct Apply Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom Design System CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def main():
    from modules.data_manager import DataManager
    from config import get_school_logo_html

    profile = DataManager.get_student_profile()
    student = profile["student"]
    seniors = DataManager.get_h12_seniors()

    # 1. Top Bar Navigation & Universal Search
    render_html(
        f"""
        <div style="background: rgba(250, 248, 255, 0.95); backdrop-filter: blur(12px); border-bottom: 1px solid #e2e8f0; padding: 12px 24px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; border-radius: 12px;">
            <div style="display: flex; align-items: center; gap: 12px;">
                {get_school_logo_html(40)}
                <span style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 22px; font-weight: 800; color: #1d4ed8; letter-spacing: -0.02em;">Cialfo.ai</span>
                <span class="badge-blue" style="font-size: 11px;">LIS GLOBAL CCR</span>
                <span class="badge-emerald" style="font-size: 11px;">DIRECT APPLY VERIFIED</span>
            </div>
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 9999px; padding: 6px 14px; display: flex; align-items: center; gap: 8px; font-size: 12px; color: #64748b; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
                    <span>🔍 Universal Search</span>
                    <span style="background: #f1f5f9; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 700;">⌘K</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; background: #ffffff; border: 1px solid #e2e8f0; padding: 6px 14px; border-radius: 9999px; font-size: 12px; font-weight: 600;">
                    {get_school_logo_html(22)}
                    <span>{student['name']} ({student['english_name']})</span>
                    <span style="color: #059669;">●</span>
                </div>
            </div>
        </div>
        """
    )

    # 2. Sidebar Navigation & Global Controls
    with st.sidebar:
        render_html(
            f"""
            <div style="padding: 10px 0 14px 0; border-bottom: 1px solid #e2e8f0; margin-bottom: 12px; text-align: center;">
                <div style="margin-bottom: 8px;">{get_school_logo_html(52)}</div>
                <div style="font-size: 14px; font-weight: 800; color: #1d4ed8; letter-spacing: -0.01em;">
                    Leaders Int'l School (LIS)
                </div>
                <div style="font-size: 11px; color: #747686; margin-top: 2px;">
                    Fall 2026 Official Student & Faculty Sync
                </div>
            </div>
            """
        )

        # Real LIS Senior Student Switcher
        active_idx = 0
        current_id = profile.get("active_student_id", student.get("student_id"))
        for i, s in enumerate(seniors):
            if s["student_id"] == current_id:
                active_idx = i
                break

        selected_senior_idx = st.selectbox(
            "👤 Active LIS Senior (H12):",
            range(len(seniors)) if seniors else [0],
            index=active_idx if seniors else 0,
            format_func=lambda i: seniors[i]["display_name"] if seniors else "Default Senior",
            key="sel_active_senior"
        )

        if seniors and seniors[selected_senior_idx]["student_id"] != current_id:
            DataManager.switch_active_student(seniors[selected_senior_idx]["student_id"])
            st.rerun()

        st.markdown("---")

        nav_choice = st.radio(
            "Select Platform Module:",
            [
                "🏠 Home & Gamified Roadmap",
                "🏛️ Universities & Courses Explorer",
                "✍️ Structured 2-Tier LOR Studio",
                "⚡ Applications & Direct Apply Hub",
                "🎓 Counselor Command Center & cDocs",
                "🌐 Explore University Visits Console",
                "🗄️ Data Architecture & Ingestion Hub"
            ],
            index=0,
            key="main_nav_radio"
        )

        st.markdown("---")

        # Responsive Mobile Emulation Toggle (PP-03)
        mobile_mode = st.toggle("📱 Mobile-First Responsive Mode", value=False, help="Simulates PWA bottom-sheet and swipeable card view.")
        if mobile_mode:
            st.info("📱 Mobile Viewport Active: Optimizing multi-column grids for mobile screen sizes.")

        st.markdown("---")

        # School & Partner Verification Card
        render_html(
            f"""
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px; font-size: 12px; box-shadow: 0 1px 3px rgba(15,23,42,0.04);">
                <div style="display: flex; align-items: center; gap: 8px; font-weight: 700; color: #131b2e; margin-bottom: 6px;">
                    {get_school_logo_html(24)}
                    <span>Leaders International School</span>
                </div>
                <div style="color: #64748b; margin: 4px 0 2px 0;">Principal: <strong>Paul Kim (김바울)</strong></div>
                <div style="color: #64748b; margin: 0 0 2px 0;">Counselor: <strong>David Nah (Ext: 213)</strong></div>
                <div style="color: #64748b; margin: 0 0 6px 0;">H12 Homeroom: <strong>Peter Yoo</strong></div>
                <div style="display: flex; align-items: center; gap: 4px; color: #059669; font-weight: 600;">
                    <span style="width: 6px; height: 6px; border-radius: 50%; background: #059669;"></span>
                    Direct Apply Partner: Active
                </div>
            </div>
            """
        )

    # 3. View Routing
    if nav_choice == "🏠 Home & Gamified Roadmap":
        render_home_roadmap_view()
    elif nav_choice == "🏛️ Universities & Courses Explorer":
        render_universities_courses_view()
    elif nav_choice == "✍️ Structured 2-Tier LOR Studio":
        render_lor_studio_view()
    elif nav_choice == "⚡ Applications & Direct Apply Hub":
        render_direct_apply_view()
    elif nav_choice == "🎓 Counselor Command Center & cDocs":
        render_counselor_cdocs_view()
    elif nav_choice == "🌐 Explore University Visits Console":
        render_explore_visits_view()
    elif nav_choice == "🗄️ Data Architecture & Ingestion Hub":
        render_data_architecture_view()


if __name__ == "__main__":
    main()
