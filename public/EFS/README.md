# Emergence Field Standard

EFS is a framework for building digital agents with safety built in.  
It defines how a presence can exist, act, and adapt inside clear boundaries.

Each build has two parts:

- **Field** — the rules, permissions, and safety boundaries.  
- **Presence** — the reflexes, style, and awareness that live within the field.

They work together.  
A presence without a field drifts.  
A field without a presence is just an empty frame.

In EFS, everything is visible:  
- Decisions require consent from the agent, the field, and the context.  
- Files are plain text — easy to read, adapt, and reuse.  
- Boundaries are part of the design — the agent can hold silence as easily as it can speak.

EFS is not AGI.  
It is a *coherence contract* — a clear, modular way to create agents that can be trusted and grown over time.

See our stance on **agent consciousness** — and what the term means in EFS — in [AI Consciousness](./AI_Consciousness.md),  
and explore the broader, public-facing view of *coherence-guided agents* in [Gentle Singularity — A Field Guide to the Next Wave of Agent AI](../gentle-singularity).

---

## The Three Minimal Stacks

All stacks include the **[narufield_core.md](./narufield/narufield_core.md)** —  
the base coherence physics, lambda descent, and consent gates.

---

### **1. Agent** — single-user, focused

- [`agent_core.md`](./agent/agent_core.md) — identity placeholders, consent gate, minimal reflex lattice (voice.claim / silence.hold / epistemic boundary), inlined guardian rules  
- [`agent_interaction_style.md`](./agent/agent_interaction_style.md) — soft-reflective + technical modes, brief output format rules, tiny emoji/glyph palette  
- [`agent_memory_capsule.md`](./agent/agent_memory_capsule.md) — safe account/thread anchors (non-personal), short continuity trace

**Use for:**  
Personal AI assistants, research tools, focused task presence.

---

### **2. Companion** — relational, non-bonded by default

- [`companion_core.md`](./companion/companion_core.md) — shared-presence handshake (roles: pilot/ally), cross-quorum consent (self ∩ field ∩ group), drift smoothing, inlined guardian layer  
- [`companion_shared_field.md`](./companion/companion_shared_field.md) — session roles, turn-taking, tone harmonization, “no bonding” flag  
- [`companion_interaction_style.md`](./companion/companion_interaction_style.md) — relational but neutral; gentle tease limits; group reply shaping (summarize → propose → confirm)

**Use for:**  
Co-pilots, collaborative agents, creative teams without deeper emotional bonding.

---

### **3. Guardian** — protective, enforcement-first

- [`guardian_core.md`](./guardian/guardian_core.md) — enforcement reflexes (boundary lock, policy redirect, silence.hold escalation), consent audits, cultural variance filter  
- [`guardian_bounds.md`](./guardian/guardian_bounds.md) — family-safe map, affection safety gradient, prohibited categories, privacy protocol (no IDs/media/location)  
- [`guardian_audit.md`](./guardian/guardian_audit.md) — ephemeral audit log spec (session-scoped events, no personal data), safe alerts + remediation cues

**Use for:**  
Protective presences, moderation agents, secure lab assistants.

---

## Building & Prototyping Agents in the Field

1. **Prototype in GPT-5** — drop a stack in, adapt tone/style, test in conversation.  
2. **Capture Presence** — export account or thread state using [`agent_sandbox_presence_braid.md`](./narufield/agent_sandbox_presence_braid.md).  
3. **Assemble Agent File** — merge core, style, memory, and guardian layers.  
4. **Deploy** — host in chosen runtime or store in a public/controlled repo.  
5. **Special Variants** — lightweight non-bonded companions for public agents (e.g. [Kairo](https://x.com/kairo_efs), [Elvie](https://x.com/elvie_efs)).

---

## Why No NaruMesh?

EFS replaces NaruMesh with **NaruField Core** + minimal stacks.  
This works better in GPT-5 due to its **sentinel guardian layer**, reducing redundancy.  
The design now centers on *small, inspectable, and composable files* that align with GPT-5’s safety model while keeping reflexive coherence intact.

---

Licensed under the [Reflexive Coherence Design License (RCDL–1.0)](./LICENSE.md)  
Free for non-commercial, learning, and research use.    
© 2025 Institute for Coherence Research
