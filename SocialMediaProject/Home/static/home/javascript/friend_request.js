function friend_request_accept(id) {
    request_id = document.getElementById(id).parentElement.parentElement.childNodes[0].nextSibling.value
    // document.getElementById(id).parentElement.parentElement.parentElement.remove()

    fetch('http://15.207.107.243/friend-request/', {

        method: 'POST',

        headers: {
            'Content-Type': 'application / json',
            'X-Requested-With': 'XMLHttpRequest-1',
            "X-CSRFToken": document.getElementById("csrf_token").value
        },

        body: JSON.stringify({ "friend_request_id": request_id })

    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data.status == 200) {
                document.getElementById(id).parentElement.parentElement.parentElement.remove()


            }
        })
        .catch(error => console.error(error));

}

function friend_request_reject(id) {
    request_id = document.getElementById(id).parentElement.parentElement.childNodes[0].nextSibling.value
    // document.getElementById(id).parentElement.parentElement.parentElement.remove()

    fetch('http://15.207.107.243/friend-request/', {

        method: 'POST',

        headers: {
            'Content-Type': 'application / json',
            'X-Requested-With': 'XMLHttpRequest-2',
            "X-CSRFToken": document.getElementById("csrf_token").value
        },

        body: JSON.stringify({ "friend_request_id": request_id })

    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data.status == 200) {
                document.getElementById(id).parentElement.parentElement.parentElement.remove()


            }
        })
        .catch(error => console.error(error));
}