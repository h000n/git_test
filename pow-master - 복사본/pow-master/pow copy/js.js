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

function doConvert(){
    let ko_lst = window.ko_list;
    let han_lst = window.han_list;
    let txtSource = document.getElementById("txtSource").value;
    let final = txtSource;
    for(let z=0; z<txtSource.length; z++){
        for(let i=0; i<ko_lst.length; i++){
            final = final.replace(ko_lst[i],han_lst[i]);
        }
    }
    document.getElementById('converted_text').value = final;
}