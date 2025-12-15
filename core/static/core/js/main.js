// Lucide icons
lucide.createIcons();

// Navbar scroll effect
const navbar = document.getElementById('navbar');
const navContainer = document.getElementById('nav-container');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navContainer.classList.add('bg-[#0A0F14]/80', 'backdrop-blur-xl');
    } else {
        navContainer.classList.remove('bg-[#0A0F14]/80', 'backdrop-blur-xl');
    }
});

// Reveal animation
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
