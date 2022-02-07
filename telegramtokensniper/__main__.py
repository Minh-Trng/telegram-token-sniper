import asyncio
import logging

import dexbuytools
from telethon import TelegramClient, events
import config
import asyncio
import cryptg
from datetime import datetime, timedelta, timezone

from telegramtokensniper import parsing, log_utils, storage, chain_utils

import chain_utils

client = TelegramClient('session_name', config.general_params['API_ID'], config.general_params['API_HASH'])

async def main():
    await sync_already_called_tokens()

async def sync_already_called_tokens():
    current_time = datetime.now(timezone.utc)

    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

        async for message in client.iter_messages(dialog.id):
            msg_timedelta = current_time - message.date
            if msg_timedelta.days < config.general_params["SYNC_LIMIT_DAYS"]:
                parse_result = parsing.parse_message(message.text)
                addresses = parse_result.addresses
                chains = parse_result.chains


                if len(addresses) > 0:
                    if len(chains) == 0:
                        log_utils.logging.info(f"address(es) found without chain: {addresses}")
                        for address in addresses:
                            storage.insert_token(address, '', dialog.id, message)
                    elif len(addresses) == 1 and len(chains) == 1:
                        storage.insert_token(addresses[0], chains[0], dialog.id, message)
                    else:
                        token_chain_pairs = chain_utils.determine_tokens(addresses, chains)
                        raise NotImplementedError


@client.on(events.NewMessage)
async def my_event_handler(event):
    pass
    # TODO: notification, if single address is found that is not part of a link and hence chain cannot be determined

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())

    # client.start()
    # client.run_until_disconnected()