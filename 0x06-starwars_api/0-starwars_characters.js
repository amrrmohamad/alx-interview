#!/usr/bin/node

const axios = require('axios');

async function getCharacters(movieId) {
  try {
    const movieResponse = await axios.get('https://swapi-api.hbtn.io/api/films/' + movieId);
    const actors = movieResponse.data.characters;

    for (const actorUrl of actors) {
      const actorResponse = await axios.get(actorUrl);
      console.log(actorResponse.data.name);
    }
  } catch (error) {
    console.error(error);
  }
}

getCharacters(process.argv[2]);
