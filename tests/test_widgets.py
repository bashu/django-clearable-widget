import pytest

from clearable_widget.widgets import ClearableInput


@pytest.mark.parametrize(
    ("value", "expected_input"),
    [
        pytest.param(
            "test",
            '<input type="text" name="field" value="test" id="id_field">',
            id="value",
        ),
        pytest.param(
            None,
            '<input type="text" name="field" id="id_field">',
            id="none",
        ),
        pytest.param(
            "<b>",
            '<input type="text" name="field" value="&lt;b&gt;" id="id_field">',
            id="escaped",
        ),
    ],
)
def test_render(value: str | None, expected_input: str) -> None:
    output = ClearableInput().render("field", value, {"id": "id_field"})

    assert output == (
        f'<div class="clear-holder">{expected_input}'
        '<span class="clear-helper hidden">X</span></div>\n'
    )
