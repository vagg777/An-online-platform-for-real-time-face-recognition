const updateUsersValidation = function validate(username, email){
    const isUsernameValid = UsernameValidation(username);
    const isEmailValid = EmailValidation(email);
    if (isUsernameValid && isEmailValid) return true;
    else return false;
}

const UsernameValidation = function validateUsername(username) {
  var returnedValue = true;
  const loginUsername = document.getElementById(username).value;
  if (loginUsername.length <= 2) {
    document.getElementById(username).style.borderColor = '#ff0000';
    document.getElementById(username + '_errors').style.color = '#ff0000';
    document.getElementById(username + '_errors').innerHTML = 'Πολύ μικρό username';
    if (loginUsername === '')  document.getElementById(username + '_errors').innerHTML = 'βαλε username';
    returnedValue = false;
    } else {
      document.getElementById(username).style.borderColor  = '#008000';
      document.getElementById(username + '_errors').style.color  = '#008000';
      document.getElementById(username + '_errors').innerHTML = 'Username is: VALID';
    }

  return returnedValue;
}

const EmailValidation = function validateEmail(email) {
  var returnedValue = true;
  const empEmail = document.getElementById(email).value;
  const atpos = empEmail.indexOf("@");
  const dotpos = empEmail.lastIndexOf(".");
  if (atpos<1 || dotpos<atpos+2 || dotpos+2>=empEmail.length) {
    document.getElementById(email).style.borderColor = '#ff0000';
    document.getElementById(email + '_errors').style.color = '#ff0000';
    document.getElementById(email + '_errors').innerHTML = 'Email Address is not valid!!!';
    returnedValue = false;
  } else {
    document.getElementById(email).style.borderColor = '#008000';
    document.getElementById(email + '_errors').style.color = '#008000';
    document.getElementById(email + '_errors').innerHTML = 'Email Address is: VALID';
  }
  if (empEmail === ''){
    document.getElementById(email).style.borderColor = '#ff0000';
    document.getElementById(email + '_errors').innerHTML = 'Please enter an email address!!!';
    returnedValue = false;
  }

  return returnedValue;
}

const loginPasswordValidation = function validatePassword(password) {
  var returnedValue = true;
  var loginPassword = document.getElementById(password).value;
  if (loginPassword.length <= 2) {
    document.getElementById(password).style.borderColor = '#ff0000';
    document.getElementById(password + '_errors').style.color = '#ff0000';
    document.getElementById(password + '_errors').innerHTML = 'Password is way too small!!!';
    if (loginPassword === '')  document.getElementById(password + '_errors').innerHTML = 'Please enter a Password!!!';
    returnedValue = false;
    } else {
      document.getElementById(password).style.borderColor = '#008000';
      document.getElementById(password + '_errors').style.color = '#008000';
      document.getElementById(password + '_errors').innerHTML = 'Password is: VALID';
    }

  return returnedValue;
}

