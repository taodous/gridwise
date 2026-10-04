import pytest

from gridwise import main


def test_print(capsys: pytest.CaptureFixture[str]) -> None:
    main()

    captured = capsys.readouterr()

    assert captured.out == "Hello from gridwise!\n"
