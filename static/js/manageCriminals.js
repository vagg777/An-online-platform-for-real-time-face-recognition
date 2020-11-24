$(document).ready(function() {
         $('#deleteModal').on('show.bs.modal', function (e) {
             var _button = $(e.relatedTarget);
             var _row = _button.parents("tr");
             var _id = _row.find(".criminal_id").text();
             var _full_name = _row.find(".criminal_full_name").text();
             $(this).find(".delete_criminal_id").val(_id);
             $(this).find(".delete_criminal_full_name").val(_full_name);
         });
    });

$(document).ready(function() {
        $('#updateModal').on('show.bs.modal', function (e) {
        var _button = $(e.relatedTarget);
        var _row = _button.parents("tr");
        var _id = _row.find(".criminal_id").text();
        var _portrait = _row.find('img').attr("src");
        var _full_name = _row.find(".criminal_full_name").text();
        var _age = _row.find(".criminal_age").text();
        var _gender = _row.find("#gender0").text();
        if (_gender == "Άντρας") {_gender = "Male";}
        if (_gender == "Γυναίκα") {_gender = "Female";}
        if (_gender == "Άλλο") {_gender = "Other";}
        var _height = _row.find(".criminal_height").text();
        var _weight = _row.find(".criminal_weight").text();
        var _eye_color = _row.find("#eyecolor0").text();
        if (_eye_color == "Μαύρο") {_eye_color= "Black";}
        if (_eye_color == "Καφέ") {_eye_color= "Brown";}
        if (_eye_color == "Σκούρο Καφέ") {_eye_color= "Dark Brown";}
        if (_eye_color == "Πράσινο") {_eye_color= "Green";}
        if (_eye_color == "Γαλάζιο") {_eye_color= "Blue";}
        if (_eye_color == "Κεχριμπαρί") {_eye_color= "Amber";}
        if (_eye_color == "Γκρί") {_eye_color= "Gray";}
        var _biography = _row.find(".criminal_bio").text();
        var _last_location = _row.find(".criminal_last_location").text();
        $(this).find(".criminal_id").val(_id);
        $(this).find(".criminal_portrait").val(_portrait);
        $(this).find(".criminal_full_name").val(_full_name);
        $(this).find(".criminal_age").val(_age);
        $(this).find(".criminal_height").val(_height);
        $(this).find(".criminal_weight").val(_weight);
        $("#criminal_eye_color").val(_eye_color).change();
        $("#criminal_gender").val(_gender).change();
        $(this).find(".criminal_bio").val(_biography);
        $(this).find(".criminal_last_location").val(_last_location);
    });
 });

document.onkeydown = fkey;
document.onkeypress = fkey
document.onkeyup = fkey;
var wasPressed = false;
function fkey(e){
   e = e || window.event;
   if( wasPressed ) return;
    if (e.keyCode == 116) {
         window.location = 'manage_criminals';
         wasPressed = true;
    }
 }

if ( window.history.replaceState ) {
      window.history.replaceState( null, null, 'manage_criminals' );
}