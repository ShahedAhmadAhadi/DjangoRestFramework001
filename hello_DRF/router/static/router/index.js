let response = await fetch(
    'https://randomuser.me/api/',
    {method: "GET",
},
    )

let data = response.json()

console.log(data)