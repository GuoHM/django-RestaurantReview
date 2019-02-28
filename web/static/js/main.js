function reply(obj) {
    var div = document.getElementById(obj);
    div.innerHTML=
    "<form method='POST'  class='form-horizontal' role='form' action='/subcomment/"+ obj +"'>"+
                        "<textarea class='form-control' rows='2'  name='comment' id='comment'></textarea>"+
                        "<button type='submit' class='btn btn-primary'>Submit</button>"+
                        "<button  class='btn btn-primary' style='float:right;' onclick='cancel("+obj+")'>Cancel</button>"+
                    "</form>";
}

function cancel(obj) {
    var div = document.getElementById(obj);
    div.innerHTML = "";
}