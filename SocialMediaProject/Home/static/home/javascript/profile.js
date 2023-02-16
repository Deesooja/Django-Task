function personal_info(id) {

    document.getElementById('user_name').addEventListener('click', function () {
        document.getElementById("error_uname").innerHTML = ''
    })

    document.getElementById('mobile').addEventListener('click', function () {
        document.getElementById("error_mobile").innerHTML = ''
    })

    document.getElementById('email').addEventListener('click', function () {
        document.getElementById("error_email").innerHTML = ''
    })


    if (id == "edit") {
        var form = document.getElementById("personal_info_form")
        // console.log(form.length)

        for (var i = 0; i < form.length; i++) {
            form[i].removeAttribute("readonly")
            console.log(form[i].value)
        }

        document.getElementById(id).innerHTML = "Save"
        document.getElementById(id).id = "save"

    } else {

        form_obj = {}
        var form = document.getElementById("personal_info_form")

        for (var i = 0; i < form.length; i++) {

            if (form[i].id == "save") {
                continue
            }
            if (form[i].value == '') {

                form_obj[form[i].name] = null

            } else {

                form_obj[form[i].name] = form[i].value
            }

        }
        console.log(form_obj)

        // if (form_obj.user_name != null && form_obj.mobile != null && form_obj.email != null) {

        if (form_obj.user_name == null) {
            document.getElementById('error_uname').innerHTML = "User name is requires"

        } else if (form_obj.mobile == null) {

            document.getElementById('error_mobile').innerHTML = "Mobile name is requires"

        } else if (form_obj.email == null) {
            document.getElementById('error_email').innerHTML = "Email name is requires"

        } else {

            fetch('http://127.0.0.1:8000/profile/', {

                method: 'POST',

                headers: {
                    'Content-Type': 'application / json',
                    'X-Requested-With': 'XMLHttpRequest',
                    "X-CSRFToken": document.getElementById("csrf_token").value
                },
                body: JSON.stringify(form_obj)
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data)

                    if (data.status == 200) {

                        for (var i = 0; i < form.length; i++) {

                            form[i].setAttribute("readonly", "");
                        }

                        document.getElementById(id).innerHTML = "Edit"
                        document.getElementById(id).id = "edit"

                    }
                })
                .catch(error => console.error(error));


        }

    }
}



function show_file_name(id) {
    file_name = document.getElementById(id).files[0].name
    document.getElementById('file_name').innerHTML = file_name

    console.log('file', document.getElementById(id).files[0].name)
    console.log('value', document.getElementById(id).value)

    alert('image upload')
}



function profile_image_upload(id) {


    const form_data_obj = new FormData(document.getElementById("profile_image_form"))

    // console.log(form_data_obj)
    // document.getElementById("inputGroupFile001").files[0]

    if (document.getElementById("inputGroupFile001").files[0]) {

        document.getElementById(id).innerHTML = "Uploading.."

        fetch('http://127.0.0.1:8000/profile/', {

            method: 'POST',

            headers: {
                // 'Content-Type': 'application / json',
                'X-Requested-With': 'XMLHttpRequest-1',
                "X-CSRFToken": document.getElementById("csrf_token").value
            },
            body: form_data_obj,
        })
            .then(response => response.json())
            .then(data => {
                console.log(data)

                if (data.status == 200) {
                    document.getElementById('cart_profile_image').src = data.data.profile_image_url
                    // console.log(data.data.profile_image_url)

                    document.getElementById(id).innerHTML = "Upload"

                }
            })
            .catch(error => console.error(error));

    } else {
        console.log('Choose Image')
    }

}


function post_delete(id) {

    document.getElementById(id).innerHTML="...."
    var parant_element = document.getElementById(id).parentElement.parentElement

    var post_id = parant_element.childNodes[0].nextElementSibling.value

    // document.getElementById(id).parentElement.parentElement.parentElement.remove()


    // fetch('http://127.0.0.1:8000/profile/' + post_id + "/", {

    //     method: 'DELETE',

    //     headers: {
    //         // 'Content-Type': 'application / json',
    //         'X-Requested-With': 'XMLHttpRequest-1',
    //         "X-CSRFToken": document.getElementById("csrf_token").value
    //     },

    // })
    //     .then(response => response.json())
    //     .then(data => {
    //         console.log(data)


    //         if (data.status == 204) {
    //             document.getElementById(id).parentElement.parentElement.parentElement.remove()


    //         }
    //     })
    //     .catch(error => console.error(error));

    // parant_element = document.getElementById(id).parentElement.parentElement
    // console.log(parant_element.childNodes[0].nextElementSibling.value)



    // parant_element = document.getElementById(id).parentElement.parentElement.parentElement.remove()

}