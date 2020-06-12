function openDropdown() {
    document.getElementById("dropdown").classList.toggle("show");
}
// When the user clicks anywhere outside of the modal, close it
// Close the dropdown if the user clicks outside of it
window.addEventListener('click', function(event) {
    if (!event.target.matches('.dropButton')) {
        let dropdowns = document.getElementsByClassName("dropdown-content");
        let i;
        for (i = 0; i < dropdowns.length; i++) {
            let openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
});