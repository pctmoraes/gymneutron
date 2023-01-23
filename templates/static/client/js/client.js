function add_pathology(){
    container = document.getElementById('form-pathology')

    html = "<br> <div> <input type='text' class='form-control' name='pathology' > </div>"

    container.innerHTML += html
}

function display_form(form){

    add_client = document.getElementById('add_client')
    ut_client = document.getElementById('up_client')

    if(form == "add"){
        ut_client.style.display = "none"
        add_client.style.display = "block"

    }else if(form == "update"){
        add_client.style.display = "none";
        ut_client.style.display = "block"
    }

}
function get_client(){
    console.log('js')
    client = document.getElementById('get_client')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_client = client.value

    data = new FormData()
    data.append('id_client', id_client)

    fetch("/client/update/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data})
}
// function get_client(){
//     client = document.getElementById('get_client')
//     csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
//     id_client = client.value

//     data = new FormData()
//     data.append('id_client', id_client)

//     fetch("/client/update/",{
//         method: "POST",
//         headers: {
//             'X-CSRFToken': csrf_token,
//         },
//         body: data

//     }).then(function(result){
//         return result.json()
//     }).then(function(data){
//         document.getElementById('form-upd-client').style.display = 'block'
        
        // id = document.getElementById('id')
        // id.value = data['id_client']

        // name_ = document.getElementById('name')
        // name_.value = data['client']['name']

        // last_name = document.getElementById('last_name')
        // last_name.value = data['client']['last_name']

        // cpf = document.getElementById('cpf')
        // cpf.value = data['client']['cpf']

        // email = document.getElementById('email')
        // email.value = data['client']['email']

        // phone = document.getElementById('phone')
        // phone.value = data['client']['phone']
//     })
// }

// function update_client(){
//     name_ = document.getElementById('name').value
//     last_name = document.getElementById('last_name').value
//     email = document.getElementById('email').value
//     cpf = document.getElementById('cpf').value
//     phone = document.getElementById('phone').value
//     id = document.getElementById('id').value

//     fetch('/client/update/' + id, {
//         method: 'POST',
//         headers: {
//             'X-CSRFToken': csrf_token,
//         },
//         body: JSON.stringify({
//             name: name_,
//             last_name: last_name,
//             email: email,
//             cpf: cpf,
//             phone: phone,
//         })

//     }).then(function(result){
//         return result.json()
//     }).then(function(data){

//         if(data['status'] == '200'){
//             name_ = data['name']
//             last_name = data['last_name']
//             email = data['email']
//             cpf = data['cpf']
//             phone = data['phone']
//             console.log('Client updated succesfully')
//         }else{
//             console.log('Unable to update Client')
//         }

//     })

// }