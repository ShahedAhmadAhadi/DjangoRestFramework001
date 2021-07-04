async function add() {
    let response = await fetch("https://randomuser.me/api/?results=10");

    let data = await response.json();

    console.log(data);
    post(data.results)
    
}

let a  = document.getElementsByName('csrfmiddlewaretoken')
console.log(a[0].value)

const csrftoken = 'document.cookie.csrftoken'
const request = new Request('http://localhost:8000/router/')

    

async function post(data) {
    data.map(
    (item, i) =>{setTimeout(() => {
        fetch('http://localhost:8000/router/', {
            headers: { "Content-type": "application/json", "X-CSRFToken": a[0].value},
            method: "POST",
            body: JSON.stringify({
                name: item.name.first + item.name.last,
                gender: item.gender,
                email: item.email,
                phone: item.phone, 
            }),
            
        })
        .then(response => response.json()).then(response => console.log(response))}, i * 5000)
    });
}

async function name(data) {
    for(let i = 0; i <= 10; i++){
        fetch('http://localhost')
    }
}


let btn = document.getElementById("add-btn");
btn.addEventListener("click", add);
