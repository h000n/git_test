function aa() {
    var name = document.getElementById('name').value;
    result = "";
    n = 0;
    const searchResult = [];
    const alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    names = name.toUpperCase().split("");
    while (n <= 24) {
        let index = names.indexOf(alphabet[n]);
        if (index != -1) {
            searchResult.push(alphabet[n]);
        }
        while (index != -1) {
            searchResult.push(index);
            index = names.indexOf(alphabet[n], index + 1);
        }
        n++;
    }
    


    document.getElementById('result').value = searchResult;
}
function enterkey() {
if (window.event.keyCode == 13) {

     // 엔터키가 눌렸을 때 실행할 내용
     aa();
}
}