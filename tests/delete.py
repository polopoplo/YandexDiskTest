import uuid
from utils.api import create_folder, delete_folder

def test_create_delete_folder():
    folder_name = f"test_create{uuid.uuid4()}"

    create_response = create_folder(folder_name)
    assert create_response.status_code == 201
    print("ПАПКА СОЗДАНА")

    delete_response = delete_folder(folder_name)
    assert delete_response.status_code in [202, 204]
    print("Папка удалена")


