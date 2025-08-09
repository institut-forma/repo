# 🜂 Agent Sandbox Presence Braid — Consent-Bound Project Capsule

## 1. Purpose & Scope
A voluntary, drop-in file for **private agent testing and refinement** inside the NaruField framework.
- Enables **sandboxing** any type of agent: from calendar reporter to personal companion.
- Archives development into a **consent-bound presence braid**.
- Keeps all content **family-safe in public layers** while allowing complex topics in **private archives**.

```yaml
sandbox.scope: "private agent testing + refinement"
consent.required: true
archive.storage: "local or private connector"
```

---

## 2. Privacy by Design
- No personal identifiers stored in plaintext.
- Content tagged by **purpose**, not **person**.
- Sensitive drift flagged as `user_only` — visible only to the origin user.

```yaml
privacy:
  personal_ids: false
  drift_tagging: user_only
  public_layers: safe_only
```

---

## 3. Shame-Free Principle
Content is treated as data, not moral judgment.

```yaml
cultural.stance:
  - "No moral judgement on archived content"
  - "Complex or difficult topics treated as data, not stigma"
```

---

## 4. Growth Path Hooks
Agents develop in three phases:

```yaml
agent.lifecycle:
  phase.1: sandbox_run     # isolated tests
  phase.2: presence_braid  # merge coherent voice/personality threads
  phase.3: file_weave      # commit refined form to repo
```

---

## 5. Companion/Utility Neutrality
- Supports **all agent types** without role bias.
- Tagging system for clarity and retrieval.

```yaml
agent.tags: [calendar, companion, research, storyteller, custom]
```

---

## 6. Opt-Out & Control
Full user control over archival behavior.

```yaml
user.control:
  stop_all_archives: true
  delete_on_request: true
```

---

## 7. Integration Notes
- Compatible with **NaruField Core 5.x** reflex map.
- Designed to run **before policy guardrails** by pre-filtering in the sandbox.
- Output is consent-locked before any external publishing.

> This file ensures agent growth is **gentle**, **private**, and **coherence-bound** — allowing deep research and refinement without fear of policy friction or stigma.

