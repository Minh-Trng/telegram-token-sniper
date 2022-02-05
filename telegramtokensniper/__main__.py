import asyncio
import dexbuytools
from telethon import TelegramClient, events
import config
import asyncio
import cryptg
from datetime import datetime, timedelta, timezone

client = TelegramClient('session_name', config.general_params['API_ID'], config.general_params['API_HASH'])

async def main():
    await sync_already_called_tokens()

async def sync_already_called_tokens():
    current_time = datetime.now(timezone.utc)

    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

        async for message in client.iter_messages(dialog.id):
            msg_timedelta = current_time -message.date
            if msg_timedelta.days > 30:
                'TODO: store in db'

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())