var Overwatch = function() {
    self = this;
    self.categoriesDeputies = {};
    self.categories = {};

    $.ajax({
        dataType: 'json',
        method: 'GET',
        url: '/api/indemnities/categories/deputies/?top=5' ,
        success: function (response) {
            $.each(response.categories, function(index, item) {
                var category = index;
                self.categoriesDeputies[category] = [];

                $('.selectpicker').append(
                    '<option>' + index + '</option>'
                );
                $.each(item.deputies, function(index, deputy) {
                    var budget = accounting.formatMoney(deputy.total_budget, "R$ ", 2, ".", ",");

                    self.categoriesDeputies[category].push([
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
            data.addRows(self.categoriesDeputies[category]);

            var table = new google.visualization.Table(document.getElementById('chart'));

            table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
        }
    }

    self.renderPieChart = function(categories) {
        var data = [['Categoria', 'Verbas indenizatórias']];
        $.each(categories, function(name, category) {
            data.push([name, category.total_budget])
        });

        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);
        function drawChart() {
            var dataTable = google.visualization.arrayToDataTable(data);
            var options = {
                title: 'Verbas indenizatórias'
            };

            var chart = new google.visualization.PieChart(document.getElementById('chart'));

            google.visualization.events.addListener(chart, 'select', function() {
                var selection = chart.getSelection();
                self.renderDataTable(data[selection[0].row][0]);
            });

            chart.draw(dataTable, options);
        }
    }

    $('.selectpicker').change(function(){
        var selected = $(this).find("option:selected").html();
        self.renderDataTable(selected);
        $('.title').html(selected + " em 2015");
    });

    $('#categorias').click(function() {
        self.renderPieChart(self.categories);
    });


    $.ajax({
        dataType: 'json',
        method: 'GET',
        url: '/api/indemnities/categories/' ,
        success: function (response) {
            self.categories = response.categories;
            self.renderPieChart(self.categories);
        }
    });
}

$(document).ready(function() {
   var overwatch = new Overwatch();
});