$(document).ready(function() {
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
    document.getElementById(username + '_errors').innerHTML = 'Username is way too small!';
    if (loginUsername === '')
        document.getElementById(username + '_errors').innerHTML = 'Please enter a Username!';
    returnedValue = false;
    } else {
      document.getElementById(username).style.borderColor  = '#008000';
      document.getElementById(username).style.borderWidth = '3px';
      document.getElementById(username + '_errors').style.color  = '#008000';
      document.getElementById(username + '_errors').innerHTML = 'Username is valid!';
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
    document.getElementById(email + '_errors').innerHTML = 'Email address is not valid!';
    returnedValue = false;
  } else {
    document.getElementById(email).style.borderColor = '#008000';
    document.getElementById(email).style.borderWidth = '3px';
    document.getElementById(email + '_errors').style.color = '#008000';
    document.getElementById(email + '_errors').innerHTML = 'Email address is valid!';
  }
  if (userEmail === ''){
    document.getElementById(email).style.borderColor = '#ff0000';
    document.getElementById(email).style.borderWidth = '3px';
    document.getElementById(email + '_errors').innerHTML = 'Please enter an email address!';
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
    document.getElementById(password + '_errors').innerHTML = 'Password is way too small!';
    if (userPassword === '')  document.getElementById(password + '_errors').innerHTML = 'Please enter a password!';
    returnedValue = false;
    } else {
      document.getElementById(password).style.borderColor = '#008000';
      document.getElementById(password).style.borderWidth = '3px';
      document.getElementById(password + '_errors').style.color = '#008000';
      document.getElementById(password + '_errors').innerHTML = 'Password is valid!';
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
    document.getElementById(retype_password + '_errors').innerHTML = 'Password is way too small!';
    if (userRetypePassword === '')  document.getElementById(retype_password + '_errors').innerHTML = 'Please enter a password!';
    returnedValue = false;
    } else {
      document.getElementById(retype_password).style.borderColor = '#008000';
      document.getElementById(retype_password).style.borderWidth = '3px';
      document.getElementById(retype_password + '_errors').style.color = '#008000';
      document.getElementById(retype_password + '_errors').innerHTML = 'Password is valid!';
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
    document.getElementById(fullname + '_errors').innerHTML = 'Full name is way too small!';
    if (userFullname === '')
        document.getElementById(fullname + '_errors').innerHTML = 'Please enter a Full Name!';
    if(/\d/.test(userFullname)) {
        document.getElementById(fullname + '_errors').innerHTML = 'A name cannot contain digits!';
    }
    returnedValue = false;
    } else {
      if(/\d/.test(userFullname)) {
          document.getElementById(fullname).style.borderColor = '#ff0000';
          document.getElementById(fullname).style.borderWidth = '3px';
          document.getElementById(fullname + '_errors').style.color = '#ff0000';
          document.getElementById(fullname + '_errors').innerHTML = 'A name cannot contain digits!';
          returnedValue = false;
      } else {
          document.getElementById(fullname).style.borderColor  = '#008000';
          document.getElementById(fullname).style.borderWidth = '3px';
          document.getElementById(fullname + '_errors').style.color  = '#008000';
          document.getElementById(fullname + '_errors').innerHTML = 'Full Name is valid!';
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
    document.getElementById(phone + '_errors').innerHTML = 'Phone length can be 10-14 digits only!';
    if (userphone === '')
        document.getElementById(phone + '_errors').innerHTML = 'Please enter a Phone number!';
    if(!(/^\d+$/.test(userphone))) {
        document.getElementById(phone + '_errors').innerHTML = 'Phone number cannot contain letters!';
    }
    returnedValue = false;
    } else {
      if(!(/^\d+$/.test(userphone))) {
          document.getElementById(phone).style.borderColor = '#ff0000';
          document.getElementById(phone).style.borderWidth = '3px';
          document.getElementById(phone + '_errors').style.color = '#ff0000';
          document.getElementById(phone + '_errors').innerHTML = 'Phone number cannot contain letters!';
          returnedValue = false;
      } else {
          document.getElementById(phone).style.borderColor  = '#008000';
          document.getElementById(phone).style.borderWidth = '3px';
          document.getElementById(phone + '_errors').style.color  = '#008000';
          document.getElementById(phone + '_errors').innerHTML = 'Phone number is valid!';
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
    document.getElementById(biography+ '_errors').innerHTML = 'Biography is way too small!';
    if (userBio === '')
        document.getElementById(biography + '_errors').innerHTML = 'Please enter the biography!';
    returnedValue = false;
    } else {
      document.getElementById(biography).style.borderColor  = '#008000';
      document.getElementById(biography).style.borderWidth = '3px';
      document.getElementById(biography + '_errors').style.color  = '#008000';
      document.getElementById(biography + '_errors').innerHTML = 'Biography length is valid!';
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
    document.getElementById(option + '_errors').innerHTML = 'Please select an Option!';
    returnedValue = false;
  } else {
    document.getElementById(option).style.borderColor = '#008000';
    document.getElementById(option).style.borderWidth = '3px';
    document.getElementById(option + '_errors').style.color = '#008000';
    document.getElementById(option + '_errors').innerHTML = 'Selection is valid!';
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
    document.getElementById(url + '_errors').innerHTML = 'Please enter a valid URL!';
    returnedValue = false;
  } else {
    document.getElementById(url).style.borderColor = '#008000';
    document.getElementById(url).style.borderWidth = '3px';
    document.getElementById(url + '_errors').style.color = '#008000';
    document.getElementById(url + '_errors').innerHTML = 'URL is valid!';
  }

  return returnedValue
}

});
