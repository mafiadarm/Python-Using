window.onload = function () {
    var level = $(".level").text();
    //console.log(level);

    var divVal1 = document.getElementById("show1");
    var divVal2 = document.getElementById("show2");
    var divVal3 = document.getElementById("show3");
    var divVal4 = document.getElementById("show4");
    var divVal5 = document.getElementById("show5");
    var divVal6 = document.getElementById("show6");
    var divVal7 = document.getElementById("show7");
    var divVal8 = document.getElementById("show8");
    var divVal9 = document.getElementById("show9");
    var divVal0 = document.getElementById("show0");
    var interV;
    sessionStorage.setItem("status", 0);

    $("#go_find").click(function () {
        var status = sessionStorage.getItem("status");

        if (status == 0) {
            $.get("/eBxdaE/", {"level": level}, function (data) {number = eval(data);});
            sessionStorage.setItem("status", 1);
            interV = setInterval(function () {  //while start
                var random_data = get_ten_num();
                divVal1.innerHTML = random_data[0];
                divVal2.innerHTML = random_data[1];
                divVal3.innerHTML = random_data[2];
                divVal4.innerHTML = random_data[3];
                divVal5.innerHTML = random_data[4];
                divVal6.innerHTML = random_data[5];
                divVal7.innerHTML = random_data[6];
                divVal8.innerHTML = random_data[7];
                divVal9.innerHTML = random_data[8];
                divVal0.innerHTML = random_data[9];
            }, 50);  //50 per

            // $("#go_find").html("停");
        }
        else if (status == 1) {
            sessionStorage.setItem("status", 0);
            window.clearInterval(interV);
            // console.log(number);
            divVal1.innerHTML = number[1];
            divVal2.innerHTML = number[2];
            divVal3.innerHTML = number[3];
            divVal4.innerHTML = number[4];
            divVal5.innerHTML = number[5];
            divVal6.innerHTML = number[6];
            divVal7.innerHTML = number[7];
            divVal8.innerHTML = number[8];
            divVal9.innerHTML = number[9];
            divVal0.innerHTML = number[0];


            // $("#go_find").html("开始抽奖");
        }
    });
};
