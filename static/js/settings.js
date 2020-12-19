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

        $('#appearanceModal').on('show.bs.modal', function (e) {
            var _button = $(e.relatedTarget);
            var _row = _button.parents("div");
            var _id = _row.find(".user_id").val();
            var _theme = _row.find("#theme0").val();
            var _language = _row.find("#language0").val();
            var _fontsize = _row.find(".user_fontsize").val();
            if (_theme == "Ανοιχτόχρωμο Θέμα") {_theme = "Light Theme"}
            if (_theme == "Σκουρόχρωμο Θέμα") {_theme = "Dark Theme"}
            if (_language == "Αγγλικά") {_language = "English"}
            if (_language == "Ελληνικά") {_language = "Greek"}
            $(this).find(".user_id").val(_id);
            $(this).find(".user_fontsize").val(_fontsize);
            $("#theme").val(_theme).change();
            $("#language").val(_language).change();
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

function manageProfile() {
      var profileDiv = document.getElementById("profileSettingsDiv");
      var profileList = document.getElementById("profileSettingsLink");
      var appearanceDiv = document.getElementById("appearanceSettingsDiv");
      var appearanceList = document.getElementById("appearanceSettingsLink");
      if (profileDiv.style.display === "none") {
        profileDiv.style.display = "block";
        profileList.classList.add('active')
        if (appearanceDiv.style.display === "block") {
            appearanceDiv.style.display = "none";
            appearanceList.classList.remove('active')
        }
      } else {
        profileDiv.style.display = "none";
        profileList.classList.remove('active')
      }
}

function manageAppearance() {
      var appearanceDiv = document.getElementById("appearanceSettingsDiv");
      var appearanceList = document.getElementById("appearanceSettingsLink");
      var profileDiv = document.getElementById("profileSettingsDiv");
      var profileList = document.getElementById("profileSettingsLink");
      if (appearanceDiv.style.display === "none") {
        appearanceDiv.style.display = "block";
        appearanceList.classList.add('active')
        if (profileDiv.style.display === "block") {
            profileDiv.style.display = "none";
            profileList.classList.remove('active')
        }
      } else {
        appearanceDiv.style.display = "none";
        appearanceList.classList.remove('active')
      }
}