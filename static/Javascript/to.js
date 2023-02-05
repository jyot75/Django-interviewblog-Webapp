let ele = document.getElementById('my_search')
ele.addEventListener('keypress', () => {
    ele.textContent = ele.value
})