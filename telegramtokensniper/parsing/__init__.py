import re
from telethon.tl import types
from typing import List

compiled_re = re.compile('0x[a-fA-F0-9]{40}')

CHAIN_SEARCH_TERMS = {
    'eth': ['dexscreener.com/ethereum', 'dextools.io/app/ether/'],
    'bsc': ['poocoin.app/tokens/', 'dexscreener.com/bsc', 'dextools.io/app/bsc'],
    'avax': ['dexscreener.com/avalanche', 'dextools.io/app/avalanche'],
    'ftm': ['dexscreener.com/fantom', 'dextools.io/app/fantom'],
    'poly': ['dexscreener.com/polygon', 'dextools.io/app/polygon']
}

#later: 'cronos': dexscreener.com/cronos/

class ParseResult:
    def __init__(self, addresses: List[str], chains: List[str]):
        self.addresses = addresses
        self.chains = chains


def parse_message(message_text) -> ParseResult:
    """
    :param message_text:
    :return: ParseResult -> address of a token or Uniswap-like pair and the chain that its on. None if no
    address contained in message
    """

    if message_text is None:
        return ParseResult([], [])

    found_addresses = compiled_re.findall(message_text)
    found_chains = []

    for chain_name, search_terms in CHAIN_SEARCH_TERMS.items():
        message_contains_any_searchterm = any(map(lambda x: x in message_text, search_terms))
        if message_contains_any_searchterm:
            found_chains.append(chain_name)

    return ParseResult(found_addresses, found_chains)
