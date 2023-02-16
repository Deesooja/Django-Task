function unfriend(id) {
    friend_id = document.getElementById(id).parentElement.parentElement.childNodes[1].value
    document.getElementById(id).innerHTML="Proccing"

    fetch('http://127.0.0.1:8000/all-friends/'+ friend_id +"/", {

        method: 'DELETE',

        headers: {
            'Content-Type': 'application / json',
            'X-Requested-With': 'XMLHttpRequest',
            "X-CSRFToken": document.getElementById("csrf_token").value
        },


    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data.status == 204) {
                document.getElementById(id).parentElement.parentElement.parentElement.remove()

            }
        })
        .catch(error => console.error(error));

}