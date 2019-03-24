const NUM_PARTICLES = 300;
const FRAMES_PER_SEC = 30;
const FILL_STYLE = "#0d203f"

function init()
{
    canvas = document.getElementById('canvas')
    context = canvas.getContext('2d')
    var dpi = window.devicePixelRatio

    // Removes pixelation
    canvas.setAttribute('height', canvas.clientHeight * dpi)
    canvas.setAttribute('width', canvas.clientWidth * dpi)

    // Set background color
    //context.fillStyle = "#3a4660"  // blueish
    //context.fillStyle = "#7dce94" //greenish
    
    context.fillStyle = FILL_STYLE
    context.fillRect(0,0,canvas.width, canvas.height)
    context.stroke()

    

}

init()

class Particle
{
    // Fields are still not supported in IE, Firefox

    /*vx; // velocity in x-axis
    vy; // velocity in y-axis
    px; // position in x-axis
    py; // position in y-axis*/

    constructor()
    {    
        this.vy = 5;
        this.vx = Math.floor(Math.random()*2)-1
        this.px = Math.floor(Math.random() * canvas.width);
        this.py = Math.floor(Math.random()*canvas.height);
    }

    update()
    {
        
        this.py = this.py + this.vy;
        this.px = this.px + this.vx;
        
        if(this.px + this.vx < 0)
        {
            this.px = canvas.width
        }

        else if(this.px + this.vx > canvas.width)
        {
            this.px = 0
        }

        if(this.py + this.vy > canvas.height)
        {
            this.py = 0;
        }

    }

    draw()
    {
        context.strokeStyle = "#ffffff"
        context.rect(this.px, this.py, 0.75, 0.75)
        context.stroke()
    }
}



(function makeParticles()
{
    particles = []

    for(var i = 0 ; i < NUM_PARTICLES; i++)
    {
        particles.push(new Particle());
    }
}());

function drawParticles()
{
    context.beginPath();
    for(var i = 0 ; i < NUM_PARTICLES; i++)
    {
        particles[i].draw();
    }
    context.closePath();
};

function updateParticles()
{
    for(var i = 0; i < NUM_PARTICLES; i++)
    {
        particles[i].update();
    }
}

function clearCanvas()
{
    context.fillStyle = "rgba(0,0,0,0)";
    context.clearRect(0,0,canvas.width, canvas.height)

    context.fillStyle = FILL_STYLE
    context.fillRect(0,0,canvas.width, canvas.height)
}

function getMousePosition(e)
{
    var rect = canvas.getBoundingClientRect();

    return  {
        x: e.clientX - rect.left,
        y: e.clientY - rect.top
    }
}

setInterval(function(){
    clearCanvas();
    updateParticles();
    drawParticles();
}, 1000/FRAMES_PER_SEC)
