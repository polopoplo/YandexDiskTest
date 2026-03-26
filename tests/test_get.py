from utils.api import get_headers, get_resources


def test_get_responces():
    response = get_resources("/")

    try:
        assert response.status_code == 200
        print("Успешно!!!")
    except AssertionError:
        print(f"Провал(: причина {response.status_code})")
        raise