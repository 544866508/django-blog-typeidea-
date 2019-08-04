//只在首次打开主页时展示站点介绍，3秒内自动折叠，折叠动画采用css的trainstion，在base.html中
function close_introduce() {
    var once = getCookie("once");
    if(once == ""){
        setCookie("once","not");    //不设置存储时间的话，默认关闭浏览器时清空cookie
        document.getElementById("my_site_introduce").style.height = '0px';
    }
    if(once == "not"){
        document.getElementById("my_site_introduce").style.display = 'none';
    }
}
window.onload = close_introduce;






