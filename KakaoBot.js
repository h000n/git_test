var com =["/code","/dode","/com","/updown","/lotto","/rsp","/??","/getm","/ud","/실검","/날씨","/cha","/won"];  // 명령어 모음 /업다운 게임 /로또번호 생성/ 가위바위보 / 명령어 설명  / 거꾸로 바꾸기 /네이버 실검 /날씨
var tryn =0;
var alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
var you =0;
var num=null;
var aq=0;
var varss =0;
var msgs=0;
var first = 1;
function ran(y){
  var r = Math.floor(Math.random()*y)+1;
  return r;
}

function response(room, msg, sender, isGroupChat, replier, imageDB, packageName) {

/*                                                                 여기부터 조건문 시작                                                                                         **/
    if(msg==com[11]){ 
        var data=org.jsoup.Jsoup.connect("https://m.search.naver.com/search.naver?query=실시간%20검색어").get().select("span.tit")+""; 
        data= data.replace(/<[^>]+>/g,""); 
        data = data.split("\n");
        var result = ""; 
        for(var n =0;n<20;n++){
            result +=(n+1)+"위: " +data[n]+"\n"; 
        }
           client.say(target,`[네이버 실시간 검색어 순위]\n\n ${result.trim()}`);
    }
    if(msg.indexOf(com[12]) == 0)  {
        var u = Utils.getWebText("https://search.naver.com/search.naver?query="+msg.substring(4)+"날씨");
        try{
        var t = u.split("<span class=\"blind\">");
        var f = t[5].split("<strong>");
        var ch = f[3].split("</strong>");
        var nn = t[5].split("</span>");
               client.say(target,);(`현재 온도: ${nn[1].replace("<span class=\"celsius\">","")} \n 최고 온도: ${f[1].replace(/(<([^>]+)>)/g,"").replace("최저 온도","").trim()} \n 최저 온도: ${f[2].replace(/(<([^>]+)>)/g,"").replace("체감 온도","").replace("체감","").trim()}\n 체감 온도: ${ch[0].trim()}`);
} catch(e){
          client.say(target,"검색되지 않습니다 /날씨 [지역명] 형태로 보내 주시길 바랍니다.");
   }
}
   if(msg.indexOf(com[14]) == 0)  {
	  var contains = "";
	  var urls =[];
	  var url = [];
        var u2 = Utils.getWebText("http://wonjugo.gwe.hs.kr/boardCnts/list.do?boardID=27680&m=0201","Mozilla/5.0 (Linux; Android 9; SM-G611K Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.125 Mobile Safari/537.36;KAKAOTALK 2108970",false,false);
        try{
        var t2 = u2.split("<tbody>");
        var f2 = t2[1].split("<a href=\"#contents\" border=\"0\" title=");
      
		for(var i2 = 0; i2<10;i2++){
			contains +=(i2+1)+". "+f2[i2+1].split(" onclick")[0].replace("\"","").replace("\"","")+' URL : http://wonjugo.gwe.hs.kr/boardCnts/view.do?boardID=27680&boardSeq='+f2[i2+1].split(" onclick=\"javascript:goView('27680','")[1].split("'")[0]+'&lev=0&searchType=S&statusYN=null&page=W&s=wonjugo&m=0201&opType=N'+"\n";
		}

		       client.say(target,);(contains);

} catch(e){
          client.say(target,);("검색되지 않습니다");
   }
}

}