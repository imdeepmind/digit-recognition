
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
        c.arc( mouseX, mouseY, 7 , 0, Math.PI*2, true );
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
	c.fillStyle = 'rgba(0,0,0,1)';
    c.fillRect(0,0,window.innerWidth,window.innerHeight);
}
function upload(){
	var data = canvas.toDataURL();
	var url = 'https://desolate-bastion-43688.herokuapp.com/recognize/';
	
	$.ajax({
		type: "POST", 
		url: url,
		data: {
			"file" : data
        },
        beforeSend: function(){
            $('.ans').html('analysing image');
        },
		success: function(e){
			if (e.success){
                $('.ans').html(e.data.digit);
            }
		}
	});
}
clear_canvas()


