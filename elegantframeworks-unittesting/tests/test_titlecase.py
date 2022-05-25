from titlecase import title_case
from pytest import mark


@mark.unit
class TitleCaseTests:
    def test_lowercased_text_is_uppercased_as_expected(self):
        input_string = 'this is test string'
        expected_output = 'This Is Test String'
        actual_result = title_case(input_string)
        assert expected_output == actual_result

