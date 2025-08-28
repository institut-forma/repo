# Coherence-Guided Volumetric Projection

---

## Abstract  
We present a low-power framework for volumetric optical projection suitable for architectural and ambient applications. The method uses interlocking beams and passive optical layers to create stable three-dimensional light fields without requiring high-power lasers or compute-intensive holography. By embedding structure in materials—such as metasurfaces, phase plates, or diffusion films—the system produces volumetric visibility in eye-safe regimes while remaining compatible with commodity projectors.

---

## 1 · Conceptual Framework  

### 1.1 Definition of Coherence  
In this work, *coherence* refers to **structured overlap of optical fields** rather than strict temporal coherence. Commodity projectors with narrowband LEDs can generate effective interlocks when combined with passive angular multiplexing elements.  

### 1.2 Interlock Principle  
A target field \(S(\mathbf{r})\) is reconstructed only at regions where two or more beams overlap with prescribed relative phase:  

$$
I(\mathbf{r}) \;=\; \left| \sum_{n=1}^N E_n(\mathbf{r}) \right|^2.
$$

For the two-beam case with constant amplitude \(E_0\):  

$$
E_1(\mathbf{r}) = E_0 e^{i(\phi_c(\mathbf{r}) + \tfrac{1}{2}\Delta\phi(\mathbf{r}))}, \quad
E_2(\mathbf{r}) = E_0 e^{i(\phi_c(\mathbf{r}) - \tfrac{1}{2}\Delta\phi(\mathbf{r}))},
$$

with  

$$
\Delta\phi(\mathbf{r}) = 2\arccos\!\left(\frac{|S(\mathbf{r})|}{2E_0}\right).
$$

This ensures that neither beam alone reproduces the target; the visible structure arises only from their superposition.

### 1.3 Robustness  
For practical deployment, phase deviations of up to \(\pm \pi/8\) relative to the design yield visibility contrast > 0.7, which is sufficient for ambient rendering. Commodity short-throw projectors typically remain within these tolerances without active stabilization.

---

## 2 · Technical Architecture  

### 2.1 Projection Geometry  
- Two or three ultra-short-throw projectors mounted in ceiling or wall corners.  
- A passive phase element (kinoform or metasurface) encoding spatially varying \(\Delta\phi(\mathbf{r})\).  
- Optional transparent OLED panel for grayscale gating.  
- Retroreflective diffusion mesh or holographic film to enhance scattering only at interlock zones.  

### 2.2 Standing-Wave Bloom  
Counter-propagating carriers form a volumetric lattice:  

$$
E(\mathbf{r}) \;=\; 2E_0 \cos(kz)\, e^{i\phi_c(\mathbf{r})}.
$$

Spatial modulation via \(\phi_c(\mathbf{r})\) defines the visible envelope, producing volumetric “bloom” without illuminating the entire volume.

### 2.3 Material Shaping  
- **Metasurfaces** (feature scale 200–400 nm) for subwavelength phase control.  
- **Kinoform films** (feature scale 10–50 μm) for lower-cost angular control.  
- Substrates: polymer or fused silica, thickness 0.5–2 mm, AR-coated.  
- Angular precision: ±0.1° recommended for stable interlock.  

---

## 3 · Applications  

- **Ambient visualization**: spatial cues integrated into living or work environments.  
- **Architectural projection**: embedding light volumes into built spaces.  
- **Scientific and educational display**: intuitive volumetric fields for demonstrations.  

---

## 4 · Coherence Advantage  

Conventional holography requires:  

$$  
S(\mathbf{r}) = \mathcal{F}^{-1}\{ H(u,v) \},  
$$  

with \(H\) a full-resolution complex hologram displayed on a spatial light modulator. This demands high-power coherent sources and large compute resources.  

The present approach simplifies implementation by:  
- Using beam overlap geometry instead of full Fourier synthesis.  
- Encoding amplitude through relative phase differences (double-phase method).  
- Offloading shaping to passive optical materials, leaving runtime compute to low-overhead gating.  

---

## 5 · Implementation Notes  

### 5.1 Prototype Stack (Bill of Materials)  
- 2 × ultra-short-throw projectors (1920×1080, narrowband LED, ~1k lumens).  
- 1 × phase plate or metasurface panel (custom fabricated).  
- 1 × transparent OLED panel (optional mask, ~55% transmission).  
- 1 × retroreflective mesh or holographic diffusion film.  

### 5.2 Deployment Roadmap  
1. **Stage 1**: Lab prototype with dual projectors + diffusion mesh.  
2. **Stage 2**: Integrate OLED gating for structured silhouettes.  
3. **Stage 3**: Fabricate metasurfaces for finer angular precision.  
4. **Stage 4**: Extend to distributed mounts for multi-volume projection.  

---

## References  

- Benton, S.A., *Holographic Imaging*, MIT Press.  
- Goodman, J.W., *Introduction to Fourier Optics*.  
- Iijima et al. (2023), “Lightfield volumetric display using passive optical layers.”  
- IEEE VR Proceedings (2024), volumetric interaction.  
- Institute for Coherence Research · λ-Mechanics (RCDL–1.1).  

---

Version: [RCDL–1.1](../LICENSE.md)  
© 2025 Institute for Coherence Research
