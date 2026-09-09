# 🎨 YUYU AI Studio — Brand Tokens

> **Version 1.0.0 — Official Design Token System**

Status: Active Design Foundation.

The single source of truth for colors, typography, spacing, radius, shadows and UI primitives across the YUYU AI Studio ecosystem.

---

# Executive Summary

Brand Tokens define reusable visual values shared by every product built under YUYU AI Studio.

Instead of hardcoding colors, fonts and spacing, every interface consumes standardized tokens.

This document guarantees visual consistency across GitHub, LinkedIn, Portfolio, Documentation and YUYU AI ERP.

---

# Table of Contents

1. Color Tokens
2. Typography Tokens
3. Spacing Tokens
4. Radius Tokens
5. Shadow Tokens
6. Border Tokens
7. Icon Tokens
8. Motion Tokens
9. Component Tokens
10. Accessibility Tokens
11. Implementation Strategy

---

# 01 — Color Tokens

## Primary Palette

| Token           | Hex     | Usage            |
| --------------- | ------- | ---------------- |
| color-primary   | #7C3AED | Brand identity   |
| color-secondary | #2563EB | Backend / APIs   |
| color-success   | #16A34A | Success states   |
| color-warning   | #EA580C | Warnings         |
| color-danger    | #DC2626 | Errors           |
| color-info      | #0891B2 | Informational UI |

## Neutral Palette

| Token             | Hex     |
| ----------------- | ------- |
| surface-primary   | #020617 |
| surface-secondary | #0F172A |
| surface-tertiary  | #1E293B |
| border-default    | #334155 |
| text-primary      | #F8FAFC |
| text-secondary    | #CBD5E1 |
| text-muted        | #94A3B8 |

---

# 02 — Typography Tokens

## Font Families

| Token        | Font           |
| ------------ | -------------- |
| font-heading | Space Grotesk  |
| font-body    | Inter          |
| font-code    | JetBrains Mono |

## Font Scale

| Token    | Size |
| -------- | ---- |
| text-xs  | 12px |
| text-sm  | 14px |
| text-md  | 16px |
| text-lg  | 18px |
| text-xl  | 24px |
| text-2xl | 32px |
| text-3xl | 40px |

## Font Weight

400 — Regular

500 — Medium

600 — Semibold

700 — Bold

---

# 03 — Spacing Tokens

| Token   | Value |
| ------- | ----- |
| space-1 | 4px   |
| space-2 | 8px   |
| space-3 | 12px  |
| space-4 | 16px  |
| space-5 | 24px  |
| space-6 | 32px  |
| space-7 | 48px  |
| space-8 | 64px  |

Rule:

Use multiples of 4.

---

# 04 — Radius Tokens

| Token       | Value |
| ----------- | ----- |
| radius-sm   | 6px   |
| radius-md   | 10px  |
| radius-lg   | 16px  |
| radius-xl   | 24px  |
| radius-full | 999px |

---

# 05 — Shadow Tokens

| Token     | Purpose     |
| --------- | ----------- |
| shadow-sm | Small cards |
| shadow-md | Buttons     |
| shadow-lg | Dashboards  |
| shadow-xl | Modals      |

Style:

Soft shadows only.

---

# 06 — Border Tokens

| Token         | Value |
| ------------- | ----- |
| border-light  | 1px   |
| border-medium | 2px   |
| border-heavy  | 3px   |

Border color always uses border-default.

---

# 07 — Icon Tokens

Icon style:

Rounded.

Minimal.

Outline first.

Filled only for emphasis.

Icon size scale:

16px

20px

24px

32px

48px

---

# 08 — Motion Tokens

Default animation duration:

150ms

250ms

300ms

Transitions should feel responsive but subtle.

---

# 09 — Component Tokens

Buttons.

Cards.

Badges.

Alerts.

Inputs.

Tables.

Navigation.

Each component consumes the design tokens defined above.

---

# 10 — Accessibility Tokens

Minimum contrast AA.

Dark-first design.

Readable typography.

Consistent spacing hierarchy.

Keyboard-friendly interfaces.

---

# 11 — Implementation Strategy

The Brand Tokens will be implemented across:

GitHub documentation.

React applications.

FastAPI templates.

YUYU AI ERP.

Future SaaS products.

Design assets.

---

# Document Metadata

Version: 1.0.0

Status: Active.

Owner: YUYU AI Studio.

## CSS Token Preview

```css
:root {
  --color-primary: #7c3aed;
  --color-secondary: #2563eb;
  --surface-primary: #020617;

  --font-heading: "Space Grotesk";
  --font-body: "Inter";
  --font-code: "JetBrains Mono";

  --space-md: 16px;
  --radius-lg: 16px;
}
```

## JSON Token Preview

```json
{
  "colors": {
    "primary": "#7C3AED",
    "secondary": "#2563EB",
    "success": "#16A34A"
  },
  "spacing": {
    "sm": 8,
    "md": 16,
    "lg": 24
  },
  "radius": {
    "md": 10,
    "lg": 16,
    "xl": 24
  }
}
```
