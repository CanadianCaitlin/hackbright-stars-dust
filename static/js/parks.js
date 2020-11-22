
function renderMaps(accessToken, parks) {
    console.log(parks)
    mapboxgl.accessToken = accessToken;
    var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/canadiancaitlin/ckgr5t4nz00dd19pacacljg37', // stylesheet location
        center: [-119.25046, 36.778259], // starting position [lng, lat] (center of coastal CA)
        zoom: 5 // starting zoom
    });

    for (const park of parks) {
        var marker = new mapboxgl.Marker({color: '#e9c46a'})
        .setLngLat([park.longitude, park.latitude])
        .setPopup(new mapboxgl.Popup().setHTML(park.title))
        .addTo(map);
    }
}