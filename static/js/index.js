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
                window.location = 'http://localhost:5000/read'
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
                  window.location = 'http://localhost:5000/read'
                }
            }
        })
      })

})
