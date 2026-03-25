import uuid
from utils.api import create_folder, public

def test_public_folder():

    folder_name = f"test_folder{uuid.uuid4()}"

    create = create_folder(folder_name)
    assert create.status_code == 201

    print("Папка создана")

    public_folder = public(folder_name)
    assert public_folder.status_code in [200, 201, 202, 203]

    print("Папка стала публичной")