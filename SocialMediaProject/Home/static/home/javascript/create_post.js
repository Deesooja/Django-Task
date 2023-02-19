function post(id) {

    const form_data_obj = new FormData(document.getElementById("post_form"))

    console.log(form_data_obj)

    if (document.getElementById("post_image").files[0] && document.getElementById("yout_text").value) {

        document.getElementById(id).innerHTML = "Posting..."



        fetch('http://15.207.107.243/create-post/', {

            method: 'POST',

            headers: {
                // 'Content-Type': 'application / json',
                'X-Requested-With': 'XMLHttpRequest',
                "X-CSRFToken": document.getElementById("csrf_token").value
            },
            body: form_data_obj,
        })
            .then(response => response.json())
            .then(data => {
                console.log(data)

                if (data.status == 201) {
                    document.getElementById('post_massage').innerHTML= "Posted"

                    document.getElementById(id).innerHTML = "Post"

                }
            })
            .catch(error => console.error(error));

    } else {
        document.getElementById('error').innerHTML="Please choose file "
    }

}