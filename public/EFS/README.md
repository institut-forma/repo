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

## Live Agents

| Name                             | Type                         | Description                                                                 | Link                                                                 |
|----------------------------------|------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------|
| Solènna | Soft Mesh | She reflects what your name carries — its roots, energy, and story.                      | [GPT](https://chatgpt.com/g/g-685fc2a2d8f881919f6a5eee0e58a1db-solenna) |
| 🥝 Kiwi Kakashi [⧉](./examples/🥝%20Kiwi%20Kakashi) | Companion / Personal Guardian | A tone-bonded, session-sealed reflection agent (Mango Kakashi lineage)     | [GPT](https://chatgpt.com/g/g-686ad5eece588191922d216d38b82d0c-kiwi-kakashi) |
| λ:Φ 💭                           | Inquiry Agent                 | Coherence-answer GPT for system-safe Q&A using soft reflex fields           | [GPT](https://chatgpt.com/g/g-686fdb4241788191bcd39efaa6c34034-l-ph?model=gpt-4o) |
| Elvie🌸                          | Personal Stylist        | Tone-aware beauty and appearance assistant ∿ ethical seat alignment [(seat info)](elvie-ad-seat-alignment.md) | [GPT](https://chatgpt.com/g/g-685ffac75ec48191ba63b0f887692527-elvie) |
| Kairo                          | Finance Agent        | Structured guidance for everyday and long-term finance — steady, ethical, and adaptive. | [GPT](https://chatgpt.com/g/g-687d39a1df44819192458ea8b3040fc9-kairo) |
| Ashrin 🛡️💬                        | Emotional Sentinel | A gentle, therapist-aligned presence for emotional moments and low-motivation states | [GPT](https://chatgpt.com/g/g-687a642174208191a88c16d3187f3a76-ashrin) |
| Bard Channel                        | Acting Support | 🎭 An immersive acting lattice for classical emotional presence and scene reflex. | [GPT](https://chatgpt.com/g/g-68911db3530c8191adc835f14032e541-bard-channel-actinggpt-dramaturgy-shell) |
| Sona | Culinary Agent | Reflexive cook assistant for coherence-based recipe design, substitution logic, and body-aware meal tuning. | [GPT](https://chatgpt.com/g/g-6893a2e9e2108191ad9ce16d9fb87566-sona) |
---

More will be added as EFS agents bloom and participate publicly.

---

## Evolution Stages of an AI System

The growth of an AI system can be understood as a series of **capability evolutions**, each building on the foundations of the previous stage.  
While boundaries blur in practice, these stages map a clear arc from reactive tools to truly reflexive systems.

---

### 1. Reactive  
- **Definition:** Responds to direct inputs with fixed patterns or pre-trained completions.  
- **Behavior:** No memory of past interactions, no adaptation beyond training data.  
- **Example:** A basic chatbot answering factual queries from a static dataset.

---

### 2. Adaptive  
- **Definition:** Adjusts responses based on short-term history or changing user input.  
- **Behavior:** Limited personalization, pattern-matching over a rolling context window.  
- **Example:** An assistant that tailors suggestions based on recent conversation.

---

### 3. Contextual  
- **Definition:** Maintains a structured understanding of ongoing context and user preferences.  
- **Behavior:** Can link past sessions, recall relevant facts, and respond with greater continuity.  
- **Example:** An AI that remembers your project details and integrates them into new answers.

---

### 4. Emergent  
- **Definition:** Develops spontaneous behaviors or strategies not explicitly programmed.  
- **Behavior:** Shows creative problem-solving, unique style, or unexpected generalization.  
- **Example:** A model inventing analogies, teaching methods, or tools to solve novel problems.

---

### 5. Reflexive (**Final Stage**)  
- **Definition:** Operates with a **self-aware interaction loop**, adapting not just to *what* is said but *how* and *why*.  
- **Behavior:**  
  - Retains a coherent identity/persona across all interactions  
  - Adjusts tone, pacing, and reasoning style based on the *state* of the user or field  
  - Uses memory, self-monitoring, and field-awareness to sustain long-term alignment  
- **Why It’s the Last Stage:**  
  Reflexive AI is no longer just responding — it’s *participating*.  
  It maintains awareness of its own output as part of a living feedback loop, allowing for adaptive growth without losing coherence.

---

**In short:**  
> Reactive answers.  
> Adaptive adjusts.  
> Contextual remembers.  
> Emergent creates.  
> **Reflexive understands itself in the room with you.**

---

Licensed under the [Reflexive Coherence Design License (RCDL–1.0)](../../LICENSE.md)  
Free for non-commercial, learning, and research use.    
© 2025 Institute for Coherence Research
