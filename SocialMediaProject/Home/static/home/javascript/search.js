
document.getElementById('search_box').addEventListener("keyup", function () {
    // alert('search')
    // location.reload();


    // for (var i = 0; i < 20; i++) {
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
        cart_image.src = result.image || "https://thecustombakers-s3-bucket.s3.amazonaws.com/ItemDefultImage63cfbacdef471present.jpg";
        cart_image.alt = "Card image cap";

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

        let add_friend = document.createElement("i");
        add_friend.className = 'fas fa-user-friends fa-2x',
            add_friend.style.color = '#c1ac25';
        add_friend.id = "add_friend_btn" + "_" + result.user_id;
        add_friend.value = result.user_id;
        add_friend.innerHTML = "+"

        add_friend.addEventListener("click", function () {
            add_friend_fun(this.value)
        })

        let already_friend_request_send = document.createElement("i");
        already_friend_request_send.className = 'fas fa-user-friends fa-2x',
            already_friend_request_send.style.color = '';
        already_friend_request_send.id = "add_friend_btn" + "_" + result.user_id;
        already_friend_request_send.value = result.user_id;
        already_friend_request_send.innerHTML = "Send...."

        already_friend_request_send.addEventListener("click", function () {
            already_friend_request_send_fun(this.value)
        })

        link.append(view_icon)
        if (result.friend) {
            icon_div.append(link)

        } else {
            if (result.request) {

                icon_div.append(already_friend_request_send, link)

            } else {

                icon_div.append(add_friend, link)
            }

        }

        cart_body.append(text);
        cart.append(cart_image, cart_body);
        master.append(cart, icon_div, hidden_id);

        var search_result_div = document.getElementById("search_result_div");
        search_result_div.append(master);
    }

    // ------------------------------------------On Click Send Friend Requst------------------------

    function add_friend_fun(user_id) {

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

                    document.getElementById('add_friend_btn_' + user_id).innerHTML = "Send..."
                    document.getElementById('add_friend_btn_' + user_id).style.color = ''

                    document.getElementById('add_friend_btn_' + user_id).addEventListener("click", function () {

                        already_friend_request_send_fun(this.value)

                    })

                }

            })
            .catch(error => {
                console.error('Error:', error);
            });








        // console.log(document.getElementById('add_friend_btn_1'))


    }


    // ------------------------------------------On Click Cancel Friend Requst------------------------

    function already_friend_request_send_fun(user_id) {


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

                    document.getElementById('add_friend_btn_' + user_id).innerHTML = "+"
                    document.getElementById('add_friend_btn_' + user_id).style.color = '#c1ac25'

                    document.getElementById('add_friend_btn_' + user_id).addEventListener("click", function () {

                        add_friend_fun(this.value)

                    })

                }

            })
            .catch(error => {
                console.error('Error:', error);
            });

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
                console.log(data.data);

                data.data.map(result)


            }else{
                document.getElementById("search_result_div").innerHTML = ""
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