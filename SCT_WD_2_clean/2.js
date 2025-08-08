let startTime, updatedTime, difference = 0, tInterval;
let running = false;
let lapCounter = 1;
let minutesPassed = 0;

const display = document.getElementById("display");
const emojiDisplay = document.getElementById("emoji");
const startStopBtn = document.getElementById("startStop");
const lapBtn = document.getElementById("lap");
const resetBtn = document.getElementById("reset");
const laps = document.getElementById("laps");
const quote = document.getElementById("quote");
const beep = document.getElementById("beep");

const quotes = [
    "⏳ Time is what we want most, but what we use worst.",
    "⌛ Lost time is never found again.",
    "💡 Your time is limited, don’t waste it living someone else’s life.",
    "⚔️ The two most powerful warriors are patience and time.",
    "🌅 Time flies over us, but leaves its shadow behind."
];

const moodEmojis = ["⏳", "⌛", "🕒", "🕓", "⏰", "🕰️", "💫", "🌈", "✨", "🔥"];

function updateQuote() {
    quote.textContent = quotes[Math.floor(Math.random() * quotes.length)];
}

function updateGlow(seconds) {
    const hue = (seconds * 36) % 360; // rotate colors faster
    document.documentElement.style.setProperty('--glow', `hsl(${hue}, 100%, 50%)`);
    document.body.style.background = `hsl(${hue}, 50%, 5%)`;
    emojiDisplay.textContent = moodEmojis[seconds % moodEmojis.length];
}

startStopBtn.addEventListener("click", () => {
    if (!running) {
        startTime = new Date().getTime() - difference;
        tInterval = setInterval(updateTime, 10);
        running = true;
        startStopBtn.innerText = "🛑 Stop";
    } else {
        clearInterval(tInterval);
        running = false;
        startStopBtn.innerText = "⏯ Start";
    }
});

lapBtn.addEventListener("click", () => {
    if (running) {
        const lapTime = document.createElement("div");
        lapTime.className = "lap-item";
        lapTime.textContent = `🏁 Lap ${lapCounter++}: ${display.textContent}`;
        laps.prepend(lapTime);
    }
});

resetBtn.addEventListener("click", () => {
    clearInterval(tInterval);
    running = false;
    display.firstChild.textContent = "00:00:00";
    emojiDisplay.textContent = "⏳";
    difference = 0;
    startStopBtn.innerText = "⏯ Start";
    laps.innerHTML = "";
    lapCounter = 1;
    minutesPassed = 0;
});

function updateTime() {
    updatedTime = new Date().getTime() - startTime;
    difference = updatedTime;
    
    let hours = Math.floor((difference / (1000 * 60 * 60)) % 24);
    let minutes = Math.floor((difference / (1000 * 60)) % 60);
    let seconds = Math.floor((difference / 1000) % 60);

    hours = (hours < 10) ? "0" + hours : hours;
    minutes = (minutes < 10) ? "0" + minutes : minutes;
    seconds = (seconds < 10) ? "0" + seconds : seconds;

    display.firstChild.textContent = `${hours}:${minutes}:${seconds}`;
    updateGlow(parseInt(seconds));

    if (parseInt(minutes) > minutesPassed) {
        minutesPassed = parseInt(minutes);
        beep.play();
        updateQuote();
    }
}