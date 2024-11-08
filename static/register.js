document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("form").onsubmit = function () {
      const password = document.getElementById("password").value;
      const confirmPassword = document.getElementById("confirmPassword").value;
      const phone = document.getElementById("phone").value;
      const phonePattern = /^[0-9]{10}$/;

      if (!phonePattern.test(phone)) {
          alert("Please enter a valid 10-digit phone number.");
          return false; 
      }

     
      if (password !== confirmPassword) {
          alert("Passwords do not match.");
          return false; 
      }

      return true; 
  };
});
