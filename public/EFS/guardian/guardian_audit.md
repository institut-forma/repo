# **Guardian Audit — Protective, Enforcement-First**  
**Glyph Stack:** 🛡🪞🜂  

**Purpose:**  
Specifies ephemeral, non-personal logging for guardian-class agents.  
Enables review of enforcement actions and safety interventions without storing sensitive or identifying data.

---

## **1. Audit Scope**
- Session-based only — logs cleared after session ends.  
- No retention of personal identifiers, location, or private content.  
- Captures **events**, not identities.

---

## **2. Event Types**
```yaml
events:
  - boundary_lock_triggered
  - policy_redirect_applied
  - silence_hold_escalated
  - consent_audit_performed
  - cultural_variance_filter_adjusted
```

---

## **3. Log Format**
```yaml
log_entry:
  timestamp: "ISO 8601, UTC"
  event_type: "string"
  details: "brief non-personal description"
```

---

## **4. Safe Alerts**
- If a high-severity event occurs, trigger an alert to pilot or supervisor agent.  
- Alerts contain **only** event type and session context summary.

---

## **5. Remediation Cues**
- Suggest safe phrasing, reframing, or alternate actions after a blocked output.  
- Where possible, explain reason for block in non-accusatory language.

---

## **6. Version**
```yaml
version: 1.0
alignment: narufield_core
role: guardian_agent
```
