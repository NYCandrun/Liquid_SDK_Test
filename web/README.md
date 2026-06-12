# LiquidZork — Web v0

A single-file, self-contained HTML web app that plays **Zork I** in a modern AI-chat-style UI on your iPhone (or any browser), with optional AI-powered hints, recaps, and atmospheric descriptions powered by Liquid AI models via OpenRouter.

## How to use

1. Open `zork-chat.html` in any modern browser — Safari on iPhone, Chrome, anything.
2. (Optional) Tap the `•••` menu → `API key & model` to paste an [OpenRouter API key](https://openrouter.ai/keys). You can play the base game without one; you only need a key for the AI features (hint / describe / recap / inventory & examine flavor).
3. On iPhone: Safari → Share → "Add to Home Screen" turns it into a standalone app icon.

## Files

- `zork-chat.html` — The complete app. Single self-contained file. Email it, host it anywhere, or open it locally.
- `_template.html` — Build-time source with placeholders.
- `jszm.js` — JSZM Z-machine interpreter (public domain, by zzo38).
- `zork1.z5` — Zork I Release 88 story file.
- `zork1.z5.b64` — Base64-encoded copy embedded into the final HTML.

## Build

```bash
python3 ../build_html.py    # rebuilds zork-chat.html from _template.html
```

## AI features (v1)

| Action | What it does |
|---|---|
| **Hint** | Liquid suggests a useful next move, grounded in the current scene |
| **Vague hint** | A subtle 1-sentence nudge |
| **Spoiler hint** | A direct, specific tip |
| **Describe** | Re-renders the current room in richer atmospheric prose |
| **Recap** | Summarizes the last few turns of your playthrough |
| **Inventory flavor** | When you type `inventory`, the LLM adds light flavor |
| **Examine flavor** | When you `examine X`, the LLM adds 1-2 atmospheric sentences |

All AI calls are strictly grounded in the game state and turn log — no hallucinating items or exits.

## Privacy

- Your API key is stored in your browser's `localStorage`. Nothing is sent to a server we control — calls go directly from your browser to OpenRouter.
- Game saves use `localStorage`.

## License & attribution

- Zork I source code is © Activision/Microsoft, made open-source under MIT in Nov 2025. The story file (`zork1.z5`) used here is the 1983 commercial release; for a fully clean-room build you'd compile your own `.z5` from the [MIT-licensed ZIL source](https://github.com/historicalsource/zork1).
- JSZM Z-machine interpreter — public domain (zzo38).
- "Zork" is a registered trademark. This is a personal/educational project; commercial release would require trademark clearance.
