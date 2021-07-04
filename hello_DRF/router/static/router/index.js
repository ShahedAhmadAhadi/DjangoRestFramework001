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
    item =>
        fetch(request, {
            headers: { "Content-type": "application/json", "X-CSRFToken": a[0].value},
            method: "POST",
            body: JSON.stringify({
                name: item.name.first + item.name.last,
                gender: item.gender,
                email: item.email,
                phone: item.phone, 
            }),
            
        }).then(response => response.json()).then(response => console.log(response))
);
}


let btn = document.getElementById("add-btn");
btn.addEventListener("click", add);
