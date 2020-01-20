//构造一个数字
function random_one() {
    //x上限，y下限
    var x = 99999999;
    var y = 0;
    var k = parseInt(Math.random() * (x - y + 1) + y);
    var v = PrefixInteger(k, 7);
    return v;
}

function get_ten_num() {
    let array_data = [];
    for (var i=0; i<10; i++) {
        var key = random_one();
        array_data.push(key);
    }
    return array_data
}

//格式化数字,自动补0
function PrefixInteger(num, n) {
    return (Array(n).join(0) + num).slice(-n);
}