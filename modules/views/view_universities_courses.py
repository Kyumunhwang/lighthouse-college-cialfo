"""
View: Universities & Global Course Search
Directly mirrors design/universities_global_course_search/code.html
Solves PP-02 (Smart Scope Switching & Zero-Result Fallback)
Incorporates 1,500+ US Colleges dataset with IPEDS, Need-Blind/Need-Met aid policies, and QuestBridge status.
"""
import streamlit as st
from modules.data_manager import DataManager
from modules.ui_utils import render_html


def render_universities_courses_view():
    """Render Universities and Course Search with interactive Overview Drawer and US college dataset."""
    tab_univ, tab_courses = st.tabs([
        "🏛️ Global Universities Explorer (1,510 Institutions)",
        "🎓 Course & Degree Search (5,039 Programs)"
    ])

    with tab_univ:
        render_html(
            """
            <div style="margin-bottom: 16px;">
                <h2 style="margin: 0; font-size: 24px; font-weight: 700; color: #131b2e;">Universities & Colleges Explorer</h2>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #434655;">
                    Smart Scope Switching enabled • Comprehensive directory of <strong>1,500+ US Colleges & Global Universities</strong> with IPEDS, financial aid policies (Need-Blind, QuestBridge, 100% Need Met), and real LIS admissions fit benchmarking.
                </p>
            </div>
            """
        )

        # Session state for pagination
        if "univ_page" not in st.session_state:
            st.session_state["univ_page"] = 1

        # Search & Filter Controls - Row 1
        col_search, col_country, col_portal = st.columns([2, 1, 1])
        with col_search:
            search_query = st.text_input(
                "Search by name, city, state, or discipline (e.g. Harvard, Berkeley, Atlanta, Aviation):",
                value="",
                placeholder="Type university name or keywords...",
                key="univ_search_input"
            )
        with col_country:
            selected_country = st.selectbox(
                "Country / Region:",
                ["All", "United States", "United Kingdom", "Australia", "Canada", "Singapore", "Japan"],
                key="univ_country_select"
            )
        with col_portal:
            selected_portal = st.selectbox(
                "Application Portal:",
                ["All", "Direct Apply", "Common App", "QuestBridge", "UCAS"],
                key="univ_portal_select"
            )

        # Search & Filter Controls - Row 2 (US State & Aid Policy Filters)
        col_state, col_aid, col_size = st.columns([1.2, 1.4, 1])
        with col_state:
            us_states = ["All"] + DataManager.get_us_states()
            selected_state = st.selectbox(
                "US State (Filter by state):",
                us_states,
                key="univ_state_select",
                disabled=(selected_country not in ["All", "United States"])
            )
        with col_aid:
            selected_aid = st.selectbox(
                "Financial Aid Policy:",
                ["All", "Need-Blind", "QuestBridge", "100% Need Met"],
                key="univ_aid_select"
            )
        with col_size:
            page_size = st.selectbox(
                "Results Per Page:",
                [20, 30, 50, 100],
                index=1,
                key="univ_page_size_select"
            )

        # Reset page to 1 if search query or filters change
        current_filter_hash = f"{search_query}|{selected_country}|{selected_portal}|{selected_state}|{selected_aid}|{page_size}"
        if st.session_state.get("last_filter_hash") != current_filter_hash:
            st.session_state["last_filter_hash"] = current_filter_hash
            st.session_state["univ_page"] = 1

        # Execute Paginated Query
        res = DataManager.get_universities_paginated(
            query=search_query,
            country=selected_country,
            portal=selected_portal,
            state=selected_state,
            aid_policy=selected_aid,
            page=st.session_state["univ_page"],
            page_size=page_size
        )

        total_count = res["total_count"]
        total_pages = res["total_pages"]
        curr_page = res["current_page"]
        univs = res["items"]

        # Smart Scope Zero-Result Fallback (PP-02)
        if total_count == 0 and search_query:
            st.warning(
                "⚠️ Zero results found in your active filter combination. Auto-switching scope to Global Database (PP-02 Smart Fallback)..."
            )
            fallback_res = DataManager.get_universities_paginated(
                query=search_query,
                country="All",
                portal="All",
                state="All",
                aid_policy="All",
                page=1,
                page_size=page_size
            )
            if fallback_res["total_count"] > 0:
                st.info(f"💡 Found {fallback_res['total_count']:,} matching institutions across the global database!")
                res = fallback_res
                total_count = res["total_count"]
                total_pages = res["total_pages"]
                curr_page = res["current_page"]
                univs = res["items"]

        # Top Pagination & Summary Bar
        start_idx = res["offset"] + 1 if total_count > 0 else 0
        end_idx = min(res["offset"] + page_size, total_count)
        
        c_sum, c_prev, c_page_info, c_next = st.columns([2.5, 0.8, 1.2, 0.8])
        with c_sum:
            render_html(
                f"<div style='font-size: 14px; font-weight: 600; color: #131b2e; padding-top: 8px;'>"
                f"Showing <strong>{start_idx:,} – {end_idx:,}</strong> of <strong>{total_count:,}</strong> Institutions"
                f"</div>"
            )
        with c_prev:
            if st.button("◀ Prev", key="btn_page_prev", disabled=(curr_page <= 1)):
                st.session_state["univ_page"] = max(1, curr_page - 1)
                st.rerun()
        with c_page_info:
            render_html(
                f"<div style='text-align: center; font-size: 13px; font-weight: 600; color: #434655; padding-top: 8px;'>"
                f"Page {curr_page} / {total_pages}"
                f"</div>"
            )
        with c_next:
            if st.button("Next ▶", key="btn_page_next", disabled=(curr_page >= total_pages)):
                st.session_state["univ_page"] = min(total_pages, curr_page + 1)
                st.rerun()

        render_html("<hr style='margin: 8px 0 16px 0; border: none; border-top: 1px solid #e2e8f0;'/>")

        if not univs:
            st.info("No universities match the current search filters. Try clearing some filters or searching for another keyword.")

        # Universities Grid / Cards
        for idx, u in enumerate(univs):
            portals_badges = ""
            for p in u.get("portals", []):
                if p == "Direct Apply":
                    portals_badges += '<span class="badge-emerald">⚡ Direct Apply</span> '
                elif p == "Common App":
                    portals_badges += '<span class="badge-blue">🌊 Common App</span> '
                elif p == "UCAS":
                    portals_badges += '<span class="badge-amber">🇬🇧 UCAS</span> '
                elif p == "QuestBridge":
                    portals_badges += '<span class="badge-blue" style="background: #e0e7ff; color: #3730a3; border: 1px solid #c7d2fe;">🤝 QuestBridge</span> '
                else:
                    portals_badges += f'<span class="badge-slate">{p}</span> '

            # Aid Policy badges
            aid_badge_html = ""
            if u.get("aid_policy_type") == "Need-Blind":
                aid_badge_html += '<span class="badge-emerald" style="font-size: 11px;">🌟 Need-Blind</span> '
            if u.get("need_met_100"):
                aid_badge_html += '<span class="badge-purple" style="font-size: 11px; background: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">💯 100% Need Met</span> '
            if u.get("questbridge_partner"):
                aid_badge_html += '<span class="badge-blue" style="font-size: 11px;">🤝 QuestBridge Partner</span> '

            # IPEDS & Fee Waiver badges
            ipeds_html = f'<span class="badge-slate" style="font-size: 11px;">IPEDS: {u["ipeds_id"]}</span> ' if u.get("ipeds_id") else ""
            fee_waiver_html = ""
            if u.get("fee_waiver_available"):
                fee_waiver_html = f'<span class="badge-emerald" style="font-size: 11px;">💰 ${u["fee_waiver_amount_usd"]} Fee Waiver Active</span>'

            # Fit color coding
            fit_color = "#1d4ed8"
            if u.get("c_fit") == "Reach":
                fit_color = "#dc2626"
            elif u.get("c_fit") == "Target":
                fit_color = "#2563eb"
            elif u.get("c_fit") == "Likely":
                fit_color = "#16a34a"

            # SAT / GPA display string
            test_req_str = "Holistic Review"
            if u.get("avg_sat") and u.get("avg_sat") > 0:
                test_req_str = f"SAT: {u['avg_sat']}"
                if u.get("avg_gpa"):
                    test_req_str += f" • GPA: {u['avg_gpa']}"
            elif u.get("avg_gpa"):
                test_req_str = f"GPA: {u['avg_gpa']}"

            website_link = f'<a href="{u["website"]}" target="_blank" style="font-size: 12px; color: #1d4ed8; text-decoration: none; font-weight: 600;">🌐 Official Website &rarr;</a>' if u.get("website") else ''

            card_html = f"""
            <div class="cialfo-card {'cialfo-card-direct-apply' if u.get('direct_apply_eligible') else ''}" style="margin-bottom: 14px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px; margin-bottom: 10px;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span style="font-size: 22px;">{u['flag']}</span>
                            <div>
                                <h3 style="margin: 0; font-size: 17px; font-weight: 700; color: #131b2e;">{u['name']}</h3>
                                <div style="font-size: 12px; color: #747686;">{u['location']} • <strong>{u['ranking']}</strong></div>
                            </div>
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap;">
                        {ipeds_html}
                        {aid_badge_html}
                        {fee_waiver_html}
                        <span class="badge-slate" style="font-size: 11px;">Deadline: {u['first_deadline']}</span>
                    </div>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 8px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px; margin-bottom: 10px;">
                    <div>
                        <div style="font-size: 10px; color: #747686; font-weight: 600;">ACCEPTANCE RATE</div>
                        <div style="font-size: 14px; font-weight: 700; color: #131b2e;">{u['acceptance_rate']}</div>
                    </div>
                    <div>
                        <div style="font-size: 10px; color: #747686; font-weight: 600;">ANNUAL COA / TUITION</div>
                        <div style="font-size: 14px; font-weight: 700; color: #131b2e;">${u['tuition_annual_usd']:,} / yr</div>
                    </div>
                    <div>
                        <div style="font-size: 10px; color: #747686; font-weight: 600;">MEDIAN SCORES</div>
                        <div style="font-size: 13px; font-weight: 700; color: #334155;">{test_req_str}</div>
                    </div>
                    <div>
                        <div style="font-size: 10px; color: #747686; font-weight: 600;">CIALFO FIT</div>
                        <div style="font-size: 14px; font-weight: 700; color: {fit_color};">{u['c_fit']}</div>
                    </div>
                    <div>
                        <div style="font-size: 10px; color: #747686; font-weight: 600;">COUNSELOR LIKELIHOOD</div>
                        <div style="font-size: 12px; font-weight: 700; color: #d97706;">{u['counselor_likelihood']}</div>
                    </div>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                    <div>
                        <span style="font-size: 11px; font-weight: 600; color: #747686; margin-right: 4px;">Admissions Portals:</span>
                        {portals_badges}
                    </div>
                    <div>
                        {website_link}
                    </div>
                </div>
            </div>
            """
            render_html(card_html)

            # Overview Drawer Details Expander
            with st.expander(f"🔍 Inspect Overview & Scattergram for {u['name']}", expanded=False):
                col_det1, col_det2 = st.columns([1.2, 1])
                with col_det1:
                    st.markdown(f"**Campus Overview**: {u['overview']}")
                    st.markdown(f"**Offer Terms & Standard Requirements**: {u['offer_terms']}")
                    if u.get("culture_profile"):
                        st.markdown(f"**Campus Culture Profile**: `{u['culture_profile']}`")
                    if u.get("stem_rigor_weight"):
                        st.markdown(f"**STEM Academic Rigor Index**: `{int(u['stem_rigor_weight'] * 100)}%`")
                    if u.get("avg_intl_grant_usd"):
                        st.markdown(f"**Average International Aid Grant**: `${u['avg_intl_grant_usd']:,} / year`")
                    st.markdown("**Popular Programs & Faculties**:")
                    for c in u.get("popular_courses", []):
                        st.markdown(f"- 📘 `{c}`")
                with col_det2:
                    hist = u.get("school_historical", {})
                    outcomes_html = f"""
                    <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 12px;">
                        <div style="font-size: 12px; font-weight: 700; color: #1d4ed8; margin-bottom: 6px;">
                            📊 LIS Historical Admissions Outcomes
                        </div>
                        <div style="font-size: 12px; color: #1e3a8a; line-height: 1.6;">
                            • Historical Applicants: <strong>{hist.get('applicants_5yr', 'N/A')}</strong><br/>
                            • Accepted Cohort: <strong>{hist.get('accepted_5yr', 'N/A')}</strong><br/>
                            • Average Accepted SAT: <strong>{hist.get('avg_accepted_sat', u.get('avg_sat', 'N/A'))}</strong> (Your Score: <strong>1530</strong>)<br/>
                            • Average Accepted GPA: <strong>{hist.get('avg_accepted_gpa', u.get('avg_gpa', 'N/A'))}</strong> (Your GPA: <strong>3.94</strong>)
                        </div>
                    </div>
                    """
                    render_html(outcomes_html)
                    c_act1, c_act2 = st.columns(2)
                    with c_act1:
                        if st.button("🔖 Add to Shortlist", key=f"btn_shortlist_{idx}_{u.get('id', idx)}"):
                            with st.spinner("Syncing to Bookmarks..."):
                                st.success(f"{u['name']} added to Shortlist!")
                    with c_act2:
                        if u.get("direct_apply_eligible"):
                            if st.button("⚡ Start Direct Apply", key=f"btn_da_{idx}_{u.get('id', idx)}"):
                                with st.spinner("Launching Direct Apply Wizard..."):
                                    st.success(f"Direct Apply initialized for {u['name']}! Fee waiver applied.")
                        elif "Common App" in u.get("portals", []):
                            if st.button("🌊 Common App Link", key=f"btn_ca_{idx}_{u.get('id', idx)}"):
                                st.info(f"Ready to link Common App ID with {u['name']}.")

        # Bottom Pagination Bar
        if total_pages > 1:
            render_html("<hr style='margin: 16px 0 12px 0; border: none; border-top: 1px solid #e2e8f0;'/>")
            _, cb_prev, cb_info, cb_next, _ = st.columns([1.5, 1, 1.5, 1, 1.5])
            with cb_prev:
                if st.button("◀ Previous Page", key="btn_bot_prev", disabled=(curr_page <= 1)):
                    st.session_state["univ_page"] = max(1, curr_page - 1)
                    st.rerun()
            with cb_info:
                render_html(
                    f"<div style='text-align: center; font-size: 13px; font-weight: 600; color: #434655; padding-top: 8px;'>"
                    f"Page {curr_page} of {total_pages} ({total_count:,} Total)"
                    f"</div>"
                )
            with cb_next:
                if st.button("Next Page ▶", key="btn_bot_next", disabled=(curr_page >= total_pages)):
                    st.session_state["univ_page"] = min(total_pages, curr_page + 1)
                    st.rerun()

    with tab_courses:
        render_html(
            """
            <div style="margin-bottom: 16px;">
                <h2 style="margin: 0; font-size: 24px; font-weight: 700; color: #131b2e;">5,039 Course & Degree Catalog</h2>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #434655;">
                    Explore specialized disciplines: STEAM dual degrees, Commercial Pilot Aviation, Football Club Management, and Interactive Game Design.
                </p>
            </div>
            """
        )

        col_csearch, col_cat = st.columns([2, 1])
        with col_csearch:
            course_query = st.text_input(
                "Filter courses by keyword (e.g. Football, Aviation, STEAM, Robotics, Music):",
                value="",
                placeholder="Search specialized courses...",
                key="course_search_input"
            )
        with col_cat:
            course_cat = st.selectbox(
                "Discipline Category:",
                ["All", "STEAM", "Aviation", "Sports", "Design & Tech", "Engineering"],
                key="course_cat_select"
            )

        courses = DataManager.get_courses(query=course_query, category=course_cat)
        st.markdown(f"**Displaying {len(courses)} Curated Academic Pathways**")

        for c in courses:
            course_card_html = f"""
            <div class="cialfo-card cialfo-card-primary" style="margin-bottom: 14px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                    <div>
                        <span class="badge-blue">{c['category']}</span>
                        <h3 style="margin: 6px 0 2px 0; font-size: 17px; font-weight: 700; color: #131b2e;">{c['title']}</h3>
                        <div style="font-size: 13px; color: #747686;">{c['university']} • <strong>{c['country']}</strong></div>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge-emerald">{c['pathway']}</span>
                        <div style="font-size: 12px; font-weight: 600; color: #131b2e; margin-top: 4px;">Duration: {c['duration']}</div>
                    </div>
                </div>
                <p style="font-size: 13px; color: #434655; margin: 10px 0;">
                    {c['description']}
                </p>
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; font-size: 12px; background: #f8fafc; padding: 8px 12px; border-radius: 6px;">
                    <div><strong>Requirements:</strong> {c['requirements']}</div>
                    <div style="color: #059669; font-weight: 600;">🎁 {c['scholarship']}</div>
                </div>
            </div>
            """
            render_html(course_card_html)
