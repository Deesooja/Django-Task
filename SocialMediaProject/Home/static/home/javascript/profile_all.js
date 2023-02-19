// document.getElementById('friend_request_send_inside_profile').addEventListener('click', function(){
//     alert("send")

//    this.id="friend_request_cancel_inside_profile"

// })

// document.getElementById('friend_request_cancel_inside_profile').addEventListener('click', function(){

//     alert("cancel")
//     this.id="friend_request_send_inside_profile"

// })

function friend_request_send_cancel(id, user_id) {
    // alert("ok")
    var user_id=document.getElementById('user_id_on_profile_page').value

    if (id == "send") {

        fetch('http://15.207.107.243/profile-all/', {

            method: "POST",

            headers: {
                'Content-Type': 'application / json',
                'X-Requested-With': 'XMLHttpRequest-1',
                "X-CSRFToken": document.getElementById('csrf_token').value
            },
            body: JSON.stringify({ user_id: user_id }),

        })
            .then(response => response.json())
            .then(data => {
                if (data.status == 201) {
                    console.log(data)
                    document.getElementById(id).style.color = ""
                    document.getElementById(id).innerHTML = "Send..."
                    document.getElementById(id).id = "cancel"
                }

            })
            .catch(error => {
                console.error('Error:', error);
            });


    } else {

        fetch('http://15.207.107.243/profile-all/', {

            method: "POST",

            headers: {
                'Content-Type': 'application / json',
                'X-Requested-With': 'XMLHttpRequest-2',
                "X-CSRFToken": document.getElementById('csrf_token').value
            },
            body: JSON.stringify({ user_id: user_id }),

        })
            .then(response => response.json())
            .then(data => {
                if (data.status == 200) {
                    console.log(data)

                    document.getElementById(id).style.color = "#c1ac25"
                    document.getElementById(id).innerHTML = "+"
                    document.getElementById(id).id = "send"
                }

            })
            .catch(error => {
                console.error('Error:', error);
            });


    }

}