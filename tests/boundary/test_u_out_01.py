from _approval import assert_matches_golden
from unitconverter.boundary.output_presenter import OutputPresenter


def test_u_out_01_length_output():
    # Given
    raw_input = "meter:2.5"
    presenter = OutputPresenter()

    # When
    actual = presenter.present(raw_input)

    # Then
    assert_matches_golden(actual, "golden/u_out_01_length_output.approved.txt")
