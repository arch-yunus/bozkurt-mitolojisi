document.addEventListener('DOMContentLoaded', () => {
    // Simulated Lore Data (In a real app, this would be fetched from the Data API / JSON files)
    const loreData = [
        {
            "kavram": "Gökbörü",
            "kaynak": "Oğuz Kağan Destanı",
            "analiz": "Işık içerisinden çıkan ilahi rehber. Stratejik keşif ve ordu yönetiminde navigasyonel bir veri kaynağı.",
            "kategori": "Navigasyon ve Rehberlik"
        },
        {
            "kavram": "Ergenekon Bozkurtu",
            "kaynak": "Ergenekon Destanı",
            "analiz": "Sıkışmış bir toplumu özgürlüğe taşıyan çıkış algoritması. Demir dağın eritilmesinin ardından beliren rehber.",
            "kategori": "Kurtarıcı ve Yol Gösterici"
        },
        {
            "kavram": "Türeyiş Kurdu",
            "kaynak": "Türeyiş Destanı",
            "analiz": "Soyun ilahi ve güçlü bir kökene dayandırılması. Tanrı'nın kurt suretinde yeryüzüne inerek soyu başlatması.",
            "kategori": "Ontoloji ve Köken"
        }
    ];

    const container = document.getElementById('lore-container');
    
    if (container) {
        container.innerHTML = ''; // Clear loader
        
        loreData.forEach(item => {
            const card = document.createElement('div');
            card.className = 'lore-card fade-in';
            card.innerHTML = `
                <span class="meta">${item.kategori} | ${item.kaynak}</span>
                <h3>${item.kavram}</h3>
                <p>${item.analiz}</p>
            `;
            container.appendChild(card);
        });
    }

    // Smooth Scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Scroll Reveal Animation (Simple)
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.section').forEach(section => {
        observer.observe(section);
    });
});
