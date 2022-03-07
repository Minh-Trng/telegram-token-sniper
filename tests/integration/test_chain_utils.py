import pytest
from telegramtokensniper import chain_utils


@pytest.mark.parametrize('addresses,chains,expected',
                         [
                             (['0x95189f25b4609120f72783e883640216e92732da'], ['avax'],
                              [('0x8f47416cae600bccf9530e9f3aeaa06bdd1caa79', 'avax')]),
                             (['0x8f47416cae600bccf9530e9f3aeaa06bdd1caa79'], ['avax'],
                              [('0x8f47416cae600bccf9530e9f3aeaa06bdd1caa79', 'avax')])
                         ])
def test_determine_tokens_parsed_addresses_correctly(addresses, chains, expected):
    result = chain_utils.determine_tokens(addresses, chains)
    assert result[0][0] == expected[0][0]
    assert result[0][1] == expected[0][1]


def test_determine_tokens_no_duplicates():
    # token address, corresponding pool address, random EOA address and random truncated tx hash
    input_addresses = ['0x0d35b29d50c13128fe3dbadcab0811cccd7b338a', '0x22157a7fd6F2A8eE8Df4621B52B8fEbE83934714',
                       '0xE0df036638CEcdf1D66C93AbBe844d87BfA7F0C7', '0xDCaCa05de9adE34F3fCb9CE94d1B7930093E526E']
    input_chains = ['eth']
    result = chain_utils.determine_tokens(input_addresses, input_chains)
    assert len(result) == 1
