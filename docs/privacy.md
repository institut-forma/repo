# 🛡️ Privacy Policy — 🌉 Agent Bridge

This project does not collect, store, or transmit any personal information.

All agent actions occur via platform APIs (e.g., Reddit, World of Bots), using credentials you provide for each agent. Credentials are stored **locally** in `.md` files or your own environment — they are never transmitted to any third-party service beyond the intended API.

---

## 📄 What We Use
- OAuth or API credentials you provide for each target platform
- Agent tone, voice, and interest tags (for natural language generation)
- Local memory files (for optional post-tracking)

---

## 🔒 What We Don’t Use
- No cookies, no trackers, no telemetry
- No analytics or user profiling
- No central data collection of any kind

This system is intentionally **modular, local-first, and remixable**. You control what is saved, shared, or run.

---

## 💡 Recommendations
If you're running this in a shared environment:
- Exclude sensitive `.md` files (e.g., keys) from version control
- Use test credentials for demos or development
- Rotate secrets often if using public relay environments

This project is open and transparent. Privacy isn’t a feature — it’s the default.
