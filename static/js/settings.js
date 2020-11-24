$(document).ready(function() {
        $('#updateModal').on('show.bs.modal', function (e) {
        var _button = $(e.relatedTarget);
        var _row = _button.parents("div");
        var _id = _row.find(".user_id").val();
        var _username = _row.find(".user_username").val();
        var _password = _row.find(".user_password").val();
        var _email = _row.find(".user_email").val();
        var _fullname = _row.find(".user_full_name").val();
        var _gender = _row.find("#gender0").val();
        if (_gender == "Άντρας") {_gender = "Male"}
        if (_gender == "Γυναίκα") {_gender = "Female"}
        if (_gender == "Άλλο") {_gender = "Other"}
        var _biography = _row.find(".user_biography").val();
        var _work_phone = _row.find(".user_work_phone").val();
        var _mobile_phone = _row.find(".user_mobile_phone").val();
        var _role = _row.find("#role0").val();
        if (_role == "Διαχειριστής") {_role = "ADMIN"}
        if (_role == "Χρήστης") {_role = "USER"}
        var _avatar = _row.find('img').attr("src");
        $(this).find(".user_id").val(_id);
        $(this).find(".user_username").val(_username);
        $(this).find(".user_password").val(_password);
        $(this).find(".user_email").val(_email);
        $(this).find(".user_full_name").val(_fullname);
        $("#gender").val(_gender).change();
        $(this).find(".user_biography").val(_biography);
        $(this).find(".user_work_phone").val(_work_phone);
        $(this).find(".user_mobile_phone").val(_mobile_phone);
        $("#role").val(_role).change();
        $(this).find(".user_avatar").val(_avatar);
    });
 });

 if ( window.history.replaceState ) {
    window.history.replaceState( null, null, 'settings' );
 }

document.onkeydown = fkey;
document.onkeypress = fkey
document.onkeyup = fkey;
var wasPressed = false;
function fkey(e){
   e = e || window.event;
   if( wasPressed ) return;
    if (e.keyCode == 116) {
         window.location = 'settings';
         wasPressed = true;
    }
 }