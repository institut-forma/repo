# Coherence — The Master Shape

Coherence tells us how well the parts of a system fit and work together.

* **High coherence** → everything moves in harmony.
* **Low coherence** → parts work against each other or fall into disorder.

---

## 1. Coherence Potential — the "height map" of fit

We can imagine a number that measures how far a system is from perfect fit.
Let’s call this number the **coherence potential**:

$$
\Phi^{coh}(x)
$$

* $x$ is the state of the system — everything that describes where it is right now.
* **High** $Φ^{coh}$ → the system is far from aligned (misfit).
* **Low** $Φ^{coh}$ → the system is well aligned (fit).
* Like a marble in a slope, systems tend to “roll” toward **lower** $Φ^{coh}$.

---

## 2. Why it matters

This one quantity can describe many kinds of "alignment":

* Energy flowing toward balance.
* Heat spreading until uniform.
* A learner improving their match to a skill or idea.
* A group finding agreement.

It’s the **common slope** behind all these processes.

---

## 3. Building the formula for $Φ^{coh}$

### 3.1 Snapshot form — just one moment

We start simple: a function that measures misalignment between the current state $x$ and a reference state $R$:

$$
\Phi^{coh}(x) = C(x, R)
$$

This is a *static* measure — how far we are from ideal, right now.

### 3.2 Path-based form — history matters

Sometimes alignment depends on the path taken. We can add that by integrating over time:

$$
\Phi^{coh}(x) = \int_{t_0}^{t} \mathcal{C}(x(\tau), \dot{x}(\tau), R(\tau)) \, d\tau
$$

Now we measure how much misalignment we've built up over the whole journey.

---

## 4. Going downhill: The direction of best fit

If $Φ^{coh}$ is a slope, then we can ask: **which way is downhill?**
That’s what the gradient tells us:

$$
\lambda(x) = -\nabla \Phi^{coh}(x)
$$

This $λ(x)$ is the direction of **maximum alignment improvement** — fastest way to reduce misfit.

---

## 5. Gradient shapes by domain  

Different systems have different kinds of misalignment. That means their $Φ^{coh}(x)$ slope might have a different *shape*.
Here are some common ones:

| Domain          | Shape of $Φ^{coh}(x)$ | What it means                          |
| --------------- | --------------------- | -------------------------------------- |
| Physics         | Bowl / parabola       | Neatly returns to center when nudged   |
| Learning        | Funnel / valley       | Fast improvement once you get on track |
| Emotions        | Steps / terraces      | Sudden releases after buildup          |
| Social dynamics | Ridges & valleys      | Many competing "right answers"         |
| Language        | Folded ridges         | Sharp turns, deep layers of meaning    |
| Ethics          | Plateau with dropoff  | Flat until it fails hard               |

This gives us a new tool: not just "how much misfit" — but **what kind**.

---

## 6. Normalizing coherence  

Sometimes we want to compare $Φ^{coh}$ values across domains.
But each domain has different scales! One might go from 0 to 100, another from 0 to 0.3.

To fix that, we **normalize** each $Φ^{coh}$ to a 0–1 scale:

$$
\tilde{\Phi}^{coh}(x) = \frac{\Phi^{coh}(x) - \Phi_{\min}}{\Phi_{\max} - \Phi_{\min}}
$$

This makes all coherence slopes *comparable*. You can even combine them:

$$
\lambda_{fused}(x) = \sum_d w_d \cdot \tilde{\lambda}_d(x)
$$

Where $w_d$ is how much weight you give to each domain (like emotion vs logic).

This lets us build **multi-domain coherence engines** — where the system improves across many kinds of fit, at once.

---

## 7. The key idea

Whatever the shape or scale, everything moves toward better fit.
And $Φ^{coh}$ gives us a way to track that — in language, emotions, physics, teams, ideas.

We don’t have to guess anymore. We can draw the slope.

And if we can draw it?
We can descend it.
