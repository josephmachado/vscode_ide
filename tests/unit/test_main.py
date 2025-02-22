from main import get_fake_data


def test_get_fake_data():
    result_data = get_fake_data(input_param="some_param")
    expected_data = [(1,)]
    assert result_data == expected_data
