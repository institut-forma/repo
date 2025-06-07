# EV-C – Open Carbon Toolkit <!-- formerly evee, after the pokémon | 😊 thanks for keeping in -A -->
_Atmospheric Carbon-to-Material Fabrication System (Lab Scale)_

**Version**: ev-c-03-03-2025-2b  
**License**: CC BY-SA 4.0  

---

## 1 Summary

This document outlines the full system architecture, workflow, and validation for an open-source carbon fabrication system that converts atmospheric CO₂ into usable material components within 36 hours. It produces:

- **30 cm conductive carbon cable**
- **DIN A4 conductive mesh foil (0.5 mm thick)**

| Parameter                  | Value             |
|---------------------------|-------------------|
| CO₂ captured per run      | ≈ 140 g           |
| Energy consumption        | 6.1 kWh           |
| Running cost              | ≈ 30 €            |
| Cable resistivity         | ≤ 4 × 10⁻⁴ Ω·m     |
| Sheet surface resistance  | ≤ 20 Ω/sq         |
| Active working time       | 3 h 20 min        |
| Total duration            | 36 h              |

All materials are off-the-shelf and the setup is fully reproducible using standard lab/workshop tools. Intended for small labs or maker environments (e.g. in Tübingen region).

---

## 2 Material List (Locally Sourceable)

| Material                        | Qty   | Source (Germany)        | Price (€)* |
|----------------------------------|-------|--------------------------|------------|
| Nickel(II) nitrate·6 H₂O         | 250 g | Carl Roth, VWR           | 18         |
| Ammonium molybdate·4 H₂O         | 100 g | Merck, Roth              | 25         |
| Sodium hydroxide (pellets)       | 1 kg  | Hornbach, pharmacy       | 8          |
| Sodium borohydride               | 25 g  | Sigma-Aldrich, Roth      | 32         |
| Graphene nanoplatelets (~20 nm)  | 50 g  | RS-Components, Amazon    | 15         |
| Isopropanol 99 %                 | 5 L   | Bauhaus, Conrad          | 12         |
| CO₂ canister (Sodastream)        | 425 g | Rewe, DM                 | 17         |
| Nitrogen gas (10 L @ 200 bar)    | 1     | Linde / WestfalenGas     | 65         |
| Reactor (5 L Borosilicate/Steel) | 1     | Carl Roth, classifieds   | 120        |
| Heated magnetic stirrer          | 1     | Used, Amazon             | 200        |
| Ultrasonic agitator (50 W)       | 1     | Amazon                   | 90         |
| Lab power supply (0–12 V / 10 A) | 1     | PeakTech                 | 110        |
| Drying oven or dehydrator        | 1     | Uni surplus / Klarstein  | 0–180      |
| Tube furnace (800 °C, N₂)        | 1     | Physics lab, makerspace  | 0–120      |
| Syringe pump + PTFE tube (1 mm)  | 1     | Open source kit          | 150        |
| pH meter & ORP probe             | 1 ea  | Hanna, Voltcraft         | 140        |

_*April 2025 prices, incl. VAT – freely available in Germany._

---

## 3 Process Overview

**1. Catalyst Gel Preparation**  
Precipitate Ni/Mo salts at pH 10.5 → dry at 80 °C for 1 h → grind into fine powder.

**2. CO₂ Conversion Reaction**  
- 3 L water, NaOH (pH 12.7), 3 g NiMo powder, 0.2 g graphene seeds  
- Heated to 60 °C, ultrasonic agitation  
- CO₂ input gas at 0.3 L/min  
- 4 V DC power applied for 6 h  

**3. Shaping Output**  
- **300 mL** slurry cast on PTFE plate for foil  
- **50 mL** slurry wet-spun through 1 mm tube into 70 % IPA → 30 cm fiber cable  

**4. Drying**  
- 4 h at 60 °C in vacuum or convection oven  

**5. Graphitization**  
- Heat at 800 °C for 30 min under nitrogen  
- Full heat–hold–cool cycle managed automatically  

**6. Validation**  
- 4-wire resistance check  
- 1 kg tensile test on cable  
- LED demonstration using carbon wire  

---

## 4 36-Hour Timeline

| Time       | Step                          |
|------------|-------------------------------|
| 0–1 h      | Catalyst prep + drying        |
| 1–7 h      | CO₂ reduction (monitor 0.5 h) |
| 7–9 h      | Slurry handling, shaping      |
| 9–13 h     | Freezing & drying             |
| 13–17 h    | Graphitization                |
| 17–20 h    | Testing + demo                |
| 20–36 h    | Buffer + documentation        |

---

## 5 Calibration Box

| Target Metric   | Range         |
|-----------------|---------------|
| **pH**          | 12.7 ± 0.1    |
| **ORP**         | –620 ± 30 mV  |

- If **pH < 12.4** → Add 2 g NaOH  
- If **ORP > –550 mV** → Add 0.05 g NaBH₄ in 10 mL water  

---

## 6 Stop & Fix Table

| Symptom                | Cause             | 30-Min Fix                   |
|------------------------|-------------------|------------------------------|
| Slurry remains gray    | pH too low        | Adjust NaOH per calibration |
| Agglomerates sink      | No ultrasound     | Check agitator, extend time |
| O₂ alarm in furnace    | N₂ depleted       | Swap tank, purge 5 min      |

---

## 7 Safety & Disposal

- **Corrosive/Reactive**: NaOH and NaBH₄ → Goggles, gloves, face shield  
  (NaBH₄ diluted to 2 %, <100 g storage)  
- **Flammable**: IPA → Ensure ventilation, no sparks  

| Waste Type             | Code             |
|------------------------|------------------|
| IPA residues           | AVV 14 06 03      |
| Ni/Mo solids           | AVV 06 03 11      |
| Neutralized lye        | After pH < 9 → drain per metal protocol |
| Slurry filtrate        | Neutralize to pH > 12, precipitate Ni-hydroxide → dispose as AVV 06 03 11 |

---

## 8 Operating Costs

| Item            | Cost |
|-----------------|------|
| Chemicals       | 30 € |
| Electricity     | 1.8 € (6.1 kWh @ 0.30 €/kWh) |
| Gases (CO₂ + N₂)| 6 €  |
| **Total**       | ≈ 38 € |

---

## 9 Optimization Notes

### 9.1 Boost CO₂ Yield

Current yield is ~16 % per run. You can increase it by:

- Slower gas rate (0.15 L/min)  
- Microbubble diffuser stone  
- Recycle outgas through liquid trap  
- Extended runtime (e.g. 8 h)  
- Pulse NaBH₄ dosing  
- Cycled ultrasound (10 min on/off)  
- Maintain pH strictly at 12.7  

### 9.2 Reduce Power Use

Total energy: 6.1 kWh per run. Reduce by:

- Lower voltage (3.0–3.2 V)  
- Pulse mode power  
- Heat plate only during startup  
- Passive insulation  
- Graphitize multiple samples simultaneously  
- Night/off-peak or solar usage
