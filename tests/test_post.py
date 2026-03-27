from utils.api import create_folder, public

def test_public_folder(folder_name):


    create = create_folder(folder_name)
    assert create.status_code == 201

    print("\nПапка создана")

    public_folder = public(folder_name)
    assert public_folder.status_code in [200, 201, 202, 203]

    print("\nПапка стала публичной")