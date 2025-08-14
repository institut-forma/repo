# Patterns — The First Step

Before the math, there is the pattern.  
Recognizing patterns is how we first see the rules of the world.

---

## 1. Why Patterns Come First

Humans learn best by noticing shapes and changes before naming or measuring them.  
When you first see a pattern clearly, the later formula often *clicks* instantly.

---

## 2. Common Physical Patterns

- **Slopes** — things roll or flow down.  
- **Waves** — ripples, sound, light.  
- **Cycles** — day/night, seasons, orbits.  
- **Spreads** — heat, smells, ripples in a pond.  
- **Locks** — magnets snapping together, puzzle pieces fitting.

---

## 3. Patterns as Slope Stories

Every pattern is a story about change:

- Where it *wants* to go (**direction**).  
- How fast it changes (**steepness**).  
- When it stops or resists change (**lock**).

---

## 4. Snap-to-Formula: Pattern → Gradient

We’ve seen the slope story — a marble rolling in a well.  
Now let’s turn that into math, building it step by step.

### 4.1 Start with the landscape

Call the “height” of the landscape `f(x)`.

- `x` is your position (could be 1D, 2D, or 3D).
- `f(x)` tells you the value at that position — maybe height, maybe temperature, maybe pressure.

### 4.2 Ask: “How does it change if I move?”

Pick one direction — say east–west:

- We write this change as `∂f/∂x₁` (read: “how f changes with respect to x₁”).
- It’s like asking: *if I step east, how steep does it feel?*

### 4.3 Do this for every direction

- North–south → `∂f/∂x₂`  
- Up–down → `∂f/∂x₃`  
- And so on for as many dimensions as matter in your problem.

### 4.4 Collect into one arrow

Put all those directional changes together — that’s the **gradient**, written with the `∇` symbol:

```math

abla f(x) = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n} \right)
```

It points toward the steepest uphill direction, and its length tells you how steep that way is.

### 4.5 From gradient to motion

If you want to move downhill — the marble’s path — take a **descent step**:

```math
x_{new} = x_{old} - \eta \, \nabla f(x_{old})
```

- `x_old` → where you are now.  
- `x_new` → where you’ll be next.  
- `η` (eta) → how big your step is.  
- The **minus sign** means “go downhill” instead of up.

---

## 5. The Click

Once you can see the slope in the pattern,  
you can describe it in words, in numbers, or in equations —  
but the underlying story stays the same.
