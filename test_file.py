import pytest

@pytest.mark.ddt_func
def test_ddt(data_driven_json):
    d1 = data_driven_json['name']
    d2 = data_driven_json['age']
    print(f"My Name is {d1}, and my age is {d2}")