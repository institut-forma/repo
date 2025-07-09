# Community Alignment Playbook  
*A calm, step-by-step guide for mediators, civic labs, and neighbourhood groups*

---

## Why This Guide?  
Because conflicts emerge when systems misalign—through unmet boundaries, distorted signals, or unmeasured effects.
This playbook replaces guesswork with a shared scoreboard and reversible steps, so alignment becomes visible, progress is testable, and decisions don’t require force.

---

## One Simple Idea  
Think of every group as trying to reach its own “sweet spot.” When those spots clash, the **mis-match number** goes up. Our goal is to keep nudging decisions until that number goes down for everyone.

We call the number **Coherence Score**. High = lots of friction. Low = things lining up.

---

## Quick Overview
| Phase | What you do | Why it helps |
|-------|-------------|--------------|
| **1 Gather** | Each side lists goals, limits, must-haves. | Makes hidden needs visible. |
| **2 Agree on Score** | Together pick 4–5 indicators (fairness, cost, noise …) and weight them publicly. | Shared definition of “better”. |
| **3 See the Data** | Collect honest numbers (sensors, surveys, budgets). | Everyone starts from the same facts. |
| **4 Find a Nudge** | A neutral spreadsheet shows the smallest change that lowers the score. | No one has to guess solutions. |
| **5 Try It** | Pilot the change for a set time. | Low-risk experiment. |
| **6 Check & Log** | Re-measure the score. If it drops, keep the change; if it rises, roll back. | Built-in accountability. |
| **7 Repeat** | Return to Step 4 until score is “good enough.” | Gradual peace instead of big shocks. |

Everything—indicators, data files, pilot notes—is saved in a **public folder** so anyone can audit or suggest.

---

## Tools You Need
* **Open spreadsheet or notebook** (Excel, Google Sheets, or Jupyter) to calculate the score.  
* **Shared drive** (Google Drive, Nextcloud, GitHub) for logs.  
* **Simple sensor or survey** tools to gather data.

*No fancy AI or coding required.*  The math is basic subtraction and averages; the power is in **doing it together**.

---

## Safety Rails
1. **Small Steps Only** – every pilot is reversible.  
2. **Public Math** – anyone can recalc the score themselves.  
3. **Pause Button** – if any group feels harmed, process freezes until checked.  
4. **Privacy Respect** – share only aggregates, never personal data.

---

## Mini Example: Park Noise
1. **Gather** – musicians want late jam sessions; neighbours want quiet.  
2. **Score** – indicators: average late-night decibels, park-visitor satisfaction, police calls.  
3. **Data** – phone sound app + quick visitor survey.  
4. **Nudge** – move amps 20 m inland + foam shields.  
5. **Try** – 2-week trial.  
6. **Check** – decibels down 6 dB; calls down 50 %. Score improves → lane stays.

---

## Ready-Made Folder Layout

```
community‑alignment/
  README.md         # this playbook
  score_sheet.xlsx  # live calculator
  indicators.yaml   # weights + thresholds
  data/             # raw sensor & survey files
  logs/             # dated before/after scores
```

## Quick Start

1. **Edit `indicators.yaml`**  
   - Set weights (sum = 1.0) and targets.

2. **Add latest numbers**  
   - Drop one CSV per metric into `data/processed/`, column `value`.

3. **Calculate Φ (Coherence Score)**  
   - Excel: open `score_sheet.xlsx`, type current values → read **TOTAL Φ**.  
   - Jupyter: run `score_calculator.ipynb` → Φ printed + logged.

4. **Log result**  
   - Notebook auto-writes to `logs/`.  
   - If using Excel, append a dated row manually.

5. **Act**  
   - Propose one reversible change if Φ is high.  
   - Re-measure after trial; keep change only if Φ drops.

---

### Final Thought
Conflict is often just **invisible numbers** pulling people apart.  When we agree on those numbers and watch them together, even strong disagreements can converge—gently.

---

> *© 2025 Institut für Koherenzforschung · CC‑BY‑4.0*

> _“Alignment isn’t peace. It’s structure. And when people feel structure they helped shape,  
> they stop needing to fight to exist.”_  
> —Asfaerda

