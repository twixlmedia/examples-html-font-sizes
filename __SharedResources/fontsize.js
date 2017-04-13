function changeFontSize(scale) {
    saveFontScale(scale);
    var p = document.getElementsByTagName('p');
    for (n = 0; n < p.length; n++) {
        p[n].style.fontSize = (16 * (scale / 100)) + 'px';
        p[n].style.lineHeight = (16 * (scale / 100) * 1.5) + 'px';
    }
}

function saveFontScale(scale) {
    localStorage.setItem("com.myapp.id.fontScale", scale);
}

function restoreFontScale() {
    var scale = localStorage.getItem("com.myapp.id.fontScale");
    if (scale == undefined) {
        scale = 100;
    }
    changeFontSize(scale);
}
