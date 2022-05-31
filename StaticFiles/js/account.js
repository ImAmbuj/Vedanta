var LoginForm = document.getElementById("LoginForm");
var RegForm = document.getElementById("RegForm");
var Indi = document.getElementById("Indi");
   
 function register(){
     RegForm.style.transform = "translateX(0px)";
     LoginForm.style.transform = "translateX(0px)";
     Indi.style.transform = "translateX(100px)";
 }
 function login(){
     RegForm.style.transform = "translateX(300px)";
     LoginForm.style.transform = "translateX(300px)";
     Indi.style.transform = "translateX(0px)";
 }

document.getElementById("dismiss-popup-btn").addEventListener("click",function(){
    document.getElementsByClassName("popup")[0].classList.remove("active");
});



