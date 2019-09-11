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


$("#id_Name").on('input propertychange', function(f) {
    let _input_limit = /^[\u4e00-\u9fa5]|\w+$/;
    let _all_input_string = $("#id_Name").val();
    if(_all_input_string.length < 11){
        for(let i=0;i<_all_input_string.length;i++){
            if(!_input_limit.test(_all_input_string[i])){
                $("#id_Name").val(null);
            }
        }
    }else {
        _all_input_string = _all_input_string.slice(0 , 11);
        for(let i=0;i<_all_input_string.length;i++){
            if(!_input_limit.test(_all_input_string[i])){
                $("#id_Name").val(null);
                break;
            }
        }
        $("#id_Name").val(_all_input_string);
    }

});

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
    $.ajax({
        url:"/user/",
        type:"POST",
        data:{
            TARGET:"consumer_is_exist",
            ACT:_all_input_string,
            csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val(),
        },
        dataType:'json',
        success:function (data) {
            if(data.result === "true"){
                console.log("用户已经存在,请返回登录或重新注册");
            }else if(data.result === "false"){
                console.log("可用的账号");
            }
        }
    });
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
$("#id_RePassword").on('input propertychange', function(f) {
    let _input_limit = /^\w+$/;
    let _Pwd = $("#id_Password").val();
    let _RePwd   = f.currentTarget.value;
    if(_Pwd !== _RePwd){
        console.log("密码不一致");
    }
});

$("#id_Phone").on('input propertychange', function(f) {
    let _input_limit = /^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/;
    let _Phone = $("#id_Phone").val();
    if(!_input_limit.test(_Phone)){
        console.log("不正确的电话号码");
    }else {
        console.log("$$$$$$");
    }
});
$("#id_Email").on('input propertychange', function(f) {
    let _input_limit = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
    let _Email = $("#id_Email").val();
    if(!_input_limit.test(_Email)){
        console.log("不正确的Email");
    }else {
        console.log("$$$$$$");
    }
});












