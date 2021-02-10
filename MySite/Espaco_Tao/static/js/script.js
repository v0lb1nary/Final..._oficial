function getPosicaoElemento(elemID) {
    var Trail = document.getElementById(elemID);
    var getLeft = 0;
    var getTop = 0;
    var getBottom = 0;
    while (Trail) {
        getLeft += Trail.offsetLeft;
        getTop += Trail.offsetTop;
        getBottom += Trail.offsetHeight;
        Trail = Trail.offsetParent;
    }
    return { left: getLeft, top: getTop, bottom:getBottom };
}
    
function setPosicao_navs(id_set, id_get_Lf, id_get_Bt) {
    var left = (getPosicaoElemento(id_get_Lf).left - 2)
    var buttom = (getPosicaoElemento(id_get_Bt).bottom)

    console.log(buttom);
    document.getElementById(id_set).style.left = left.toString() + "px";
    document.getElementById(id_set).style.buttom = buttom.toString() + "px";
}


function camp_nav_visible(id) {
        if (id == "camp_nav_01") {
        document.getElementById("camp_visible_nav_01").style.visibility = "visible";
        document.getElementById("camp_nav_01").style.borderBottom = "1px solid black";
        } else {
            if (id == 'camp_nav_02') {
                document.getElementById("camp_visible_nav_02").style.visibility = "visible";
                document.getElementById("camp_nav_02").style.borderBottom = "1px solid black";
                document.getElementById("seta").style.visibility = "hidden";
            } else {}
    }
}

function camp_nav_invisible(id) {
    if (id == "camp_nav_01") {
        document.getElementById("camp_visible_nav_01").style.visibility = "hidden";
        document.getElementById("camp_nav_01").style.borderBottom = "0";
    } else {
        if (id == 'camp_nav_02') {
            document.getElementById("camp_visible_nav_02").style.visibility = "hidden";
            document.getElementById("camp_nav_02").style.borderBottom = "0";
            document.getElementById("seta").style.visibility = "visible";
        } else {}
    }
}


