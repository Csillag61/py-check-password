from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_too_short_password() -> None:
    assert check_password("Str@ng") is False  # 6 characters


def test_min_length_edge_case() -> None:
    # These have all requirements (upper, digit, special) but are too short
    assert check_password("A1@bcde") is False  # 7 characters
    assert check_password("Pass@1!") is False  # 7 characters
    assert check_password("B2#cdef") is False  # 7 characters
    assert check_password("C3$defg") is False  # 7 characters


def test_max_length_with_all_requirements() -> None:
    # This has all requirements but is too long
    assert check_password("A1@bcdefghijklmnop") is False  # 17 characters


def test_no_uppercase_with_good_length() -> None:
    # Good length, has digit and special, but no uppercase
    assert check_password("pass@word1") is False  # 10 characters


def test_no_digit_with_good_length() -> None:
    # Good length, has uppercase and special, but no digit
    assert check_password("Pass@word") is False  # 9 characters


def test_no_special_with_good_length() -> None:
    # Good length, has uppercase and digit, but no special character
    assert check_password("Password1") is False  # 9 characters


def test_too_long_password() -> None:
    assert check_password("ThisIsWayTooLong@123") is False  # 20 characters


def test_missing_uppercase() -> None:
    assert check_password("pass@word1") is False


def test_missing_digit() -> None:
    assert check_password("Pass@word") is False


def test_missing_special_char() -> None:
    assert check_password("Password1") is False


def test_invalid_character() -> None:
    assert check_password("Pass@word1🙂") is False  # Emoji not allowed


def test_boundary_min_length_valid() -> None:
    assert check_password("A1@bcdef") is True  # 8 characters


def test_boundary_max_length_valid() -> None:
    assert check_password("A1@abcdefghijklm") is True  # 16 characters


def test_only_valid_special_chars() -> None:
    for char in "$@#&!-_":
        assert check_password(f"A1{char}bcdef") is True


def test_invalid_special_chars() -> None:
    for char in "*%^+=(){}[]":
        assert check_password(f"A1{char}bcdef") is False
