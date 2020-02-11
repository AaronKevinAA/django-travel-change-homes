var url = 'http://127.0.0.1:8000';
var path = window.location.pathname;
var search = window.location.search;
var obj = {};
$(document).ready(function () {
    //如果字符串里面存在?
    if (search.indexOf("?") !== -1) {
        //从url的索引1开始提取字符串
        var str = search.substring(1);
        //如果存在&符号，则再以&符号进行分割
        var arr = str.split("&");
        //遍历数组
        for (var i = 0; i < arr.length; i++) {
            obj[arr[i].split("=")[0]] = unescape(arr[i].split("=")[1]);
        }
    }
});