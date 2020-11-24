$(document).ready(function() {
         $('#deleteModal').on('show.bs.modal', function (e) {
             var _button = $(e.relatedTarget);
             var _row = _button.parents("tr");
             var _id = _row.find(".user_id").text();
             var _username = _row.find(".user_username").text();
             $(this).find(".delete_user_id").val(_id);
             $(this).find(".delete_user_username").val(_username);
         });
    });

$(document).ready(function() {
        $('#updateModal').on('show.bs.modal', function (e) {
        var _button = $(e.relatedTarget);
        var _row = _button.parents("tr");
        var _id = _row.find(".user_id").text();
        var _username = _row.find(".user_username").text();
        var _password = _row.find(".user_password").text();
        var _email = _row.find(".user_email").text();
        var _fullname = _row.find(".user_full_name").text();
        var _gender = _row.find("#gender0").text();
        if (_gender == "Άντρας") {_gender = "Male"}
        if (_gender == "Γυναίκα") {_gender = "Female"}
        if (_gender == "Άλλο") {_gender = "Other"}
        var _biography = _row.find(".user_biography").text();
        var _work_phone = _row.find(".user_work_phone").text();
        var _mobile_phone = _row.find(".user_mobile_phone").text();
        var _role = _row.find("#role0").text();
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
    window.history.replaceState( null, null, 'manage_users' );
 }

document.onkeydown = fkey;
document.onkeypress = fkey
document.onkeyup = fkey;
var wasPressed = false;
function fkey(e){
   e = e || window.event;
   if( wasPressed ) return;
    if (e.keyCode == 116) {
         window.location = 'manage_users';
         wasPressed = true;
    }
 }