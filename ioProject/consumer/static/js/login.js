//main-box高度自适应
let screenHeight = window.screen.height;
let mainBoxCss = {
    "height":screenHeight-101,
};
$("#main-box").css(mainBoxCss);

//旋转    main-half-box
rotateMainHalfBox();
function rotateMainHalfBox(){
    let rotateWidth = document.getElementById('main-box').offsetWidth;
    let rotateHeight = document.getElementById('main-box').offsetHeight;
    let rotateDeg = Math.atan(rotateHeight/rotateWidth)/(Math.PI / 180);
    let mainHalfBoxCss = {
        "width": "3000px",
        "height": rotateHeight + "px",
        "background": "aquamarine",
        "transform-origin": "0px 0px",
        "transform": "rotate("+rotateDeg+"deg)",
    };
    $("#main-half-box").css(mainHalfBoxCss).show();
}

window.onresize = function(){
    rotateMainHalfBox();
};


$("#id_Account").on('input propertychange', function(f) {
    let _input_limit = /^\w+$/;
    let _all_input_string = $("#id_Account").val();
    if(_all_input_string.length < 20){
        for(let i=0;i<_all_input_string.length;i++){
            if(!_input_limit.test(_all_input_string[i])){
                $("#id_Account").val(null);
            }
        }
    }else {
        _all_input_string = _all_input_string.slice(0 , 20);
        for(let i=0;i<_all_input_string.length;i++){
            if(!_input_limit.test(_all_input_string[i])){
                $("#id_Account").val(null);
                break;
            }
        }
        $("#id_Account").val(_all_input_string);
    }
});

$("#id_Password").on('input propertychange', function(f) {
    let _input_limit = /^\w+$/;
    let _all_input_string = $("#id_Password").val();
    if(_all_input_string.length < 18){
        for(let i=0;i<_all_input_string.length;i++){
            if(!_input_limit.test(_all_input_string[i])){
                $("#id_Password").val(null);
            }
        }
    }else {
        _all_input_string = _all_input_string.slice(0 , 18);
        for(let i=0;i<_all_input_string.length;i++){
            if(!_input_limit.test(_all_input_string[i])){
                $("#id_Password").val(null);
                break;
            }
        }
        $("#id_Password").val(_all_input_string);
    }
});












