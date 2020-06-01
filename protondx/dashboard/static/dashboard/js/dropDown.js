function openDropdown() {
    document.getElementById("dropdown").classList.toggle("show");
}
const modal = document.getElementById("myModal");


// When the user clicks anywhere outside of the modal, close it
// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    else if (!event.target.matches('.dropButton')) {
        let dropdowns = document.getElementsByClassName("dropdown-content");
        let i;
        for (i = 0; i < dropdowns.length; i++) {
            let openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}
