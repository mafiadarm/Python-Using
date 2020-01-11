window.onload = function () {
    var interV;
    sessionStorage.setItem("status", 0);

    $("#go_find").click(function () {
        var status = sessionStorage.getItem("status");

        if (status == 0) {
            $.get("/szPEZb/", function (data) {number = data;});
            sessionStorage.setItem("status", 1);
            interV = setInterval(function () {  //while start
                var val = random_one();
                $("#one_jiangpiao").html("<h2 id=\"text3d\">" + val + "</h2>");
            }, 50);  //50 per

            // $("#go_find").html("停");
        }
        else if (status == 1) {
            sessionStorage.setItem("status", 0);
            window.clearInterval(interV);
            $("#one_jiangpiao").html("<h2 id=\"text3d\">" + number + "</h2>")

            // $("#go_find").html("开始抽奖");
        }
    });
};