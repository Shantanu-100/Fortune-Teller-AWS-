document.getElementById('fortune-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const question = document.getElementById('question').value;

    try {
        const response = await fetch(`<YOUR API GATEWAY>/API-STAGE?question=${encodeURIComponent(question)}`);
        const data = await response.json();

        document.getElementById('fortune-text').textContent = data.fortune;
        document.getElementById('fortune-result').classList.remove('hidden');
    } catch (error) {
        console.error('Error fetching fortune:', error);
        alert('An error occurred while fetching your fortune. Please try again later.');
    }
});
