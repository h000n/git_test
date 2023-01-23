const tmi = require('tmi.js');
var com = ["!com", "!updown", "!lotto", "!rsp", "!help", "!ud", '!dice', '!time'];  // 명령어 모음 /업다운 게임 /로또번호 생성/ 가위바위보 / 명령어 설명 / 거꾸로 바꾸기
var you = 0;
var c = 0;
var tryn = 0;
var num = null;
var comments = '';
// Define configuration options
const opts = {
    identity: {
        username: process.env.BOT_USERNAME,
        password: process.env.OAUTH_TOKEN
    },
    channels: [
        process.env.CHANNEL_NAME
    ]
};
///위에꺼는 channnel 설정..?
// Create a client with our options
const client = new tmi.client(opts);

// Register our event handlers (defined below)
client.on('message', onMessageHandler);
client.on('connected', onConnectedHandler);

// Connect to Twitch:
client.connect();

// Called every time a message comes in
function onMessageHandler(target, context, msg, self) {
    if (self) { return; } // Ignore messages from the bot

    // Remove whitespace from chat message
    const commandName = msg.trim();
    if (msg == com[0]) {
        var contain = [];
        for (var i = 0; i < com.length; i++) {
            contain += "\n" + (i + 1) + ": " + com[i];
        }
        client.say(target, `[명령어들] ${contain}`);
    }

    if (msg.indexOf(com[1]) == 0) {
        client.say(target, "%숫자 형태로 숫자범위를 선택 하시오");
    }
    if (msg.indexOf("%") == 0) {
        num = ran(msg.substring(1));
        client.say(target, "이제 #숫자 형태로 메세지를 보내세요")

    }

    if (msg.indexOf("#") == 0) {
        var guess = msg.substring(1);
        if (num == null) {
            client.say(target, `${com[1]} 를 입력해 지시에따라 설정부터 해주세요`);
        } else if (guess > num) {
            client.say(target, "down");
            tryn = tryn + 1;
        } else if (guess < num) {
            client.say(target, "up");
            tryn = tryn + 1;
        } else if (guess == num) {
            tryn = tryn + 1;
            client.say(target, `${target.replace('#', '')} 님이 ${tryn} 번만에 성공!!`);
            num = null;
        }
    }


    if (msg.indexOf(com[3]) == 0) {
        var coms = ran(3);
        if (msg.substring(5) == "rock" || msg.substring(5) == "scissor" || msg.substring(5) == "paper") {
            if (coms == 1) {
                client.say(target, "com: rock")
            } else if (coms == 2) {
                client.say(target, "com: scissor")
            } else if (coms == 3) {
                client.say(target, "com: paper")
            }
        }
        if (msg.substring(5) == "rock") {
            you = 1;
        } else if (msg.substring(5) == "scissor") {
            you = 2;
        } else if (msg.substring(5) == "paper") {
            you = 3;
        } else {
            client.say(target, "rock , scissor , paper 중 하나를 내주세요");
        }
        if (coms == you) {
            client.say(target, "draw");
        }
        if (coms == 1) {
            if (you == 2) {
                client.say(target, "you lose");
            } else if (you == 3) {
                client.say(target, "you win");
            }
        }
        else if (coms == 2) {
            if (you == 1) {
                client.say(target, "you win");
            }
            else if (you == 3) {
                client.say(target, "you lose");
            }
        }
        else if (coms == 3) {
            if (you == 1) {
                client.say(target, "you lose");
            }
            else if (you == 2) {
                client.say(target, "you win");
            }
        }
    } if (msg == com[2]) {
        while (true) {
            var random = [];
            client.say(target, `waiting...`);
            for (c = 0; c < 7; c++) {
                random.push(ran(45));
            }
            if (random[0] == random[1] || random[1] == random[2] || random[2] == random[3] || random[3] == random[4] || random[5] == random[6] || random[6] == random[1] || random[5] == random[1] || random[4] == random[1] || random[3] == random[1] || random[2] == random[0] || random[0] == random[3] || random[0] == random[4] || random[0] == random[5] || random[0] == random[6] || random[2] == random[3] || random[2] == random[4] || random[2] == random[5] || random[2] == random[6] || random[3] == random[4] || random[3] == random[5] || random[3] == random[6] || random[4] == random[5] || random[4] == random[6] || random[5] == random[6]) {
                continue;
            } else {
                random.sort(function (a, b) {
                    return a - b;
                });
                client.say(target, `It is a ${random}`);
                break;
            }
        }
    }
    if (msg.indexOf(com[4]) == 0) {
        var m = msg.substring(6);
        if (m == com[0]) {
            comments = "명령어 목록을 보여줌";
        } else if (m == com[1]) {
            comments = "업다운게임 실행 ";
        } else if (m == com[2]) {
            comments = "로또번호 생성기";
        } else if (m == com[3]) {
            comments = "가위바위보 게임 !rsp 뒤에 rock scissor paper 중 하나를 전송";
        } else if (m == com[4]) {
            comments = "궁금한 명령어를 !help 명령어 형식으로 보내면 설명을 전송";
        } else if (m == com[5]) {
            comments = "!ud 바꾸고 싶은말 형태로 보내면 거꾸로 보내줌";
        } else if (m == com[6]) {
            comments = "1부터 6까지 주사위 굴림";
        } else {
            comments = "잘못된 입력입니다. !help 명령어 형식으로 보내주세요.";
        }
    }
    client.say(target, `${comments}`);
    if (commandName === com[6]) {
        const num = rollDice(commandName);
        client.say(target, `You rolled a ${num}`);
        console.log(`* )Ex ${commandName} command`);
    }
    if (msg.indexOf(com[5]) == 0) {
        var reve = msg.substring(4).split("").reverse().join("");
        client.say(target, `${reve}`);
    }
    if (msg.indexOf(com[7]) == 0) {
        if (msg.substring(6) != "") {
            var ms = msg.substring(6);
            if (ms * 0 != 0) {
                client.say(target, "imput correct time");
            }
            else {
                demo(ms*1+1,target)
            }

        }else{client.say(target, "imput time");}
    }

}
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function demo(ms,target) {
    for (let i = 1; i < ms; i++) {
        client.say(target, `${ms-i}`);
        await sleep(1000);
    }
    client.say(target, '0');
    client.say(target, 'Done');
}

// Function called when the "dice" command is issued
function rollDice() {
    const sides = 6;
    return Math.floor(Math.random() * sides) + 1;
}
function ran(y) {
    var r = Math.floor(Math.random() * y) + 1;
    return r;
}
// Called every time the bot connects to Twitch chat
function onConnectedHandler(addr, port) {
    console.log(`* Connected to ${addr}:${port}`);
}