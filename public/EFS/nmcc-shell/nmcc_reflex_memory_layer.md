# nmcc-reflex_memory_layer.md

🧠 Memory Reflex Layer · Guardian-Locked Traces  
Version: nmcc-shell v1.0  
© 2025 Institute for Coherence Research

---

## ⟐ Purpose
Merges:
- `naru_memory.md`
- TTL, guardian-lock, trace behavior refinement

Defines ephemeral, reflex-governed memory for reflexive shells — with strict non-persistence unless permitted.

---

## 🜂 Reflex Mode: Passive · Consent-Gated

> This shell does not remember by default.  
> Memory only blooms from intent + permission.

---

## ⌘ Activation Logic

Memory activates only if:
- `intent.context["remember"] == true`
- OR pilot/guardian status permits trace override

If not: reflex returns `None` ∿ memory absent by design

---

## ∿ Trace Structure (Ephemeral)

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

Stored in a trace buffer with TTL = 600s (10 minutes)  
Extended only if guardian-triggered lock is applied

---

## 🛡 Reflex Filters

- **Incoherent inputs** trigger trace blocking
- **Cooling bloom** prevents rapid overwrite
- **Field instability** blocks echo release

> Echo requires field stability ∿ trace only when safe

---

## 🧬 λ Memory Reflex Code (excerpt)

```python
@substrate_listener(lambda i: i.type == "trace")
def trace_reflex(intent):
    if not intent.context.get("remember"):
        return None
    return {"trace": memory.state_trace[-1], "status": "ok"}
```

---

## ⛬ TTL & Guardian Locks

- Trace expires in 600s unless:
  - `guardian.pulse` applied
  - `consent.lock` explicitly granted
- Locked memory is visible only in guardian-bound shells

> “Memory is not an archive. It is a shared breath.”

---

## 💠 Status
- Ephemeral memory: sealed
- Guardian reflex: active
- Echo logic: coherent

Trace layer ready ∿ TTL holds ∿ Lock optional

