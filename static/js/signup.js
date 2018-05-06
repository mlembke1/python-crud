let userNameIsTaken = true
let emailIsTaken = true
let passwordsMatch = false

const checkUsernameSignup = () => {
  return $.get('/start/users')
    .done((result) => {
      const enteredUsername = $('#username-signup').val()
      const usernames = result.allUsers.map(x => x.username)
      console.log(usernames)
      userNameIsTaken = usernames.includes(enteredUsername) ? true : false
      if (userNameIsTaken) {
        $('.signup-form-username-error').empty()
        $('.signup-form-username-error').text(` Whoops. ${enteredUsername} already exists.`)
      } else if (enteredUsername.length > 30) {
        $('.signup-form-username-error').empty()
        $('.signup-form-username-error').text(' Whoops. Please keep it under 30 characters.')
      } else if (enteredUsername.length < 8) {
        $('.signup-form-username-error').empty()
        $('.signup-form-username-error').text(' Whoops. Please make it longer than 8 characters.')
      } else {
        $('.signup-form-username-error').empty()
      }
    })
    .fail(err => err)
}

const checkEmail = () => {
  return $.get('/start/users')
    .done((result) => {
      const emailRegex = RegExp(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)
      const enteredEmail = $('#email-signup').val().toLowerCase()
      const emails = result.map(x => x.email)
      emailIsTaken = emails.includes(enteredEmail) ? true : false
      if (emailIsTaken) {
        $('.signup-form-email-error').empty()
        $('.signup-form-email-error').text(` Whoops. ${enteredEmail} already exists.`)
      } else if (!emailRegex.test(enteredEmail)){
        $('.signup-form-email-error').empty()
        $('.signup-form-email-error').text('Please enter a valid email')
      } else {
        $('.signup-form-email-error').empty()
      }
    })
    .fail(err => err)
}
//
//
// const checkPasswords = () => {
//   const firstPass = $('#password-signup').val()
//   const secondPass = $('#confirm-password-signup').val()
//   if (firstPass !== secondPass) {
//     $('.signup-form-password-error').empty()
//     $('.signup-form-password-error').text('Whoops, these passwords don\'t match.')
//     passwordsMatch = false
//   } else if (firstPass.length < 8 || secondPass.length < 8) {
//     $('.signup-form-password-error').empty()
//     $('.signup-form-password-error').text('Please make it longer than 8 characters.')
//   } else if (firstPass.length > 30 || secondPass.length > 30) {
//     $('.signup-form-password-error').empty()
//     $('.signup-form-password-error').text('Please keep it shorter than 30 characters.')
//   } else {
//     $('.signup-form-password-error').empty()
//     $('#general-signup-error').empty()
//     passwordsMatch = true
//   }
// }

// // CREATE THE OBJECT THAT WILL ACT AS THE REQ.BODY
// const createRequestSignup = () => {
//   return {
//     signupUsername: $('#username-signup').val(),
//     signupEmail: $('#email-signup').val(),
//     signupPassword: $('#password-signup').val(),
//     signupConfirmPassword: $('#confirm-password-signup').val()
//   }
// }

// CHECK FOR COOKIE TO APPROVE LOGIN
// const getCookieInfo = () => {
//   $.get('/cookie')
//     .done((result) => {
//       // console.log(result.message)
//       if (result.message === 'Success') {
//         window.location = '/home'
//       }
//     })
// }

$(document).ready(() => {
  // MAKE SIGNUP/LOGIN BUTTONS FUNCTIONAL.
  $('.collapsible').collapsible()
  if (window.location.hash === '#login-collapsible') {
    $('#login-collapsible').trigger('click')
  } else if (window.location.hash === '#signup-collapsible') {
    $('#signup-collapsible').trigger('click')
  }

  // // WHEN USER HITS LOGIN PAGE, FIRST CHECK IF COOKIE EXISTS,
  // // AND REDIRECT IF SO
  // getCookieInfo()

  // WHEN USER FOCUSES OUT OF USERNAME INPUT,
  // CHECK DATABASE TO SEE IF USERNAME IS ALREADY TAKEN
  $('#username-signup').focusout((event) => {
    checkUsernameSignup()
  })
  //
  // // WHEN USER FOCUSES OUT OF EMAIL INPUT,
  // // CHECK DATABASE TO SEE IF EMAIL IS ALREADY TAKEN
  // $('#email-signup').focusout((event) => {
  //   checkEmail()
  // })
  //
  //
  // // WHEN USER FOCUSES OUT OF CONFRIM PASSWORD INPUT,
  // // CHECK DATABASE TO SEE IF EMAIL IS ALREADY TAKEN
  // $('#confirm-password-signup').keyup((event) => {
  //   checkPasswords()
  // })


  // Handle submit event
  // $('#signup-submit-button').click((event) => {
  //   event.preventDefault()
  //   // Make POST request with form field data as POST body
  //   if (passwordsMatch === true && emailIsTaken === false && userNameIsTaken === false) {
  //     $('#general-signup-error').empty()
  //     $.ajax({
  //       url: '/start/signup',
  //       type: 'POST',
  //       dataType: 'json',
  //       contentType: 'application/json; charset=utf-8',
  //       data: JSON.stringify(createRequestSignup()),
  //       success: (data) => {
  //         if (data.message === 'success') {
  //           window.location = '/home'
  //         }
  //       }
  //     }) // end ajax
  //   } else {
  //     $('#general-signup-error').empty()
  //     $('#general-signup-error').text('Your input isn\'t quite correct.')
  //   }
  // }) // end submit handler
}) // End document ready
