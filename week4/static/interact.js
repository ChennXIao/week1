document.getElementById("btn").addEventListener('submit', (e)=>{
    var q = document.getElementById("checked")
    if(!q.checked){
        alert("請同意會員條款");
        e.preventDefault();
        return false;
    }else{
        //pass
    }
}
)

document.getElementById("forms").addEventListener("submit", function(event) {
    event.preventDefault(); 
    var number = document.getElementById("count").value;
    number = Number(number);
    if(Number.isInteger(number) == false || number<0){
        alert("請輸入正整數");
    }else{
        var square_url = '/square/'+ number;
        window.location.href = square_url;
    }
});


