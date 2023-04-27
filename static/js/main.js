let sign_up_form = document.getElementById('sign_up')
let login_form = document.getElementById('login')
let or_text = document.getElementById('or_text')
let changer = document.getElementById('changer')
let changer2 = document.getElementById('changer2')
let sign_up_btn = document.getElementById('sign_up_btn')
let username = document.getElementById('s_username')
let password1 = document.getElementById('s_password1')
let password2 = document.getElementById('s_password2')


changer.addEventListener('click', function(){
    login_form.style.display = 'none'
    sign_up_form.style.display = 'block'
    or_text.style.display = 'none'
})

changer2.addEventListener('click', function(){
    login_form.style.display = 'block'
    sign_up_form.style.display = 'none'
    or_text.style.display = 'block'
})


setInterval(function(){
    if (username.value.length >= 5 && /^[a-zA-Z]+$/.test(username.value)){

    }else{
        sign_up_btn.disabled = true
        return
    }

    if (password1.value.length >= 8 && password1.value == password2.value){

    }else{
        sign_up_btn.disabled = true
        return
    }

    sign_up_btn.disabled = false
}, 1000)
