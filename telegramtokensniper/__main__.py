import asyncio
import logging
import time

import dexbuytools
from telethon import TelegramClient, events
import config
import asyncio
import cryptg
from datetime import datetime, timedelta, timezone

from telegramtokensniper import parsing, log_utils, storage, chain_utils, notifications

import chain_utils

client = TelegramClient('session_name', config.general_params['API_ID'], config.general_params['API_HASH'])

sync_completed = False

async def main():
    await sync_already_called_tokens()


async def sync_already_called_tokens():
    current_time = datetime.now(timezone.utc)

    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

        offset_date = current_time - timedelta(days=config.general_params["SYNC_LIMIT_DAYS"])

        async for message in client.iter_messages(dialog.id, reverse=True, offset_date=offset_date):
            _process_message(message, dialog.id)

    global sync_completed
    sync_completed = True



@client.on(events.NewMessage)
async def my_event_handler(event):
    if not sync_completed:
        notifications.send_telegram_message(f'Message {event.message.id} in chat {event.message.chat_id} was not '
                                            f'handled because sync wasnt completed')
        return

    _process_message(event.message, event.message.chat_id, buy_new_tokens=True)

def _process_message(message, dialog_id, buy_new_tokens=False):
    parse_result = parsing.parse_message(message.text)
    addresses = parse_result.addresses
    chains = parse_result.chains

    unseen_addresses = list(filter(lambda x: not storage.address_already_seen(x), addresses))

    if len(unseen_addresses) > 0:

        if len(chains) == 0:
            log_utils.logging.info(f"address(es) found without chain: {unseen_addresses}")
            for address in unseen_addresses:
                storage.insert_token(address, '', dialog_id, message)
        else:
            address_chain_pairs = chain_utils.determine_tokens(unseen_addresses, chains)
            for address, chain in address_chain_pairs:
                storage.insert_token(address, chain, dialog_id, message)
            if buy_new_tokens:
                chain_utils.buy(address_chain_pairs)


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())

    while True:
        try:
            client.start()
            client.run_until_disconnected()
        except:
            notifications.send_telegram_message("TTS: client disconnected, attempt restart")
            time.sleep(60)