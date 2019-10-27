
function renderCanvas(canvas)
{
    
    ctx = canvas.getContext('2d');
    ctx.canvas.width = window.innerWidth * 0.4;
    ctx.canvas.height = window.innerHeight * 0.7;

    var drawElement = function(id, c_x, c_y, radius, text, text_size, text_center_x, text_center_y, vel_x, vel_y)
    {
        this.id = id;
        this.c_x = c_x;
        this.c_y = c_y;
        this.radius = radius;
        this.hover = false;
        this.text = text;
        this.text_size = text_size;
        this.text_center_x = text_center_x;
        this.text_center_y = text_center_y;
        this.scale = 1.0;
    }

    drawElement.prototype.draw = function(){
        var toScale = this.hover;
        if(toScale && this.scale < 1.5)
            this.scale = this.scale + 0.1;
        else if(!toScale && this.scale > 1.0)
            this.scale = this.scale - 0.1;

        var radius = this.radius * this.scale;
        ctx.fillStyle = "#feda6a";
        ctx.beginPath();
        ctx.arc(this.c_x, this.c_y, radius, 0, Math.PI*2, false);
        ctx.fill();
        ctx.fillStyle = "#ffffff";
        ctx.font = this.text_size + ' Raleway';
        ctx.fillText(this.text, this.text_center_x, this.text_center_y);

    }

    drawElement.prototype.hovering = function(x, y){
        return x >= this.c_x - this.radius && x <= this.c_x + this.radius && y <= this.c_y + this.radius && y >= this.c_y - this.radius;
    }

    var Board = function(element)
    {
        this.element = element;
        this.drawElements = [];
    } 

    Board.prototype.addDrawElement = function(element){
        this.drawElements.push(element);
    }

    Board.prototype.render = function(){
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        this.element.width = this.element.width;
        for(var i = 0; i < this.drawElements.length; i++)
        {
            this.drawElements[i].draw();
        }

        ctx.strokeStyle = "#feda6a";
        for(var i = 0; i < this.drawElements.length; i++)
        {
            ctx.beginPath();
            ctx.moveTo(this.drawElements[i].c_x, this.drawElements[i].c_y);
            ctx.lineTo(this.drawElements[(i + 1) % this.drawElements.length].c_x,this.drawElements[(i + 1) % this.drawElements.length].c_y);
            ctx.stroke();            
        }
    }


    Board.prototype.setHover = function(selectedElement){
        for(var i = 0; i < this.drawElements.length; i++)
        {
            this.drawElements[i].hover = (this.drawElements[i] == selectedElement);
        }
        this.render();
    }

    Board.prototype.select = function(x, y){
        for(var i =0 ; i < this.drawElements.length; i++)
        {
            if(this.drawElements[i].hovering(x,y))
            {
                return this.drawElements[i];
            }
        }
        return null;
    }

    var board = new Board(ctx);
    var element1 = new drawElement(1, 300 ,150 , 70, "About", '20pt', 265, 155);
    var element2 = new drawElement(2, 650, 300, 60, "Contact", '15pt', 617, 305);
    var element3 = new drawElement(3, 450, 450, 80, "Skills", '20pt', 420, 460);

    board.addDrawElement(element1);
    board.addDrawElement(element2);
    board.addDrawElement(element3);

    board.render();

    function onMouseMove(event)
    {
        var x = event.x - canvas.offsetLeft;
        var y = event.y - canvas.offsetTop;

        var el = board.select(x, y);

        board.setHover(el);
    }

    function onMouseClick(event)
    {
        var x = event.x - canvas.offsetLeft;
        var y = event.y - canvas.offsetTop;

        var el = board.select(x, y);

        if(el === null)
            return;
        
        window.location.href = "/"+el.text.toLowerCase();
    }

    canvas.addEventListener('mousemove', onMouseMove);
    canvas.addEventListener('mouseup', onMouseClick);

}





var canvas = document.getElementById('draw-canvas');

if(canvas.getContext)
{
    renderCanvas(canvas);
}
else
{
   // nothing
}   