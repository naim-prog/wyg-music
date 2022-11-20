// This allow to clear the body div and request other html
// from another endpoint of the web and we can still have
// the header and the music player on the bottom of the page
function clearHTMLandLoad(endpoint) {
    $("#body-container").load(endpoint);
}