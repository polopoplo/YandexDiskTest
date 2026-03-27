from utils.api import get_headers, get_resources


def test_get_responces():
    response = get_resources("/")

    try:
        assert response.status_code == 200
        print("\nУспешно!!!")
    except AssertionError:
        print(f"\nПровал(: причина {response.status_code})")
        raise