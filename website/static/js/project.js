function showHide(id, btn){
    let div = document.getElementById(id);
    let showBtn = document.getElementById(btn);
    if (div.className === "hidden") {
        div.className = "hidden active";
        showBtn.className = "hidden active";
        showBtn.innerHTML = "Hide";
    } else {
        div.className = "hidden";
        showBtn.className = "hidden";
        showBtn.innerHTML = "Show more";
    }
}