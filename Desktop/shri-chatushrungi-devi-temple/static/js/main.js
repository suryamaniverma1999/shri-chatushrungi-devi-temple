/* global document */
function toggleMenu() {
    var nav = document.getElementById("navLinks");
    if (nav) {
        nav.classList.toggle("show");
    }
}