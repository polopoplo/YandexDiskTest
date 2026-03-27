from utils.api import create_folder, delete_folder, get_resources

def test_create_delete_folder(folder_name):

    create_response = create_folder(folder_name)
    assert create_response.status_code == 201
    print("\nПАПКА СОЗДАНА")



    get_response = get_resources(folder_name)
    assert get_response.status_code == 200 #папка существует

    delete_response = delete_folder(folder_name)
    assert delete_response.status_code in [202, 204]
    print("\nПроверили что папка существукт и удалили ее")


    check_folder = get_resources(folder_name)
    assert check_folder.status_code == 404
    print("\nпапка точно удалена")

####################################################
def test_bad_request():
    response = create_folder("")

    assert response.status_code == 400
    print("\nнормально обработали запрос")

####################################################
def test_existing_folder():
    folder_name = "test"
    create_folder(folder_name)

    response = create_folder(folder_name)

    assert response.status_code == 409

    print("\n" + response.text)
    print(f"Ожидали 409, получили {response.status_code}")










