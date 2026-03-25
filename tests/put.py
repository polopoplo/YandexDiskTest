import uuid
from utils.api import create_folder



def test_create_folder():
    folder_name = f"test_folder{uuid.uuid4()}"
    response = create_folder(folder_name)

    if response.status_code == 201:
        print("Папка создана")

    else:
        print(f"Ошибка создания папки: {response.status_code}")

    assert response.status_code == 201