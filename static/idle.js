console.log("hello")

// Define idle time in milliseconds (5 seconds in this example)
var idleTime = 300000; // 5 minute

// Variable to hold the timeout function
var idleTimer;

// Function to redirect to another page
function redirectToAnotherPage() {
  window.location.href = '/' // Replace "another-page.html" with your desired page
}

// Function to reset the idle timer
function resetIdleTimer() {
  clearTimeout(idleTimer);
  idleTimer = setTimeout(redirectToAnotherPage, idleTime);
}

// Event listeners to reset idle timer on user interaction
document.addEventListener("mousemove", resetIdleTimer);
document.addEventListener("keypress", resetIdleTimer);

// Start the idle timer
resetIdleTimer();