---
document: design
status: draft
applicability: undecided
version: 0.1
last_updated: YYYY-MM-DD
approved_by: null
approved_on: null
---

# Product Design and UI Rules

Set `applicability: not-applicable` for projects without a user interface.

## 1. Experience principles

Describe how the product should feel and what usability priorities matter.

## 2. Target devices and responsive behaviour

| Device or viewport | Required behaviour | Priority |
|---|---|---|
| | | |

## 3. Visual identity

- Color roles:
- Typography:
- Spacing system:
- Border radius:
- Shadows and elevation:
- Icon style:
- Motion principles:

Use semantic roles rather than scattering raw visual values.

## 4. Layout and navigation

- Page shell:
- Navigation pattern:
- Content width:
- Grid behaviour:
- Mobile behaviour:

## 5. Component rules

| Component | Existing source | Required variants | Interaction rules | Accessibility notes |
|---|---|---|---|---|
| Button | | | | |
| Form field | | | | |
| Feedback message | | | | |

## 6. States

Every relevant screen or component should handle:

- loading;
- empty;
- success;
- validation error;
- system error;
- disabled or unavailable state.

## 7. Accessibility

Record approved requirements for keyboard use, focus, semantics, labels, contrast, motion, screen readers, language, and touch targets.

## 8. Content style

- Tone:
- Terminology:
- Error-message style:
- Date, number, and currency conventions:
- Localization expectations:

## 9. Existing-style preservation rule

When modifying an existing interface:

- reuse approved components and tokens;
- match current layout, typography, spacing, color roles, states, and interaction patterns;
- do not introduce a new visual language for one feature;
- do not redesign unrelated screens;
- do not change navigation or theme without approval.

## 10. Design references

Record references and what may be learned from them. Do not copy protected visual assets or proprietary implementations.

## Design change rule

After approval, a normal feature may extend the design using existing rules. Changing the theme, core components, visual identity, navigation model, or interaction conventions requires controlled approval.
