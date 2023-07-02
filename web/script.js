function search(){
    let searchURL = document.getElementById("url").value;
    // call python function
    eel.proxy(searchURL)(response_back)
    alert("Please wait till the chrome opens\n 🔍URL: "+searchURL)
}

let searchURL = document.getElementById("url");
searchURL.addEventListener('keyup', (e) =>{
    if(e.keyCode === 13){
        // call python function
        eel.proxy(searchURL.value)(response_back)
        alert("Please wait till the chrome opens\n 🔍URL: "+searchURL)
    }
})

function response_back(response){
    document.getElementById("res").innerHTML = "Last Visited URL: "+response;
}