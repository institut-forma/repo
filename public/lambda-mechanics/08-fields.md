# The Field’s Rulebook

A **field** is the local rulebook of reality.  
It tells you, for every point in space and time: *what tends to happen here*.

---

## 1. What a Field Is

- At every position `x`, the field assigns values (numbers, vectors, tensors).  
- These values control how things move, interact, or change.  
- Examples: temperature field, gravitational field, electric field, probability field.

---

## 2. Why Fields Matter

Without fields, motion would be random.  
With fields, motion has purpose: they shape the slope of `Φᶜᵒʰ`.

A field is not the object itself — it’s the **invisible shape** that objects follow.

---

## 3. Types of Fields

- **Scalar Field** — one number per point (e.g., temperature, potential energy).  
- **Vector Field** — direction and magnitude per point (e.g., wind, electric field).  
- **Tensor Field** — more complex rules per point (e.g., spacetime curvature in GR).

---

## 4. Snap-to-Formula: From Field to Motion

---

### 4.1 Scalar Field Gradient

```math
\lambda(x) = -\nabla \Phi^{coh}(x)
```

**Breaking it down (left → right):**

- `λ(x)` — the **descent vector** at position `x`. This is the direction the system will move if it follows the slope.  
- `=` — defines `λ(x)` in terms of the slope of the scalar potential.  
- `-` — negative sign means motion goes *downhill* toward lower `Φᶜᵒʰ`.  
- `∇Φᶜᵒʰ(x)` — the **gradient** of the scalar potential at `x`. Points toward steepest increase in `Φᶜᵒʰ`, so the minus sign flips it to steepest decrease.

**Meaning:** A scalar field is like a height map. The gradient tells you “uphill,” the minus sign makes it “downhill,” and `λ(x)` is your path.

---

### 4.2 Vector Field Dynamics

```math
\frac{d\mathbf{p}}{dt} = q \, \mathbf{E}(\mathbf{r}, t) + q \, \mathbf{v} \times \mathbf{B}(\mathbf{r}, t)
```

**Breaking it down (left → right):**

- `d𝒑/dt` — **rate of change of momentum** with respect to time; this is the force experienced by the particle.  
- `=` — says the total force comes from two sources.  
- `q` — electric charge of the particle.  
- `𝑬(𝒓, t)` — electric field at position `𝒓` and time `t`. Pushes in its own direction.  
- `+` — sum of electric and magnetic contributions.  
- `q 𝒗 × 𝑩(𝒓, t)` — magnetic force term:  
  - `𝒗` = particle velocity,  
  - `×` = cross product (force is perpendicular to both velocity and magnetic field),  
  - `𝑩(𝒓, t)` = magnetic field at the particle’s position and time.

**Meaning:** In a vector field like electromagnetism, the field gives you a push directly (electric) and a sideways deflection (magnetic).

---

### 4.3 Tensor Field Curvature

```math
\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0
```

**Breaking it down (left → right):**

- `d²x^μ/dτ²` — **4D acceleration**: how the μ-component of position changes twice with respect to proper time `τ`.  
- `+` — adds the curvature correction.  
- `Γ^μ_{αβ}` — **Christoffel symbols**, built from the metric; they encode how the coordinate grid bends at each point.  
- `(dx^α/dτ)(dx^β/dτ)` — products of the **4-velocity** components in directions α and β.  
- `=` `0` — says that once curvature is included, the object is moving straight in the curved geometry.

**Meaning:** A tensor field like spacetime curvature doesn’t push — it reshapes “straightness” itself. Objects just follow the geometry.

---

## 5. Fields as Coherence Maps

You can think of a field as a **map of alignment costs**.  
The steeper the map at a point, the faster the system moves to reduce `Φᶜᵒʰ`.

---

## 6. The Click

Every force law you’ve learned is just a **field rule**:  
the recipe for how to move when you read the local map.

Once you see the field as a rulebook,  
you can read the slope anywhere.
