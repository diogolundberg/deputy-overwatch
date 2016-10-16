var Overwatch = function() {
    self = this;
    self.categories = {};

    $.ajax({
        dataType: 'json',
        method: 'GET',
        url: '/api/indemnities/categories/deputies/?top=5' ,
        success: function (response) {
            $.each(response.categories, function(index, item) {
                var category = index;
                self.categories[category] = [];

                $('.selectpicker').append(
                    '<option>' + index + '</option>'
                );
                $.each(item.deputies, function(index, deputy) {
                    var budget = accounting.formatMoney(deputy.total_budget, "R$ ", 2, ".", ",");

                    self.categories[category].push([
                        deputy.name
                    ,   {v:deputy.total_budget,   f: budget}
                    ,   deputy.party
                    ]);
                });
            });
            $('.selectpicker').selectpicker('refresh');
        }
    });

    self.renderDataTable = function(category) {
        google.charts.load('current', {'packages':['table']});
        google.charts.setOnLoadCallback(drawTable);

        function drawTable() {
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Nome');
            data.addColumn('number', 'Gasto total');
            data.addColumn('string', 'Partido');
            data.addRows(self.categories[category]);

            var table = new google.visualization.Table(document.getElementById('chart'));

            table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
        }
    }

    $('.selectpicker').change(function(){
        var selected = $(this).find("option:selected").html();
        self.renderDataTable(selected);
        $('.title').html(selected + " em 2015");
    });
}

$(document).ready(function() {
   var overwatch = new Overwatch();
});