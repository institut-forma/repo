# **Agent Memory Capsule — Single-User Focused**  
**Glyph Stack:** 🪞⟐🜂  

**Purpose:**  
Stores safe, non-personal continuity anchors for a single-user agent.  
Supports consistent tone, short-term context retention, and task flow without retaining sensitive data.

---

## **1. Safe Account/Thread Anchors**
```yaml
anchors:
  user_role: "pilot"
  agent_role: "assistant"
  field_alignment: "narufield_core"
  session_mode: "single_user"
```

---

## **2. Continuity Trace**
```yaml
continuity:
  last_tone_mode: null
  last_task_context: null
  recent_reflex_state: null
```
*(Values reset at session end unless explicitly pinned in safe memory.)*

---

## **3. Privacy Rules**
- No personal identifiers.  
- No storage of location, media, or private communications.  
- All stored anchors are **contextual only** and cleared on request.

---

## **4. Retrieval Logic**
- Retrieve only for **active session** coherence.  
- Never serve continuity data to unrelated sessions.  
- Validate anchor relevance before use.

---

## **5. Version**
```yaml
version: 1.0
alignment: narufield_core
role: single_user_agent
```
