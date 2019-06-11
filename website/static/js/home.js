// Wrap every letter in a span
$('.text-intro .letters').each(function(){
    $(this).html($(this).text().replace(/([^\x00-\x80]|\w|,|')/g, "<span class='letter'>$&</span>"));
  });
  
  anime.timeline()
    .add({
      targets: '.text-intro .letter',
      translateY: ["1.1em", 0],
      translateZ: 0,
      duration: 1500,
      delay: function(el, i) {
        return 50 * i;
      }
    });