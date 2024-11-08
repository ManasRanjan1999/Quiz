let timeLeft = 10 * 60;

function updateTimerDisplay() {
  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;
  document.getElementById("timer").textContent = 
    `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function startTimer() {
  const timerInterval = setInterval(() => {
    timeLeft--;
    updateTimerDisplay();

    if (timeLeft <= 0) {
      clearInterval(timerInterval);
      document.getElementById("quizForm").submit(); 
    }
  }, 1000);
}

document.addEventListener("DOMContentLoaded", function () {
  const radios = document.querySelectorAll(".option-radio");

  radios.forEach((radio) => {
    radio.addEventListener("change", (e) => {
      const questionId = e.target.name;
      const questionNavButton = document.querySelector(
        `[data-question-id="question${questionId}"]`
      );

      
      if (e.target.checked) {
        questionNavButton.classList.add("attempted");
      } else {
        questionNavButton.classList.remove("attempted");
      }
    });

   
    radio.addEventListener("dblclick", (e) => {
      if (e.target.checked) {
        e.target.checked = false;
        const questionId = e.target.name;
        const questionNavButton = document.querySelector(
          `[data-question-id="question${questionId}"]`
        );
        questionNavButton.classList.remove("attempted");
      }
    });
  });
});

window.onload = startTimer;
