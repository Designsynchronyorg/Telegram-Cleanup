import os

from telethon.errors import UserNotParticipantError
from telethon.sync import TelegramClient
from dotenv import load_dotenv
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import DeleteHistoryRequest

# Load from .env
load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = 'cleaner_session'

# Connect to Telegram
with TelegramClient(session_name, api_id, api_hash) as client:
    dialogs = client.get_dialogs()

    print("\n🧾 ALL CHATS:")
    for dialog in dialogs:
        print(f"- {dialog.name}")

    keep_chats_input = input("\n📌 Enter chat/group/channel names to KEEP (comma-separated): ")
    keep_chat_names = {x.strip().lower() for x in keep_chats_input.split(",") if x.strip()}

    print("\n🧹 Starting the digital exorcism...\n")
    deleted_count = 0

    for dialog in dialogs:
        name = dialog.name.lower()
        if name in keep_chat_names:
            print(f"✅ Keeping: {dialog.name}")
            continue

        try:
            if dialog.is_group or dialog.is_channel:
                print(f"👋 Leaving: {dialog.name}")
                try:
                    client(LeaveChannelRequest(dialog.entity))
                except UserNotParticipantError:
                    print(f"  ⚠️ Already not a member of: {dialog.name}")
            print(f"🗑️ Deleting chat: {dialog.name}")
            client(DeleteHistoryRequest(peer=dialog.entity, max_id=0, revoke=True))
            deleted_count += 1
        except Exception as e:
            print(f"⚠️ Could not process {dialog.name}: {e}")

    print(f"\n✅ Done! Deleted {deleted_count} chats not in your keep list.")