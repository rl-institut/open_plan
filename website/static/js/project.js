function showHide(id, btn){
    let div = document.getElementById(id);
    let showBtn = document.getElementById(btn);
    if (div.className === "hidden") {
        div.className = "hidden  active";
        showBtn.innerHTML = "hide";
    } else {
        div.className = "hidden";
        showBtn.innerHTML = "show more";
    }
}