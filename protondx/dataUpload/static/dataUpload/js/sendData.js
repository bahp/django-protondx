$("#uploadAllButton").click(function(event){
    event.preventDefault();

    const obj = {
        "test_result": true,
        "date_test":"2020-05-26T00:00",
        "patient_first_name": "Test1111",
        "patient_last_name": "Tester1111",
        "patient_gender": "X",
        "patient_dob": "2020-05-26",
        "patient_postcode": "SW5 0TU",
        "testing_centre_type":"Hospital",
        "testing_centre_long":"-0.1895885700734055",
        "testing_centre_lat":"51.49584463473821"
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });


    $.ajax({
        type : "POST",
        url : "/dataUpload/api/sample-poster/",
        csrfmiddlewaretoken: "{{ csrf_token }}",
        data : JSON.stringify(obj),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        success: function(){
            console.log("Saved! It worked.");
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
        }
    });
});

// JSON format
// {
// "test_result": true,
// "date_test":"2020-05-26T00:00",
// "patient_first_name": "Test1111",
// "patient_last_name": "Tester1111",
// "patient_gender": "X",
// "patient_dob": "2020-05-26",
// "patient_postcode": "SW5 0TU",
// "testing_centre_centre_type":"Hospital",
// "testing_centre_long":"-0.1895885700734055",
// "testing_centre_lat":"51.49584463473821"
// }