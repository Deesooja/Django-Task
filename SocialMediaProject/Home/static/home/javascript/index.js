// document.getElementById('btn').addEventListener('click', function(){

//     alert('index')
// })

function home_page_load() {

    fetch('http://127.0.0.1:8000/', {
        method: "GET",

        headers: {
            'Content-Type': 'application / json',
            'X-Requested-With': 'XMLHttpRequest',
        },

    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}