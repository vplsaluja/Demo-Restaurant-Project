
/*function btnClick(dishAdded)
{
    if(dishAdded!=0){
        var cookieVal=[];
        var cookie=getCookie("added_dish");
        var data=document.cookie;
        {document.getElementById("go_to_cart").style.display="block";}
        if(cookie==''){
            cookieVal.push(dishAdded);
        }
        else{
            cookieVal=[];
            var cookies=[getCookie("added_dish")];
            console.log("size is="+cookies.length);
            for(i=0;i<cookies.length;i++){
                cookieVal.push(cookies[i]);
            }
            cookieVal.push(dishAdded);
        }
        document.cookie = "added_dish="+cookieVal+";path=/;";
     }
     else{
        window.location.href="/cart";
     }
}*/

function btnClick(dishAdded)
{
    if(dishAdded!=0){

        var cookieVal=new Object();

        var cookie=getCookie("added_dish");
        {document.getElementById("go_to_cart").style.display="block";}
        if(cookie==''||cookie==null){
            cookieVal[dishAdded]=1;
            document.cookie = "added_dish="+JSON.stringify(cookieVal)+";path=/;";
        }
        else{
            cookieVal=JSON.parse(getCookie("added_dish"));
            quantity=cookieVal[dishAdded];
            if(quantity==undefined)
                quantity=0;
            cookieVal[dishAdded]=quantity+1;
            document.cookie = "added_dish="+JSON.stringify(cookieVal)+";path=/;";
        }

     }
     else{
        window.location.href="/cart";
     }
}


function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + "; path=/;";
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
            return (c.substring(name.length, c.length));
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

//set the past time to delete a cookie along with its path
var delete_cookie = function(name) {
    document.cookie = name + '=;Path=/;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
};

function onCheckoutClick()
{
//    delete_cookie("added_dish");
    window.location.href="/checkout";
}
