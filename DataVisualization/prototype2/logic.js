
function openFile(event) {
  var input = event.target;

  var reader = new FileReader();
  reader.onload = function(){
    var dataURL = reader.result;
    var output = document.getElementById('UpFile');
    output.src = dataURL;
    console.log(dataURL);
    var text = document.getElementById("loadedFile");
    var str = (output.value.split("\\")[output.value.split("\\").length - 1]).split(".");
    text.innerHTML = "<b>Loaded file: </b>"+ str[0].substring(0, 5) + "..." + str[1] ;
    text.style.fontSize = "18px";
  };
  reader.readAsText(input.files[0]);
};
