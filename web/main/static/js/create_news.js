$(document).ready(function(){
    var f = document.getElementsById('create_news_frm');
    f.preventDefault()

    $('#create_news_button').click(function(){
        $.ajax({
            url: 'main/create_news.html',
            type: 'post',
            data: {
                JSON.parse($('#create_news_frm'))
            },
            success: function(){
                alert("Form created!")
            }
        }
        )
    })

})
