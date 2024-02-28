document.getElementById("registerform").addEventListener("submit",async function(event){
    event.preventDefault();
    const formDat = new FormData();
    FormData.append('username',document.getElementById("username").value);
    FormData.append('email',document.getElementById("mail").value);
    FormData.append('password',document.getElementById("password").value);
    try{
        const response = await fetch('/register',{
            method: 'POST',
            body: FormData
        });
        if(response.ok){
            window.location.href = "/login.html";

        }else{
            const errorMessage = await response.text();
            alert(errorMessage);
        }
    }catch (error){
        console.error('Error')
    }
});