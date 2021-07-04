async function add(){
    let response = await fetch(
        'https://randomuser.me/api/'
        )
    
    let data = await response.json()
    
    console.log(data)
}


let btn = document.getElementById('add-btn')
btn.addEventListener('click', add)