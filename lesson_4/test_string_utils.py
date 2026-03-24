from typing import Literal

import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str: Literal['skypro'] | Literal['hello world'] | Literal['python'], expected: Literal['Skypro'] | Literal['Hello world'] | Literal['Python']):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str: Literal['123abc'] | Literal[''] | Literal['   '], expected: Literal['123abc'] | Literal[''] | Literal['   ']):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "Skypro"),
    ("  Hello world", "Hello world"),
    ("  Python", "Python"),
])
def test_trim_positive(input_str: Literal['  skypro'] | Literal['  Hello world'] | Literal['  Python'], expected: Literal['Skypro'] | Literal['Hello world'] | Literal['Python']):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("  123abc", "123abc"),
    ("  ", ""),
    ("   ", ""),
])
def test_trim_negative(input_str: Literal['  123abc'] | Literal['  '] | Literal['   '], expected: Literal['123abc'] | Literal['']):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("SkyPro", "'S' -> True"),
    ("SkyPro", "'U' -> False")
])
def test_contains_positive(input_str: Literal['SkyPro'], expected: Literal['\'S\' -> True'] | Literal['\'U\' -> False']):
    assert string_utils.contains(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "'1' -> True"),
    
])
def test_contains_negative(input_str: Literal['123abc'], expected: Literal['\'1\' -> True']):
    assert string_utils.contains(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
     ("SkyPro", "'k' -> SyPro"),
     ("SkyPro", "'Pro' -> Sky")
])
def test_delete_symbol_positive(input_str: Any, expected: Any):
    assert string_utils.delete_symbol(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("SkyPro", "'k' -> SyPro"),
    ("SkyPro", "'Pro' -> Sky")
])
def test_delete_symbol_negative(input_str: Literal['123abc'], expected: Literal['\'1\' -> True']):
    assert string_utils.delete_symbol(input_str) == expected