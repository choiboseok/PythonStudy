$(document).ready(function(){
    $(document).on('click', 'tr', function(){
        alert($(this).find('td').eq(2).text());
        let code = $(this).find('td').eq(2).text();
        let subUrl = 'http://192.168.0.27:5500/main'
        $.ajax({
            url : subUrl,
            type : 'POST',
            data : JSON.stringify({'market':code}),
            contentType : 'application/json',
            dateType : 'json',
            success : function(res){
                console.log(res);
            },
            error :function(err){
                console.log(err);
            }
        })
    });
});