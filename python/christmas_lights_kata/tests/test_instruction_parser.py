import pytest
from python.christmas_lights_kata.src.instruction_parser import InstructionParser

def test_parse_command_success():
    line = "turn on 10,20 through 30,40"
    action, start, end = InstructionParser.parse(line)
    assert action == "on"
    assert start == (10, 20)
    assert end == (30, 40)

def test_parse_command_invalid_raises():
    with pytest.raises(ValueError):
        InstructionParser.parse("invalid command line")

