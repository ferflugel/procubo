var elem = document.getElementById("dummy");

var list;
list = ["Hello", "world", "my", "name", "is", "dummy"];

var newCode = '<p>';
for (var i = 0; i < list.length; i++) {
    newCode = newCode + list[i] + '<br>';
}
newCode = newCode + '<\p>'

elem.innerHTML = newCode
