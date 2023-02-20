
document.getElementById('search_box').addEventListener("keyup", function () {

    document.getElementById("search_msg").innerHTML = 'Searching.....'

    function result(result) {
        let master = document.createElement("div")
        master.className = "border border-primary  p-1 ml-4 mt-4 ";
        // <input type="hidden" name="carta-id" id="cart_id" value="">

        let hidden_id = document.createElement("input");
        hidden_id.type = "hidden";
        hidden_id.id = "cart_id_hidden_input";
        hidden_id.value = result.user_id;

        let cart = document.createElement("div");
        cart.className = "cart";
        cart.style.width = "18rem";

        let cart_image = document.createElement("img");
        cart_image.className = "card-img-top border border-success";
        cart_image.src = result.image || "https://t3.ftcdn.net/jpg/05/03/24/40/360_F_503244059_fRjgerSXBfOYZqTpei4oqyEpQrhbpOML.jpg";
        cart_image.alt = "Card image cap";
        cart_image.style.width = "290px";
        cart_image.style.height = "290px";

        let cart_body = document.createElement("div");
        cart_body.className = "card-body";

        let text = document.createElement("p");
        text.className = "card-text";
        text.textContent = result.name;

        icon_div = document.createElement("div")
        icon_div.id = "icon_div_id"

        let view_icon = document.createElement("i");
        view_icon.className = "fas fa-eye fa-2x text-danger";
        view_icon.id = "view_btn";
        view_icon.value = result.user_id;



        var link = document.createElement("a")
        if (result.friend) {
            link.href = "http://127.0.0.1:8000/profile/?user_id=" + result.user_id
        } else {

            link.href = "http://127.0.0.1:8000/profile-all/?user_id=" + result.user_id
        }

        var small = document.createElement("small")
        small.className = "text-danger"
        small.id = "msg_" + result.user_id

        let add_friend = document.createElement("i");
        add_friend.className = 'fas fa-user-friends fa-2x',
            add_friend.style.color = '#c1ac25';
        add_friend.id = "add_friend_btn" + "_" + result.user_id;
        add_friend.value = result.user_id;
        add_friend.innerHTML = "+"


        add_friend.addEventListener("click", function () {
            request_send_cancel(this.value, this.id, this.id)
        })

        let already_friend_request_send = document.createElement("i");
        already_friend_request_send.className = 'fas fa-user-friends fa-2x',
            already_friend_request_send.style.color = '';
        already_friend_request_send.id = "remove_friend_btn" + "_" + result.user_id;
        already_friend_request_send.value = result.user_id;
        already_friend_request_send.innerHTML = "Send...."

        already_friend_request_send.addEventListener("click", function () {
            request_send_cancel(this.value, this.id)
        })

        // var small=document.createElement("small")
        // small.className="text-danger"
        // small.id="msg"


        link.append(view_icon)
        if (result.friend) {
            icon_div.append(link)

        } else {
            if (result.request) {

                icon_div.append(already_friend_request_send, small, link)

            } else {

                icon_div.append(add_friend, small, link)
            }

        }

        cart_body.append(text);
        cart.append(cart_image, cart_body);
        master.append(cart, icon_div, hidden_id);

        var search_result_div = document.getElementById("search_result_div");
        search_result_div.append(master);
    }




    // ------------------------------------------On Click  Friend Requst And Cancel-------------

    function request_send_cancel(user_id, id) {

        document.getElementById('msg_' + user_id).innerHTML = "wait"

        if (id == ("add_friend_btn" + "_" + user_id)) {

            fetch('http://127.0.0.1:8000/search/', {
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

                        document.getElementById(id).innerHTML = "Send..."
                        document.getElementById(id).style.color = ''
                        document.getElementById(id).id = "remove_friend_btn_" + user_id
                        document.getElementById('msg').innerHTML = ''

                    }

                })
                .catch(error => {
                    console.error('Error:', error);
                });

        } else {

            fetch('http://127.0.0.1:8000/search/', {

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
                        document.getElementById(id).innerHTML = "+"
                        document.getElementById(id).style.color = '#c1ac25'
                        document.getElementById(id).id = "add_friend_btn_" + user_id
                        document.getElementById('msg').innerHTML = ''

                    }

                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }

    }

    // ------------------------------------------Search Ajax---------------------------------------

    var key = document.getElementById('search_box').value
    fetch('http://127.0.0.1:8000/search/?key=' + key, {
        method: "GET",

        headers: {
            'Content-Type': 'application / json',
            'X-Requested-With': 'XMLHttpRequest',
        },

    })
        .then(response => response.json())
        .then(data => {
            if (data.status == 200) {
                document.getElementById("search_result_div").innerHTML = ""
                document.getElementById("search_msg").innerHTML = ''
                console.log(data.data);

                data.data.map(result)

            } else {
                if (data.key) {

                    document.getElementById("search_result_div").innerHTML = data.massage
                    document.getElementById("search_msg").innerHTML = ''
                } else {
                    document.getElementById("search_result_div").innerHTML = "Search Your Feverate Onece"
                    document.getElementById("search_msg").innerHTML = ''

                }
            }

        })
        .catch(error => {
            console.error('Error:', error);
        });

    // alert('search')

})

// function myFunction(){
//     alert("searching")
// }

// document.getElementById('btn').addEventListener('click', function () {

//     alert('search')

// })