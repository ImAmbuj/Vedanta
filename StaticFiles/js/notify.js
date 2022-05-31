var box = document.getElementById('box');
var down = false;
function toggleNotify(){
    if (down){
        box.style.height = '0px';
        box.style.opacity = 0;
        down = false;
        box.style.zIndex = 0;
    }else{
        box.style.height = '410px';
        box.style.opacity = 1;
        down = true;
        box.style.zIndex = 2;
    }
}