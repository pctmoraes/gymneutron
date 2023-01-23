function display_form(form){

    add_instructor = document.getElementById('add_instructor')
    ut_instructor = document.getElementById('up_instructor')

    if(form == "add"){
        ut_instructor.style.display = "none"
        add_instructor.style.display = "block"

    }else if(form == "update"){
        add_instructor.style.display = "none";
        ut_instructor.style.display = "block"
    }

}

function get_instructor(){
    instructor = document.getElementById('get_instructor')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_instructor = instructor.value

    data = new FormData()
    data.append('id_instructor', id_instructor)

    fetch("/instructor/update/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('form-upd-instructor').style.display = 'block'
        
        id = document.getElementById('id')
        id.value = data['id_instructor']

        name_ = document.getElementById('name')
        name_.value = data['instructor']['name']

        last_name = document.getElementById('last_name')
        last_name.value = data['instructor']['last_name']

        cpf = document.getElementById('cpf')
        cpf.value = data['instructor']['cpf']

        email = document.getElementById('email')
        email.value = data['instructor']['email']

        phone = document.getElementById('phone')
        phone.value = data['instructor']['phone']
    })
}

function update_instructor(){
    name_ = document.getElementById('name').value
    last_name = document.getElementById('last_name').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value
    phone = document.getElementById('phone').value
    id = document.getElementById('id').value

    fetch('/instructor/update/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            name: name_,
            last_name: last_name,
            email: email,
            cpf: cpf,
            phone: phone,
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){

        if(data['status'] == '200'){
            name_ = data['name']
            last_name = data['last_name']
            email = data['email']
            cpf = data['cpf']
            phone = data['phone']
            console.log('Instructor updated succesfully')
        }else{
            console.log('Unable to update Instructor')
        }

    })

}