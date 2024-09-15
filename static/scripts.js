$(document).ready(function() {
    $('form').on('submit', function(e) {
        e.preventDefault();
        
        var $submitButton = $(this).find('input[type="submit"]');
        var $spinner = $(this).find('.spinner');
        
        $submitButton.hide();
        $spinner.show(

        )
        // Simulating form submission with a timeout
        setTimeout(function() {
            $spinner.hide();
            $submitButton.show();
        }, 3000);
    });
});