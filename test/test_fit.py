import pytest
from models.fit import Cardio, Gym, Exercise

def test_cardio_initialization():
    c = Cardio(stage=1, body=3, sex=0, sessions=4, time=30)
    assert c.stage == 1
    assert c.body == 3
    assert c.sex == 0
    assert c.sessions == 4
    assert c.time == 30

def test_gym_initialization():
    g = Gym(day="Monday", exercise="Squats", sets=3, reps=12)
    assert g.day == "Monday"
    assert g.exercise == "Squats"
    assert g.sets == 3
    assert g.reps == 12

def test_exercise_initialization_and_methods():
    e = Exercise(
        id=101,
        name="Push-Up",
        link="http://example.com/pushup",
        overview="Strengthens chest;Improves core",
        introductions="Start in plank;Lower body;Push up"
    )

    # Check attributes
    assert e.id == 101
    assert e.name == "Push-Up"
    assert e.link == "http://example.com/pushup"

    # Check method outputs
    overview = e.get_overview_paragraph()
    intro = e.get_introductions_detail()

    assert isinstance(overview, list)
    assert len(overview) == 2
    assert overview[0] == "Strengthens chest"

    assert isinstance(intro, list)
    assert "Lower body" in intro