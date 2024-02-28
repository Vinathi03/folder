document.querySelector("form").addEventListener("submit",async function(event){
    event.preventDefault();
    const formData=new FormData();
    formData.append('file',document.querySelector('input[type="file"]').files[0]);
    formData.append('keyword',document.getElementById("Keyword").value);
    try{
        const response=await fetch('/pdf_search',{
            method:'POST',
            body:formData
        });
        if(response.ok){
            const message=await response.text();
            document.getElementById('message').innerText=message;

        }else{
            const errorMessage=await response.text();
            alert(errorMessage);
        }

    }catch (error){
        console.error('Error:',error);
        alert('An error occured while processing your request.Please try again later.');
    }
});