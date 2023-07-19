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

    //
    for(let i = 3; i<15;i++){
        let Attraction = result[i]["stitle"]
        let File=result[i]["file"]
        File = "https"+File.split('https')[1]
        
        //picbox創建div
        var SP1 = document.getElementById("picbox");
        console.log(SP1, 1)


        //創建ID陣列
        let ID =[]
        for(let i = 1; i<13;i++){
            ID.push("pic"+i.toString())
        }
        //製作一個完整圖和標題的function
        function adding(data){

            //在第一層div中再建div
            var small_title = document.createElement('div');
            small_title.id = data;
            SP1.appendChild(small_title);
            SP2 = document.getElementById(data);

            //創建第二層img
            var small_img = document.createElement('img');
            small_img.className = "smallpic";
            small_img.setAttribute('src', File);
            SP2.appendChild(small_img);
            
            //創建第二層標題div
            var small_title = document.createElement('div');
            small_title.className = "text2";
            small_title.textContent = Attraction
            SP2.appendChild(small_title);
        }

        if(i == 3){
            adding(ID[0]);
        }else if(i == 4){
            adding(ID[1]);
        }else if(i == 5){
            adding(ID[2]);
        }else if(i == 6){
            adding(ID[3]);
        }else if(i == 7){
            adding(ID[4]);
        }else if(i == 8){
            adding(ID[5]);
        }else if(i == 9){
            adding(ID[6]);
        }else if(i == 10){
            adding(ID[7]);
        }else if(i == 11){
            adding(ID[8]);
        }else if(i == 12){
            adding(ID[9]);
        }else if(i == 13){
            adding(ID[10]);
        }else{
            adding(ID[11]);
        }
       
    }   
}    
    
)
