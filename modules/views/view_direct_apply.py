"""
View: Applications & Direct Apply Hub
Directly mirrors design/applications_direct_apply_hub/code.html
Features UK Conditional Offer Full Transparency & Embedded Flywire Payment
"""
import streamlit as st
from modules.data_manager import DataManager
from modules.ui_utils import render_html


def render_direct_apply_view():
    """Render Applications & Direct Apply Hub."""
    apps = DataManager.get_applications()

    render_html(
        """
        <div style="margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 26px;">⚡</span>
                <h2 style="margin: 0; font-size: 24px; font-weight: 700; color: #131b2e;">Applications & Direct Apply Hub</h2>
            </div>
            <p style="margin: 4px 0 0 0; font-size: 13px; color: #434655;">
                5-step direct admissions, fee waivers, transparent UK conditional offer tracking, and embedded Flywire tuition payment.
            </p>
        </div>
        """
    )

    # 1. Direct Apply Summary Banner
    render_html(
        """
        <div style="background: linear-gradient(135deg, #059669 0%, #004f35 100%); border-radius: 12px; padding: 22px; color: #ffffff; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(5,150,105,0.15);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                <div>
                    <span style="background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700; text-transform: uppercase;">Direct Apply Guaranteed Network</span>
                    <h3 style="margin: 8px 0 4px 0; font-size: 20px; font-weight: 800;">$450 Total Application Fees Waived</h3>
                    <p style="margin: 0; font-size: 13px; opacity: 0.9;">
                        2 Direct Apply submissions completed without external agency fees. Full Conditional Offer terms unlocked.
                    </p>
                </div>
                <div style="display: flex; gap: 10px;">
                    <div style="background: rgba(255,255,255,0.15); border-radius: 8px; padding: 10px 14px; text-align: center;">
                        <div style="font-size: 11px; opacity: 0.85;">SHEPHERD ADVISOR</div>
                        <div style="font-size: 14px; font-weight: 700;">Marcus Sterling</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.15); border-radius: 8px; padding: 10px 14px; text-align: center;">
                        <div style="font-size: 11px; opacity: 0.85;">VISA SUCCESS</div>
                        <div style="font-size: 14px; font-weight: 700;">100% Rate</div>
                    </div>
                </div>
            </div>
        </div>
        """
    )

    # 2. Applications List
    for app in apps:
        is_da = (app.get("portal") == "Direct Apply")
        card_class = "cialfo-card-direct-apply" if is_da else "cialfo-card-primary"
        fw = app.get("flywire_payment", {})
        
        # Build conditions rows if present
        conditions_html = ""
        if app.get("conditions"):
            cond_items = "".join([
                f"""<div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid #e2e8f0; font-size: 12px;">
                    <div>
                        <strong>{c['description']}</strong>
                        <div style="color: #64748b; font-size: 11px;">Target: <strong>{c['target_grade']}</strong> | Your Forecast/Score: <strong>{c['predicted_grade']}</strong></div>
                    </div>
                    <span class="{'badge-emerald' if c['status'] == 'Met & Verified' else ('badge-blue' if c['status'] == 'On Track' else 'badge-amber')}">
                        {c['status']}
                    </span>
                </div>""" for c in app["conditions"]
            ])
            conditions_html = f"""
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; margin: 12px 0;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-size: 12px; font-weight: 700; color: #004f35; text-transform: uppercase;">
                        🔍 Full Itemized Conditions Breakdown (Direct Apply Exclusive)
                    </span>
                    <span class="badge-emerald">Live Syndicate Feed</span>
                </div>
                {cond_items}
            </div>
            """

        fee_saved_badge = f'<span class="badge-emerald">💰 ${app["fee_waiver_saved_usd"]} Saved</span>' if app.get('fee_waiver_applied') else ''

        app_card_html = f"""
        <div class="cialfo-card {card_class}" style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 28px;">{app['flag']}</span>
                    <div>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <h3 style="margin: 0; font-size: 18px; font-weight: 700; color: #131b2e;">{app['university_name']}</h3>
                            <span class="badge-emerald" style="font-weight: 700;">{app['portal']}</span>
                            {fee_saved_badge}
                        </div>
                        <div style="font-size: 13px; color: #434655;">{app['program']}</div>
                    </div>
                </div>
                <div style="text-align: right;">
                    <span class="badge-blue" style="font-size: 13px; font-weight: 700;">{app['current_stage']}</span>
                    <div style="font-size: 11px; font-weight: 600; color: #d97706; margin-top: 4px;">{app['offer_type']}</div>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; margin: 12px 0 16px 0; text-align: center;">
                <div style="background: #ecfdf5; border: 1px solid #a7f3d0; padding: 6px; border-radius: 6px; font-size: 11px; font-weight: 700; color: #059669;">1. Profile Sync</div>
                <div style="background: #ecfdf5; border: 1px solid #a7f3d0; padding: 6px; border-radius: 6px; font-size: 11px; font-weight: 700; color: #059669;">2. Hubs Documents</div>
                <div style="background: {'#ecfdf5' if app['stage_step'] >= 3 else '#f1f5f9'}; border: 1px solid {'#a7f3d0' if app['stage_step'] >= 3 else '#e2e8f0'}; padding: 6px; border-radius: 6px; font-size: 11px; font-weight: 700; color: {'#059669' if app['stage_step'] >= 3 else '#64748b'};">3. Submission</div>
                <div style="background: {'#ecfdf5' if app['stage_step'] >= 4 else '#f1f5f9'}; border: 1px solid {'#a7f3d0' if app['stage_step'] >= 4 else '#e2e8f0'}; padding: 6px; border-radius: 6px; font-size: 11px; font-weight: 700; color: {'#059669' if app['stage_step'] >= 4 else '#64748b'};">4. Offer Received</div>
                <div style="background: {'#ecfdf5' if app['stage_step'] >= 5 else '#eff6ff'}; border: 1px solid {'#a7f3d0' if app['stage_step'] >= 5 else '#bfdbfe'}; padding: 6px; border-radius: 6px; font-size: 11px; font-weight: 700; color: {'#059669' if app['stage_step'] >= 5 else '#1d4ed8'};">5. Flywire Deposit</div>
            </div>

            {conditions_html}

            <div style="background: #ffffff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px; margin-top: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-size: 20px;">💳</span>
                        <div>
                            <div style="font-size: 13px; font-weight: 700; color: #1e3a8a;">Flywire Embedded Global Payment</div>
                            <div style="font-size: 11px; color: #64748b;">Ref: <code>{fw.get('flywire_reference')}</code> • 240 Countries / 140+ Currencies</div>
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge-blue" style="font-weight: 700;">Status: {fw.get('status')}</span>
                        <div style="font-size: 14px; font-weight: 800; color: #131b2e; margin-top: 2px;">
                            ${fw.get('amount_usd'):,} USD {f"({fw.get('amount_gbp')} GBP)" if 'amount_gbp' in fw else ''}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        render_html(app_card_html)

        col_act1, col_act2 = st.columns([1, 1.2])
        with col_act1:
            if st.button(f"💳 Pay Deposit via Flywire ({app['university_name']})", key=f"btn_pay_{app['id']}"):
                with st.spinner("Connecting securely to Flywire Education Gateway..."):
                    DataManager.update_flywire_status(app["id"], "Processing in Transit")
                    st.success("Payment initiated! Real-time status set to 'Processing in Transit'. Transferred to institution within 24-48 hrs.")
                    st.rerun()

        with col_act2:
            if app.get("urgent_chat_available"):
                if st.button(f"🚨 Urgent Chat with Cialfo Guide ({app['uea_counselor']})", key=f"btn_chat_{app['id']}"):
                    with st.spinner("Connecting to 1-Minute Priority Queue..."):
                        st.info(f"Connected to {app['uea_counselor']}! Estimated wait: 35 seconds. Your visa checklist is synchronized.")
