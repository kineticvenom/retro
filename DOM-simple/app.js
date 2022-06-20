// const btn = document.querySelector('button');

// function random(number) {
//   return Math.floor(Math.random() * (number+1));
// }

// function bgChange(e) {
//   const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
//   e.target.style.backgroundColor = rndCol;
//   console.log(e);
// }

// btn.addEventListener('click', bgChange);

// const btn = document.querySelector('.off');
// let click = 0
// btn.addEventListener('click', () => {
//     click+=1  
//     console.log('click',click)
     
//     // if (btn.textContent === 'Machine is off'){
//     //     btn.textContent = 'Machine is on'
//     // } else if(btn.textContent === 'Machine is on'){
//     //     btn.textContent = 'Machine is off'
//     // }
//     if (click%2 === 0){
//         btn.textContent = 'Machine is off'
//     } else{
//         btn.textContent = 'Machine is on'
//     }
// })
// Add your code here

const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

function drawCircle(x, y, size) {
  ctx.fillStyle = 'white';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.beginPath();
  ctx.fillStyle = 'black';
  ctx.arc(x, y, size, 0, 2 * Math.PI);
  ctx.fill();
}

let x = 50;
let y = 50;
const size = 30;

drawCircle(x, y, size);

canvas.addEventListener('keydown', (e) => {
    console.log('keydown')
    if (e.key === 'w'){
        y-= 1
    }
    if(e.key === 's'){
        y+=1
    }
    if(e.key === 'a'){
        x-=1
    }
    if(e.key === 'd'){
        x+=1
    }

    drawCircle(x,y,size)
})