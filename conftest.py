import pytest, uuid

@pytest.fixture
def folder_name():
    return f"test_folder_{uuid.uuid4()}"