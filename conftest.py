import pytest
import json
data_path = "dummy_json_data.json" # Add your file path

def data_func(path):
    with open(path,'r') as fd:
        data = json.load(fd)
        return data

@pytest.fixture(params=data_func(data_path))
def data_driven_json(request):
    return request.param