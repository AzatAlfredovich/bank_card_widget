from unittest.mock import mock_open, patch

import pytest

from src.utils import convertor_to_rubles, open_json


# Тест при верной и неверной (неполной) структуре JSON-файла
def test_open_json_correct():
    with patch("builtins.open", mock_open(read_data='{"1" : "2"}')):
        assert open_json("") == {"1": "2"}
    with patch("builtins.open", mock_open(read_data='{"1" : "2"')):
        assert open_json("") == []
    assert open_json("") == []


# Параметризированный тест при верной и неверной (неполной) структуре обрабатываемого словаря
def test_convertor_to_rubles():
    #     need_result = convertor_to_rubles(oper_dict)
    #     assert need_result == result
    assert convertor_to_rubles({"operationAmount": {"amount": "100", "currency": {"name": "RUB", "c": "RUB"}}}) == 0.0
    assert (
        convertor_to_rubles({"operationAmount": {"amount": "100", "currency": {"name": "RUB", "code": "RUB"}}}) == 100
    )
    with patch("requests.get") as r_mock:
        r_mock.return_value.json.return_value = {"result": 95}
        assert (
            convertor_to_rubles({"operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}}})
            == 95
        )
