<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Freeze Screen</title>
<style>
    body, html {
        margin: 0;
        padding: 0;
        overflow: hidden;
        background: black;
        color: #00ff00;
        font-family: monospace;
    }

    #overlay {
        position: fixed;
        width: 100%;
        height: 100%;
        background: black;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        z-index: 9999;
    }

    #timer {
        font-size: 50px;
        color: red;
    }

    #text {
        font-size: 30px;
        margin-top: 20px;
    }

    #bar {
        width: 80%;
        height: 20px;
        border: 1px solid #00ff00;
        margin-top: 30px;
    }

    #progress {
        height: 100%;
        width: 0%;
        background: #00ff00;
    }
</style>
</head>

<body>

<div id="overlay">
    <div id="timer">5</div>
    <div id="text">SYSTEM FREEZE...</div>
    <div id="bar"><div id="progress"></div></div>
</div>

<script>
let seconds = 5;
let progress = 0;

// Block user input inside page
document.addEventListener("keydown", e => e.preventDefault());
document.addEventListener("click", e => e.preventDefault());
document.addEventListener("touchstart", e => e.preventDefault());

// Timer
let timer = setInterval(() => {
    seconds--;
    document.getElementById("timer").innerText = seconds;

    if (seconds <= 0) {
        clearInterval(timer);
        document.getElementById("overlay").style.display = "none";
    }
}, 1000);

// Loading bar
let bar = setInterval(() => {
    progress += 2;
    document.getElementById("progress").style.width = progress + "%";
    if (progress >= 100) clearInterval(bar);
}, 100);
</script>

</body>
</html>
