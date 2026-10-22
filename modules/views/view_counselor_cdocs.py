"""
View: Counselor Command Center & cDocs Hub
Directly mirrors design/counselor_command_center_cdocs_hub/code.html
Features Dynamic Cohort Switcher, Cialfo Groups Broadcast, and Alumni Scattergram Network
"""
import streamlit as st
from modules.data_manager import DataManager
from config import get_school_logo_html
from modules.ui_utils import render_html


def render_counselor_cdocs_view():
    """Render Counselor Command Center & cDocs Hub."""
    c_data = DataManager.get_counselor_data()
    counselor = c_data["counselor"]
    metrics = c_data["cohort_metrics"]
    groups = c_data["cialfo_groups"]
    students = c_data["students_table"]
    alumni = c_data["alumni_scattergram_network"]

    render_html(
        f"""
        <div style="margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 12px;">
                {get_school_logo_html(44)}
                <div>
                    <h2 style="margin: 0; font-size: 24px; font-weight: 700; color: #131b2e;">Counselor Command Center & cDocs Hub</h2>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #434655;">
                        Logged in as <strong>{counselor['name']}</strong> ({counselor['role']} at {counselor['school']})
                    </p>
                </div>
            </div>
        </div>
        """
    )

    # 1. Macro Cohort Metrics Cards
    render_html(
        f"""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-bottom: 20px;">
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px; box-shadow: 0 1px 3px rgba(15,23,42,0.05);">
                <div style="font-size: 11px; font-weight: 600; color: #747686; text-transform: uppercase;">Average Countries / Student</div>
                <div style="font-size: 22px; font-weight: 800; color: #1d4ed8; margin-top: 4px;">{metrics['avg_countries_per_student']} Nations</div>
                <div style="font-size: 11px; color: #059669; font-weight: 600;">Global benchmark: 3.0</div>
            </div>
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px; box-shadow: 0 1px 3px rgba(15,23,42,0.05);">
                <div style="font-size: 11px; font-weight: 600; color: #747686; text-transform: uppercase;">Direct Apply Adoption</div>
                <div style="font-size: 22px; font-weight: 800; color: #059669; margin-top: 4px;">{metrics['direct_apply_adoption']}</div>
                <div style="font-size: 11px; color: #059669; font-weight: 600;">${metrics['total_fee_waivers_saved_usd']:,} saved in fees</div>
            </div>
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px; box-shadow: 0 1px 3px rgba(15,23,42,0.05);">
                <div style="font-size: 11px; font-weight: 600; color: #747686; text-transform: uppercase;">Active Submissions</div>
                <div style="font-size: 22px; font-weight: 800; color: #131b2e; margin-top: 4px;">{metrics['total_applications_active']} Active</div>
                <div style="font-size: 11px; color: #747686;">Across 114 seniors</div>
            </div>
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px; box-shadow: 0 1px 3px rgba(15,23,42,0.05);">
                <div style="font-size: 11px; font-weight: 600; color: #747686; text-transform: uppercase;">cDocs Dispatch Rate</div>
                <div style="font-size: 22px; font-weight: 800; color: #d97706; margin-top: 4px;">{metrics['cdocs_dispatched_rate']}</div>
                <div style="font-size: 11px; color: #d97706; font-weight: 600;">Parchment & Common App</div>
            </div>
        </div>
        """
    )

    tab_students, tab_broadcast, tab_alumni, tab_faculty = st.tabs([
        "📋 Cohort Roster & cDocs Delivery Matrix",
        "📢 Cialfo Groups & Target Broadcast",
        "👥 Alumni Scattergram & Mentorship Bridge",
        "🏫 LIS Faculty & Staff Directory (33 Members)"
    ])

    with tab_students:
        col_c_sel, col_filter = st.columns([1.5, 2])
        with col_c_sel:
            cohort_view = st.radio("Cohort View:", ["12th Grade (College Applications)", "9th Grade (Career & Quest)"], horizontal=True)

        selected_grade = "12" if "12th" in cohort_view else "9"
        displayed_students = [s for s in students if str(s.get("grade", "")) == selected_grade]

        student_rows_list = []
        for s in displayed_students:
            s_name = s.get("name", "Student")
            s_initial = s_name[0] if s_name else "S"
            s_id = s.get("id", "H12")
            s_persona = s.get("persona", "Applying Alpaca")
            s_apps = s.get("apps_count", 5)
            s_top = s.get("top_choice") or (", ".join(s.get("target_countries", [])) + " Higher Ed" if s.get("target_countries") else "US Top 30")
            s_cdocs = s.get("cdocs_status", "Ready to Send")
            s_deadline = s.get("next_deadline") or s.get("first_deadline") or "Nov 1 (Early Decision)"
            badge_class = 'badge-emerald' if 'Dispatched' in s_cdocs else ('badge-blue' if 'Ready' in s_cdocs else 'badge-amber')

            student_rows_list.append(
                f"""<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; border-bottom: 1px solid #f1f5f9; font-size: 13px;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 36px; height: 36px; border-radius: 50%; background: #eff6ff; color: #1d4ed8; display: flex; align-items: center; justify-content: center; font-weight: 700;">
                            {s_initial}
                        </div>
                        <div>
                            <strong>{s_name}</strong> <span class="badge-slate">ID: {s_id}</span> <span class="badge-blue">{s_persona}</span>
                            <div style="color: #64748b; font-size: 12px;">{s_apps} Active Apps • Target: {s_top}</div>
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <span class="{badge_class}">{s_cdocs}</span>
                        <div style="font-size: 11px; color: #ba1a1a; font-weight: 600; margin-top: 3px;">Due: {s_deadline}</div>
                    </div>
                </div>"""
            )
        student_rows = "".join(student_rows_list)

        render_html(
            f"""
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px; margin-top: 10px;">
                <h4 style="margin: 0 0 12px 0; font-size: 15px; font-weight: 700; color: #131b2e;">
                    Assigned LIS Students — Grade {selected_grade} ({len(displayed_students)} Students Active)
                </h4>
                {student_rows}
            </div>
            """
        )

        if st.button("📤 Batch Dispatch cDocs Envelope to Common App & Parchment", key="btn_dispatch_cdocs"):
            with st.spinner("Cryptographically signing and dispatching electronic transcripts and counselor evaluations..."):
                st.success("cDocs batch transmission complete! 42 student envelopes dispatched with zero validation errors.")

    with tab_broadcast:
        render_html(
            """
            <div class="cialfo-card cialfo-card-primary" style="margin-bottom: 16px;">
                <h3 style="margin: 0 0 6px 0; font-size: 17px; font-weight: 700; color: #131b2e;">Targeted Cialfo Groups</h3>
                <p style="margin: 0; font-size: 13px; color: #434655;">
                    Send customized multi-channel broadcasts (Email, SMS, In-App) to specific subgroups without spamming the entire grade.
                </p>
            </div>
            """
        )

        col_grp, col_msg = st.columns([1, 1.4])
        with col_grp:
            selected_grp_idx = st.selectbox(
                "Select Target Cialfo Group:",
                range(len(groups)),
                format_func=lambda i: f"{groups[i]['name']} ({groups[i]['student_count']} students)",
                key="sel_cialfo_group"
            )
            g = groups[selected_grp_idx]
            render_html(
                f"""
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; margin-top: 8px; font-size: 12px;">
                    <div><strong>Group ID:</strong> <code>{g['id']}</code></div>
                    <div><strong>Critical Deadline:</strong> <span style="color: #ba1a1a; font-weight: 700;">{g['deadline']}</span></div>
                    <div><strong>Current Focus:</strong> {g['status']}</div>
                    <div style="margin-top: 6px;"><strong>Tags:</strong> {', '.join(g['tags'])}</div>
                </div>
                """
            )

        with col_msg:
            b_channel = st.multiselect("Broadcast Channels:", ["In-App Notification", "Student Email", "Parent WhatsApp/SMS"], default=["In-App Notification", "Student Email"])
            b_subject = st.text_input("Broadcast Subject:", value=f"Urgent: Action required before {g['deadline']} deadline")
            b_body = st.text_area(
                "Broadcast Message Body:",
                value=f"Dear {g['name']} students,\n\nPlease log in to Cialfo to verify your final documents and recommendations ahead of the upcoming {g['deadline']} deadline.",
                height=110
            )

            if st.button("🚀 Send Targeted Broadcast", key="btn_send_broadcast"):
                with st.spinner("Dispatching multi-channel messages..."):
                    st.success(f"Broadcast sent to {g['student_count']} students and parents via {', '.join(b_channel)}!")

    with tab_alumni:
        render_html(
            """
            <div class="cialfo-card cialfo-card-warning" style="margin-bottom: 16px;">
                <h3 style="margin: 0 0 6px 0; font-size: 17px; font-weight: 700; color: #131b2e;">
                    Alumni Scattergram Drilldown & Mentorship Bridge (Video 8)
                </h3>
                <p style="margin: 0; font-size: 13px; color: #434655;">
                    While students and parents only view anonymous scattergram plots, counselors have full access to real alumni names to connect current seniors with matriculated university mentors.
                </p>
            </div>
            """
        )

        for a in alumni:
            render_html(
                f"""
                <div class="cialfo-card" style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                        <div>
                            <h4 style="margin: 0; font-size: 16px; font-weight: 700; color: #131b2e;">{a['university']}</h4>
                            <div style="font-size: 13px; color: #1d4ed8; font-weight: 600;">Alumni Mentor: {a['alumni_name']} ({a['program']})</div>
                            <div style="font-size: 12px; color: #64748b; margin-top: 2px;">Admit Profile: {a['admit_stats']} • Email: <code>{a['email']}</code></div>
                        </div>
                        <div>
                            <span class="badge-emerald">Mentorship Active</span>
                        </div>
                    </div>
                </div>
                """
            )

        prof = DataManager.get_student_profile()
        active_student_name = prof["student"]["name"]
        if st.button(f"🤝 Connect {active_student_name} with Min-woo Park (Imperial Computing Mentor)", key="btn_connect_alumni"):
            with st.spinner("Facilitating warm counselor introduction..."):
                st.success(f"Mentorship introduction email drafted for {active_student_name} and scheduled for Peter Yoo's review!")

    with tab_faculty:
        render_html(
            f"""
            <div class="cialfo-card cialfo-card-primary" style="margin-bottom: 16px;">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 6px;">
                    {get_school_logo_html(40)}
                    <div>
                        <h3 style="margin: 0; font-size: 18px; font-weight: 700; color: #131b2e;">
                            Leaders International School (LIS) Faculty & Staff Directory
                        </h3>
                        <p style="margin: 2px 0 0 0; font-size: 13px; color: #434655;">
                            Official 2026 Academic Faculty Roster (33 members) across Leadership, Secondary/Elementary Teaching, and Administration.
                        </p>
                    </div>
                </div>
            </div>
            """
        )

        fac_list = DataManager.get_faculty_directory()
        col_f_search, col_f_div = st.columns([2, 1])
        with col_f_search:
            f_q = st.text_input("Search faculty by name or role:", value="", placeholder="e.g. David Nah, Paul Kim, Computer Science, Math...", key="fac_search_q")
        with col_f_div:
            f_div = st.selectbox("Division Filter:", ["All", "ADMININSTRATIVE", "TEACHING", "FACILITY"], key="fac_div_sel")

        filtered_fac = []
        for f in fac_list:
            if f_div != "All" and f_div not in f.get("division", ""):
                continue
            if f_q:
                match = (
                    f_q.lower() in f.get("korean_name", "").lower()
                    or f_q.lower() in f.get("english_name", "").lower()
                    or f_q.lower() in f.get("role", "").lower()
                )
                if not match:
                    continue
            filtered_fac.append(f)

        st.markdown(f"**Showing {len(filtered_fac)} Faculty & Staff Members**")

        for f in filtered_fac:
            ext_badge = f"<span class='badge-blue'>Ext: {f['extension']}</span>" if f['extension'] else ""
            render_html(
                f"""
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <strong style="font-size: 14px; color: #131b2e;">No.{f['no']} {f['english_name']} ({f['korean_name']})</strong>
                            <span class="badge-slate">{f['division']}</span>
                            {ext_badge}
                        </div>
                        <div style="font-size: 12px; color: #1d4ed8; font-weight: 600; margin-top: 2px;">
                            {f['role']}
                        </div>
                    </div>
                    <div>
                        <span class="badge-emerald">{f['employment']}</span>
                    </div>
                </div>
                """
            )
