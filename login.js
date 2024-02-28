document.getElementById("loginForm").addEventListener("submit",async function(event){
    event.preventDefault();
    const username=document.getElementById("username").ariaValueMax;
    const password=document.getElementById("psw").ariaValueMax;
    window.location.href="upload.html"

});
