let result;
let url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
fetch(url).then(function(response){
        return response.json()    
}).then(function(data){
    result =data["result"]["results"]
    for(let i = 0; i<3;i++){
        let Attraction = result[i]["stitle"]
        let File=result[i]["file"]
        File = "https"+File.split('https')[1]
        if(i == 0){
            var SP = document.getElementById("label1");
        }else if(i == 1){
            var SP = document.getElementById("label2");
        }else{
            var SP = document.getElementById("label3");
    }
        // 建立img
        var small_img = document.createElement('img');
        small_img.className = "smallpic";
        small_img.setAttribute('src', File);
        SP.appendChild(small_img);

        //建立小標題
        var small_title = document.createElement('div');
        small_title.textContent = Attraction
        SP.appendChild(small_title);
    }

    //picbox創建div
    var SP1 = document.getElementById("picbox2");
    //先建立12個box, 再將資訊以Loop 方式放進去
    function Create_box(){
        for(let i = 0; i<12;i++){
            let BOX = document.querySelectorAll('#box');
            var box_div = document.createElement('div');
            box_div.id = "box";
            if(BOX.length<55){
            // box_div.textContent = "frfr "
            SP1.appendChild(box_div);
            // SP2 = document.getElementById("box");
            }else{
                //pass
            }
            }

    }
    function button(){
        var btn = document.createElement('div');
        btn.id = "btn";
        btn.textContent = "Loading";
        btn.onmousedown = function(){
            btn.style.color = "black";
            Create_box();
            put_In();
        };
        document.body.appendChild(btn);
    }
    Create_box();
    button();
    
    function put_In(){
        let BOX = document.querySelectorAll('#box');
        console.log(BOX)
        for(let box in BOX){
            if(BOX[box].innerHTML == ""){
                let pic_num = parseInt(box) + 3;
                
                let Attraction = result[pic_num]["stitle"];
                let File=result[pic_num]["file"];
                File = "https"+File.split('https')[1];
                
                var small_img = document.createElement('img');
                small_img.className = "smallpic";
                small_img.setAttribute('src', File);
                BOX[box].appendChild(small_img);

                // 創建第二層標題div
                var small_title = document.createElement('div');
                small_title.className = "text2";
                small_title.textContent = Attraction;
                BOX[box].appendChild(small_title);
            }else{
                //pass
            }
            }
        }
    put_In();

}    
)


