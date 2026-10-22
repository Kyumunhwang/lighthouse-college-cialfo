"""
View: Home & Gamified Roadmap
Directly mirrors design/home_gamified_roadmap/code.html
"""
import streamlit as st
from modules.data_manager import DataManager
from modules.ai_copilot import SaigeAICopilot
from config import get_school_logo_html
from modules.ui_utils import render_html


def render_home_roadmap_view():
    """Render Home & Gamified Roadmap dashboard."""
    profile = DataManager.get_student_profile()
    student = profile["student"]
    roadmap = profile["roadmap"]
    quest = profile["quest_persona"]
    tasks = profile["urgent_tasks"]
    counselor_notes = profile["counselor_notes"]
    kudos_feed = profile["classmate_kudos"]

    # 1. Header Banner & Welcome with Horizontal Stepper
    header_html = f"""
    <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(15,23,42,0.05);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
            <div style="display: flex; align-items: center; gap: 14px;">
                <div style="width: 56px; height: 56px; border-radius: 12px; background: #ffffff; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                    {get_school_logo_html(44)}
                </div>
                <div>
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <h2 style="margin: 0; font-size: 24px; font-weight: 700; color: #131b2e;">Hello, {student['name']}!</h2>
                        <span class="badge-emerald">{roadmap['cycle']}</span>
                    </div>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #434655;">
                        {student['cohort']} • {student['school']} • <strong>{student['active_applications_count']} Target Applications Active</strong>
                    </p>
                </div>
            </div>
            <div style="background: #f2f3ff; padding: 8px 14px; border-radius: 8px; border: 1px solid #e2e7ff; font-size: 13px; font-weight: 600;">
                <span style="color: #059669;">●</span> Next Critical Date: <strong style="color: #ba1a1a;">{roadmap['next_critical_date']}</strong>
            </div>
        </div>

        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: #747686;">University Preparation Journey</span>
            <span style="font-size: 12px; font-weight: 700; color: #1d4ed8;">{roadmap['stage_title']}</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;">
            <div style="background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 8px; padding: 12px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-size: 11px; font-weight: 700; color: #059669;">✓ STAGE 1</span>
                    <span style="font-size: 11px; font-weight: 700; background: #85f8c4; color: #002114; padding: 2px 6px; border-radius: 9999px;">100%</span>
                </div>
                <div style="font-weight: 700; font-size: 14px; color: #131b2e;">Profile & Foundation</div>
                <div style="font-size: 12px; color: #434655;">IB Diploma & high school records locked.</div>
            </div>
            <div style="background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 8px; padding: 12px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-size: 11px; font-weight: 700; color: #059669;">✓ STAGE 2</span>
                    <span style="font-size: 11px; font-weight: 700; background: #85f8c4; color: #002114; padding: 2px 6px; border-radius: 9999px;">100%</span>
                </div>
                <div style="font-weight: 700; font-size: 14px; color: #131b2e;">Discovery & Quest</div>
                <div style="font-size: 12px; color: #434655;">Majors calibrated & psychometrics locked.</div>
            </div>
            <div style="background: #eff6ff; border: 2px solid #1d4ed8; border-radius: 8px; padding: 12px; box-shadow: 0 2px 4px rgba(29,78,216,0.08);">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-size: 11px; font-weight: 700; color: #1d4ed8;">⚡ STAGE 3 (ACTIVE)</span>
                    <span style="font-size: 11px; font-weight: 700; background: #cad3ff; color: #001551; padding: 2px 6px; border-radius: 9999px;">65%</span>
                </div>
                <div style="font-weight: 700; font-size: 14px; color: #131b2e;">Build Lists & Apply</div>
                <div style="font-size: 12px; color: #434655;">Direct Apply & LOR studio in high gear.</div>
            </div>
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; opacity: 0.85;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-size: 11px; font-weight: 700; color: #747686;">STAGE 4</span>
                    <span style="font-size: 11px; font-weight: 700; background: #e2e8f0; color: #475569; padding: 2px 6px; border-radius: 9999px;">0%</span>
                </div>
                <div style="font-weight: 700; font-size: 14px; color: #131b2e;">Offer, Flywire & Enroll</div>
                <div style="font-size: 12px; color: #434655;">Conditional clears & visa completion.</div>
            </div>
        </div>
    </div>
    """
    render_html(header_html)

    # 2. Main Content Layout (2 Columns)
    col_left, col_right = st.columns([1.2, 1], gap="medium")

    with col_left:
        # University Quest Animal Persona Widget
        persona_html = f"""
        <div class="cialfo-card cialfo-card-warning">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-size: 28px;">🦙</span>
                        <div>
                            <h3 style="margin: 0; font-size: 18px; color: #131b2e;">University Quest Persona: {quest['name']}</h3>
                            <span class="badge-amber">Level {quest['level']} • Summer Quest 88% Completion Benchmark</span>
                        </div>
                    </div>
                </div>
                <div style="text-align: right;">
                    <span style="font-size: 20px; font-weight: 800; color: #d97706;">👏 {quest['kudos_count']}</span>
                    <div style="font-size: 11px; font-weight: 600; color: #747686;">Classmate Kudos</div>
                </div>
            </div>
            <p style="font-size: 13px; color: #434655; margin-bottom: 14px; font-style: italic;">
                "{quest['tagline']}"
            </p>
            <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                <div style="font-size: 12px; font-weight: 700; color: #92400e; margin-bottom: 4px;">🎯 CURRENT FOCUS AREA</div>
                <div style="font-size: 13px; color: #78350f; font-weight: 600;">{quest['focus_area']}</div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 12px; margin-bottom: 12px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 10px; border-radius: 8px;">
                    <strong style="color: #166534;">✅ What to Embrace:</strong>
                    <p style="margin: 4px 0 0 0; color: #14532d;">{quest['what_to_embrace']}</p>
                </div>
                <div style="background: #fef2f2; border: 1px solid #fecaca; padding: 10px; border-radius: 8px;">
                    <strong style="color: #991b1b;">⚠️ What to Avoid:</strong>
                    <p style="margin: 4px 0 0 0; color: #7f1d1d;">{quest['what_to_avoid']}</p>
                </div>
            </div>
        </div>
        """
        render_html(persona_html)

        # Kudos Action Button & Social Feed
        c_btn, c_info = st.columns([1, 1.5])
        with c_btn:
            target_classmate = kudos_feed[0]['student'] if kudos_feed else "HYUNDO KIM (김현도)"
            if st.button(f"👏 Send Kudos to {target_classmate.split('(')[0].strip()}", key="btn_kudos", use_container_width=True):
                with st.spinner("Broadcasting Kudos to Classmate..."):
                    new_count = DataManager.update_student_kudos(1)
                    st.success(f"Kudos sent to {target_classmate}! Total received: {new_count} 👏")
                    st.rerun()

        kudos_rows = "".join([
            f"""<div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #f1f5f9; font-size: 13px;">
                <div>
                    <strong>{k['student']}</strong> <span style="font-size: 11px; color: #747686;">({k['persona']})</span>
                    <div style="color: #434655;">{k['action']}</div>
                </div>
                <span style="font-size: 11px; color: #94a3b8; font-weight: 500;">{k['time']}</span>
            </div>""" for k in kudos_feed
        ])
        render_html(f"""
        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px; margin-top: 10px;">
            <h4 style="margin: 0 0 10px 0; font-size: 14px; font-weight: 700; color: #131b2e;">Classmate Live Milestones</h4>
            {kudos_rows}
        </div>
        """)

        # Direct Apply Spotlight Card
        direct_apply_spotlight = f"""
        <div class="cialfo-card cialfo-card-direct-apply" style="margin-top: 16px;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                <span style="font-size: 22px;">⚡</span>
                <h3 style="margin: 0; font-size: 16px; font-weight: 700; color: #004f35;">Direct Apply Benefit Engine Active</h3>
            </div>
            <p style="font-size: 13px; color: #434655; margin-bottom: 10px;">
                You are utilizing {student['school']}'s verified Cialfo Direct Apply network. 
                Enjoy <strong>$200–$300 fee waivers</strong>, full transparency for UK conditional offers, and an assigned Cialfo Guide.
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                <span class="badge-emerald">✓ Instant Fee Waiver</span>
                <span class="badge-emerald">✓ 5-Step Unified Submission</span>
                <span class="badge-emerald">✓ 100% Visa Guidance</span>
            </div>
        </div>
        """
        render_html(direct_apply_spotlight)

    with col_right:
        # Pinned Urgent Tasks & Action Items
        tasks_rows = "".join([
            f"""<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span class="badge-slate">{t['type']}</span>
                    <strong style="font-size: 12px; color: #ba1a1a;">Due: {t['due']}</strong>
                </div>
                <div style="font-size: 13px; font-weight: 600; color: #131b2e;">{t['title']}</div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 6px;">
                    <span style="font-size: 11px; color: #d97706; font-weight: 600;">Status: {t['status']}</span>
                    <span style="font-size: 11px; color: #1d4ed8; font-weight: 600;">Action Link →</span>
                </div>
            </div>""" for t in tasks
        ])
        render_html(f"""
        <div class="cialfo-card cialfo-card-primary">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 20px;">📌</span>
                    <h3 style="margin: 0; font-size: 16px; font-weight: 700; color: #131b2e;">To-Do's (Pinned High-Priority Tasks)</h3>
                </div>
                <span class="badge-blue">{len(tasks)} Pending</span>
            </div>
            {tasks_rows}
        </div>
        """)

        # Recent Counselor Notes
        counselor_items = "".join([f"<li>{item}</li>" for item in counselor_notes.get("action_items", [])])
        notes_html = f"""
        <div class="cialfo-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 20px;">💬</span>
                    <h3 style="margin: 0; font-size: 16px; font-weight: 700; color: #131b2e;">Counselor Notes: {counselor_notes['counselor']}</h3>
                </div>
                <span style="font-size: 12px; color: #747686;">{counselor_notes['date']}</span>
            </div>
            <p style="font-size: 13px; color: #434655; line-height: 1.5; margin-bottom: 10px;">
                "{counselor_notes['summary']}"
            </p>
            <div style="background: #f2f3ff; border-radius: 8px; padding: 10px;">
                <div style="font-size: 12px; font-weight: 700; color: #1d4ed8; margin-bottom: 4px;">Key Action Items:</div>
                <ul style="margin: 0; padding-left: 18px; font-size: 12px; color: #131b2e;">
                    {counselor_items}
                </ul>
            </div>
        </div>
        """
        render_html(notes_html)

        # Quick Saige Copilot Trigger
        render_html("""
        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px; box-shadow: 0 1px 3px rgba(15,23,42,0.05); margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                <span style="font-size: 20px;">🦁</span>
                <h4 style="margin: 0; font-size: 15px; font-weight: 700; color: #904d00;">Ask Saige Copilot</h4>
            </div>
            <p style="font-size: 12px; color: #434655; margin: 0;">
                Ask questions about diploma recognition, STEAM degrees, or UK conditional offer benchmarks.
            </p>
        </div>
        """)
        sample_q = st.selectbox(
            "Select quick question or enter below:",
            [
                "Does Imperial College recognize Turkish diplomas or require foundation year?",
                "What universities offer dual degrees in STEAM (Music & Computer Science)?",
                "What are the benefits of Cialfo Direct Apply over standard UCAS?"
            ],
            key="home_saige_prompt_select"
        )
        if st.button("Consult Saige AI", key="btn_home_saige"):
            with st.spinner("Saige AI is analyzing global database..."):
                response = SaigeAICopilot.ask_saige(sample_q)
                st.info(response)
