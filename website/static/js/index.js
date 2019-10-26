
function renderCanvas(canvas)
{
    
    ctx = canvas.getContext('2d');
    ctx.canvas.width = window.innerWidth * 0.4;
    ctx.canvas.height = window.innerHeight * 0.7;

    var drawElement = function(id, c_x, c_y, radius, text)
    {
        this.id = id;
        this.c_x = c_x;
        this.c_y = c_y;
        this.radius = radius;
        this.hover = false;
        this.text = text;
    }

    drawElement.prototype.draw = function(){
        var scale = this.hover ? 1.5: 1;
        var radius = this.radius * scale;
        ctx.fillStyle = "#feda6a";
        ctx.beginPath();
        ctx.arc(this.c_x, this.c_y, radius, 0, Math.PI*2, false);
        ctx.fill();
        ctx.fillStyle = "#ffffff";
        ctx.fillText(this.text, this.c_x, this.c_y);
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
    var element1 = new drawElement(1, 150 ,150 , 60, "About");
    var element2 = new drawElement(2, 500, 300, 45, "Contact");
    var element3 = new drawElement(3, 300, 450, 60, "Skills");

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