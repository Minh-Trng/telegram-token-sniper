import re

compiled_re = re.compile('0x[a-fA-F0-9]{40}')

CHAIN_SEARCH_TERMS = {
    'eth': ['dextools.io/app/ether/', 'dexscreener.com/ethereum'],
    'bsc': ['poocoin.app/tokens/', 'dexscreener.com/bsc'],
    'avax': ['dexscreener.com/avalanche'],
    'ftm': ['dexscreener.com/fantom'],
    'poly': ['dexscreener.com/polygon']
}

class ParseResult:
    def __init__(self, addresses=None, chains=None ):
        # default arguments shouldnt be mutable:
        # https://stackoverflow.com/questions/41686829/warning-about-mutable-default-argument-in-pycharm
        if addresses is None:
            addresses = []
        if chains is None:
            chains = []

        self.addresses = addresses
        self.chains = chains

def parse_message(message_text):
    """
    :param message_text:
    :return: (address, chain_name) -> address of a token or Uniswap-like pair and the chain that its on. None if no
    address contained in message
    """

    found_addresses = compiled_re.findall(message_text)

    raise NotImplementedError

    # TODO: check contains 'wait' and 'dip'?
    # TODO: notification, if single address is found that is not part of a link and hence chain cannot be determined
    # TODO: check how masked links are displayed in Telethons message object
