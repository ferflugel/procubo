const btn = document.getElementById('expMenu')

btn.children[0].addEventListener("click", function(){
  if(btn.children[0].className=='gg-chevron-right-o') {
    btn.children[0].className = 'gg-close-o';
    btn.children[1].className = 'openedMenu'
  } else {
    btn.children[0].className = 'gg-chevron-right-o';
    btn.children[1].className = 'closedMenu'
  }
})
