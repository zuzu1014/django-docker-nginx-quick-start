


function flex(element) {
    element.style.display = "flex";
}

function block(element) {
    element.style.display = "block";
}

function hide(element) {
    element.style.display = "none";
}

function blur(element) {
    element.style.opacity = "0.7";
}

function shuffle(a) {
    console.log(a)
    let j,
        x,
        i;
    for (i = a.length; i; i -= 1) {
        j = Math.floor(Math.random() * i);
        x = a[i - 1];
        a[i - 1] = a[j];
        a[j] = x;
    }
    return a;
}

const generateRandom = function (min, max) {
    let ranNum = Math.floor(Math.random() * (max - min + 1)) + min;
    return ranNum;
};

const generateOrderdArray = (start, finish) => {
    return new Promise((resolve, reject) => {
        let orderdArray = []
        for (let i = start; i < finish + 1; i++) {
            orderdArray.push(i)
        }
        resolve(orderdArray)
    })
}


/* var */


let flag__rememberCheckbox = 0
let flag__searchbar = 0

