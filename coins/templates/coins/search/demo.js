$(document).ready(function(){
     $( "input#search" ).autocomplete({
                            source: "{% url search %}",
                            minLength: 2
        });
});
