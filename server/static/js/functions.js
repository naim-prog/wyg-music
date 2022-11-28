// This allow to clear the body div and request other html
// from another endpoint of the web and we can still have
// the header and the music player on the bottom of the page

window.onload = function() {
}


function hrefClickHome() {
    $.ajax({
        url: '/',
        timeout: 5000,
        type: 'GET',
        headers: {'Ajax-Render': true},
        success: function(msg, status) {
            if(status === 'success') {
                history.replaceState('','','/');
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
            if(status === 'success') {
                history.replaceState('','','/user/');
                $('#body-container').html(msg);
            }
            document.title = 'WYG - User profile';
        }
    })
}


function hrefSearch(event) {
    if(event.keyCode == 13) {
        var query = document.getElementById("search-form-input-search").value;
        $.ajax({
            url: '/search/?search='+query,
            timeout: 5000,
            type: 'GET',
            headers: {'Ajax-Render': true},
            success: function(msg, status) {
                if(status === 'success') {
                    history.replaceState('','','/search/?search='+query);
                    $('#body-container').html(msg);
                }
                document.title = 'WYG - Search '+query;
            }
        })
        return true;
    } else {
        return false;
    }
}
