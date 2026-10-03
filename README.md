# Creig OS

Creig OS is a zero-trust desk for one AI worker. The worker uses your apps the way an employee does: open Chrome, read the page, click, type, move to the next app. The apps do not need an API.

It is not a new Windows or Mac operating system. It sits on top of Gmail, Sheets, and your website.

The GitHub repo is the map. The worker runs on the laptop. The phone cannot run the worker.

## What it is for

Use it for work a person already does in a browser.

- Answer a customer email. Read the thread and leave a draft. Do not send.
- Find an order. Read the email, open the order sheet, write the status.
- Process a document. Copy the total, date, and name into one row.
- Monitor a website. Open the page on a timer and log only what changed.
- Qualify a lead. Write the name, city, service, and a score. Hot leads wait for you.
- Move between apps. Gmail, then Sheets, then the site, in one job.

Do not use it to send mail, pay, delete files, change prices, or type a password. Those stay with you.

## How to use it

1. On the laptop, install Ollama from https://ollama.com and run `ollama pull qwen3:8b`.
2. Clone this repo and run `pip install browser-use`.
3. Open Chrome and log into Gmail yourself. Leave that window open.
4. Open `desk/index.html` in a browser. That page is the desk. It does not start the worker.
5. Run the first job: `python worker/draft_gmail.py`.
6. Check Gmail Drafts. If the draft is wrong, do not send it.

The worker never types a password. If Gmail asks for a login, stop.

## Rules

| Action | Rule |
| --- | --- |
| Open Gmail, Sheets, your site | Allow |
| Read and draft | Allow |
| Send, pay, delete, change a price | Hold for you |
| Type a password or leave the allow list | Block |

A draft in Gmail is the proof it works. Until that draft exists, this repo is the plan, not the employee.
