"""
Cialfo Next-Gen Global CCR Platform Configuration & Design Tokens
Derived from design/global_guidance_direct_admissions/DESIGN.md & prd.md
"""
from dataclasses import dataclass
from typing import Dict, Any

DEFAULT_PORT = 3088

# Design System Color Tokens (Plus Jakarta Sans & Inter)
THEME_COLORS = {
    "primary": "#1d4ed8",              # Royal Blue: Navigation & Primary Actions
    "primary_dark": "#0037b0",
    "primary_light": "#cad3ff",
    "primary_container": "#1d4ed8",
    "secondary": "#d97706",            # Lion Gold: Milestones, Scholarships, Deadlines
    "secondary_container": "#fe932c",
    "tertiary": "#059669",             # Direct Apply Emerald: Verified & Unconditional Offers
    "tertiary_container": "#006948",
    "tertiary_light": "#ecfdf5",
    "surface": "#faf8ff",              # Base Canvas
    "surface_container_lowest": "#ffffff", # Elevated Cards
    "surface_container_low": "#f2f3ff",
    "surface_container": "#eaedff",
    "surface_container_high": "#e2e7ff",
    "on_surface": "#131b2e",           # Slate Ink
    "on_surface_variant": "#434655",
    "outline": "#747686",
    "outline_variant": "#e2e8f0",
    "error": "#ba1a1a",
    "error_container": "#ffdad6"
}

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #131b2e;
}

h1, h2, h3, h4, .headline-font {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700;
}

/* Base Streamlit Overrides */
.stApp {
    background-color: #faf8ff;
}

/* Card Styling */
.cialfo-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 1px 3px 0 rgba(15, 23, 42, 0.05);
    transition: all 0.2s ease-in-out;
}

.cialfo-card:hover {
    border-color: #cbd5e1;
    box-shadow: 0 4px 6px -1px rgba(15, 23, 42, 0.08);
}

.cialfo-card-direct-apply {
    border-left: 4px solid #059669;
}

.cialfo-card-warning {
    border-left: 4px solid #d97706;
}

.cialfo-card-primary {
    border-left: 4px solid #1d4ed8;
}

/* Badges */
.badge-emerald {
    background-color: #ecfdf5;
    color: #059669;
    border: 1px solid #a7f3d0;
    padding: 4px 10px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

.badge-blue {
    background-color: #eff6ff;
    color: #1d4ed8;
    border: 1px solid #bfdbfe;
    padding: 4px 10px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

.badge-amber {
    background-color: #fffbeb;
    color: #b45309;
    border: 1px solid #fde68a;
    padding: 4px 10px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

.badge-slate {
    background-color: #f1f5f9;
    color: #475569;
    border: 1px solid #e2e8f0;
    padding: 4px 10px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

/* Stepper Bar */
.stepper-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin: 16px 0;
}

.stepper-step {
    background: #f2f3ff;
    border-radius: 10px;
    padding: 12px 14px;
    border: 1px solid #e2e7ff;
}

.stepper-step.active {
    background: #ffffff;
    border: 2px solid #1d4ed8;
    box-shadow: 0 2px 4px rgba(29, 78, 216, 0.1);
}

.stepper-step.done {
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
}

/* Buttons */
.stButton>button {
    border-radius: 8px;
    font-weight: 600;
    font-family: 'Inter', sans-serif;
    transition: all 0.2s;
}

/* Metric Display Overrides */
div[data-testid="stMetricValue"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700;
    color: #131b2e;
}
</style>
"""

import base64
from pathlib import Path

_EMBLEM_PATH = Path(__file__).parent / "emblum.png"
_CACHED_DATA_URI = None

def get_school_logo_data_uri() -> str:
    """Return base64 Data URI for the official school emblem (emblum.png)."""
    global _CACHED_DATA_URI
    if _CACHED_DATA_URI is None:
        if _EMBLEM_PATH.exists():
            with open(_EMBLEM_PATH, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
                _CACHED_DATA_URI = f"data:image/png;base64,{b64}"
        else:
            _CACHED_DATA_URI = ""
    return _CACHED_DATA_URI

def get_school_logo_html(size: int = 36, style: str = "") -> str:
    """Return an <img> HTML string with the official school emblem."""
    uri = get_school_logo_data_uri()
    if not uri:
        return "🏫"
    return f'<img src="{uri}" alt="LIS Emblem" style="width: {size}px; height: {size}px; object-fit: contain; vertical-align: middle; {style}" />'
