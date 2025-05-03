
document.addEventListener('DOMContentLoaded', function() {
    // Select the element where the status is displayed.
    const statusEl = document.getElementById('status');
  
    // Optionally, you could send a message to the background script to get dynamic status information.
    // For now, we'll simply update the status text to "Active".
    statusEl.textContent = 'Active';
  
    // Example: If you later add a button to refresh or check status,
    // you can attach an event listener to it like this:
    // document.getElementById('refreshButton').addEventListener('click', function() {
    //   // Code to refresh status or interact with the background script.
    // });
  });