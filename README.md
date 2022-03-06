# telegram-token-sniper
Application to parse token addresses from telegram messages and automatically buy tokens that get mentioned for the first time.

# Installation
> pip install -r requirements.txt

# Configuration
In telegramtokensniper/config/general.yml you need to provide an Api-Id and an Api-hash for a telegram account that you want to use 
(see https://my.telegram.org, under API Development for more information).

In telegramtokensniper/dbt_config_template/ you will find a README.md with details on how to configure buying of tokens.

# Usage
> python3 __main__.py 

# How the program works
At launch the program will start to read all past messages for all chats of the given account. From these messages all addresses will 
get parsed and stored in a local database

After the sync is finished, whenever a new message arrives, if it contains an address that can be linked to a token + chain 
(requires a link to a tokentracking page like [dextools](https://dextools.io), [dexscreener](https://dexscreener.com/), 
[poocoin](https://poocoin.app/) within the same message) and is not contained in the 
database yet, it will be bought automatically.

The sync can be limited to a certain amount of most recent days with the SYNC_LIMIT_DAYS parameter in config/general.yml


# Limitations
Only works for tokens that have liquidity on the main exchange with the main token of a network, e.g. for Ethereum there needs to be a ETH/XyzToken-Pool on Uniswap