---
name: Global Guidance & Direct Admissions
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#434655'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#747686'
  outline-variant: '#c4c5d7'
  surface-tint: '#2151da'
  primary: '#0037b0'
  on-primary: '#ffffff'
  primary-container: '#1d4ed8'
  on-primary-container: '#cad3ff'
  inverse-primary: '#b7c4ff'
  secondary: '#904d00'
  on-secondary: '#ffffff'
  secondary-container: '#fe932c'
  on-secondary-container: '#663500'
  tertiary: '#004f35'
  on-tertiary: '#ffffff'
  tertiary-container: '#006948'
  on-tertiary-container: '#76eab6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b7c4ff'
  on-primary-fixed: '#001551'
  on-primary-fixed-variant: '#0039b5'
  secondary-fixed: '#ffdcc3'
  secondary-fixed-dim: '#ffb77d'
  on-secondary-fixed: '#2f1500'
  on-secondary-fixed-variant: '#6e3900'
  tertiary-fixed: '#85f8c4'
  tertiary-fixed-dim: '#68dba9'
  on-tertiary-fixed: '#002114'
  on-tertiary-fixed-variant: '#005137'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  title-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
  title-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-sm: 1rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

The design system is engineered for global college and career readiness (CCR), high school counseling suites, and direct university application workflows. It bridges high-stakes academic administration with aspirational student milestones. The visual narrative balances institutional authority, warmth, and momentum.

The design language balances **Modern EdTech Corporate** with **Targeted Vibrancy**:
- **Clarity & Confidence:** Utilitarian clarity derived from data-dense administrative dashboards, paired with humanized progress markers for students and guardians.
- **Milestone Orientation:** Workflows emphasize step progression, document completion (LORs, transcripts), and direct application status through purposeful color shifts.
- **Tone:** Professional, globally inclusive, motivating, and transparent. It avoids childish motifs while steering clear of cold, archaic academic software.

## Colors

The palette organizes multi-tiered educational tasks by intent: administrative control, achievement highlights, and direct admissions actions.

- **Primary (`#1D4ED8` - Royal Blue):** Anchors global navigation, primary action buttons, focused states, and institutional identity. Communicates security and trust.
- **Secondary (`#D97706` - Lion Gold):** Reserved for student milestones, scholarship indicators, counselor recommendations, high-priority deadlines, and attention-required flags.
- **Tertiary (`#059669` - Direct Apply Emerald):** Dedicated exclusively to the direct application pathway, document verification, submission success, and positive admission statuses.
- **Neutral (`#0F172A` - Slate Ink):** Serves as deep primary text, high-contrast borders, and structural container accents. Paired with canvas surfaces (`#F8FAFC`) and crisp container backgrounds (`#FFFFFF`).
- **Dividers & Outlines:** Bound with `#E2E8F0` to maintain clean spatial separation across dense data grids without visual clutter.

## Typography

The type scale combines **Plus Jakarta Sans** for expressive, modern headings with **Inter** for dense, ultra-legible body text and analytical tabular views.

- **Plus Jakarta Sans (Headings & Display):** Features gentle geometric terminals that make high-stakes guidance interfaces approachable and human.
- **Inter (Body, Tables, Forms, Badges):** Employs standard tabular lining figures for numerical alignment across GPAs, test scores, ranking brackets, and status chips.
- **Hierarchy Rules:** Section titles over tables and card grids use `title-lg` or `title-md` in bold/semibold weights to establish an unmistakable scan line before dense data displays.

## Layout & Spacing

The layout utilizes a structured 12-column fluid grid system paired with strict inner-component vertical rhythms:

- **Desktop (1280px+):** 12 columns, 24px (`1.5rem`) gutters, 32px (`2rem`) margins. Content area accommodates an 80px collapsed or 240px expanded navigation rail alongside multi-column dashboards.
- **Tablet (768px - 1279px):** 8 columns, 16px (`1rem`) gutters, 24px (`1.5rem`) margins. Sidebar transforms into an off-canvas drawer; multi-metric application dashboards reflow from 3 to 2 columns.
- **Mobile (< 768px):** 4 columns, 16px (`1rem`) gutters, 16px (`1rem`) margins. Grid tracks collapse to single-column lists; table views switch to stacked card structures.
- **Rhythm:** Layout blocks adhere to an 8px base grid, using `space-xs` (4px) and `space-sm` (8px) for internal pill/field alignment, up to `space-xl` (40px) for separating major dashboard stages.

## Elevation & Depth

Visual hierarchy uses crisp boundary lines paired with subtle ambient diffusion:

- **Level 0 (Flat/Base):** Page canvas rests at `#F8FAFC`. Background surfaces are non-elevated and anchor all structural grids.
- **Level 1 (Cards & Data Tables):** Surface `#FFFFFF` bordered by a 1px solid `#E2E8F0` stroke. Shadow: `0 1px 3px 0 rgba(15, 23, 42, 0.05), 0 1px 2px -1px rgba(15, 23, 42, 0.05)`.
- **Level 2 (Interactive Cards Hover & Popovers):** Elevated `#FFFFFF` surface with a 1px border. Shadow: `0 4px 6px -1px rgba(15, 23, 42, 0.07), 0 2px 4px -2px rgba(15, 23, 42, 0.05)`.
- **Level 3 (Modals, Overlays, Floating Action Bars):** Shadow: `0 20px 25px -5px rgba(15, 23, 42, 0.1), 0 8px 10px -6px rgba(15, 23, 42, 0.06)`.
- **Direct Apply Accentuation:** Cards eligible for Direct Apply employ an emerald ring halo on focus or hover: `0 0 0 1px #059669`.

## Shapes

The design system adopts **Rounded (`2`)** geometry, balancing structural predictability with modern softness:

- **Base Corner Radius (0.5rem / 8px):** Applied to form text fields, table containers, action buttons, and modal dialogs.
- **Large Radius (`rounded-lg` - 1rem / 16px):** University spotlight cards, roadmap journey containers, and summary stat blocks.
- **Full Radius (Pill / 9999px):** Status badges, roadmap step indicators, quick filters, and the universal global search bar.

## Components

### Buttons
- **Primary:** `#1D4ED8` background, `#FFFFFF` text, `rounded` (8px), font weight 600. Hover: `#1E40AF`.
- **Direct Apply Action:** `#059669` background, `#FFFFFF` text, `rounded` (8px), bold text with an integrated forward arrow icon. Hover: `#047857`.
- **Secondary / Outline:** `#FFFFFF` background, `#0F172A` text, 1px `#E2E8F0` border. Hover: `#F8FAFC` background with `#CBD5E1` border.
- **Destructive:** `#EF4444` background with `#FFFFFF` text.

### Badges & Status Pills
- **Done / Enrolled / Submitted:** `#ECFDF5` background, `#059669` text, full pill radius, `label-sm` font.
- **In Progress / Reviewing:** `#FFFBEB` background, `#D97706` text, full pill radius, `label-sm` font.
- **Not Started / Missing:** `#F1F5F9` background, `#475569` text, full pill radius, `label-sm` font.
- **Direct Apply Verified:** Pill with `#ECFDF5` background, `#059669` text, featuring an emerald lightning or spark icon.

### Universal Search Pill
- Centered or top-left in global headers. Height 44px, full pill radius (9999px), background `#FFFFFF`, border 1px solid `#E2E8F0`.
- Includes a leading search icon, placeholder text in `#94A3B8`, and an end-aligned keyboard shortcut tag (`⌘K` / `Ctrl+K`) in `#F1F5F9`.

### Form Inputs & Questionnaire Fields
- Input containers feature 1px `#E2E8F0` borders on `#FFFFFF` surfaces with 8px corner radii.
- Focus: 2px `#1D4ED8` outline ring with zero offset.
- Completed question card rows in LOR (Letter of Recommendation) forms show a subtle left vertical accent line (3px solid `#059669` when valid, `#D97706` when partial).

### High-Contrast Data Tables
- Header row: `#F8FAFC` background, `#475569` uppercase `label-xs` typography, 1px bottom border `#CBD5E1`.
- Rows: `#FFFFFF` surface alternating with clean row separators. Hover state triggers `#F8FAFC`. Padded cell layouts maintain compact vertical height (48px default).

### University & Program Cards
- Container: `#FFFFFF`, 16px radius, 1px `#E2E8F0` border, `elevation-1`.
- Includes institutional crest slot (48x48px), institution title, country flag, acceptance rate pill, dead-line countdown, and an anchored Direct Apply button badge.