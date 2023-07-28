document.getElementById("btn").addEventListener('submit', (e)=>{
    let q = document.getElementById("checked")
    let Accout = document.getElementById("account")
    let Password = document.getElementById("password")

    if(!q.checked){
        alert("請同意會員條款");
        e.preventDefault();
    }else{
        //pass
    }
}
)

document.getElementById("forms").addEventListener("submit", function(event) {
    event.preventDefault(); 
    let number = document.getElementById("count").value;
    number = Number(number);
    if(Number.isInteger(number) == false || number<0){
        alert("請輸入正整數");
    }else{
        let square_url = '/square/'+ number;
        window.location.href = square_url;
    }
});


