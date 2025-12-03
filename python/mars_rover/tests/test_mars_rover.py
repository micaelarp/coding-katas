from python.mars_rover.mars_rover import MarsRover


def test_initial_position():
    rover = MarsRover(0, 0, "N")
    assert rover.execute("") == "0:0:N"


def test_rotate_right():
    rover = MarsRover(0, 0, "N")
    assert rover.execute("R") == "0:0:E"
    assert rover.execute("R") == "0:0:S"
    assert rover.execute("R") == "0:0:W"
    assert rover.execute("R") == "0:0:N"


def test_rotate_left():
    rover = MarsRover(0, 0, "N")
    assert rover.execute("L") == "0:0:W"
    assert rover.execute("L") == "0:0:S"
    assert rover.execute("L") == "0:0:E"
    assert rover.execute("L") == "0:0:N"


def test_move_forward():
    rover = MarsRover(0, 0, "N")
    assert rover.execute("M") == "0:1:N"
    assert rover.execute("M") == "0:2:N"


def test_wrap_around_north():
    rover = MarsRover(0, 9, "N")
    assert rover.execute("M") == "0:0:N"


def test_wrap_around_east():
    rover = MarsRover(9, 0, "E")
    assert rover.execute("M") == "0:0:E"


def test_obstacle_detection():
    rover = MarsRover(0, 0, "N", obstacles=[[0, 2]])
    assert rover.execute("MM") == "O:0:1:N"
