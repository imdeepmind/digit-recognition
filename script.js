var canvas = document.querySelector( 'canvas' ),
c = canvas.getContext( '2d' ),
mouseX = 0,
mouseY = 0,
width = 300,
height = 300,
colour = 'white',
mousedown = false;

canvas.width = width;
canvas.height = height;

function draw() {
    if (mousedown) {
        c.fillStyle = colour; 
        c.beginPath();
        c.arc( mouseX, mouseY, 10 , 0, Math.PI*2, true );
        c.closePath();
        c.fill();
    }
}

canvas.addEventListener( 'mousemove', function( event ) {
        if( event.offsetX ){
            mouseX = event.offsetX;
            mouseY = event.offsetY;
        } else {
            mouseX = event.pageX - event.target.offsetLeft;
            mouseY = event.pageY - event.target.offsetTop;
        }
        draw();
    }, false );

canvas.addEventListener( 'mousedown', function( event ) {
    mousedown = true;
}, false );
canvas.addEventListener( 'mouseup', function( event ) {
    mousedown = false;
}, false );



function clear_canvas(){
    c.clearRect(0, 0, canvas.width, canvas.height);
    console.log('clear');
}







// var link = document.createElement('a');
//     link.innerHTML = 'download image';
// link.addEventListener('click', function(ev) {
//     console.log(canvas.toDataURL());
//     // link.href = canvas.toDataURL();
//     // link.download = "mypainting.png";
// }, false);
// document.body.appendChild(link);