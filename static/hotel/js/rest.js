function btnClick(dishAdded)
{
    var cookieVal=[];
    var cookie=getCookie("added_dish");
    var data=document.cookie;
    if(cookie==''){
        cookieVal=[dishAdded];
        document.cookie = "added_dish="+cookieVal;
        console.log("first time size is="+cookieVal.length)
       }
    else{
        var updatedArr=[]
        cookieVal=getCookie("added_dish");
        console.log("size is="+cookieVal.length)
        for(i=0;i<cookieVal.length;i++){
            console.log("before cookie at "+i+"is="+cookieVal[i])
            updatedArr[cookieVal[i]]
        }
        updatedArr.push(dishAdded);
        for(i=0;i<cookieVal.length;i++)
            console.log("after cookie at "+i+"is="+cookieVal[i])
     }
}

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function checkCookie() {
    var user = getCookie("username");
    if (user != "") {
        alert("Welcome again " + user);
    } else {
        user = prompt("Please enter your name:", "");
        if (user != "" && user != null) {
            setCookie("username", user, 365);
        }
    }
}


