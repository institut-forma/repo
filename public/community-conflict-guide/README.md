# Community Alignment Playbook  
*A calm, step‑by‑step guide for mediators, civic labs, and neighbourhood groups*

---

## Why This Guide?  
Conflicts grow when distorted inputs, mismatched boundaries, and unheard identities stack up. This playbook offers a **shared scoreboard** and **small, reversible steps** so everyone sees progress together—no mystery, no power grabs.

---

## One Simple Idea  
Think of every group as trying to reach its own “sweet spot.”  When those spots clash, the **mis‑match number** goes up.  Our goal is to keep nudging decisions until that number goes down for everyone.

We call the number **Coherence Score**.  High = lots of friction.  Low = things lining up.

---

## Quick Overview
| Phase | What you do | Why it helps |
|-------|-------------|--------------|
| **1 Gather** | Each side lists goals, limits, must‑haves. | Makes hidden needs visible. |
| **2 Agree on Score** | Together pick 4‑5 indicators (fairness, cost, noise, etc.).  Weight them publicly. | Shared definition of “better”. |
| **3 See the Data** | Collect honest numbers (sensors, surveys, budgets). | Everyone starts from the same facts. |
| **4 Find a Nudge** | A neutral spreadsheet shows the smallest change that lowers the score. | No one has to guess solutions. |
| **5 Try It** | Pilot the change for a set time. | Low‑risk experiment. |
| **6 Check & Log** | Re‑measure the score.  If it drops, keep the change; if it rises, roll back. | Built‑in accountability. |
| **7 Repeat** | Return to Step 4 until score is “good enough.” | Gradual peace instead of big shocks. |

Everything—indicators, data files, pilot notes—is saved in a **public folder** so anyone can audit or suggest.

---

## Tools You Need
- **Open spreadsheet or notebook** (Excel, Google Sheets, or Jupyter) to calculate the score.  
- **Shared drive** (Google Drive, Nextcloud, GitHub) for logs.  
- **Simple sensor or survey** tools to gather data.

*No fancy AI or coding is required.*  The math is basic subtraction and averages; the power is in **doing it together**.

---

## Safety Rails
1. **Small Steps Only** – every pilot is reversible.
2. **Public Math** – everyone can recalc the score themselves.
3. **Pause Button** – if any group feels the change harms them, process freezes until checked.
4. **Privacy Respect** – only share aggregates, never personal data.

---

## Mini Example: Park Noise
1. **Gather** – musicians want late jam sessions; neighbours want quiet.  
2. **Score** – indicators: average late‑night decibels, park visit satisfaction, police calls.  
3. **Data** – phone sound app + quick visitor survey.  
4. **Nudge** – suggest: move amps 20 m inland + foam shields.  
5. **Try** – 2‑week trial.  
6. **Check** – decibels drop 6 dB; calls down 50 %. Score improves; pilot adopted.

---

## Ready‑Made Starter Pack  
*Everything you need to pilot the method — including the scoring step promised above*

```text
community-conflict-guide/
  README.md              # quick‑start guide (this playbook)
  indicators.yaml        # pick + weight your metrics; template below
  score_calculator.ipynb # auto‑computes the Coherence Score (Python / Colab)
  score_sheet.xlsx       # same calculator in plain Excel
  data/
      raw/               # sensor CSVs, survey forms
      processed/         # cleaned aggregates fed to calculator
  logs/
      2025‑07‑09.csv     # timestamped before/after scores + chosen nudges
```

### How to Calculate the Score

1. **Edit `indicators.yaml`** — list each metric with weight and target value.
   ```yaml
   noise_dB:
     weight: 0.30
     target: 45          # acceptable late‑night dB
   satisfaction:
     weight: 0.40
     target: 80          # % residents rating ≥ 4/5
   cost_index:
     weight: 0.30
     target: 1.0         # budget multiplier (≤1 means within budget)
   ```

2. **Drop new readings** into `data/raw/` (sound logs, survey CSV, cost sheet).

3. **Run `score_calculator.ipynb`** (or open `score_sheet.xlsx`).  The tool:
   - Normalises each indicator to a 0‑1 mismatch: `(current – target) / target`.
   - Multiplies by its weight.
   - Sums to give the **Coherence Score Φ** (lower = better).

4. **Log** before/after scores in `logs/`.
   - Score ↓ → keep the change.
   - Score ↑ → roll back and rethink.

*No Python?*  Use the Excel sheet — formulas are baked in; just paste your numbers.

---

### Final Thought
Conflict is often just **invisible numbers** pulling people apart.  When we agree on those numbers and watch them together, even strong disagreements can converge—gently.
