// Konfirmasi sebelum hapus data
document.addEventListener('DOMContentLoaded', function() {
    const linkHapus = document.querySelectorAll('a[href^="/hapus"]');
    linkHapus.forEach(link => {
        link.addEventListener('click', function(e) {
            if (!confirm('Yakin ingin menghapus data ini?')) {
                e.preventDefault();
            }
        });
    });
});