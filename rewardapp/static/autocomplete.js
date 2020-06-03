var data
      $(function() {
         $( "#phonenumber" ).autocomplete({
            source: function (request, response) {
                             $.getJSON('/autocomplete?term=' + request.term, function (data) {
                                 response($.map(data, function (item) {
                                     
                                     return {
                                         label: item.c_phone_number,
                                         value: item.c_phone_number,
                                         data: item
                                         
                                     };
                                 }));
                             });
                         },
            minLength:2,
            select: function(event, ui) {
             document.getElementById("customerName").value = ui.item.data.c_name;
             document.getElementById("customerEmail").value = ui.item.data.c_email;
           }
         });
      });
///////////////////////////////////////////////////////////////////////////////////////////////////////////
      $(document).on('click', '#deleteCustomer', function(e){
        event.preventDefault();
            
            swal({
                title: 'Are you sure?',
                text: "You won't be able to revert this!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes, delete it!'
            }).then(function () {
              form = $('#searchCustomerForm')
              console.log(form)
              $.ajax({
                  type: "POST",
                  url: "",
                  data: form.serialize(),
                  cache: false,
                  success: function(response) {
                      if (response.redirect) {
                        window.location.href = response.redirect;
                      }
                      swal(
                      "Sccess!",
                      "Your note has been saved!",
                      "success"
                      )
                  },
                  failure: function (response) {
                      window.location.href = "/searchCustomer"
                      swal(
                      "Internal Error",
                      "Oops, your note was not saved.", // had a missing comma
                      "error"
                      )
                  }
              });
    
            }).catch(swal.noop);
        })