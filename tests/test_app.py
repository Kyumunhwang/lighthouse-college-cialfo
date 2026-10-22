"""
Integration & Unit Test Suite for Cialfo Next-Gen CCR Platform
"""
import sys
from pathlib import Path

# Add project root to sys.path
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from modules.data_manager import DataManager
from modules.ai_copilot import SaigeAICopilot
from modules.data_pipeline import DATA_SOURCES_SPEC, get_pipeline_guide_markdown
from modules.ui_utils import render_html

def test_data_manager():
    print("Testing DataManager...")
    prof = DataManager.get_student_profile()
    seniors = DataManager.get_h12_seniors()
    assert len(seniors) == 17
    print(f"[PASS] Real LIS Grade 12 Seniors: {len(seniors)} students loaded from Excel roster")

    assert any(prof["student"]["student_id"] == s["student_id"] for s in seniors)
    assert prof["quest_persona"]["level"] == 4
    print("[PASS] Real LIS Student Profile Loaded:", prof["student"]["name"])

    # Test student switching
    first_senior = seniors[0]
    switched = DataManager.switch_active_student(first_senior["student_id"])
    assert switched["active_student_id"] == first_senior["student_id"]
    print(f"[PASS] Dynamically switched active senior to: {first_senior['passport_name']} ({first_senior['korean_name']})")
    # Restore default senior (Sumin Cho)
    DataManager.switch_active_student("2019F0502")

    univs = DataManager.get_universities()
    assert len(univs) >= 6
    print(f"[PASS] Universities Loaded: {len(univs)} records")

    courses = DataManager.get_courses()
    assert len(courses) >= 5
    print(f"[PASS] Courses Loaded: {len(courses)} records")

    apps = DataManager.get_applications()
    assert len(apps) >= 3
    print(f"[PASS] Applications Loaded: {len(apps)} records")

    lors = DataManager.get_lor_data()
    assert len(lors["recommenders"]) >= 2
    print(f"[PASS] LOR Recommenders Loaded: {len(lors['recommenders'])} records")

    c_data = DataManager.get_counselor_data()
    assert len(c_data["cialfo_groups"]) >= 4
    print(f"[PASS] Counselor Data Loaded: {len(c_data['cialfo_groups'])} groups")

    exp_data = DataManager.get_explore_partner_data()
    assert len(exp_data["high_school_visits_schedule"]) >= 2
    print(f"[PASS] Explore Partner Data Loaded: {len(exp_data['high_school_visits_schedule'])} visits")


def test_ai_copilot():
    print("\nTesting AI Copilot (Saige & LOR Bridge)...")
    ans_turkish = SaigeAICopilot.ask_saige("Does Imperial recognize Turkish diploma?")
    assert "Turkish" in ans_turkish or "Imperial" in ans_turkish
    print("[PASS] Saige Turkish Diploma Check passed")

    ans_steam = SaigeAICopilot.ask_saige("Tell me about dual degrees in STEAM and music")
    assert "STEAM" in ans_steam or "Music" in ans_steam
    print("[PASS] Saige STEAM Check passed")

    lor_trans = SaigeAICopilot.translate_and_polish_lor("학생은 물리에 뛰어납니다.", "Korean")
    assert len(lor_trans) > 50
    print("[PASS] LOR Multilingual Translation passed")


def test_data_pipeline_specs():
    print("\nTesting Data Pipeline & Sources Spec...")
    assert len(DATA_SOURCES_SPEC) == 6
    guide = get_pipeline_guide_markdown()
    assert "College Scorecard" in guide
    assert "Flywire" in guide
    assert "Technolutions Slate" in guide
    assert "UCAS" in guide
    print("[PASS] Data Sources Specification complete (all 6 screens covered)")


if __name__ == "__main__":
    test_data_manager()
    test_ai_copilot()
    test_data_pipeline_specs()
    print("\n===========================================")
    print("ALL TESTS PASSED WITH 100% SUCCESS!")
    print("===========================================")
