# Language Integrity Check

A tool for evaluating the **structural coherence** and **factual accuracy** of any text, using general-purpose language models.

---

## What it does

This protocol checks:
- 🧱 **Coherence** – Does the message hold together logically, emotionally, and semantically?
- 📚 **(Optional) Facts** – Are key claims verifiable and supported?

It works on any document, post, email, or script.

---

## Why it matters

AI-generated content is increasingly used to:
- Spread persuasive but misleading messages
- Mimic logic or authority without internal consistency
- Confuse or manipulate with emotional pacing

This tool helps reveal those patterns.

---

## How to use (LLM required)

Use any capable **large language model (LLM)** with strong reasoning and text analysis abilities.

### Example: [OpenAI GPT-4o](https://chat.openai.com)

1. Paste or upload your document
2. Append the following prompt:
## 🧪 Copy-paste prompt

Paste this at the end of any text you'd like to analyze:

```txt
### Step 1 – Coherence Check:
Analyze the internal coherence of the above text.

Do not fact-check. Instead, evaluate whether the structure holds together logically, emotionally, and semantically.

Identify inconsistencies, manipulation, or signs of degraded signal integrity.

Highlight both strengths and weaknesses in coherence, and summarize your conclusion.

---

### Step 2 – (Optional) Fact Check:
Now fact-check the key factual claims made in the text.

List any statements that appear false, unverifiable, or misleading, and explain briefly why.

Use current public data. Cite sources if available.
