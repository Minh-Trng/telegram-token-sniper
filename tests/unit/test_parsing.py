import pytest as pytest
from test_data import sample_messages

from telegramtokensniper import parsing

@pytest.mark.parametrize('message,expected',
                         [
                             (sample_messages.avax_dextools_msg,
                              parsing.ParseResult(['0x0cdb6427e2f737071f661a11c33656c096f6fc9e'], ['avax'])),
                             (sample_messages.avax_dexscreener_msg,
                              parsing.ParseResult(['0xdB9438f5E3Afa5cED760BE9692604c3c5Ab816d1'], ['avax'])),
                             (sample_messages.bsc_poocoin_msg,
                              parsing.ParseResult(['0x317d61ba51a625218286a952f04b381a7189082a'], ['bsc'])),

                         ])
def test_parse_message(message, expected):
    parse_result = parsing.parse_message(message)
    assert parse_result.addresses[0] == expected.addresses[0]
    assert parse_result.chains[0] == expected.chains[0]