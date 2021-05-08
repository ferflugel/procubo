const realFileBtn = document.getElementById("actualBtn");
const customBtn = document.getElementById("customBtn");
const customTxt = document.getElementById("customTxt");

customBtn.addEventListener("click", function() {
  realFileBtn.click();
});

realFileBtn.addEventListener("change", function() {
  if (realFileBtn.value) {
    customTxt.innerHTML = realFileBtn.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[1];
  } else {
    customTxt.innerHTML = "No file chosen, yet.";
  }
});

//Applies the 'click' event listener to all buttons to prevent repetition
let inputs = document.querySelectorAll('.inputOptions');
inputs.forEach(element => {
  element.children[1].addEventListener("click", function(){
    if(element.children[1].className=='gg-chevron-right-o') {
      element.children[1].className = 'gg-close-o';
      element.children[2].style.display = 'block';
      element.children[2].className = 'openedMenu';
    } else {
      element.children[1].className = 'gg-chevron-right-o';
      element.children[2].className = 'closedMenu';
      setTimeout(() => {element.children[2].style.display = 'none';}, 500);
    }
  });
});
