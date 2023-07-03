let searchURL = document.getElementById("url");

function search(){
    if(searchURL.value == ""){
        document.querySelector(".req-field").style.display="block"
    }
    else{
        // call python function
        eel.proxy(searchURL.value)(response_back)
        alert("Please wait till the chrome opens\n 🔍URL: "+searchURL.value)
    }
}

// check if enter key is pressed
searchURL.addEventListener('keyup', (e) =>{
    if(e.keyCode === 13){
        // call python function
        eel.proxy(searchURL.value)(response_back)
        alert("Please wait till the chrome opens\n 🔍URL: "+searchURL.value)
    }
})
function response_back(response){
    document.getElementById("res").innerHTML = "Last Visited URL: "+response;
}

// alert desc
let alertDesc = document.querySelector(".alert-desc")
let pattern1 = "http://"
let pattern2 = "https://"

searchURL.addEventListener("input", () =>{
    if (searchURL.value.match(pattern1) || searchURL.value.match(pattern2)){
        alertDesc.style.display="none";
    }
    else{
        alertDesc.style.display="block";
        document.querySelector(".req-field").style.display="none"
    }
})
