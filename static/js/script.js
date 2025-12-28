// Dark mode toggle
const toggleBtn = document.createElement('button');
toggleBtn.textContent = "Toggle Dark Mode";
toggleBtn.classList.add('dark-toggle');
document.body.appendChild(toggleBtn);

toggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});
