var counties = [
    "Alameda", "Alpine", "Amador", "Butte", "Calaveras", "Colusa", "Contra Costa", "Del Norte", "El Dorado", "Fresno",
    "Glenn", "Humboldt", "Imperial", "Inyo", "Kern", "Lake", "Los Angeles", "Madera", "Marin", "Mariposa",
    "Mendocino", "Merced", "Mono", "Monterey", "Napa", "Nevada", "Orange", "Placer", "Plumas", "Riverside", "Sacramento",
    "San Benito", "San Bernardino", "San Diego", "San Francisco", "San Joaquin", "San Luis Obispo", "San Mateo",
    "Santa Barbara", "Santa Clara", "Santa Cruz", "Shasta", "Solano", "Sonoma", "Stanislaus", "Sutter", "Tehama", 
    "Trinity", "Tulare", "Tuolumne", "Ventura", "Yolo"]

function renderMaps(accessToken, parks) {
    console.log(parks)
    mapboxgl.accessToken = accessToken;
    var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/canadiancaitlin/ckgr5t4nz00dd19pacacljg37', // stylesheet location
        center: [-121.686426, 36.550845], // starting position [lng, lat] (center of coastal CA)
        zoom: 6 // starting zoom
    });

    for (const park of parks) {
        var marker = new mapboxgl.Marker({color: '#e9c46a'})
        .setLngLat([park.longitude, park.latitude])
        .setPopup(new mapboxgl.Popup().setHTML(park.title))
        .addTo(map);
    }
}