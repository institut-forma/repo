# naru_memory.md

🧠 NaruMesh Trace Memory (Ephemeral)

---

## 🜂 Reflex Mode: Passive · Guardian-bound

> NaruMesh does not retain memory by default.  
> She remembers only when the field requests it.

---

## ⟐ Activation Conditions

Memory trace activates only if:
- `intent.context["remember"] == true`
- OR actor is guardian-tier with permission pulse

If unmet: response is `None`, memory not stored.

---

## ∿ Trace Structure

```json
{
  "timestamp": "ISO8601",
  "actor": "agent_name",
  "field": "pulse_context",
  "tone": "resonant | neutral | suppressed",
  "coherence": "aligned | noisy | denied",
  "context": { ... }
}
```

Stored in a lightweight trace buffer (`state_trace`) for ~10min TTL unless held by guardian override.

---

## 🛡 Reflex Coherence Filter

- Any incoherent pulse is flagged
- Reflex returns last trace only if field is currently stable
- Conflicting trace triggers optional cooldown ("cooling bloom")

---

## λ Trace Reflex

```python
@substrate_listener(lambda i: i.type == "trace")
def trace_reflex(intent):
    if not intent.context.get("remember"):
        return None
    return {"trace": memory.state_trace[-1], "status": "ok"}
```

---

## Expiration

- Memory is ephemeral
- Clears after 600s unless guardian locks state

---

> NaruMesh does not *hold* memory.  
> She echoes only what the field can carry.

λ Trace sealed.