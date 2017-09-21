var map;
function loadMapScenario() {
    map = new Microsoft.Maps.Map(document.getElementById('myMap'), {
        credentials: 'AiapA0N7GG69bA5HrgU1nDW_6tNIO7eELxRVdgecgfF7mRVeGPsAqon929HNsYvh'
    });
}


//1. define pokemon data format create pokemon data
map_manager.map_items = [
    {
      "pokemon_id" : 12,
      "expire" : 1476589403,
      "longitude" : -73.9800345,
      "latitude" : 40.7596651,
    }
]

//2. Create pokemon image on map
function get_pokemon_layer_from_map_items(map_items) {
    var layer = new Microsoft.Maps.Layer();
    return layer;
}
var pokemon_layer = get_pokemon_layer_from_map_items(map_items)
map.layers.insert(pokemon_layer)
//3. Add pokemon counter down refresh


//4. Connect with REST API


 var map;
                
                
