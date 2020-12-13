const CriminalsValidation = function validate(criminal_full_name,criminal_portrait,criminal_height,criminal_weight,criminal_gender,criminal_eye_color,criminal_age,criminal_bio){
    const isFullnameValid = FullnameValidation(criminal_full_name);
    const isURLValid = URLValidation(criminal_portrait);
    const isHeightValid = DigitsValidation(criminal_height);
    const isWeightValid = DigitsValidation(criminal_weight);
    const isGenderValid = DropdownValidation(criminal_gender);
    const isEyeColorValid = DropdownValidation(criminal_eye_color);
    const isAgeValid = DigitsValidation(criminal_age);
    const isBiographyValid = BiographyValidation(criminal_bio);
    if (isFullnameValid && isURLValid && isHeightValid && isWeightValid && isGenderValid && isEyeColorValid && isAgeValid && isBiographyValid)
        return true;
    else
        return false;
}

const FullnameValidation = function validate(fullname) {
  var returnedValue = true;
  const userFullname = document.getElementById(fullname).value;
  if (userFullname.length <= 2) {
    document.getElementById(fullname).style.borderColor = '#ff0000';
    document.getElementById(fullname).style.borderWidth = '3px';
    document.getElementById(fullname + '_errors').style.color = '#ff0000';
    document.getElementById(fullname + '_errors').innerHTML = 'Το όνομα είναι πολύ μικρό!';
    if (userFullname === '')
        document.getElementById(fullname + '_errors').innerHTML = 'Εισάγεται όνομα!';
    if(/\d/.test(userFullname)) {
        document.getElementById(fullname + '_errors').innerHTML = 'Το όνομα δεν μπορεί να περιέχει αριθμούς!';
    }
    returnedValue = false;
    } else {
      if(/\d/.test(userFullname)) {
          document.getElementById(fullname).style.borderColor = '#ff0000';
          document.getElementById(fullname).style.borderWidth = '3px';
          document.getElementById(fullname + '_errors').style.color = '#ff0000';
          document.getElementById(fullname + '_errors').innerHTML = 'Το όνομα δεν μπορεί να περιέχει αριθμούς!';
          returnedValue = false;
      } else {
          document.getElementById(fullname).style.borderColor  = '#008000';
          document.getElementById(fullname).style.borderWidth = '3px';
          document.getElementById(fullname + '_errors').style.color  = '#008000';
          document.getElementById(fullname + '_errors').innerHTML = 'Το όνομα είναι έγκυρο!';
      }
    }

  return returnedValue;
}

const DigitsValidation = function validate(number) {
  var returnedValue = true;
  const usernumber = document.getElementById(number).value;
  if ( (usernumber.length < 0) || (usernumber.length > 3))  {
    document.getElementById(number).style.borderColor = '#ff0000';
    document.getElementById(number).style.borderWidth = '3px';
    document.getElementById(number + '_errors').style.color = '#ff0000';
    document.getElementById(number + '_errors').innerHTML = 'Η τιμή μπορεί να είνια 0-3 ψηφία μόνο!';
    if (usernumber === '')
        document.getElementById(number + '_errors').innerHTML = 'Εισάγετε έγκυρη τιμή!';
    if(!(/^\d+$/.test(usernumber))) {
        document.getElementById(number + '_errors').innerHTML = 'Δεν επιτρέπονται γράμματα!';
    }
    returnedValue = false;
    } else {
      if(!(/^\d+$/.test(usernumber))) {
          document.getElementById(number).style.borderColor = '#ff0000';
          document.getElementById(number).style.borderWidth = '3px';
          document.getElementById(number + '_errors').style.color = '#ff0000';
          document.getElementById(number + '_errors').innerHTML = 'Δεν επιτρέπονται γράμματα!';
          returnedValue = false;
      } else {
          document.getElementById(number).style.borderColor  = '#008000';
          document.getElementById(number).style.borderWidth = '3px';
          document.getElementById(number + '_errors').style.color  = '#008000';
          document.getElementById(number + '_errors').innerHTML = 'Η τιμή είναι έγκυρη';
      }
    }

  return returnedValue;
}

const BiographyValidation = function validate(biography) {
  var returnedValue = true;
  const userBio = document.getElementById(biography).value;
  if (userBio.length <= 2) {
    document.getElementById(biography).style.borderColor = '#ff0000';
    document.getElementById(biography).style.borderWidth = '3px';
    document.getElementById(biography + '_errors').style.color = '#ff0000';
    document.getElementById(biography+ '_errors').innerHTML = 'Το μήκος του βιογραφικού είναι πολύ μικρό!';
    if (userBio === '')
        document.getElementById(biography + '_errors').innerHTML = 'Εισάγετε βιογραφικό!';
    returnedValue = false;
    } else {
      document.getElementById(biography).style.borderColor  = '#008000';
      document.getElementById(biography).style.borderWidth = '3px';
      document.getElementById(biography + '_errors').style.color  = '#008000';
      document.getElementById(biography + '_errors').innerHTML = 'Το μήκος του βιογραφικού είναι έγκυρο!';
    }

  return returnedValue;
}

const DropdownValidation = function validate(option) {
  var returnedValue = true;
  const selectedOption = document.getElementById(option).value;
  if (selectedOption === ''){
    document.getElementById(option).style.borderColor = '#ff0000';
    document.getElementById(option).style.borderWidth = '3px';
    document.getElementById(option + '_errors').style.color = '#ff0000';
    document.getElementById(option + '_errors').innerHTML = 'Παρακαλούμε επιλέξτε μια επιλογή!';
    returnedValue = false;
  } else {
    document.getElementById(option).style.borderColor = '#008000';
    document.getElementById(option).style.borderWidth = '3px';
    document.getElementById(option + '_errors').style.color = '#008000';
    document.getElementById(option + '_errors').innerHTML = 'Η επιλογή είναι έγκυρη!';
  }

  return returnedValue;
}

const URLValidation = function validate(url) {
  var regexp = /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/
  var returnedValue = true;
  const imageUrl = document.getElementById(url).value;
  if (!regexp.test(imageUrl)){
    document.getElementById(url).style.borderColor = '#ff0000';
    document.getElementById(url).style.borderWidth = '3px';
    document.getElementById(url + '_errors').style.color = '#ff0000';
    document.getElementById(url + '_errors').innerHTML = 'Παρακαλούμε εισάγετε έγκυρο σύνδεσμο';
    returnedValue = false;
  } else {
    document.getElementById(url).style.borderColor = '#008000';
    document.getElementById(url).style.borderWidth = '3px';
    document.getElementById(url + '_errors').style.color = '#008000';
    document.getElementById(url + '_errors').innerHTML = 'Ο σύνδεσμος είναι έγκυρος';
  }

  return returnedValue
}