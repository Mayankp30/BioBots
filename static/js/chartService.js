//Javascript to load google chart

google.load('visualization', '1', {packages:['corechart']});

google.setOnLoadCallback(drawChart);

function drawChart(columnChartValues, columnChartValues1, columnChartValues2, columnChartValues3, columnChartValues4, columnChartValues5, columnChartValues6 ) {
  
  var optionsColumn = {
              //Dead Percent live Percent and Elasticity
              title: "Print Data", 
              width: '100%',
              height: '100%',
              titleTextStyle:{fontSize: 18},
              legend: { position: 'in' , maxlines: 2},
              hAxis:{ title : 'Range'},
              vAxis:{ title : 'Values'},
              bar: { groupWidth: '60%' },
              colors: ['#bcbddc', '#756bb1','#e0440e'],
              isStacked: false,
              };
              
  var optionsColumn1 = {
              title: "Info - Pressure", 
              width: '100%',
              height: '100%',
              titleTextStyle:{fontSize: 18},
              legend: { position: 'in' , maxlines: 2},
              hAxis:{ title : 'Range'},
              vAxis:{ title : 'Values'},
              bar: { groupWidth: '65%' },
              colors: ['#f6c7b6', '#e6693e'],
              isStacked: false,
              };

   var optionsColumn2 = {
              title: "Info - Resolution - Layer number", 
              width: '100%',
              height: '100%',
              titleTextStyle:{fontSize: 18},
              legend: { position: 'in' , maxlines: 2},
              hAxis:{ title : 'Range'},
              vAxis:{ title : 'Values'},
              bar: { groupWidth: '65%' },
              colors: ['#cc66ff'],
              isStacked: false,
              };

    var optionsColumn3 = {
              title: "Info - Wellplate", 
              width: '100%',
              height: '100%',
              titleTextStyle:{fontSize: 18},
              legend: { position: 'in' , maxlines: 2},
              hAxis:{ title : 'Range'},
              vAxis:{ title : 'Values'},
              bar: { groupWidth: '65%' },
              colors: ['#cccc00'],
              isStacked: false,
              };

    var optionsColumn4 = {
              title: "Info - Resolution - Layer height", 
              width: '100%',
              height: '100%',
              titleTextStyle:{fontSize: 18},
              legend: { position: 'in' , maxlines: 2},
              hAxis:{ title : 'Range(in mm)'},
              vAxis:{ title : 'Values'},
              bar: { groupWidth: '65%' },
              colors: ['#009933'],
              isStacked: false,
              };

    var optionsColumn5 = {
              title: "Info - Cross Linking - Cl intensity", 
              width: '100%',
              height: '100%',
              titleTextStyle:{fontSize: 18},
              legend: { position: 'in' , maxlines: 2},
              hAxis:{ title : 'Range(in percent)'},
              vAxis:{ title : 'Values'},
              bar: { groupWidth: '65%' },
              colors: ['#ff0000'],
              isStacked: false,
              };

    var optionsColumn6 = {
              title: "Info - Cross Linking - Cl duration", 
              width: '100%',
              height: '100%',
              titleTextStyle:{fontSize: 18},
              legend: { position: 'in' , maxlines: 1},
              hAxis:{ title : 'Range(in seconds)'},
              vAxis:{ title : 'Values'},
              bar: { groupWidth: '25%' },
              colors: ['#ff6600'],
              isStacked: false,
              };

  var dataColumn = google.visualization.arrayToDataTable(JSON.parse(JSON.stringify(columnChartValues)));
  var dataColumn1 = google.visualization.arrayToDataTable(JSON.parse(JSON.stringify(columnChartValues1)));
  var dataColumn2 = google.visualization.arrayToDataTable(JSON.parse(JSON.stringify(columnChartValues2)));
  var dataColumn3 = google.visualization.arrayToDataTable(JSON.parse(JSON.stringify(columnChartValues3)));
  var dataColumn4 = google.visualization.arrayToDataTable(JSON.parse(JSON.stringify(columnChartValues4)));
  var dataColumn5 = google.visualization.arrayToDataTable(JSON.parse(JSON.stringify(columnChartValues5)));
  var dataColumn6 = google.visualization.arrayToDataTable(JSON.parse(JSON.stringify(columnChartValues6)));

  //document.getElementById('graphSlider').style.display="block"; 
  
  document.getElementById("graphSlider").style.display="block"; 

  var ColChartContainer = document.getElementById('chart_div');
  var ColChartContainer1 = document.getElementById('chart_div1');
  var ColChartContainer2 = document.getElementById('chart_div2');
  var ColChartContainer3 = document.getElementById('chart_div3');
  var ColChartContainer4 = document.getElementById('chart_div4');
  var ColChartContainer5 = document.getElementById('chart_div5');
  var ColChartContainer6 = document.getElementById('chart_div6');

  //document.getElementById("graphSlider").style.display="inline-block";  

  ColChartContainer.style.display = 'block';
  ColChartContainer1.style.display = 'block';
  ColChartContainer2.style.display = 'block';
  ColChartContainer3.style.display = 'block';
  ColChartContainer4.style.display = 'block';
  ColChartContainer5.style.display = 'block';
  ColChartContainer6.style.display = 'block';

  
  var chartCol = new google.visualization.ColumnChart(ColChartContainer);
  var chartCol1 = new google.visualization.ColumnChart(ColChartContainer1);
  var chartCol2 = new google.visualization.ColumnChart(ColChartContainer2);
  var chartCol3 = new google.visualization.ColumnChart(ColChartContainer3);
  var chartCol4 = new google.visualization.ColumnChart(ColChartContainer4);
  var chartCol5 = new google.visualization.ColumnChart(ColChartContainer5);
  var chartCol6 = new google.visualization.ColumnChart(ColChartContainer6);

  
  google.visualization.events.addListener(chartCol, 'ready', function () {
    ColChartContainer.style.display = 'none';
  });
  
  google.visualization.events.addListener(chartCol1, 'ready', function () {
    ColChartContainer1.style.display = 'none';
  });

  google.visualization.events.addListener(chartCol2, 'ready', function () {
    ColChartContainer2.style.display = 'none';
  });

  google.visualization.events.addListener(chartCol3, 'ready', function () {
    ColChartContainer3.style.display = 'none';
  });

  google.visualization.events.addListener(chartCol4, 'ready', function () {
    ColChartContainer4.style.display = 'none';
  });
  
  google.visualization.events.addListener(chartCol5, 'ready', function () {
    ColChartContainer5.style.display = 'none';
  });

  google.visualization.events.addListener(chartCol6, 'ready', function () {
    ColChartContainer6.style.display = 'none';
  });

  chartCol.draw(dataColumn, optionsColumn);
  chartCol1.draw(dataColumn1, optionsColumn1);
  chartCol2.draw(dataColumn2, optionsColumn2);
  chartCol3.draw(dataColumn3, optionsColumn3);
  chartCol4.draw(dataColumn4, optionsColumn4);
  chartCol5.draw(dataColumn5, optionsColumn5);
  chartCol6.draw(dataColumn6, optionsColumn6);

  ColChartContainer.style.display = 'block';
  ColChartContainer3.style.display = 'block';
  ColChartContainer2.style.display = 'block';
  ColChartContainer1.style.display = 'block';
  ColChartContainer4.style.display = 'block';
  ColChartContainer5.style.display = 'block';
  ColChartContainer6.style.display = 'block';

  }