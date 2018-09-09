// Daniel Shiffman
// http://codingtra.in
// http://patreon.com/codingtrain

// Color Predictor
// https://youtu.be/KtPpoMThKUs

// Inspired by Jabril's SEFD Science
// https://youtu.be/KO7W0Qq8yUE
// https://youtu.be/iN3WAko2rL8

let brain;

let userR, userL, cpuR, cpuL;

let userSplit;
let userRightCpuRight;
let userRightCpuLeft;
let userLeftCpuRight;
let userLeftCpuLeft;

var once = true;

function generateScenario() {
    userR = Math.floor(Math.random()*5);
    userL = Math.floor(Math.random()*5);
    cpuR = Math.floor(Math.random()*5);
    cpuL = Math.floor(Math.random()*5);
    console.log("userR: " + userR);
    console.log("userL: " + userL);
    console.log("cpuR: " + cpuR);
    console.log("cpuL: " + cpuL);
}

function setup() {
  createCanvas(300, 750);
  noLoop();
  brain = new NeuralNetwork(4, 4, 5);
  brain2 = new NeuralNetwork(4,4,5);

  generateScenario();

}

function mousePressed() {
    if (mouseY>450 && mouseY<600){
        predictor();
    }
    else{
        if(mouseY>600){
            if(once){
               // brain2 = brain;
            }
            once = false;
            predictor2();
        }
        else{
            let targets;
            if (mouseX < 150 && mouseY<150) 
                targets = [1,0,0,0,0];
            if (mouseX > 150 && mouseY<150) 
                targets = [0,1,0,0,0];
            if (mouseX < 150 && mouseY>150 && mouseY < 300) 
                targets = [0,0,1,0,0];
            if (mouseX > 150 && mouseY>150 && mouseY < 300) 
                targets = [0,0,0,1,0];
            if (mouseY>300 && mouseY<450) 
                targets = [0,0,0,0,1];
            
            let inputs = [userR, userL, cpuR, cpuL];
            
            brain.train(inputs, targets);
            brain2.train(inputs, targets);
    
            generateScenario();
        }
    }
    
}


function predictor() {
    let inputs = [userR, userL, cpuR, cpuL];
    let outputs = brain.predict(inputs);
    console.log(outputs);
}

function predictor2() {
    let inputs = [userR, userL, cpuR, cpuL];
    let outputs = brain2.predict(inputs);
    console.log('brain 2: ' + outputs);
}

var canvas = document.getElementById("myCanvas");
    var ctx = canvas.getContext("2d")

function drawEnemyHands(){
    //left palm
    ctx.beginPath();
    ctx.rect(120,40,80,80);
    ctx.fillStyle = "red";
    ctx.fill();
    ctx.closePath();

    //right palm
    ctx.beginPath();
    ctx.rect(280,40,80,80);
    ctx.fillStyle = "red";
    ctx.fill();
    ctx.closePath();

    //left fingers
    var initX = 195;
    for(var i=0; i<cpuL; i++){
        var initY = (i<4) ? 120 : 80;
        initX = (i<4) ? initX : 215;
        ctx.beginPath();
        ctx.rect(initX,initY,-15,50);
        ctx.fillStyle = "red";
        ctx.fill();
        ctx.closePath();
        initX-=20;
    }

    //right fingers
    var initX = 285;
    for(var i=0; i<cpuR; i++){
        var initY = (i<4) ? 120 : 80;
        initX = (i<4) ? initX : 265;
        ctx.beginPath();
        ctx.rect(initX,initY,15,50);
        ctx.fillStyle = "red";
        ctx.fill();
        ctx.closePath();
        initX+=20;
    }
}
function drawPlayerHands(){
    //left palm
    ctx.beginPath();
    ctx.rect(120,360,80,80);
    ctx.fillStyle = "green";
    ctx.fill();
    ctx.closePath();

    //right palm
    ctx.beginPath();
    ctx.rect(280,360,80,80);
    ctx.fillStyle = "green";
    ctx.fill();
    ctx.closePath();

    //left fingers
    var initX = 195;
    for(var i=0; i<userL; i++){
        var initY = (i>0) ? 360 : 400;
        initX = (i>0) ? 215-(20*i) : 215;
        ctx.beginPath();
        ctx.rect(initX,initY,-15,-50);
        ctx.fillStyle = "green";
        ctx.fill();
        ctx.closePath();
    }

    //right fingers
    var initX = 285;
    for(var i=0; i<userR; i++){
        var initY = (i>0) ? 360 : 400;
        initX = (i>0) ? 265+(20*i) : 265;
        ctx.beginPath();
        ctx.rect(initX,initY,15,-50);
        ctx.fillStyle = "green";
        ctx.fill();
        ctx.closePath();
    }
}


function draw() {
  strokeWeight(4);
  stroke(0);
  line(width / 2, 0, width / 2, 300);
  line(0, 300, width, 300);
  line(0, 150, width, 150);
  line(0, 450, width, 450);
  line(0, 600, width, 600);
  textSize(12);
  noStroke();
  fill(0);
  textAlign(CENTER, CENTER);
  text("userRcpuR", 50, 50);
  text("userRcpuL", 250, 50);
  text("userLcpuR", 50, 250);
  text("userLcpuR", 250, 250);
  text("split", 200, 350);
  fill(255);

  ctx.clearRect(0,0,canvas.width, canvas.height);
  drawEnemyHands();
  drawPlayerHands();
}
setInterval(draw, 10);
