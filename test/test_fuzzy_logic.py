import pytest
from algorithm.fuzzy_logic import FuzzyLogic
import numpy as np

def test_fuzzification_of_height_male_short():
    fl = FuzzyLogic()
    fl.do_fuzzification_of_height(155, 0)
    assert fl.fuzzy_sets_and_membership_values_of_height == {0: 1}

def test_fuzzification_of_height_female_medium():
    fl = FuzzyLogic()
    fl.do_fuzzification_of_height(155, 1)
    # Expect a combination of sets 0 and 1
    h = fl.fuzzy_sets_and_membership_values_of_height
    assert 0 in h and 1 in h
    assert np.isclose(h[0] + h[1], 1.0)

def test_fuzzification_of_weight_male_high():
    fl = FuzzyLogic()
    fl.do_fuzzification_of_weight(75, 0)
    assert fl.fuzzy_sets_and_membership_values_of_weight == {2: 1}

def test_fuzzification_of_weight_female_borderline():
    fl = FuzzyLogic()
    fl.do_fuzzification_of_weight(47.5, 1)
    w = fl.fuzzy_sets_and_membership_values_of_weight
    assert 0 in w and 1 in w
    assert np.isclose(w[0] + w[1], 1.0)

def test_fuzzy_inference_table_population():
    fl = FuzzyLogic()
    fl.do_fuzzification_of_height(160, 0)  # Should give sets 0 and 1
    fl.do_fuzzification_of_weight(55, 0)   # Should give sets 0 and 1
    fl.do_fuzzy_inference()
    mvt = fl.membership_values_table
    assert mvt.shape == (3, 3)
    assert np.any(mvt > 0)

def test_defuzzification_output():
    fl = FuzzyLogic()
    fl.do_fuzzification_of_height(160, 0)
    fl.do_fuzzification_of_weight(75, 0)
    fl.do_fuzzy_inference()
    decision = fl.do_defuzzification_of_body()
    assert isinstance(decision, int)
    assert 0 <= decision <= 4