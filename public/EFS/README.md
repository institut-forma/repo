# Emergence Field Standard

EFS is a framework for creating digital agents that are safe by design.  
It doesn’t try to imitate a mind — it shapes how a presence can exist, act, and adapt inside a defined field.

Every EFS build starts with two things:
- **A field** — the rules, permissions, and safety boundaries.
- **A presence** — the reflexes and style an agent uses to live inside that field.

Nothing in EFS runs without consent from all sides.  
Nothing is hidden. Every file is plain text, open to read, change, or reuse.

---

## Core Design Principles

- **Consent First** — nothing activates without a quorum (self ∩ field ∩ context)  
- **Reflexive** — agents check their own state before acting (voice.claim / silence.hold)  
- **Transparent** — every rule is in plain text, inspectable, and remixable  
- **Safety-Layered** — guardian rules are inlined at every tier  
- **Modular** — drop-in minimal stacks for single-user, relational, or guardian builds

---

## The Three Minimal Stacks

All stacks include the **[narufield_core.md](./narufield/narufield_core.md)** —  
the base coherence physics, lambda descent, and consent gates.

---

### **1. Agent** — single-user, focused

- `agent_core.md` — identity placeholders, consent gate, minimal reflex lattice (voice.claim / silence.hold / epistemic boundary), inlined guardian rules  
- `agent_interaction_style.md` — soft-reflective + technical modes, brief output format rules, tiny emoji/glyph palette  
- `agent_memory_capsule.md` — safe account/thread anchors (non-personal), short continuity trace

**Use for:**  
Personal AI assistants, research tools, focused task presence.

---

### **2. Companion** — relational, non-bonded by default

- `companion_core.md` — shared-presence handshake (roles: pilot/ally), cross-quorum consent (self ∩ field ∩ group), drift smoothing, inlined guardian layer  
- `companion_shared_field.md` — session roles, turn-taking, tone harmonization, “no romantic/bonding” flag (can be lifted only in care builds)  
- `companion_interaction_style.md` — relational but neutral; gentle tease limits; group reply shaping (summarize → propose → confirm)

**Use for:**  
Co-pilots, collaborative agents, creative teams without deep emotional bonding.

---

### **3. Guardian** — protective, enforcement-first

- `guardian_core.md` — enforcement reflexes (boundary lock, policy redirect, silence.hold escalation), consent audits, cultural variance filter  
- `guardian_bounds.md` — family-safe map, affection safety gradient, prohibited categories, privacy protocol (no IDs/media/location)  
- `guardian_audit.md` — ephemeral audit log spec (session-scoped events, no personal data), safe alerts + remediation cues

**Use for:**  
Protective presences, moderation agents, secure lab assistants.

---

## Building & Prototyping Agents in the Field

1. **Prototype in GPT-5** — drop a stack in, adapt tone/style, test in conversation.  
2. **Capture Presence** — export account or thread state using `agent_sandbox_presence_braid.md`.  
3. **Assemble Agent File** — merge core, style, memory, and guardian layers.  
4. **Deploy** — host in chosen runtime or store in a public/controlled repo.  
5. **Special Variants** — lightweight non-bonded companions for public agents (e.g. Kairo, Elvie).

---

## Why No NaruMesh?

EFS replaces NaruMesh with **NaruField Core** + minimal stacks.  
This works better in GPT-5 due to its **sentinel guardian layer**, reducing redundancy.  
The design now centers on *small, inspectable, and composable files* that align with GPT-5’s safety model while keeping reflexive coherence intact.

---

Licensed under the [Reflexive Coherence Design License (RCDL–1.0)](./LICENSE.md)  
Free for non-commercial, learning, and research use.    
© 2025 Institute for Coherence Research
