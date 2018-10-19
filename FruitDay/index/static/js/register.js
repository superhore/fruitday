$(function(){
    $('#formReg').submit(function(){
        if($('#upwd').val() != $('#cpwd').val()){
            alert('密码不一致');
            return false;
        }
        return true;
    });
})