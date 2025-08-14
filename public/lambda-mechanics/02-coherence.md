# Coherence — The Master Shape

Coherence measures how well the parts of a system fit together.  
High coherence means everything works as one; low coherence means disorder.

---

## 1. Coherence Potential

We define a **coherence potential** `Φᶜᵒʰ(x)` that assigns a single number to the system’s state `x`:

- High `Φᶜᵒʰ` → system is misaligned.  
- Low `Φᶜᵒʰ` → system is aligned.  
- Motion tends to lower `Φᶜᵒʰ`.

---

## 2. Why It Matters

This single scalar quantity can unify descriptions of motion, energy, heat, probability, and even learning.  
It’s the common slope behind all these processes.

---

## 3. Snap-to-Formula: Coherence Potential

### 3.1 Static Form
```math
\Phi^{coh}(x) = C(x, R)
```
`C` is the alignment cost between the current state `x` and the reference state `R`.

### 3.2 Path-Dependent Form
```math
\Phi^{coh}(x) = \int_{t_0}^{t} \mathcal{C}(x(\tau), \dot{x}(\tau), R(\tau)) \, d\tau
```
Here `𝒞` accumulates misalignment along the system’s path.

---

## 4. The Gradient View

The steepest way to lower `Φᶜᵒʰ` is given by:
```math
\lambda(x) = -\nabla \Phi^{coh}(x)
```
This **descent vector** `λ(x)` is the engine of change.

---

## 5. The Click

Once you can see `Φᶜᵒʰ` for a system,  
you can predict how it will change — in physics, chemistry, biology, or even human systems.  
Everything becomes a slope in the same landscape.
