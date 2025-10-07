function showMessage() {
    alert("Semangat Belajar Web!");
}

var i = 0;
var txt = 'Saya Muhammad Ihsan';
var speed = 150;

function typeWrite() {
    if (i< txt.lenght) {
        document.getElementsById("demo").innerHTMl += txt.charAt(i);
        i++;
        setTimeout(typeWrite,speed);
    }
}


window.unload = function () {
    typeWrite();
};