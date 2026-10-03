# Creig OS

One desk. One worker. One warden.

This is not a new Windows. The worker uses the apps you already use by opening Chrome, reading the page, clicking, and typing. No API is required.

The phone repo is the map. The worker runs on the laptop.

## What is live

- `desk/index.html` is the desk. Open it in a browser. Adding a job only updates the page.
- `worker/draft_gmail.py` is the first real job. It is not running until you start it on the laptop.
- Send, pay, and delete are off. The job may only draft.

## First run on the laptop

1. Install Ollama and pull a model: `ollama pull qwen3:8b`
2. In this folder: `pip install browser-use`
3. Open Chrome and log into Gmail yourself. Leave that window open.
4. Run: `python worker/draft_gmail.py`
5. Check Gmail Drafts. If the draft is wrong, do not send it.

The worker never types a password. If Gmail asks for a login, stop.
