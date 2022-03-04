import pytest
from telegramtokensniper import chain_utils


@pytest.mark.parametrize('addresses,chains,expected',
                         [
                             (['0x95189f25b4609120f72783e883640216e92732da'], ['avax'],
                              [('0x8f47416cae600bccf9530e9f3aeaa06bdd1caa79', 'avax')]),
                             (['0x8f47416cae600bccf9530e9f3aeaa06bdd1caa79'], ['avax'],
                              [('0x8f47416cae600bccf9530e9f3aeaa06bdd1caa79', 'avax')])
                         ])
def test_determine_tokens(addresses, chains, expected):
    result = chain_utils.determine_tokens(addresses, chains)
    assert result[0][0] == expected[0][0]
    assert result[0][1] == expected[0][1]