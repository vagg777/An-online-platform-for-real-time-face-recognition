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

const DigitsValidation = function validate(number) {
  var returnedValue = true;
  const usernumber = document.getElementById(number).value;
  if ( (usernumber.length < 0) || (usernumber.length > 3))  {
    document.getElementById(number).style.borderColor = '#ff0000';
    document.getElementById(number).style.borderWidth = '3px';
    document.getElementById(number + '_errors').style.color = '#ff0000';
    document.getElementById(number + '_errors').innerHTML = 'This number can only be 0-3 digits only!';
    if (usernumber === '')
        document.getElementById(number + '_errors').innerHTML = 'Please enter a correct value!';
    if(!(/^\d+$/.test(usernumber))) {
        document.getElementById(number + '_errors').innerHTML = 'This field cannot contain letters!';
    }
    returnedValue = false;
    } else {
      if(!(/^\d+$/.test(usernumber))) {
          document.getElementById(number).style.borderColor = '#ff0000';
          document.getElementById(number).style.borderWidth = '3px';
          document.getElementById(number + '_errors').style.color = '#ff0000';
          document.getElementById(number + '_errors').innerHTML = 'This field cannot contain letters!';
          returnedValue = false;
      } else {
          document.getElementById(number).style.borderColor  = '#008000';
          document.getElementById(number).style.borderWidth = '3px';
          document.getElementById(number + '_errors').style.color  = '#008000';
          document.getElementById(number + '_errors').innerHTML = 'This number is valid!';
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
    document.getElementById(biography+ '_errors').innerHTML = 'Criminal Record is way too small!';
    if (userBio === '')
        document.getElementById(biography + '_errors').innerHTML = 'Please enter the Criminal Record!';
    returnedValue = false;
    } else {
      document.getElementById(biography).style.borderColor  = '#008000';
      document.getElementById(biography).style.borderWidth = '3px';
      document.getElementById(biography + '_errors').style.color  = '#008000';
      document.getElementById(biography + '_errors').innerHTML = 'Criminal Record length is valid!';
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