const UsersValidation = function validate(username, email, password, retype_password, full_name, work_phone, mobile_phone, biography, gender, role, url){
    const isUsernameValid = UsernameValidation(username);
    const isEmailValid = EmailValidation(email);
    const isPasswordValid = PasswordValidation(password);
    const isRetypePasswordValid = RetypePasswordValidation(retype_password);
    const isFullnameValid = FullnameValidation(full_name);
    const isWorkPhoneValid = PhoneValidation(work_phone);
    const isMobilePhoneValid = PhoneValidation(mobile_phone);
    const isBiographyValid = BiographyValidation(biography);
    const isGenderValid = DropdownValidation(gender);
    const isRoleValid =DropdownValidation(role);
    const isURLValid = URLValidation(url);
    if (isUsernameValid && isEmailValid && isPasswordValid && isRetypePasswordValid && isFullnameValid && isWorkPhoneValid && isMobilePhoneValid && isBiographyValid && isGenderValid && isRoleValid && isURLValid) return true;
    else return false;
}

const UsernameValidation = function validate(username) {
  var returnedValue = true;
  const loginUsername = document.getElementById(username).value;
  if (loginUsername.length <= 2) {
    document.getElementById(username).style.borderColor = '#ff0000';
    document.getElementById(username).style.borderWidth = '3px';
    document.getElementById(username + '_errors').style.color = '#ff0000';
    document.getElementById(username + '_errors').innerHTML = 'Το όνομα χρήστη παραείναι μικρό!';
    if (loginUsername === '')
        document.getElementById(username + '_errors').innerHTML = 'Παρακαλούμε εισάγετε όνομα χρήστη';
    returnedValue = false;
    } else {
      document.getElementById(username).style.borderColor  = '#008000';
      document.getElementById(username).style.borderWidth = '3px';
      document.getElementById(username + '_errors').style.color  = '#008000';
      document.getElementById(username + '_errors').innerHTML = 'Το όνομα χρήστη είναι έγκυρο';
    }

  return returnedValue;
}


const EmailValidation = function validate(email) {
  var returnedValue = true;
  const userEmail = document.getElementById(email).value;
  const atpos = userEmail.indexOf("@");
  const dotpos = userEmail.lastIndexOf(".");
  if (atpos<1 || dotpos<atpos+2 || dotpos+2>=userEmail.length) {
    document.getElementById(email).style.borderColor = '#ff0000';
    document.getElementById(email).style.borderWidth = '3px';
    document.getElementById(email + '_errors').style.color = '#ff0000';
    document.getElementById(email + '_errors').innerHTML = 'Η διεύθυνση email δεν είναι έγκυρη!';
    returnedValue = false;
  } else {
    document.getElementById(email).style.borderColor = '#008000';
    document.getElementById(email).style.borderWidth = '3px';
    document.getElementById(email + '_errors').style.color = '#008000';
    document.getElementById(email + '_errors').innerHTML = 'Η διεύθυνση email είναι έγκυρη!';
  }
  if (userEmail === ''){
    document.getElementById(email).style.borderColor = '#ff0000';
    document.getElementById(email).style.borderWidth = '3px';
    document.getElementById(email + '_errors').innerHTML = 'Παρακαλούμε εισάγετε μια διεύθυνση email';
    returnedValue = false;
  }

  return returnedValue;
}

const PasswordValidation = function validate(password) {
  var returnedValue = true;
  var userPassword = document.getElementById(password).value;
  if (userPassword.length <= 2) {
    document.getElementById(password).style.borderColor = '#ff0000';
    document.getElementById(password).style.borderWidth = '3px';
    document.getElementById(password + '_errors').style.color = '#ff0000';
    document.getElementById(password + '_errors').innerHTML = 'Ο κωδικός είναι πολύ μικρός!';
    if (userPassword === '')  document.getElementById(password + '_errors').innerHTML = 'Παρακαλούμε εισάγετε κωδικό!';
    returnedValue = false;
    } else {
      document.getElementById(password).style.borderColor = '#008000';
      document.getElementById(password).style.borderWidth = '3px';
      document.getElementById(password + '_errors').style.color = '#008000';
      document.getElementById(password + '_errors').innerHTML = 'Ο κωδικός είναι έγκυρος!';
    }

  return returnedValue;
}

const RetypePasswordValidation = function validate(retype_password) {
  var returnedValue = true;
  var userRetypePassword = document.getElementById(retype_password).value;
  if (userRetypePassword.length <= 2) {
    document.getElementById(retype_password).style.borderColor = '#ff0000';
    document.getElementById(retype_password).style.borderWidth = '3px';
    document.getElementById(retype_password + '_errors').style.color = '#ff0000';
    document.getElementById(retype_password + '_errors').innerHTML = 'Ο κωδικός είναι πολύ μικρός!';
    if (userRetypePassword === '')  document.getElementById(retype_password + '_errors').innerHTML = 'Παρακαλούμε εισάγετε κωδικό!';
    returnedValue = false;
    } else {
      document.getElementById(retype_password).style.borderColor = '#008000';
      document.getElementById(retype_password).style.borderWidth = '3px';
      document.getElementById(retype_password + '_errors').style.color = '#008000';
      document.getElementById(retype_password + '_errors').innerHTML = 'Ο κωδικός είναι έγκυρος!';
    }

  return returnedValue;
}


const FullnameValidation = function validate(fullname) {
  var returnedValue = true;
  const userFullname = document.getElementById(fullname).value;
  if (userFullname.length <= 2) {
    document.getElementById(fullname).style.borderColor = '#ff0000';
    document.getElementById(fullname).style.borderWidth = '3px';
    document.getElementById(fullname + '_errors').style.color = '#ff0000';
    document.getElementById(fullname + '_errors').innerHTML = 'Το πλήρες όνομα είναι πολύ μικρό!';
    if (userFullname === '')
        document.getElementById(fullname + '_errors').innerHTML = 'Παρακαλούμε εισάγετε το πλήρες όνομα!';
    if(/\d/.test(userFullname)) {
        document.getElementById(fullname + '_errors').innerHTML = 'Το πλήρες όνομα δεν μπορεί να περιέχει αριθμούς!';
    }
    returnedValue = false;
    } else {
      if(/\d/.test(userFullname)) {
          document.getElementById(fullname).style.borderColor = '#ff0000';
          document.getElementById(fullname).style.borderWidth = '3px';
          document.getElementById(fullname + '_errors').style.color = '#ff0000';
          document.getElementById(fullname + '_errors').innerHTML = 'Το πλήρες όνομα δεν μπορεί να περιέχει αριθμούς!';
          returnedValue = false;
      } else {
          document.getElementById(fullname).style.borderColor  = '#008000';
          document.getElementById(fullname).style.borderWidth = '3px';
          document.getElementById(fullname + '_errors').style.color  = '#008000';
          document.getElementById(fullname + '_errors').innerHTML = 'Το πλήρες όνομα είναι έγκυρο!';
      }
    }

  return returnedValue;
}

const PhoneValidation = function validate(phone) {
  var returnedValue = true;
  const userphone = document.getElementById(phone).value;
  if ( (userphone.length < 10) || (userphone.length > 14))  {
    document.getElementById(phone).style.borderColor = '#ff0000';
    document.getElementById(phone).style.borderWidth = '3px';
    document.getElementById(phone + '_errors').style.color = '#ff0000';
    document.getElementById(phone + '_errors').innerHTML = 'Το μήκος του τηλεφωνικού αριθμού μπορεί να είναι 10-14 ψηφία μόνο!';
    if (userphone === '')
        document.getElementById(phone + '_errors').innerHTML = 'Παρακαλούμε εισάγετε τον τηλεφωνικό αριθμό!';
    if(!(/^\d+$/.test(userphone))) {
        document.getElementById(phone + '_errors').innerHTML = 'Ο τηλεφωνικός αριθμός δεν μπορεί να περιέχει γράμματα!';
    }
    returnedValue = false;
    } else {
      if(!(/^\d+$/.test(userphone))) {
          document.getElementById(phone).style.borderColor = '#ff0000';
          document.getElementById(phone).style.borderWidth = '3px';
          document.getElementById(phone + '_errors').style.color = '#ff0000';
          document.getElementById(phone + '_errors').innerHTML = 'Ο τηλεφωνικός αριθμός δεν μπορεί να περιέχει γράμματα!';
          returnedValue = false;
      } else {
          document.getElementById(phone).style.borderColor  = '#008000';
          document.getElementById(phone).style.borderWidth = '3px';
          document.getElementById(phone + '_errors').style.color  = '#008000';
          document.getElementById(phone + '_errors').innerHTML = 'Ο τηλεφωνικός αριθμός είναι έγκυρος';
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
    document.getElementById(biography+ '_errors').innerHTML = 'Το βιογραφικό είναι πολύ μικρό!';
    if (userBio === '')
        document.getElementById(biography + '_errors').innerHTML = 'Παρακαλούμε εισάγετε το βιογραφικό!';
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
