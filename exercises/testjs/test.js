


const split_test="co-co-cat".split("-");
console.log(split_test);
const a = split_test[2];
console.log("a");

const login=greet("Miyui");
function greet(name){
    const greets=name+"さん、こんにちは"
    return greets;
}


// let btn_node = document.getElementById("text_change_button");
// btn_node.addEventListener("click",changetext);
// function changetext(){
// let text_node=document.getElementById("text")
// text_node.textContent="8:15";
// }

$(function($){
    $("#text").text("こうしん！！");
});
