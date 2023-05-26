
document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.querySelector(".navbar");
  const menuButton = document.querySelector(".navbar-toggler");
  const navLinks = document.querySelectorAll(".nav-item");

  // Add click event listener to the menu button
  menuButton.addEventListener("click", () => {
    navbar.classList.toggle("show");
  });

  // Add click event listener to each nav link
  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      navbar.classList.remove("show");
    });
  });
});