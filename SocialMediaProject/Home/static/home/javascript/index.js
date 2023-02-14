// document.getElementById('btn').addEventListener('click', function(){

//     alert('index')
// })

function home_page_load() {

    function post_load(post) {


        var master = document.createElement("div")
        master.className = "border border-primary  p-1 ml-1 mt-4 ";

        let cart_ship = document.createElement("div");
        cart_ship.className = "chip";
        cart_ship.innerHTML = post?.posted_by?.name || "Name"

        let cart_chip_img = document.createElement("img");

        cart_chip_img.src = post?.posted_by?.image || "https://mdbootstrap.com/img/Photos/Avatars/avatar-6.webp";
        cart_chip_img.alt = "Card image chip";

        cart_ship.append(cart_chip_img)



        let cart = document.createElement("div");
        cart.className = "cart";
        cart.style.width = "41.7rem";

        let cart_image = document.createElement("img");
        cart_image.className = "card-img-top border border-success";
        cart_image.src = post.post.image || "https://thecustombakers-s3-bucket.s3.amazonaws.com/ItemDefultImage63cfbacdef471present.jpg";
        cart_image.alt = "Card image cap";

        let cart_body = document.createElement("div");
        cart_body.className = "card-body";

        let text = document.createElement("p");
        text.className = "card-text";
        text.textContent = post.post.text || "Some quick example text to build on the card title and make up the bulk of the card content";

        cart_body.append(text);
        cart.append(cart_ship, cart_image, cart_body);
        master.append(cart);


        // super_master.append(master)

        var main_div = document.getElementById("post_div_main");
        main_div.append(master);
    }

    function user_info_fun(user) {

        console.log("user_info", user)
        let cart_ship = document.createElement("div");
        cart_ship.className = "chip ";
        cart_ship.innerHTML = user.name || "Name"

        let cart_chip_img = document.createElement("img");

        cart_chip_img.src = user.image || "https://mdbootstrap.com/img/Photos/Avatars/avatar-6.webp";
        cart_chip_img.alt = "Card image chip";

        cart_ship.append(cart_chip_img)
        var user_info_div=document.getElementById('user_info_div')
        user_info_div.append(cart_ship)

        // document.getElementById('user_info_div').innerHTML = user.name || Name

        // document.getElementById('user_image').src = "https://mdbootstrap.com/img/Photos/Avatars/avatar-6.webp"

    }

    fetch('http://127.0.0.1:8000/', {
        method: "GET",

        headers: {
            'Content-Type': 'application / json',
            'X-Requested-With': 'XMLHttpRequest',
        },

    })
        .then(response => response.json())
        .then(data => {
            // console.log(data);
            if (data.status == 200) {
                console.log(data);

                console.log(data.data.post)

                data.data.post.map(post_load)

                user_info_fun(data.data.user_info)

            }

        })
        .catch(error => {
            console.error('Error:', error);
        });


    // alert('ok')

    // for (var i = 0; i < 20; i++) {

    // let master = document.createElement("div")
    // master.className = "border border-primary  p-1 ml-4 mt-4 ";

    // let hidden_id = document.createElement("input");
    // hidden_id.type = "hidden";
    // hidden_id.id = "cart_id_hidden_input" + "_" + i;
    // hidden_id.value = i;


    // let cart = document.createElement("div");
    // cart.className = "cart";
    // cart.style.width = "28rem";

    // let cart_image = document.createElement("img");
    // cart_image.className = "card-img-top border border-success";
    // cart_image.src = "https://thecustombakers-s3-bucket.s3.amazonaws.com/ItemDefultImage63cfbacdef471present.jpg";
    // cart_image.alt = "Card image cap";
    // cart_image.style.height = "28rem";

    // let cart_body = document.createElement("div");
    // cart_body.className = "card-body";
    // ---------------
    // let cart_ship = document.createElement("div");
    // cart_ship.className = "chip";
    // cart_ship.innerHTML = 'cart_ship'


    // let cart_chip_img = document.createElement("img");
    // cart_chip_img.src = "https://mdbootstrap.com/img/Photos/Avatars/avatar-6.webp";
    // // cart_chip_img.style.height = "100px";
    // // cart_chip_img.style.width = "100px";
    // cart_chip_img.alt = "Card image chip";

    // cart_ship.append(cart_chip_img)

    // let text = document.createElement("p");
    // text.className = "card-text";
    // text.textContent = "Some quick example text to build on the card title and make up the bulk of the card content";

    // cart_body.append(text);
    // cart.append(cart_image, cart_body);
    // master.append(cart_ship, cart, delete_icon, hidden_id);

    // var main_div = document.getElementById("post_div");
    // main_div.append(master);

    // let delete_icon = document.createElement("i");
    // delete_icon.className = "fas fa-trash-alt text-danger";
    // delete_icon.id = "cart_delete_btn";
    // delete_icon.value = i;


    // delete_icon.addEventListener("click", function () {
    //     cart_delete_fun(this.value)
    // })


}
