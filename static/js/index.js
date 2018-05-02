$(document).ready(() => {
      $(".dropdown-trigger").dropdown()

      // HANDLE CLICK EVENT THAT UPDATES A JOURNAL ENTRY
      $('.update-button').click((e) => {
        e.preventDefault()
        $.get('/update')
      })

      // HANDLE CLICK EVENT THAT DELETES AN ENTRY
      $('#confirm-delete-button').click((e) => {
        e.preventDefault()
        const id = $(e.target).data('id')
        $.ajax({
            url: `/delete/${id}`,
            type: 'DELETE'
        })
      })

})
