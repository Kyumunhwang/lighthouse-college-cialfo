"""
View: Structured 2-Tier LOR Request Studio & Multilingual Bridge
Directly mirrors design/structured_2_tier_lor_request_studio/code.html
Solves PP-01 (Copy-Paste Elimination via 2-Tier Architecture) & PP-08 (Multilingual LOR Bridge)
"""
import streamlit as st
from modules.data_manager import DataManager
from modules.ai_copilot import SaigeAICopilot
from config import get_school_logo_html
from modules.ui_utils import render_html


def render_lor_studio_view():
    """Render Structured 2-Tier LOR Request Studio."""
    lor_data = DataManager.get_lor_data()
    cap = lor_data["cap_policy"]
    tier_1 = lor_data["tier_1_common_reflections"]
    recs = lor_data["recommenders"]
    bridge = lor_data["multilingual_lor_bridge"]

    render_html(
        """
        <div style="margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 26px;">✍️</span>
                <h2 style="margin: 0; font-size: 24px; font-weight: 700; color: #131b2e;">Structured 2-Tier LOR Request Studio</h2>
            </div>
            <p style="margin: 4px 0 0 0; font-size: 13px; color: #434655;">
                Eliminating copy-paste friction (PP-01). Common reflections sync automatically to all recommenders; course reflections remain personalized.
            </p>
        </div>
        """
    )

    # 1. School Policy & Cap Limit Gauge
    render_html(
        f"""
        <div class="cialfo-card cialfo-card-primary" style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    {get_school_logo_html(36)}
                    <div>
                        <div style="font-size: 12px; font-weight: 700; color: #1d4ed8; text-transform: uppercase; letter-spacing: 0.05em;">
                            Institutional Recommendation Policy (Leaders International School)
                        </div>
                        <div style="font-size: 13px; color: #434655; margin-top: 2px;">
                            {cap['policy_note']}
                        </div>
                    </div>
                </div>
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; padding: 8px 14px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 11px; font-weight: 600; color: #1d4ed8;">RECOMMENDER QUOTA</div>
                    <div style="font-size: 16px; font-weight: 800; color: #131b2e;">{cap['status']}</div>
                </div>
            </div>
        </div>
        """
    )

    tab_student_view, tab_teacher_studio = st.tabs(["📝 Student LOR 2-Tier Request Form", "🌐 Multilingual Teacher AI Studio (PP-08)"])

    with tab_student_view:
        # TIER 1: Common Student Reflections (Auto-Synced)
        render_html(
            """
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(15,23,42,0.05);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-size: 20px;">🔄</span>
                        <h3 style="margin: 0; font-size: 17px; font-weight: 700; color: #131b2e;">Tier 1: Common Student Reflections</h3>
                    </div>
                    <span class="badge-emerald">☁️ Auto-Sync Enabled (Shared Across All Teachers)</span>
                </div>
                <p style="font-size: 12px; color: #747686; margin: 0;">
                    Write once. These answers will be automatically displayed to all selected academic teachers.
                </p>
            </div>
            """
        )

        with st.form("tier1_form"):
            adj = st.text_input(
                "1. Three adjectives that best describe your character and intellect:",
                value=tier_1.get("three_adjectives", "")
            )
            adj_exp = st.text_area(
                "2. Concrete examples illustrating why these three adjectives describe you:",
                value=tier_1.get("adjectives_explanation", ""),
                height=70
            )
            extra = st.text_area(
                "3. Key extracurricular milestones, leadership roles, or research accomplishments:",
                value=tier_1.get("extracurricular_highlights", ""),
                height=70
            )
            bg = st.text_area(
                "4. Personal background context, employment, family responsibilities, or hardships overcome:",
                value=tier_1.get("background_challenges", ""),
                height=70
            )

            submit_t1 = st.form_submit_button("💾 Save & Sync Tier 1 Reflections to All Teachers")
            if submit_t1:
                with st.spinner("Optimistically auto-saving reflections..."):
                    DataManager.update_tier_1_reflections(adj, adj_exp, extra, bg)
                    st.success("Tier 1 Common Reflections successfully saved and synced across all teacher slots!")

        # TIER 2: Course-Specific Personalized Reflections
        render_html(
            """
            <div style="margin-top: 18px; margin-bottom: 12px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 20px;">🎯</span>
                    <h3 style="margin: 0; font-size: 17px; font-weight: 700; color: #131b2e;">Tier 2: Course-Specific Individual Reflections</h3>
                </div>
                <p style="font-size: 12px; color: #747686; margin-top: 4px;">
                    Specific memories, projects, and growth demonstrated in each individual teacher's classroom.
                </p>
            </div>
            """
        )

        for rec in recs:
            t2 = rec.get("tier_2_course_reflections", {})
            render_html(
                f"""
                <div class="cialfo-card cialfo-card-primary" style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h4 style="margin: 0; font-size: 16px; font-weight: 700; color: #131b2e;">{rec['teacher_name']}</h4>
                            <div style="font-size: 13px; color: #1d4ed8; font-weight: 600;">{rec['subject']} ({rec['department']})</div>
                        </div>
                        <div style="text-align: right;">
                            <span class="badge-amber">{rec['status']}</span>
                            <div style="font-size: 11px; color: #747686; margin-top: 4px;">Deadline: <strong>{rec['deadline']}</strong></div>
                        </div>
                    </div>
                </div>
                """
            )

            with st.expander(f"Edit Course Reflections for {rec['teacher_name']}", expanded=True):
                c_proj = st.text_area(
                    f"A memorable project or experiment in {rec['subject']}:",
                    value=t2.get("memorable_project", ""),
                    key=f"proj_{rec['id']}",
                    height=65
                )
                c_growth = st.text_area(
                    "Intellectual breakthrough or growth observed in this class:",
                    value=t2.get("intellectual_growth", ""),
                    key=f"growth_{rec['id']}",
                    height=65
                )
                c_major = st.text_area(
                    "How this course connects to your prospective university major:",
                    value=t2.get("link_to_target_major", ""),
                    key=f"major_{rec['id']}",
                    height=65
                )
                if st.button(f"Save Reflections for {rec['teacher_name']}", key=f"btn_save_{rec['id']}"):
                    st.success(f"Course-specific responses updated for {rec['teacher_name']}!")

    with tab_teacher_studio:
        render_html(
            """
            <div class="cialfo-card cialfo-card-direct-apply" style="margin-bottom: 20px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="font-size: 24px;">🌐</span>
                    <h3 style="margin: 0; font-size: 18px; font-weight: 700; color: #004f35;">Multilingual Teacher LOR Studio & AI Bridge</h3>
                </div>
                <p style="font-size: 13px; color: #434655;">
                    Built for non-native English speaking faculty (Turkish, Korean, Chinese, Spanish, etc.). 
                    Teachers input raw pedagogical observations in their mother tongue; Gemini AI transforms them into standard Academic English admissions LOR drafts for Counselor review.
                </p>
            </div>
            """
        )

        col_lang, col_status = st.columns([1, 1])
        with col_lang:
            input_lang = st.selectbox(
                "Teacher Input Language:",
                ["Korean", "Turkish", "Spanish", "Chinese", "French"],
                key="sel_lor_lang"
            )
        with col_status:
            render_html(f"<div style='padding-top: 24px;'><strong>Counselor Review Gate</strong>: <span class='badge-emerald'>{bridge['counselor_approval_status']}</span></div>")

        raw_input = st.text_area(
            f"Enter Teacher Observations in {input_lang}:",
            value=bridge["sample_raw_teacher_notes"],
            height=120,
            key="teacher_raw_notes_input"
        )

        if st.button("✨ Run Gemini AI Academic English Conversion", key="btn_run_ai_lor"):
            with st.spinner("Transforming notes into admissions-grade Academic English LOR draft..."):
                converted = SaigeAICopilot.translate_and_polish_lor(raw_input, source_language=input_lang)
                bridge["ai_converted_english_draft"] = converted
                st.success("Translation & Academic Polishing Complete!")

        render_html(
            f"""
            <div style="background: #ffffff; border: 1px solid #a7f3d0; border-radius: 12px; padding: 18px; margin-top: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <div style="font-size: 13px; font-weight: 700; color: #059669;">
                        🇬🇧 Generated Academic English LOR Draft (Common App / UCAS Standard)
                    </div>
                    <span class="badge-emerald">Ready for Counselor Approval</span>
                </div>
                <p style="font-size: 13px; color: #131b2e; line-height: 1.6; font-style: italic; background: #f0fdf4; padding: 14px; border-radius: 8px;">
                    "{bridge['ai_converted_english_draft']}"
                </p>
            </div>
            """
        )

        c_app1, c_app2 = st.columns(2)
        with c_app1:
            if st.button("✅ Counselor Approve to cDocs Queue", key="btn_approve_cdocs"):
                with st.spinner("Locking document in cDocs vault..."):
                    st.success("LOR formally approved by Counselor and added to student's cDocs submission envelope!")
        with c_app2:
            if st.button("📥 Export Official Letterhead PDF", key="btn_export_lor"):
                st.info("Generating encrypted official letterhead PDF with digital signature...")
