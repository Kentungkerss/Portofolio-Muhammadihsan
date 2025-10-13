function showMessage() {
    alert("HALO APA KABAR?!! ")
}

var i = 0;
var txt = 'Saya Muhammad Ihsan';
var speed = 150;

function typerWrite() {
    if (i < txt.length) {
        document.getElementById("demo").innerHTML += txt.charAt(i);
    i++
    setTimeout(typerWrite, speed);
    }
}

window.onload = function() {
    typerWrite();
}