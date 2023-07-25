
function pop(){
    var q = document.getElementById("checked")
    console.log(q.checked)
    if(!q.checked){
        alert("請勾選同意條款")
    }else{
        //pass
    }
}

function notInt(){
    var a = document.getElementById("count").value
    a = Number(a);
    if(Number.isInteger(a) == false){
        alert("請輸入正整數");
    }else{
        //pass
    }
    


}