import requests as requests

from telegramtokensniper import config


def send_telegram_message(message):
    bot_token = config.general_params['TG_BOT_TOKEN']
    chat_id = config.general_params['TG_CHAT_ID']

    if bot_token is None or chat_id is None:
        return

    send_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'

    response = requests.get(send_url)

    return response.json()
