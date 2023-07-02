function search(){
    let searchURL = document.getElementById("url").value;
    console.log(searchURL)
    // call python function
    eel.proxy(searchURL)(response_back)
}

function response_back(response){
    document.getElementById("res").innerHTML = "Last Visited URL: "+response;
}