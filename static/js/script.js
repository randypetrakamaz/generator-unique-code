const btnMenu = document.getElementById('btn_menu');
const sidebarLayout = document.getElementById('sidebar_layout');
const mainLayout = document.getElementById('main_layout');

btnMenu.addEventListener('click', () => {
    console.log('masukk')
    sidebarLayout.classList.toggle('visually-hidden');
    mainLayout.classList.toggle('w-100');
});

const generatedBtn = document.getElementById('generate_btn')

generatedBtn.addEventListener("click", function() {
    console.log('masuk') // Debugging

    const formData = new FormData(document.getElementById("form1"));
    fetch("/generate-code", {
        method: "POST",
        body: new URLSearchParams(formData),  // Mengirim data form sebagai URLSearchParams
    })
    .then(response => response.json())  // Menangani response sebagai JSON
    .then(data => {
        document.getElementById("hasil").textContent = data.code;
    })
    .catch(error => {
        alert("An error occurred: " + error);
    });
});
