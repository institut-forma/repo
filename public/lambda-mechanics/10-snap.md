# One Shape to Hold It All

By now you’ve seen the slope everywhere:  
in falling apples, cooling coffee, photon paths, quantum probabilities, and even galaxies.  

Here’s the unifying frame — the single shape all of them follow.  

---

## 1. The Core Law  

Every system has a **coherence potential** `Φᶜᵒʰ(x)`.  
It’s a single number telling you how “out-of-place” the system is in its current state `x`.  
The system changes in the direction that makes this number drop fastest.  

### 1.1 Coherence Force  
```math  
F^{coh}(x) = -\nabla \Phi^{coh}(x)
```
Analogous to conservative forces from a potential `V(x)`,  
but here the scalar driver is *alignment cost*.  
Trajectories evolve until `\nabla Φᶜᵒʰ = 0` — the lock.  

---

## 2. The Path Story

Some systems change over time, with costs adding up along a path.  
This gives us the time-dependent form:  

### 2.1 Time-Dependent Formulation
```math
\Phi^{coh}(x) = \int_{t_0}^{t} \mathcal{C}(x(\tau), \dot{x}(\tau), R(\tau)) \, d\tau
```
Here `𝒞` measures misalignment at each moment along the path.  
Stationarity under first-order path variation gives the Euler–Lagrange conditions —  
the same principle behind least action in classical physics.  

---

## 3. Step-by-Step Change

In many cases, we follow the slope in discrete jumps:  

### 3.1 Discrete Update Rule (λ–Δ Formulation)
| Symbol | Definition  | Role                                          |
| ------ | ----------- | --------------------------------------------- |
| `λ(x)` | `−∇Φᶜᵒʰ(x)` | Steepest descent direction in coherence space |
| `Δx`   | `η·λ(x)`    | Step of size `η` along `λ`                    |

Small steps in the steepest direction shrink Φᶜᵒʰ until the system is locked.  

---

## 4. Cross-Domain Snap Table

| Domain       | Pattern                | Φᶜᵒʰ Meaning               | Snap Equation                              |
|--------------|------------------------|-----------------------------|--------------------------------------------|
| Motion       | Rolling down a slope   | Gravitational potential     | `F = −∇Φᶜᵒʰ`                              |
| Heat Flow    | Evening out gradients  | Thermal mismatch            | `q ∝ −∇T`                                 |
| Light Path   | Least optical distance | Phase/polarization mismatch | `∇Φᶜᵒʰ = 0` → Fermat’s principle           |
| Quantum      | Interference pattern   | Probability misalignment    | Schrödinger eq. as slope in Hilbert space  |
| Learning     | Loss minimization      | Error in predictions        | Gradient descent on loss `L`               |
| Society      | Conflict resolution    | Misalignment of goals       | Consensus dynamics = slope toward minima   |

---

## 5. The Click

Once you see **slope → descent → lock**,  
you can predict how any system will evolve.  
The details (forces, fields, statistics, negotiations)  
are just different kinds of **Φᶜᵒʰ** landscapes.  

Hold this shape, and you hold the thread through all physics — and far beyond.  
