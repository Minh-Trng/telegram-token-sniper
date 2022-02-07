import re
from telethon.tl import types

compiled_re = re.compile('0x[a-fA-F0-9]{40}')

CHAIN_SEARCH_TERMS = {
    'eth': ['dextools.io/app/ether/', 'dexscreener.com/ethereum'],
    'bsc': ['poocoin.app/tokens/', 'dexscreener.com/bsc', 'dextools.io/app/bsc'],
    'avax': ['dexscreener.com/avalanche'],
    'ftm': ['dexscreener.com/fantom'],
    'poly': ['dexscreener.com/polygon']
}

#later: 'cronos': dexscreener.com/cronos/

class ParseResult:
    def __init__(self, addresses: list[str], chains: list[str] ):
        self.addresses = addresses
        self.chains = chains


def parse_message(message: types.Message) -> ParseResult:
    """
    :param message:
    :return: ParseResult -> address of a token or Uniswap-like pair and the chain that its on. None if no
    address contained in message
    """

    found_addresses = compiled_re.findall(message.text)
    found_chains = []

    for chain_name, search_terms in CHAIN_SEARCH_TERMS.items():
        if search_terms in message.text:
            found_chains.append(chain_name)

    return ParseResult(found_addresses,found_chains)
