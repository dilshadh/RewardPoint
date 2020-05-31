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