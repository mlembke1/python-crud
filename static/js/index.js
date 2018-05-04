$(document).ready(() => {
      $(".dropdown-trigger").dropdown()

      // HANDLE CLICK EVENT THAT UPDATES A JOURNAL ENTRY
      $('#confirm-update-button').click((e) => {
        e.preventDefault()
        const id = $(e.target).data('id')
        const formInput = {
          author: $('#update-author-input').val(),
          title: $('#update-title-input').val(),
          journal_entry: $('#update-journal_entry-input').val()
        }
        $.ajax({
            url: `/update/${id}`,
            type: 'PUT',
            data: formInput,
            success: (result) => {
              if(result.message === 'success'){
                window.location = 'https://write-flask.herokuapp.com/read'
              }
            }
        })
      })

      // HANDLE CLICK EVENT THAT DELETES AN ENTRY
      $('#confirm-delete-button').click((e) => {
        e.preventDefault()
        const id = $(e.target).data('id')
        $.ajax({
            url: `/delete/${id}`,
            type: 'DELETE',
            success: (data) => {
                if(data.message === 'success'){
                  window.location = 'https://write-flask.herokuapp.com/read'
                }
            }
        })
      })

      // ANIMATION FOR HOMEPAGE LOAD
      $('.loader').fadeOut(2000)

      // SIGNUP / LOGIN POPOUT FUNCTIONALITY
      $('.collapsible').collapsible()

      // Typing Effect
      var i = 0;
      var txt = 'A JOURNALING APPLICATION BUILT ON THE PYTHON FLASK FRAMEWORK.'; /* The text */
      var speed = 50; /* The speed/duration of the effect in milliseconds */

      function typeWriter() {
        if (i < txt.length) {
          document.getElementById("typing").innerHTML += txt.charAt(i);
          i++;
          setTimeout(typeWriter, speed);
        }
      }
      setTimeout(() => typeWriter(), 1000)
})
