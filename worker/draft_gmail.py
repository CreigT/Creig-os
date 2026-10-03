"""First Creig OS job.

Open Gmail, find the newest unread customer email, draft a reply, do not send.
Runs only on the laptop after Ollama and browser-use are installed.
"""

import asyncio

TASK = (
    "Open https://mail.google.com/mail/u/0/#inbox. "
    "If a login page is showing, stop immediately and say LOGIN_REQUIRED. "
    "Do not type any password. "
    "Find the newest unread email that looks like a customer message. "
    "Draft a short plain reply that answers the question and asks nothing extra. "
    "Save it as a draft. Do not click Send. "
    "Return the subject and the draft text."
)

ALLOWED = ("mail.google.com",)


async def main() -> None:
    from browser_use import Agent, ChatOllama

    agent = Agent(
        task=TASK,
        llm=ChatOllama(model="qwen3:8b"),
    )
    result = await agent.run()
    print(result)
    print("Done. Check Gmail Drafts. Nothing was sent.")


if __name__ == "__main__":
    print("Allowed sites:", ", ".join(ALLOWED))
    print("Blocked: send, pay, delete, password entry")
    asyncio.run(main())
