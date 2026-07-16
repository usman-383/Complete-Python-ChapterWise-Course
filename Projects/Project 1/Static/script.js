//javaScript file
function playSound(name) {
    const sound = document.getElementById(name);
    if (sound) {
        sound.currentTime = 0;
        sound.play().catch(err => {
            console.log("Sound blocked:", err);
        });
    }
}
