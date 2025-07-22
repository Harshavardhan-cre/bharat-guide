document.getElementById('filterForm').addEventListener('submit', async function(e) {
  e.preventDefault();

  const formData = new FormData(this);
  const userInput = Object.fromEntries(formData.entries());

  const response = await fetch('/filter', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(userInput)
  });

  const data = await response.json();

  const results = document.getElementById('results');
  results.innerHTML = '<h3>Matching Schemes:</h3>' + data.map(s => `<p>${s.name}</p>`).join('');
});
