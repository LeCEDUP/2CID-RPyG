const fetchPokemon = async () => {
    const pokemonInput = window.document.getElementById('pokemon-input').value;
    const URL = `https://pokeapi.co/api/v2/pokemon/${pokemonInput}`;
    
    try {
        let pokemon = await fetch(URL);
        let pokemonData = await pokemon.json();
        
        const img = window.document.getElementById('pokemon-sprite');
        img.src = pokemonData.sprites.front_default;
        img.style.display = 'block';
    } catch (error) {
        console.error('O erro que deu foi: ', error.message)
    }
};

const fetchAllPokemon = async () => {
    const URL = `https://pokeapi.co/api/v2/pokemon/?limit=151`;
    let allPokemons = await fetch(URL);
    let allPokemonsData = await allPokemons.json();

    const listaPokemon = window.document.getElementById('lista-151');
    allPokemonsData.results.forEach((pokemon) => {
        const linha = window.document.createElement('li');
        linha.innerText = pokemon.name;
        listaPokemon.appendChild(linha);
    });
};

window.onload = fetchAllPokemon()
const searchButton = window.document.getElementById('search');        
searchButton.addEventListener('click', fetchPokemon);