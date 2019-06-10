var CONTACT_OPEN = false;
var ANIMATE_WIDTH = 52;
var elem = document.getElementById('contact-container')
function contactMe()
{
    if(CONTACT_OPEN === false)
    {
        CONTACT_OPEN = true;
    }
    else
    {
        CONTACT_OPEN = false;
    }
    animateSidebar(CONTACT_OPEN)
}


function animateSidebar(val)
{
    if(val==true)
    {
        var currentVal = ANIMATE_WIDTH
        var interval = setInterval(function(){
            elem.style['left'] = currentVal + 'vh'
            currentVal -= 1;
            console.log(currentVal)
            if(currentVal === -1)
                clearInterval(interval);
        },2);
    }
    else
    {
        var currentVal = 0;
        var interval = setInterval(function(){
            elem.style['left'] = currentVal + 'vh'
            currentVal += 1;
            console.log(currentVal)
            if(currentVal === ANIMATE_WIDTH)
                clearInterval(interval);
        },2);
    }
}