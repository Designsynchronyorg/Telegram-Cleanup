# 🧹 Telegram Chat Cleaner

Effortlessly declutter your Telegram chats by automatically **leaving**, **deleting**, and **silencing** the noise — all from one script.  
Built with 💖 by [Design Synchrony](https://designsynchrony.com.ng) & [abreel](https://github.com/abreel).

---

## 🚀 Features

- Lists all your current chats
- Keeps only the ones you specify
- Leaves Telegram groups/channels
- Deletes chats and chat history
- Saves you from Telegram chaos ✨
---

## 📦 Requirements

- Python 3.8+
- [Telethon](https://github.com/LonamiWebs/Telethon)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- Telegram API credentials (get yours from [my.telegram.org](https://my.telegram.org))

---

## ⚙️ Installation

```bash
git clone https://github.com/Designsynchronyorg/Telegram-Cleanup.git
cd telegram-chat-cleaner

pip install -r requirements.txt
````

---

## 🔐 Setup

Create a `.env` file in the root of the project:

```ini
API_ID=your_api_id
API_HASH=your_api_hash
```

> 💡 Don’t know where to get these? Log in at [my.telegram.org](https://my.telegram.org) → API Development → Create a new app.

---

## ▶️ Usage

```bash
python main.py
```

You’ll see a list of all your chats, like so:

```diff
🧾 ALL CHATS:
- Cool Group
- Work Stuff
- Random Channel
```

Then enter the **names you want to keep**, comma-separated:

```bash
📌 Enter chat/group/channel names to KEEP (comma-separated): Work Stuff
```

That’s it — we’ll sweep through and leave/delete everything else! 🧹

---

## 📸 Screenshot

```yaml
🧾 ALL CHATS:
- Cat Memes Central
- Project Alpha
- Spamzilla News

📌 Enter chat/group/channel names to KEEP (comma-separated): Project Alpha

✅ Keeping: Project Alpha
👋 Leaving: Cat Memes Central
🗑️ Deleting chat: Cat Memes Central
👋 Leaving: Spamzilla News
🗑️ Deleting chat: Spamzilla News

✅ Done! Deleted 2 chats not in your keep list.
```

---

## ✨ Credits

Big thanks to:

* [**Design Synchrony**](https://designsynchrony.com.ng) – Branding, tools & testing
* [**abreel**](https://github.com/abreel) – Core scripting & concept

---

## ☠️ Warning

This script **actually leaves and deletes chats.**
No take-backs. No regrets. So be sure about what you’re keeping before you hit enter.

---

## 📄 License

MIT — Do what you want, just don’t sue us 😎

