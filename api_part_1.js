const request = require('request');
const json = require('json');

/*
    A function that returns all the available pets
    return: all available pets
*/
function getAvailablePets() {
  const getAvailablPetsUrl = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available';
  const response = request.request('GET', getAvailablPetsUrl);
  const allAvailablePetsRes = response.json();
  return allAvailablePetsRes;
}

function getPetIdFromAvailablePets() {
  const allAvailablePets = getAvailablePets();
  const petId = allAvailablePets[0]['id'];
  return petId;
}

function getPetById(petId) {
  const getPetUrl = `https://petstore.swagger.io/v2/pet/${petId}`;
  const response = request.request('GET', getPetUrl);
 return response;
}

function postNewAnimal() {
  const url = 'https://petstore.swagger.io/v2/pet';

  const payload = {
    id: 0,
    category: {
      id: 0,
      name: 'string',
    },
    name: 'fish',
    photoUrls: [
      'string',
    ],
    tags: [
      {
        id: 0,
        name: 'string',
      },
    ],
    status: 'available',
  };

  const headers = {
    'Content-Type': 'application/json',
  };

  const response = request.request('POST', url, { headers, data: payload });

  const newPet = response.json();
  const newPetStatusCode = response.statusCode;
  return [newPet, newPetStatusCode];
}

function testGetEndpoint() {
  const allAvailablePets = getAvailablePets();
  if (!allAvailablePets) throw new Error(`Expected to get True, Instead got False`);
  const petId = getPetIdFromAvailablePets();
  const [pet, response] = getPetById(getPetIdFromAvailablePets());
  if (petId !== pet['id'])
    throw new Error(`Expected to get ${petId}, Instead got ${pet['id']}`);
  if (response.statusCode !== 200)
    throw new Error(`Expected to get 200, Instead got ${response.statusCode}`);
  if (!response.ok) throw new Error(`Expected to get True, Instead got False`);
  if (!allAvailablePets.includes(pet))
    throw new Error(`Expected to get True, Instead got False`);
}

function testPostEndpoint() {
  const [newPet, newPetStatusCode] = postNewAnimal();
  if (!newPet) throw new Error(`Expected to get True, Instead got False`);
  if (newPetStatusCode !== 200)
    throw new Error(`Expected to get 200, Instead got ${newPetStatusCode}`);
  if (!newPet.ok) throw new Error(`Expected to get True, Instead got False`);
  const allAvailablePets = getAvailablePets

  const request = require('request');
const { expect } = require('chai');
