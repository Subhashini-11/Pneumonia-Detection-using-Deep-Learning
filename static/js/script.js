// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Handle file input preview
  const fileInput = document.getElementById("formFile");
  if (fileInput) {
    fileInput.addEventListener("change", function (event) {
      const file = event.target.files[0];
      if (file) {
        // Create preview container if it doesn't exist
        let previewContainer = document.getElementById("imagePreview");
        if (!previewContainer) {
          previewContainer = document.createElement("div");
          previewContainer.id = "imagePreview";
          previewContainer.className = "mt-3 text-center";
          fileInput.parentNode.appendChild(previewContainer);
        }

        // Show selected file name
        const fileName = document.createElement("p");
        fileName.textContent = `Selected file: ${file.name}`;

        // Create image preview
        const reader = new FileReader();
        reader.onload = function (e) {
          const preview = document.createElement("img");
          preview.src = e.target.result;
          preview.className = "img-fluid mt-2 rounded border";
          preview.style.maxHeight = "300px";

          // Clear previous content and add new elements
          previewContainer.innerHTML = "";
          previewContainer.appendChild(fileName);
          previewContainer.appendChild(preview);
        };
        reader.readAsDataURL(file);
      }
    });
  }

  // Handle form submission
  const uploadForm = document.querySelector('form[action*="upload_file"]');
  if (uploadForm) {
    uploadForm.addEventListener("submit", function (event) {
      const fileInput = document.getElementById("formFile");
      if (fileInput && fileInput.files.length > 0) {
        // Show loading indicator
        const submitBtn = uploadForm.querySelector('button[type="submit"]');
        const originalContent = submitBtn.innerHTML;
        submitBtn.innerHTML =
          '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Analyzing...';
        submitBtn.disabled = true;

        // Let the form submit normally
      } else {
        // Prevent form submission if no file selected
        event.preventDefault();
        alert("Please select an image file to upload.");
      }
    });
  }

  // Initialize tooltips
  const tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // Add smooth scrolling to all links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();

      const targetId = this.getAttribute("href");
      if (targetId === "#") return;

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    });
  });

  // Auto-dismiss alerts after 5 seconds
  const alerts = document.querySelectorAll(
    ".alert:not(.alert-warning):not(.alert-danger)"
  );
  alerts.forEach((alert) => {
    setTimeout(() => {
      const bsAlert = new bootstrap.Alert(alert);
      bsAlert.close();
    }, 5000);
  });

  // Enable animations for elements when they come into view
  const animateOnScroll = function () {
    const elements = document.querySelectorAll(".animate-on-scroll");
    elements.forEach((element) => {
      const elementPosition = element.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;

      if (elementPosition < windowHeight - 50) {
        element.classList.add("animated");
      }
    });
  };

  // Add scroll event listener for animation
  if (document.querySelectorAll(".animate-on-scroll").length > 0) {
    window.addEventListener("scroll", animateOnScroll);
    // Trigger once on load
    animateOnScroll();
  }
});
