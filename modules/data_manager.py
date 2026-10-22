"""
Data Manager Module for Cialfo Next-Gen CCR Platform
Handles loading, caching, querying, and optimistic saving of local JSON databases.
"""
import json
import os
from pathlib import Path
from typing import Dict, Any, List, Optional

DATA_DIR = Path(__file__).parent.parent / "data"

class DataManager:
    """Manages local JSON databases with defensive error handling."""
    
    @staticmethod
    def _read_json(filename: str) -> Any:
        path = DATA_DIR / filename
        if not path.exists():
            raise FileNotFoundError(f"Database file not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def _write_json(filename: str, data: Any) -> None:
        path = DATA_DIR / filename
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @classmethod
    def get_student_profile(cls) -> Dict[str, Any]:
        """Fetch active student profile, roadmap stages, and animal persona."""
        return cls._read_json("student_profile.json")

    @classmethod
    def update_student_kudos(cls, increment: int = 1) -> int:
        """Increment Kudos count on gamified quest persona."""
        profile = cls.get_student_profile()
        profile["quest_persona"]["kudos_count"] += increment
        cls._write_json("student_profile.json", profile)
        return profile["quest_persona"]["kudos_count"]

    @classmethod
    def get_universities(
        cls,
        query: str = "",
        country: str = "All",
        portal: str = "All",
        state: str = "All",
        aid_policy: str = "All",
        limit: Optional[int] = None,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """Fetch global universities (1,500+ records) with keyword, state, and aid filtering."""
        univs = cls._read_json("universities.json")
        filtered = []
        q = query.strip().lower()
        for u in univs:
            if country != "All" and u.get("country") != country:
                continue
            if state != "All" and u.get("state") != state:
                continue
            if portal != "All" and portal not in u.get("portals", []):
                continue
            if aid_policy != "All":
                if aid_policy == "Need-Blind" and u.get("aid_policy_type") != "Need-Blind":
                    continue
                if aid_policy == "QuestBridge" and not u.get("questbridge_partner"):
                    continue
                if aid_policy == "100% Need Met" and not u.get("need_met_100"):
                    continue
            if q:
                match = (
                    q in u.get("name", "").lower()
                    or q in u.get("location", "").lower()
                    or q in u.get("state", "").lower()
                    or q in u.get("city", "").lower()
                    or any(q in c.lower() for c in u.get("popular_courses", []))
                )
                if not match:
                    continue
            filtered.append(u)
        
        if limit is not None:
            return filtered[offset : offset + limit]
        return filtered

    @classmethod
    def get_universities_paginated(
        cls,
        query: str = "",
        country: str = "All",
        portal: str = "All",
        state: str = "All",
        aid_policy: str = "All",
        page: int = 1,
        page_size: int = 30
    ) -> Dict[str, Any]:
        """Fetch paginated universities with total count and page metadata."""
        all_matches = cls.get_universities(
            query=query,
            country=country,
            portal=portal,
            state=state,
            aid_policy=aid_policy,
            limit=None,
            offset=0
        )
        total_count = len(all_matches)
        total_pages = max(1, (total_count + page_size - 1) // page_size)
        curr_page = max(1, min(page, total_pages))
        offset = (curr_page - 1) * page_size
        items = all_matches[offset : offset + page_size]
        return {
            "total_count": total_count,
            "total_pages": total_pages,
            "current_page": curr_page,
            "page_size": page_size,
            "offset": offset,
            "items": items
        }

    @classmethod
    def get_us_states(cls) -> List[str]:
        """Return sorted unique list of US states present in the college dataset."""
        univs = cls._read_json("universities.json")
        states = sorted(list(set(u["state"] for u in univs if u.get("state"))))
        return states

    @classmethod
    def get_courses(cls, query: str = "", category: str = "All") -> List[Dict[str, Any]]:
        """Fetch course catalog (STEAM, Aviation, Sports, etc.)."""
        courses = cls._read_json("courses.json")
        filtered = []
        q = query.strip().lower()
        for c in courses:
            if category != "All" and c.get("category") != category:
                continue
            if q:
                match = (
                    q in c.get("title", "").lower()
                    or q in c.get("university", "").lower()
                    or q in c.get("description", "").lower()
                )
                if not match:
                    continue
            filtered.append(c)
        return filtered

    @classmethod
    def get_applications(cls) -> List[Dict[str, Any]]:
        """Fetch active applications, UK conditional offers, and Flywire payments."""
        return cls._read_json("applications.json")

    @classmethod
    def update_flywire_status(cls, app_id: str, new_status: str) -> bool:
        """Simulate updating Flywire real-time payment status."""
        apps = cls.get_applications()
        updated = False
        for a in apps:
            if a["id"] == app_id:
                a["flywire_payment"]["status"] = new_status
                updated = True
                break
        if updated:
            cls._write_json("applications.json", apps)
        return updated

    @classmethod
    def get_lor_data(cls) -> Dict[str, Any]:
        """Fetch 2-tier structured LOR form state, recommenders, and AI bridge."""
        return cls._read_json("lor_requests.json")

    @classmethod
    def update_tier_1_reflections(cls, adjectives: str, explanation: str, extracurricular: str, background: str) -> None:
        """Update Tier 1 common reflection fields with optimistic auto-save."""
        data = cls.get_lor_data()
        data["tier_1_common_reflections"]["three_adjectives"] = adjectives
        data["tier_1_common_reflections"]["adjectives_explanation"] = explanation
        data["tier_1_common_reflections"]["extracurricular_highlights"] = extracurricular
        data["tier_1_common_reflections"]["background_challenges"] = background
        cls._write_json("lor_requests.json", data)

    @classmethod
    def get_counselor_data(cls) -> Dict[str, Any]:
        """Fetch Counselor Command Center cohorts, cDocs, and alumni network."""
        return cls._read_json("counselor_data.json")

    @classmethod
    def get_explore_partner_data(cls) -> Dict[str, Any]:
        """Fetch Explore partner dashboard, 4-stage funnel, and high school visits."""
        return cls._read_json("explore_partner.json")

    @classmethod
    def get_faculty_directory(cls) -> List[Dict[str, Any]]:
        """Fetch full official faculty directory (33 members) from LIS Faculty Roster."""
        return cls._read_json("lis_faculty.json")

    @classmethod
    def get_h12_seniors(cls) -> List[Dict[str, Any]]:
        """Fetch all real 17 seniors from LIS Grade 12 (H12)."""
        data = cls.get_student_profile()
        return data.get("all_h12_seniors", [])

    @classmethod
    def switch_active_student(cls, student_id: str) -> Dict[str, Any]:
        """Switch active student profile to the specified LIS real student ID."""
        profile = cls.get_student_profile()
        seniors = profile.get("all_h12_seniors", [])
        matched = next((s for s in seniors if s["student_id"] == student_id), None)
        if matched:
            profile["active_student_id"] = matched["student_id"]
            profile["student"]["student_id"] = matched["student_id"]
            profile["student"]["name"] = f"{matched['passport_name']} ({matched['korean_name']})"
            profile["student"]["english_name"] = matched["english_name"] or "Senior"
            profile["student"]["korean_name"] = matched["korean_name"]
            profile["student"]["homeroom_teacher"] = matched.get("homeroom_teacher", "Peter Yoo")
            profile["student"]["dob"] = matched.get("dob", "")
            profile["student"]["gender"] = matched.get("gender", "")
            profile["student"]["address"] = matched.get("address", "")
            profile["student"]["guardians"] = {
                "father": matched.get("father", ""),
                "mother": matched.get("mother", ""),
                "contact": matched.get("cell", "")
            }
            cls._write_json("student_profile.json", profile)
        return profile
