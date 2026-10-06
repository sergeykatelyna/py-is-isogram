from app.main import is_isogram


class TestIsIsogramPositive:
    def test_should_pass_unique_letters(self) -> None:
        assert (
            is_isogram("playgrounds")
        ), "Function should pass unique letters"

    def test_should_pass_empty_string(self) -> None:
        assert (
            is_isogram("")
        ), "Function should pass empty string"


class TestIsIsogramNegative:
    def test_should_detect_duplicate_letters(self) -> None:
        assert (
            not is_isogram("look")
        ), "Function should not allow duplicated chars"

    def test_should_be_case_insensitive(self) -> None:
        assert (
            not is_isogram("Adam")
        ), "Function should be case insensitive"
