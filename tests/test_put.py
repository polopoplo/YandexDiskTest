from utils.api import create_folder, get_resources


def test_create_folder(folder_name):
    response = create_folder(folder_name)

    assert response.status_code == 201
    print("\nПапка создана")

    check_folder = get_resources(folder_name)



    assert check_folder.status_code == 200

    print(f"\nПапка существует")