
// fetch('https://api.example.com/data', {
//     method: "GET",

// headers: {
// 'Content-Type': 'application / json',
// 'X-Requested-With': 'XMLHttpRequest',
// "X-CSRFToken": form.elements.csrf_token.value
// },

// })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data);
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });

document.getElementById('name').addEventListener('click', function () {
    document.getElementById("error_name").innerHTML = ''
})

document.getElementById('user_name').addEventListener('click', function () {
    document.getElementById("error_uname").innerHTML = ''
})

document.getElementById('mobile').addEventListener('click', function () {
    document.getElementById("error_mobile").innerHTML = ''
})

document.getElementById('email').addEventListener('click', function () {
    document.getElementById("error_email").innerHTML = ''
})

document.getElementById('pwd').addEventListener('click', function () {
    document.getElementById("error_password").innerHTML = ''
})

document.getElementById('cpwd').addEventListener('click', function () {
    document.getElementById("error_cpassword").innerHTML = ''
})



document.getElementById('btn').addEventListener('click', function () {

    // window.location.href = "http://127.0.0.1:8000/auth/login/";


    var token = document.getElementById('csrf_token_id').value

    var signup_obj = {
        name: document.getElementById('name').value,
        uname: document.getElementById('user_name').value,
        mobile: document.getElementById('mobile').value,
        email: document.getElementById('email').value,
        password: document.getElementById('pwd').value,
        conform_password: document.getElementById('cpwd').value,
    }

    console.log(signup_obj)

    if (signup_obj.name != "" && signup_obj.uname != "" && signup_obj.mobile != "" && signup_obj.email != "" && signup_obj.password != "" && signup_obj.conform_password != "") {

        fetch('http://127.0.0.1:8000/auth/signup/', {

            method: 'POST',

            headers: {
                'Content-Type': 'application / json',
                'X-Requested-With': 'XMLHttpRequest',
                "X-CSRFToken": token
            },
            body: JSON.stringify(signup_obj)
        })
            .then(response => response.json())
            .then(data => {

                if (data.data == true){
                    console.log(data)
                    
                    window.location.href = "http://127.0.0.1:8000/auth/login/";
                }else{
                    document.getElementById('error_msg_from_backendside').innerHTML=data.massage
                }
            })
            .catch(error => console.error(error));


    } else if (signup_obj.name == "") {

        document.getElementById("error_name").innerHTML = 'Name is required'

    } else if (signup_obj.user_name == "") {

        document.getElementById("error_uname").innerHTML = 'Name is required'

    } else if (signup_obj.mobile == "") {

        document.getElementById("error_mobile").innerHTML = 'Mobile is required'

    } else if (signup_obj.email == "") {

        document.getElementById("error_email").innerHTML = 'Email is required'

    } else if (signup_obj.password == "") {

        document.getElementById("error_password").innerHTML = 'Password is required'

    } else if (signup_obj.conform_password == "") {

        document.getElementById("error_cpassword").innerHTML = 'Conform Password is required'

    }

})






// fetch('https://api.example.com/data/123', {
//     method: 'DELETE'
// })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data);
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });



// fetch('https://api.example.com/data/123', {
//     method: 'PUT',
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({
//         title: 'New Title',
//         body: 'New Body'
//     })
// })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data);
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
