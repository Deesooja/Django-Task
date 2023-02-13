// document.getElementById('btn').addEventListener('click', function(){
//     alert("login alert")
// })




document.getElementById('mobile').addEventListener('click', function () {
    document.getElementById("error_mobile").innerHTML = ''
})


document.getElementById('pwd').addEventListener('click', function () {
    document.getElementById("error_password").innerHTML = ''
})





document.getElementById('btn').addEventListener('click', function () {

    // window.location.href = "http://127.0.0.1:8000";


    var token = document.getElementById('csrf_token_id').value

    var login_obj = {

        mobile: document.getElementById('mobile').value,
        password: document.getElementById('pwd').value,

    }

    console.log(login_obj)

    if (login_obj.mobile != "" && login_obj.password != "") {

        fetch('http://127.0.0.1:8000/auth/login/', {

            method: 'POST',

            headers: {
                'Content-Type': 'application / json',
                'X-Requested-With': 'XMLHttpRequest',
                "X-CSRFToken": token
            },
            body: JSON.stringify(login_obj)
        })
            .then(response => response.json())
            .then(data => {
                // console.log(data)

                if (data.data == true) {
                    
                    console.log(data)

                    window.location.href = "http://127.0.0.1:8000";
                }
            })
            .catch(error => console.error(error));

    } else if (login_obj.mobile == "") {

        document.getElementById("error_mobile").innerHTML = 'Mobile is required'

    } else if (login_obj.password == "") {

        document.getElementById("error_password").innerHTML = 'Password is required'

    }

})