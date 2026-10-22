"""
View: Explore Partner Console (University Admissions & Visits)
Directly mirrors design/explore_university_admissions_high_school_visits_console/code.html
Features 4-Stage Funnel, AI Recommended Visits, and Slate CRM Push
"""
import streamlit as st
from modules.data_manager import DataManager
from modules.ui_utils import render_html


def render_explore_visits_view():
    """Render Explore Partner Console for University Admissions Officers."""
    partner_data = DataManager.get_explore_partner_data()
    inst = partner_data["institution"]
    funnel = partner_data["funnel_metrics"]
    ai_recs = partner_data["ai_recommended_visits"]
    visits = partner_data["high_school_visits_schedule"]

    render_html(
        f"""
        <div style="margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 26px;">🌐</span>
                <h2 style="margin: 0; font-size: 24px; font-weight: 700; color: #131b2e;">Explore by Cialfo — Admissions Partner Console</h2>
            </div>
            <p style="margin: 4px 0 0 0; font-size: 13px; color: #434655;">
                Logged in as <strong>{inst['officer_name']}</strong> ({inst['role']} at {inst['name']})
            </p>
        </div>
        """
    )

    # 1. Slate CRM Status Bar
    render_html(
        f"""
        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 12px 16px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span class="badge-emerald">Technolutions Slate CRM</span>
                <span style="font-size: 13px; color: #131b2e; font-weight: 600;">{inst['slate_crm_sync']}</span>
            </div>
            <div style="font-size: 12px; color: #747686;">
                Auto-Pushing Qualified Connections Leads Every 60 Minutes
            </div>
        </div>
        """
    )

    # 2. 4-Stage Admissions Funnel
    render_html("<h3 style='font-size: 18px; font-weight: 700; color: #131b2e; margin-bottom: 12px;'>4-Stage Global Admissions Funnel</h3>")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_html(
            f"""
            <div class="cialfo-card cialfo-card-primary" style="padding: 16px;">
                <div style="font-size: 11px; font-weight: 700; color: #1d4ed8; text-transform: uppercase;">1. Connections</div>
                <div style="font-size: 24px; font-weight: 800; color: #131b2e; margin: 4px 0;">{funnel['connections']['total']:,}</div>
                <span class="badge-emerald">{funnel['connections']['yoy_growth']} YoY</span>
                <div style="font-size: 11px; color: #64748b; margin-top: 6px;">Profile & Event Opt-ins</div>
            </div>
            """
        )

    with c2:
        render_html(
            f"""
            <div class="cialfo-card cialfo-card-primary" style="padding: 16px;">
                <div style="font-size: 11px; font-weight: 700; color: #1d4ed8; text-transform: uppercase;">2. Shortlisted</div>
                <div style="font-size: 24px; font-weight: 800; color: #131b2e; margin: 4px 0;">{funnel['shortlisted']['total']:,}</div>
                <span class="badge-emerald">{funnel['shortlisted']['yoy_growth']} YoY</span>
                <div style="font-size: 11px; color: #64748b; margin-top: 6px;">Active Student Lists</div>
            </div>
            """
        )

    with c3:
        render_html(
            f"""
            <div class="cialfo-card cialfo-card-direct-apply" style="padding: 16px;">
                <div style="font-size: 11px; font-weight: 700; color: #059669; text-transform: uppercase;">3. Applicants</div>
                <div style="font-size: 24px; font-weight: 800; color: #131b2e; margin: 4px 0;">{funnel['applicants']['total']:,}</div>
                <div style="font-size: 12px; color: #059669; font-weight: 600;">{funnel['applicants']['direct_apply_count']} Direct Apply</div>
                <div style="font-size: 11px; color: #64748b; margin-top: 2px;">{funnel['applicants']['ucas_standard_count']} via UCAS</div>
            </div>
            """
        )

    with c4:
        render_html(
            f"""
            <div class="cialfo-card cialfo-card-warning" style="padding: 16px;">
                <div style="font-size: 11px; font-weight: 700; color: #d97706; text-transform: uppercase;">4. Offers Issued</div>
                <div style="font-size: 24px; font-weight: 800; color: #131b2e; margin: 4px 0;">{funnel['offers']['total']:,}</div>
                <div style="font-size: 12px; color: #d97706; font-weight: 600;">Acceptance: {funnel['offers']['offer_acceptance_rate']}</div>
                <div style="font-size: 11px; color: #64748b; margin-top: 2px;">{funnel['offers']['conditional_offers']} Conditional</div>
            </div>
            """
        )

    # 3. AI Recommended High School Visits
    render_html(
        """
        <div class="cialfo-card cialfo-card-primary" style="margin-top: 10px; margin-bottom: 16px;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                <span style="font-size: 20px;">🤖</span>
                <h3 style="margin: 0; font-size: 17px; font-weight: 700; color: #131b2e;">AI-Recommended High Schools to Visit</h3>
            </div>
            <p style="margin: 0; font-size: 13px; color: #434655;">
                Detected anomalous surges in student search queries and shortlist additions over the past 30 days.
            </p>
        </div>
        """
    )

    for rec in ai_recs:
        render_html(
            f"""
            <div class="cialfo-card" style="margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                    <div>
                        <h4 style="margin: 0; font-size: 16px; font-weight: 700; color: #131b2e;">{rec['high_school']}</h4>
                        <div style="font-size: 13px; color: #1d4ed8; font-weight: 600;">{rec['city']}, {rec['country']} • Counselor: {rec['counselor_contact']}</div>
                        <div style="font-size: 12px; color: #059669; font-weight: 600; margin-top: 4px;">📈 {rec['reason']}</div>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge-blue">Recommended: {rec['recommended_dates']}</span>
                        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Format: {rec['preferred_mode']}</div>
                    </div>
                </div>
            </div>
            """
        )

    # 4. Confirmed & Requested School Visits
    render_html("<h3 style='font-size: 18px; font-weight: 700; color: #131b2e; margin: 18px 0 12px 0;'>Scheduled High School Tours & Visits</h3>")
    for vis in visits:
        render_html(
            f"""
            <div class="cialfo-card cialfo-card-direct-apply" style="margin-bottom: 14px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <h4 style="margin: 0; font-size: 16px; font-weight: 700; color: #131b2e;">{vis['school_name']}</h4>
                            <span class="badge-emerald">{vis['booking_type']}</span>
                        </div>
                        <div style="font-size: 13px; color: #64748b; margin-top: 2px;">
                            {vis['city']} • <strong>{vis['date']} ({vis['time_slot']})</strong> • {vis['format']}
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge-blue">Registered: {vis['registered_students']} Students</span>
                        <div style="font-size: 11px; color: #059669; font-weight: 600; margin-top: 4px;">
                            Visit Rating: ★ {vis['rating']['overall_experience']} / 5.0
                        </div>
                    </div>
                </div>
                <div style="background: #f8fafc; border-radius: 6px; padding: 10px; margin-top: 10px; font-size: 12px; color: #434655;">
                    <strong>Security Instructions:</strong> {vis['security_instructions']}
                </div>
            </div>
            """
        )

    c_act1, c_act2 = st.columns(2)
    with c_act1:
        if st.button("📤 Export Slate CRM Lead Packets (.json / .csv)", key="btn_export_slate"):
            with st.spinner("Extracting qualified student leads formatted for Slate Configurable Joins..."):
                st.success("Slate data packet generated! 128 new student leads exported with FERPA/GDPR compliance tokens.")
    with c_act2:
        if st.button("📅 Download Full Tour Itinerary (.pdf)", key="btn_download_itinerary"):
            st.info("Compiling Southeast Asia & East Asia High School Visit Itinerary...")
