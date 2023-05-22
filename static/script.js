document.addEventListener("DOMContentLoaded", () => {
    // Get all section elements
    const sections = document.querySelectorAll("section");
  
    // Add click event listener to each nav link
    document.querySelectorAll(".nav-item").forEach((link) => {
      link.addEventListener("click", () => {
        // Get the ID of the section to scroll to
        const targetId = link.getAttribute("data-scroll");
  
        // Get the corresponding section element
        const targetSection = document.getElementById(targetId);
  
        // Scroll to the section
        targetSection.scrollIntoView();
  
        // Get the corresponding h2 element
        const targetHeading = targetSection.querySelector("h2");
  
        // Display the h2 element at the top of the page
        const header = document.querySelector(".site-header");
        const headerHeight = header.offsetHeight;
        window.scrollTo({
          top: targetHeading.offsetTop - headerHeight,
          behavior: "smooth",
        });
      });
    });
  });