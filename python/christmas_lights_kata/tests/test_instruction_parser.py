import pytest
from python.christmas_lights_kata.src.instruction_parser import InstructionParser
from python.christmas_lights_kata.src.position import LightPosition
from python.christmas_lights_kata.src.action import LightAction


def test_parse_command_success():
    line = "turn on 10,20 through 30,40"
    action, start, end = InstructionParser.parse(line)
    assert action == LightAction.TURN_ON
    assert start == LightPosition(10, 20)
    assert end == LightPosition(30, 40)


def test_parse_command_invalid_raises():
    with pytest.raises(ValueError):
        InstructionParser.parse("invalid command line")


def test_parse_command_empty_line():
    with pytest.raises(ValueError, match="Empty command line"):
        InstructionParser.parse("")


def test_parse_command_spaces_only():
    with pytest.raises(ValueError, match="Empty command line"):
        InstructionParser.parse("   ")


def test_parse_command_uppercase():
    line = "TURN ON 1,2 THROUGH 3,4"
    action, start, end = InstructionParser.parse(line)
    assert action == LightAction.TURN_ON
    assert start == LightPosition(1, 2)
    assert end == LightPosition(3, 4)


def test_parse_command_extra_spaces():
    line = "turn on   5,6   through   7,8"
    action, start, end = InstructionParser.parse(line)
    assert action == LightAction.TURN_ON
    assert start == LightPosition(5, 6)
    assert end == LightPosition(7, 8)


def test_parse_command_negative_coords():
    line = "turn on -1,0 through 2,2"
    with pytest.raises(ValueError):
        InstructionParser.parse(line)


def test_parse_command_non_numeric_coords():
    line = "turn on a,b through 2,2"
    with pytest.raises(ValueError):
        InstructionParser.parse(line)
