$("#submission-alert").hide();

$('#contact-form').submit(function (e) {
    // Ref: https://stackoverflow.com/q/42626969/3860168
    e.preventDefault();

    var formData = $(this).serializeArray();
   	var fieldsWithErrors = [];
   	$(formData).each((function (index, element) {
		var required = $(this).find('[name="' + element.name + '"]').attr('required');
   		var empty = (element.value.trim().length === 0);

    	if (required && empty) {
    		fieldsWithErrors.push(element.name);
    	}
   	}).bind(this));

	if (fieldsWithErrors.length === 0) {
   		var payload = $.param(formData);
        var name = $(this).find('[name="name"]').val().trim();

        $.ajax({
            type:'POST',
            url:'{% url "contact" %}',
            data: payload,
            success: function(json){
                $("#submission-alert").fadeTo(5000, 500).slideUp(500, function() {
                  $("#submission-alert").slideUp(500);
                });
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
   		$(this).get(0).reset();
    }
	return false;
});
