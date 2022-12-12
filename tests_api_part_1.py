from methods_api_part_1 import *


def test_get_endpoint():
    """
    Checks 'all_available_pets' is not NULL : Assert True
    Checks 'pet_id' is equaled to the pet's object id : Assert Success
    Checks the response status code is 200 and status is ok (True) : Assert Success
    Checks the 'pet' is in 'all_available_pets' Assert True
    """
    all_available_pets = get_available_pets()
    assert all_available_pets, f'Expected to get True, Instead got False'
    pet_id = get_pet_id_from_available_pets()
    pet, response = get_pet_by_id(get_pet_id_from_available_pets())
    assert pet_id == pet["id"], f'Expected to get {pet_id}, Instead got {pet["id"]}'
    assert response.status_code == 200, f'Expected to get 200, Instead got {response.status_code}'
    assert response.ok, f'Expected to get True, Instead got False'
    assert pet in all_available_pets, f'Expected to get True, Instead got False'


def test_post_endpoint():
    """
    Checks 'new_pet' is not NULL : Assert True
    Checks 'new_pet' added status code is 200 and status is ok (True) : Assert Success
    Checks that the 'new_pet' that was added now, is in 'all_available_pets' :  Assert Success
    Checks using the function of 'get_pet_by_id' with the new pet ID, The ID equals and the pet exists : Assert Success
    Checks the response status code is 200 and status is ok (True) : Assert Success
    """
    new_pet, new_pet_status_code = post_new_animal()
    assert new_pet, f'Expected to get True, Instead got False'
    assert new_pet_status_code == 200, f'Expected to get 200, Instead got {new_pet_status_code}'

    all_available_pets = get_available_pets()
    assert new_pet in all_available_pets, f'Expected to get True, Instead got False'

    pet, response = get_pet_by_id(new_pet["id"])
    assert pet["id"] == new_pet["id"], f'Expected to get {pet["id"]}, Instead got {new_pet["id"]}'
    assert response.status_code == 200, f'Expected to get 200, Instead got {response.status_code}'
    assert response.ok, f'Expected to get True, Instead got False'