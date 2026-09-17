const ilya = document.getElementById('ilya!')
ilya.addEventListener('dblclick', function() {
    let originalText = ilya.textContent
    this.textContent = "Это я!"
    setTimeout(() => {
        this.textContent = originalText
    }, 2000)
})
const ilya_bushmelev = document.getElementById('ilya-bushmelev')
ilya_bushmelev.addEventListener('dblclick', function() {
    let originalText = this.textContent
    this.textContent = "Мой ник на GitHub!"
    setTimeout(() => {
        this.textContent = originalText
    },2000)
})
const chizhik = document.getElementById('footer-chizhik')
chizhik.addEventListener('dblclick', function() {
    let originalText = chizhik.textContent
    console.log('%cЧижик: "Я люблю семечки!"', 'color:#0f0; font-size: 16px;')
    this.textContent = "Кря! Где мои семечки?";
    setTimeout(() => {
        this.textContent = originalText;
    }, 2000)
})
const pyzhulya = document.getElementById('footer-pyzhulya');
pyzhulya.addEventListener('dblclick', function() {
    let originalText = pyzhulya.textContent
    this.textContent = 'я особенная.';
    console.log('%cПыжуля: "ты нашёл меня? или ты изучаешь сайт?"', 'color:#dd0; font-size: 16px;')
    setTimeout(() => {
        this.textContent = originalText;
    }, 2000)
});
console.log("%cIlya's:Shell","background: linear-gradient(90deg, #0f0, #0ff); background-clip: text; color: transparent; font-size: 24px; font-weight: 700;")
console.log("знали бы вы КАК Я ЗАДОЛБАЛСЯ")