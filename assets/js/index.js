$(document).ready(function() {
  let slider = $('#password-length');
  let number = $('#slider-value');
  let display = $('#password-display');
  let checkboxes = $('.checkbox-container input');

  function postPasswordLength(length) {
    let uppercase = $('#uppercase').is(':checked');
    let lowercase = $('#lowercase').is(':checked');
    let numbers = $('#numbers').is(':checked');
    let symbols = $('#symbols').is(':checked');

    $.ajax({
      url: generatePasswordURL,
      type: 'POST',
      data: JSON.stringify({
        'length': length,
        'uppercase': uppercase,
        'lowercase': lowercase,
        'numbers': numbers,
        'symbols': symbols
      }),
      contentType: 'application/json',
      dataType: 'json',
      success: function(data) {
        display.text(data.password);
      },
      error: function(xhr, status, error) {
        if (xhr.status === 400) {
          alert(xhr.responseJSON.error);
        } else {
          console.error('Error: ' + error);
        }
      }
    });
  }

  slider.on('input', function() {
    let value = this.value;
    number.val(value);
    postPasswordLength(value);
  });

  number.on('change', function() {
    let value = parseInt(this.value);
    let min = parseInt(number.attr('min'));
    let max = parseInt(number.attr('max'));

    if (isNaN(value) || value < min) {
      number.val(min);
    } else if (value > max) {
      number.val(max);
    }
    slider.val(this.value);
    postPasswordLength(this.value);
  });

  checkboxes.on('change', function() {
    let checked = checkboxes.filter(':checked');
    if (checked.length === 0) {
      $(this).prop('checked', true);
    }
    postPasswordLength(slider.value);
  });

  $('#copy-password').click(function() {
    let password = display.text();
    navigator.clipboard.writeText(password).then(() => {
      $(this).text('Copied!');
      setTimeout(() => {
        $(this).text('Copy Password');
      }, 2000);
    }, function(err) {
      console.error('Could not copy password: ', err);
    });
  });

});