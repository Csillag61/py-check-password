from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_too_short_password() -> None:
    assert check_password("Str@ng") is False  # 7 characters


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
