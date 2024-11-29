// static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    // Add any global JavaScript functionality here
});

// Example: Countdown timer for auctions
function startCountdown(endTime) {
    const countdownElement = document.getElementById('countdown');
    
    function updateCountdown() {
        const now = new Date().getTime();
        const timeLeft = endTime - now;

        if (timeLeft < 0) {
            countdownElement.innerHTML = 'Auction ended';
        } else {
            const hours = Math.floor(timeLeft / (1000 * 60 * 60));
            const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

            countdownElement.innerHTML = `${hours}h ${minutes}m ${seconds}s`;
            setTimeout(updateCountdown, 1000);
        }
    }

    updateCountdown();
}

// Use this function in your auction detail template:
// startCountdown(new Date("{{ auction.end_time|date:'c' }}").getTime());