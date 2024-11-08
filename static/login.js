document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("form").onsubmit = function () {
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      if (!email || !password) {
          alert("Please fill in both fields.");
          return false;  
      }

      return true; 
  };
});
