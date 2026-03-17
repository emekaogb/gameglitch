from logic_utils import check_guess, get_range_for_difficulty, parse_guess

# Bug: Normal and Hard ranges were swapped
def test_normal_difficulty_range():
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_hard_difficulty_range():
    assert get_range_for_difficulty("Hard") == (1, 100)


# Bug: parse_guess had no range validation
def test_parse_guess_above_range():
    ok, _, err = parse_guess("101", 1, 100)
    assert not ok
    assert err == "That number is not in range."

def test_parse_guess_below_range():
    ok, _, err = parse_guess("0", 1, 100)
    assert not ok
    assert err == "That number is not in range."

def test_parse_guess_in_range():
    ok, value, _ = parse_guess("50", 1, 100)
    assert ok
    assert value == 50


# Bug: check_guess hints were backwards (Too High said Go HIGHER, Too Low said Go LOWER)
def test_check_guess_too_high_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_check_guess_too_low_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
