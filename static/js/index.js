var searchbtn = document.getElementById("searchbtn");
$(function () {
    $('#date').datetimepicker({
        format: 'YYYY-MM-DD',
        locale: 'zh-CN'
    });
    if (obj.hasOwnProperty("hcity")) {
        const tag = obj["hcity"];
        $('#hot_city li').eq(0).removeClass('active');
        $('#hot_city li').eq(tag - 1).addClass('active');
    }
});
searchbtn.onclick = function () {
    var city = $("#search_city").val();
    var date = $("#search_date").val();
    if (city === '') {
    } else {
        location.href = url+'/search/?city='+city+'&date='+date;
    }
}