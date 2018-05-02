$(document).ready(() => {
      $(".dropdown-trigger").dropdown()

      // HANDLE CLICK EVENT THAT UPDATES A JOURNAL ENTRY
      // $('.update-button').click((e) => {
      //   e.preventDefault()
      //   const id = $(e.target).data('id')
      //   $.ajax({
      //       url: `/update/${id}`,
      //       type: 'PUT'
      //   })
      // })

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
