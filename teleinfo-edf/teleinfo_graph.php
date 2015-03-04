<?php require_once('teleinfo_func.php'); ?>

<script type="text/javascript" src="https://www.google.com/jsapi"></script>

<div id="puissance">
  <div id="chart_div"></div>
  <div id="filter_div"></div>
</div>
<div id="conso"></div>


<script type="text/javascript">
  google.load('visualization', '1.0', {'packages':['controls']});
  google.setOnLoadCallback(drawDashboard);
  
  function drawDashboard() {

    var data = new google.visualization.DataTable();
        data.addColumn('date', 'Date');
        data.addColumn('number', 'V.A');
        data.addColumn('number', 'kW');
        data.addRows([<?php echo getDatasPuissance (5); ?>]);

    var dashboard = new google.visualization.Dashboard(
            document.getElementById('puissance'));

    var rangeSlider = new google.visualization.ControlWrapper({
          'controlType': 'ChartRangeFilter',
          'containerId': 'filter_div',
          'options': {
             filterColumnLabel : 'Date',
             ui : {chartType: 'LineChart', chartOptions: {
                             height : 80,
                             backgroundColor: '#FFF',
                             colors : ['#375D81', '#ABC8E2'],
                             curveType : 'function',
                             focusTarget : 'category',
                             lineWidth : '1',
                             'legend': {'position': 'none'},
                             'hAxis': {'textPosition': 'in'},
                             'vAxis': {
                               'textPosition': 'none',
                               'gridlines': {'color': 'none'}
                             }
                 }}
          }
        });
        
    var lineChart = new google.visualization.ChartWrapper({
          'chartType': 'LineChart',
          'containerId': 'chart_div',
          'options': {
                             title: '',
                             height : 400,
                             backgroundColor: '#FFF',
                             colors : ['#375D81', '#ABC8E2'],
                             curveType : 'function',
                             focusTarget : 'category',
                             lineWidth : '1',
                             legend : {position: 'bottom',  alignment: 'center', textStyle: {color: '#333', fontSize: 16}},
                             vAxis : {textStyle : {color : '#555', fontSize : '16'}, gridlines : {color: '#CCC', count: 'auto'}, baselineColor : '#AAA', minValue : 0},
                             hAxis : {textStyle : {color : '#555'}, gridlines : {color: '#DDD'}}
          }
        });

    dashboard.bind(rangeSlider, lineChart);
    dashboard.draw(data);

  }
  
  google.load("visualization", "1", {packages:["corechart"]});
  google.setOnLoadCallback(drawChart);
  
  function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Date');
    data.addColumn('number', 'Heures pleines');
    data.addColumn('number', 'Heures creuses');
    data.addRows([<?php echo getDatasConso (365); ?>]);
    var options = {
                   title: '',
                   height : 200,
                   backgroundColor: '#FFF',
                   colors : ['#375D81', '#ABC8E2'],
                   curveType : 'function',
                   focusTarget : 'category',
                   lineWidth : '1',
                   isStacked: true,
                   legend : {position: 'bottom',  alignment: 'center', textStyle: {color: '#333', fontSize: 16}},
                   vAxis : {textStyle : {color : '#555', fontSize : '16'}, gridlines : {color: '#CCC', count: 'auto'}, baselineColor : '#AAA', minValue : 0},
                   hAxis : {textStyle : {color : '#555'}, gridlines : {color: '#DDD'}}
              };
    var chart = new google.visualization.ColumnChart(document.getElementById("conso"));
    chart.draw(data, options);
  }


</script>

