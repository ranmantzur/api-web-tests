import requests
import json


def get_available_pets():
    """
    A function that returns all the available pets
    :return: all available pets
    """
    url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
    response = requests.request("GET", url)
    all_available_pets = response.json()
    return all_available_pets


def get_pet_id_from_available_pets():
    """
    A functions that returns a single pet ID, from all available pets
    :return: ID of a pet
    """
    all_available_pets = get_available_pets()
    pet_id = all_available_pets[0]['id']
    return pet_id


def get_pet_by_id(pet_id):
    """
    A function that gets a pet ID, and returns the pet itself and the response of it
    :param pet_id:
    :return: pet, response
    """
    url = f'https://petstore.swagger.io/v2/pet/{pet_id}'
    response = requests.request("GET", url)
    pet = response.json()
    return pet, response

def post_new_animal():
    """
    Adding a new pet to the store
    :return: The new pet added, new pet response status code
    """
    url = "https://petstore.swagger.io/v2/pet"

    payload = json.dumps({
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "fish",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    new_pet = response.json()
    new_pet_status_code = response.status_code
    return new_pet, new_pet_status_code










