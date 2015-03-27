(function(){
    function load_chart() {
        $.get('/load_chart', {
            'region': $('#region_id').val()
        }).done(function (data) {
            var table = $('#regions');
            table.html('');
            data.regions.forEach(function (region) {
                var row = $('<tr>');
                row.append($('<td>').text(region.name));
                table.prepend(row);
            });
            table.prepend($('<tr> <th>region_name</th></tr>'));
        });
    }
    load_chart();

})();