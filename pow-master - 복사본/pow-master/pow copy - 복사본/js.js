function clearText() {
    const txtSource = document.getElementById("txtSource");
    const destElem = document.getElementById("txtConv");

    txtSource.value = "";
    destElem.value = "";
}
function copyResult() {
    const destElem = document.getElementById("converted_text");
    destElem.select();
    const res = document.execCommand("copy");
    if (!res) {
        window.alert("결과를 복사할 수 없습니다.");
    }
}
function Notdoconvert(){
    let ko_lst = window.ko_list;
    let han_lst = window.han_list;
    let txtSource = document.getElementById("txtSource").value;
    let final = txtSource;
    for(let z=0; z<txtSource.length; z++){
        for(let i=0; i<ko_lst.length; i++){
            final = final.replace(han_lst[i],ko_lst[i]);
        }
    }
    document.getElementById('converted_text').value = final;
}
function pass(){
    var userInput = prompt("password"+"");
    if(userInput == "admin0131"){
        alert("access allowed");
    }
    else{
        alert("access denied");
        document.getElementsByTagName("body")[0].style.display="none";
    }
}