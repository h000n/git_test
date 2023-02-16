function aa() {
    var a_1 = document.getElementById('a1').value;
    var a_2 = document.getElementById('a2').value;
    var a_3 = document.getElementById('a3').value;
    var b = 0;//0->공차 1-> 공비
    var c = 0; //1-> 공차 or 공비2->둘다
    a_1 = parseInt(a_1);
    a_2 = parseInt(a_2);
    a_3 = parseInt(a_3);
    if (a_2 * 2 == a_1 + a_3) {
        c += 1;
        b = 0;
        var ad = a_2 - a_1; // 공차
    }
    if (Math.pow(a_2, 2) == a_1 * a_3) {
        c += 1;
        b = 1;
        if (a_1 != 0) {
            var ar = a_2 / a_1;
        } else ar = 0; // 공비
    }
    if (c == 1 && b == 0) {
        alert("등차 수열 공차:  " + ad);
    }
    else if (c == 1 && b == 1) {
        alert(" 등비 수열 공비: " + ar);
    }
    else if (c == 2) {
        alert("등차 수열 공차:  " + ad + " or " + " 등비 수열 공비: " + ar);
    }
    else {
        alert("error");
    }
}

function bb() {
    var d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    var a = document.getElementById('kk').value;
    for (var z = d.length; z >= 0; z--) {
        if (a >= Math.pow(2, z)) {
            a -= Math.pow(2, z);
            d[d.length - z] = 1;
        }
        else {
            d[d.length - z] = 0;
        }
    }
    d = d.toString().replace(/,/g, "");
    alert(d.replace(d.split("1")[0], ""));
}
function cc() {
    var d = 0;
    var a = document.getElementById('kk').value;
    for (var z = 1000; z >= 0; z--)//1001
    {
        while (a >= Math.pow(10, z)) {
            a -= Math.pow(10, z);
            d += Math.pow(2, z);
        }
    }
    alert(d);
}
function dd() {
    document.getElementById('txtConv').value = "너무 큰 수를 대입시 에러 발생";
    var times = document.getElementById('times').value;
    var text = document.getElementById('text').value;
    times = parseInt(times);
    final = text.repeat(times);
    if (final == "iamadmin".repeat(131)) {
        document.getElementsByClassName("admin")[0].style.display = "block";
        document.getElementsByClassName("admin")[1].style.display = "block";
        alert("welcome");
    } if (final == "") {
        alert("error");
    }
    else {
        document.getElementById('txtConv').value = final;
    }
}


function ma() {

    value_1 = document.getElementsByClassName('values')[0].value;
    value_2 = document.getElementsByClassName('values')[1].value;
    value_3 = document.getElementsByClassName('values')[2].value;
    value_4 = document.getElementsByClassName('values')[3].value;
    value_5 = document.getElementsByClassName('valuess')[0].value;
    value_6 = document.getElementsByClassName('valuess')[1].value;
    value_7 = document.getElementsByClassName('valuess')[2].value;
    value_8 = document.getElementsByClassName('valuess')[3].value;
    y= document.getElementById('pre').value;
    var 독립변수 = [value_1, value_2, value_3, value_4];
    var 종속변수 = [value_5, value_6, value_7, value_8];
    var 원인_데이터_변환 = tf.tensor(독립변수);
    var 결과_데이터_변환 = tf.tensor(종속변수);

    // 2. 모델의 모양을 만듭니다. 
    var 독립변수_개수 = 1;
    var 종속변수_개수 = 1;
    var X = tf.input({ shape: [독립변수_개수] });
    var H = tf.input({ shape: [1] });
    var Y = tf.layers.dense({ units: 종속변수_개수 }).apply(H);
    var model = tf.model({ inputs: X, outputs: Y });
    var compileParam = { optimizer: tf.train.adam(), loss: tf.losses.meanSquaredError }
    model.compile(compileParam);

    // 3. 데이터로 모델을 학습시킵니다. 
     var fitParam = { epochs: 5000} 
    model.fit(원인_데이터_변환, 결과_데이터_변환, fitParam).then(function (result) {
        document.getElementById('results').style.display = block;
        alert("model complete")
        document.getElementById('results').value = a(y);
    });

}


// 4.2 새로운 데이터를 이용
function predict(y) {
    var 다음주원인 = tf.tensor([y]);
    var 다음주결과 = model.predict(다음주원인);
    return 다음주결과.arraySync();
}
function a(x) {
    var i;
    var value = 0;
    for (i = 0; i < model.getWeights().length; i++) {
        if (i == model.getWeights().length - 1) {
            value += model.getWeights()[i].arraySync()[0];
        }
        else {
            x *= model.getWeights()[i].arraySync()[0][0];
            value += x;
        }
    }
    return value;
}
function b() {
    var text = "";
    var i;
    for (i = 0; i < model.getWeights().length; i++) {
        if (i == model.getWeights().length - 1) {
            text += model.getWeights()[i].arraySync()[0];
        }
        else {
            text += model.getWeights()[i].arraySync()[0][0] + "*x" + i + 1 + "+";
        }
    }
    console.log(text);
}
