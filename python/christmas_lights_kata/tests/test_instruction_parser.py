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
