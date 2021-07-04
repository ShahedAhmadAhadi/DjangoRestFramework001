async function add() {
    let response = await fetch("https://randomuser.me/api/?results=10");

    let data = await response.json();

    console.log(data);
    post(data.results)
    
}

const csrftoken = 'document.cookie.csrftoken'
async function post(data) {
    data.map(
    item =>
        fetch("http://localhost:8000/router/", {
            headers: { "Content-type": "application/json", "X-CSRFToken": csrftoken , "csrfmiddlewaretoken": "nVApnU8XGVNcCblL1lTZkwaV9cB8s544KShByxvUscuiZ2E2M1uI4ze5Iby3gn3J"},
            method: "POST",
            body: JSON.stringify({
                name: item.name.first + item.name.last,
                gender: item.gender,
                email: item.email,
                phone: item.phone, 
            }),
            
        })
);
}


let btn = document.getElementById("add-btn");
btn.addEventListener("click", add);
