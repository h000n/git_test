const express = require('express');
const app = express();
const port =3000;

app.get('/',(req,res) => {
    res.sendFile(__dirname+'/index.html');
});

app.get('/path/:page',(req,res)=>{
    res.send(req.params);
    res.send('Hello');
    
});

app.listen(port,()=>{
    console.log('http://localhost:'+port);
});

app.use(express.urlencoded({extended: false}));

app.post('/act',(req,res) => {
    console.log(req.body);
    res.send('login success');
});
