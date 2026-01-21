 let coords = null;

    window.onload = () => { getLocation(); };

    function getLocation() {
        const status = document.getElementById('status-gps');
        const overlay = document.getElementById('overlay-gps');

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (pos) => {
                    coords = pos.coords;
                    status.innerHTML = `✅ Lokasi Berhasil Didapatkan`;
                    status.style.color = "green";
                    overlay.style.display = "none";
                },
                (err) => {
                    overlay.style.display = "flex";
                    status.innerHTML = "❌ Lokasi Gagal Didapatkan";
                    status.style.color = "red";
                },
                { enableHighAccuracy: true }
            );
        }
    }

    function switchTab(role) {
        if(role === 'mhs') {
            document.getElementById('form-mhs').classList.remove('hidden');
            document.getElementById('form-dsn').classList.add('hidden');
            document.getElementById('tab-mhs').classList.add('active');
            document.getElementById('tab-dsn').classList.remove('active');
            getLocation();
        } else {
            document.getElementById('form-mhs').classList.add('hidden');
            document.getElementById('form-dsn').classList.remove('hidden');
            document.getElementById('tab-dsn').classList.add('active');
            document.getElementById('tab-mhs').classList.remove('active');
            document.getElementById('overlay-gps').style.display = "none";
        }
    }

