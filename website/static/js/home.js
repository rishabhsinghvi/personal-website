var links = document.querySelectorAll('.ext_link');

var width = window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

var height = window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;


$('.text-intro .letters').each(function(){
    $(this).html($(this).text().replace(/([^\x00-\x80]|\w|,|')/g, "<span class='letter'>$&</span>"));
  });
  
anime.timeline()
    .add({
      targets: '.text-intro .letter',
      translateY: ["1.2em", 0],
      translateZ: 0,
      duration: 1500,
      delay: function(el, i) {
        return 50 * i;
      }
    })
    .add({
      targets: links,
      translateX: [-width, 0],
      delay: function(el, i, t){
        return i*100;
      },
      endDelay: function(el, i, t)
      {
        return (t-i)*100;
      },
      duration: 2000
    });

    