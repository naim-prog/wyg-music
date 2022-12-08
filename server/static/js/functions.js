// This allow to clear the body div and request other html
// from another endpoint of the web and we can still have
// the header and the music player on the bottom of the page

window.htmx = require('htmx.org');

window.onload = function() {
}

function songHolderODrag(evt) {
    evt.preventDefault();
};

function songHolderODrop(evt) {
    // pretty simple -- but not for IE :(
    fileInput.files = evt.dataTransfer.files;

    // If you want to use some of the dropped files
    const dT = new DataTransfer();
    dT.items.add(evt.dataTransfer.files[0]);
    dT.items.add(evt.dataTransfer.files[3]);
    fileInput.files = dT.files;

    evt.preventDefault();
};

function uploadFiles() {
    var files = document.getElementById('file_upload').files;
    if(files.length==0){
        alert("Please first choose or drop any file(s)...");
        return;
    }
    var filenames="";
    for(var i=0;i<files.length;i++){
        filenames+=files[i].name+"\n";
    }
    alert("Selected file(s) :\n____________________\n"+filenames);
}