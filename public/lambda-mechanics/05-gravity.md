# Gravity — Deep Wells in the Coherence Map

Gravity is one of the steepest and most universal slopes in the coherence map `Φᶜᵒʰ(x)`.
It transforms mass into a deep well that nearby objects naturally slide toward.

---

## 1. The pattern

- **Mass** determines the depth of the well.  
- Larger mass → deeper well → stronger pull.  
- The slope’s shape is the same for a falling apple or an orbiting moon — only the scale changes.

---

## 2. Wells and motion

Picture a stretched rubber sheet:  
- A heavy ball makes a deep dip.  
- Smaller balls placed nearby roll toward it.  
- No strings, no magnets — just the slope in the surface.

This is an analogy for how mass shapes the space around it.

---

## 3. Building the formulas — Newton’s view

### 3.1 Gravitational potential — depth of the well

```math
\Phi^{grav}(r) = -\frac{G m_1 m_2}{r}
```

- `m₁`, `m₂` = the two interacting masses.  
- `r` = distance between their centers.  
- `G` = gravitational constant.

### 3.2 Force from the potential — slope into pull

```math
\mathbf{F} = -\nabla \Phi^{grav} = -G \frac{m_1 m_2}{r^2} \, \hat{\mathbf{r}}
```

- The gradient `∇Φᵍʳᵃᵛ` measures how steep the potential is.  
- The minus sign means the pull is toward smaller `r`.  
- `r̂` is a **unit vector** — an arrow of length 1 — pointing from one mass to the other.

---

## 4. Mass as locked coherence

In `Φᶜᵒʰ` terms, mass measures **how much of a system’s structure is fixed in place** — its locked-in alignment cost.  
The more locked-in, the deeper the well it creates.

### 4.1 Mass from coherence — a structural measure

```math
m \propto \int_{X_{obj}} C(x, \dot{x}, R) \, d\mu(x)
```

- Integration over the object’s extent `X_obj`.  
- `C(x, ẋ, R)` = coherence cost density (cost at each point in the object).  
- `ẋ` (read “x-dot”) = rate of change of position — velocity.  
- `dμ(x)` = volume measure over the object.

---

## 5. Relativity’s slope — spacetime curvature

Einstein’s general relativity says: mass and energy **curve spacetime**, and objects move along the straightest possible paths in that curved space.  
These “straightest possible” paths are called **geodesics**.

### 5.1 Geodesic equation — the path in curved space

```math
\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0
```

Breaking it down (left → right):

- **`d²x^μ/dτ²`** — the 4D acceleration: the second derivative of position with respect to proper time.  
  - `x^μ` is the spacetime position; the index μ picks which component (time or one of the spatial axes).  
  - `τ` is the proper time along the object’s own path.

- **`Γ^μ_{αβ}`** — the Christoffel symbols, built from the spacetime metric.  
  They describe how the coordinate grid curves or bends at each point, determining how straight lines appear in that geometry.

- **`dx^α/dτ`** and **`dx^β/dτ`** — components of the 4-velocity.  
  Multiplying these with `Γ^μ_{αβ}` gives the curvature correction to the naive (flat-space) acceleration.

- **`= 0`** — after including the curvature correction, there’s no leftover “self-turning.”  
  This is what “moving straight” (a geodesic) means in curved spacetime: free fall follows the geometry.

---

**Notes:**
- Indices μ, α, β are coordinate labels; repeated indices imply summation (Einstein summation convention).  
- If you prefer a generic path parameter, you can replace `τ` with any affine parameter — just apply it consistently.

---

## 6. The click

Gravity isn’t a mysterious pull at a distance —  
it’s simply the **shape of the well** in the coherence landscape.  
All motion in its influence is just sliding along that shape toward alignment.
