function setCookie(cname,cvalue)
{
    document.cookie = cname + "="+ escape (cvalue);
}


function getCookie(cname)
{
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++)
    {
    var c = ca[i].trim();
    if (c.indexOf(name)==0) return c.substring(name.length,c.length);
    }
    return "";
}


function delCookie(cname)
{
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cvalue=getCookie(cname);
    if(cvalue!=null)
    document.cookie= cname + "="+cvalue+";expires="+exp.toGMTString();
}