import pytest


@pytest.mark.parametrize(
    'value,i',
    range(10)
)
def test_multi_param_stuff(value):
    assert 0 == value
