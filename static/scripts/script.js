
setTimeout(function() {
    const button = document.getElementById('portfolio-btn');
    button.style.opacity = '1'; // Make the button fully visible
    button.style.visibility = 'visible'; // Make it visible
    button.style.transition = 'opacity 0.5s ease'; // Smooth transition
    }, 1700); // Show button after the complete animation

// Function to update the visitor count
function updateVisitorCount() {
    // Get the current count from local storage or set it to 0 if it doesn't exist
    let count = parseInt(localStorage.getItem('visitorCount')) || 0;

    // Increment the count
    count++;

    // Store the updated count back in local storage
    localStorage.setItem('visitorCount', count);

    // Log the count to the console or update the UI as needed
    console.log(`Visitor count: ${count}`);
}

// Add event listener to the button for the portfolio navigation
document.getElementById('portfolio-btn').addEventListener('click', function() {
    updateVisitorCount();
    // Redirect to the portfolio page (replace 'portfolio.html' with your actual URL)
    window.location.href = 'portfolio.html';
});

// Display the current visitor count on page load
window.onload = function() {
    const count = localStorage.getItem('visitorCount') || 0;
    document.getElementById('visitorCountDisplay').textContent = count;
};
