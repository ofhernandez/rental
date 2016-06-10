/**
 * Created by Administrador on 24/05/2016.
 */
function show_modal(type)
{
    close_modal('comment');
    close_modal('suggestion');
    close_modal('contact');
    document.getElementById('my_modal_' + type).className = type + ' my_modal visible';
    if(type != 'contact')
    {
        var modal = document.getElementById('text_' + type);
        modal.focus();
    }
}

function close_modal(type)
{
    document.getElementById('my_modal_' + type).className = type + ' my_modal invisible';
}