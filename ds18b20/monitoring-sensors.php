<html>
<head></head>
<body>

<script src="js/jquery-1.11.1.min.js"></script>
<script src="js/highcharts.js"></script>
<script src="js/exporting.js"></script>

<div id="container" style="min-width: 310px; height: 400px; margin: 0 auto"></div>

<script type="text/javascript">

$(function () {
    $(document).ready(function () {
        Highcharts.setOptions({
            global: {
                useUTC: false
            }
        });

        $('#container').highcharts({
            chart: {
                type: 'spline',
                zoomType: 'x',
                animation: Highcharts.svg, // don't animate in old IE
                marginRight: 10/*,
                events: {
                    load: function () {

                        // set up the updating of the chart each 5 minutes
                        var series = this.series[0];
			var lastpushedvalue = series.data.pop().x.getTime();

                        setInterval(function () {
			    response = jQuery.ajax({
			        url: "https://home.ubbdf.fr/sensors/",
			        dataType: "json",
			        async: false
			    });
                            var lastsensorvalue = response.responseJSON.pop();
                            if ( lastsensorvalue.timestamp*1000 > lastpushedvalue ) {
                                var x = lastsensorvalue.timestamp*1000,
                                    y = lastsensorvalue.temp;
				lastpushedvalue = x;
                                series.addPoint([x, y], false, false, true);
				jQuery(this).redraw();  // pb with chart.redraw() OR series.addPoint([x, y], true, true, true);
                            }
                        }, 30000);
                    }
                }*/
            },
            title: {
                text: 'Temperature (C)'
            },
            xAxis: {
                type: 'datetime',
                minRange: 2 * 3600000, // 2 hours
                tickPixelInterval: 150
            },
            yAxis: {
                title: {
                    text: 'Value'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                formatter: function () {
                    return '<b>' + this.series.name + '</b><br/>' +
                        Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                        Highcharts.numberFormat(this.y, 2);
                }
            },
            legend: {
                enabled: true
            },
            exporting: {
                enabled: false
            },
            series: [{
                name: 'Kitchen',
		turboThreshold: 0,
                data: (function () {

		    response = jQuery.ajax({
			url: "https://home.ubbdf.fr/sensors/",
			dataType: "json",
			async: false
		    });
		    
		    var res = [];
		    response.responseJSON.forEach(
			function(d){
			    var tmp = new Date();
			    tmp.setTime(d.timestamp*1000); // timestamp in milliseconds
			    res.push({
				x: tmp,
				y: parseFloat(d.temp)
			    });
			}
		    );

		    return res;
                }())
            }]
        });
    });
});
</script>
</body>
