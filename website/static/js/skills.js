var skills = {
    'cpp': 100,
    'python': 100,
    'c': 100,
    'js': 80,
    'java': 70,
    'mysql': 60,
    'flask': 90,
    'opengl': 80,
    'tensorflow': 75,
    'numpy': 75,
    'pandas': 75,
    'vue': 70
};


function doAnim()
{
    var elements = document.getElementsByClassName('to-anim');
    var width = 0;
    var f = setInterval(anim, 10);

    function anim()
    {
        if(width >= 100)
        {
            clearInterval(f);
        }
        else
        {
            width++;
            for(var i = 0; i < elements.length; i++)
            {
                var elem = elements[i];
            
                if(width <= skills[elem.id])
                {
                    elem.style.width = width + '%';
                }
    
            }
        }   
    }
}

window.onload = function()
{
    this.doAnim();
}