import time

from telethon import TelegramClient, events
from datetime import datetime, timedelta, timezone

from telegramtokensniper import parsing, log_utils, storage, chain_utils, notifications, config, chain_utils

client = TelegramClient('session_name', config.general_params['API_ID'], config.general_params['API_HASH'])

sync_completed = False

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
                storage.insert_address(address, '', dialog_id, message)
        else:
            tokenaddress_chain_pairs = chain_utils.determine_tokens(unseen_addresses, chains)

            tokenaddresses = [x[0] for x in tokenaddress_chain_pairs]

            for unseen_address in unseen_addresses:
                if unseen_address not in tokenaddresses:
                    #store non-token-addresses like pair-contracts to filter them out in future messages
                    storage.insert_address(unseen_address, '', dialog_id, message)

            unseen_tokenaddress_chain_pairs = [x for x in tokenaddress_chain_pairs if not storage.address_already_seen(x[0])]

            for address, chain in unseen_tokenaddress_chain_pairs:
                storage.insert_address(address, chain, dialog_id, message)

            if buy_new_tokens:
                chain_utils.buy(unseen_tokenaddress_chain_pairs)


if __name__ == "__main__":
    try:
        with client:
            client.loop.run_until_complete(sync_already_called_tokens())
    except Exception as e:
        notifications.send_telegram_message("TTS: sync failed")
        log_utils.logging.error(f'Exception during sync: {e}')
        exit()

    while True:
        try:
            client.start()
            client.run_until_disconnected()
        except Exception as e:
            notifications.send_telegram_message("TTS: client disconnected or exception occured, attempt restart")
            log_utils.logging.error(f'Exception caught in main-loop: {e}')
            time.sleep(60)
