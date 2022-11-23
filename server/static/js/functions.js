// This allow to clear the body div and request other html
// from another endpoint of the web and we can still have
// the header and the music player on the bottom of the page

function hrefClickHome() {
    $.ajax({
        url: '/',
        timeout: 5000,
        type: 'GET',
        headers: {'Ajax-Render': true},
        success: function(msg, status) {
            console.log(status);
            if(status == 'success') {
                history.replaceState('','','/');
                console.log("url: /");
                $('#body-container').html(msg);
            }
            document.title = 'WYG - Home';
        }
    })
}

function hrefClickUser() {
    $.ajax({
        url: '/user/',
        timeout: 5000,
        type: 'GET',
        headers: {'Ajax-Render': true},
        success: function(msg, status) {
            console.log(status);
            if(status == 'success') {
                history.replaceState('','','/user/');
                console.log("url: /user/");
                $('#body-container').html(msg);
            }
            document.title = 'WYG - User profile';
        }
    })
}

function formClickSearch() {
    var search_text = document.getElementById('search-form-input-search').value;
    console.log("/search/?search=" + search_text);
    $.ajax({
        url: "/search/",
        timeout: 5000,
        type: 'GET',
        arguments: {"search": search_text},
        headers: {'Ajax-Render': true},
        success: function(msg, status) {
            console.log(msg);
            console.log(status);
            if(status == 'success') {
                history.replaceState('','','/search/');
                console.log("url: /search/" + search_text);
                $('#body-container').html(msg);
            }
            document.title = 'WYG - Search ' + search_text;
        }
    })
}