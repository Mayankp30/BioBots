var bioApp = angular.module('bioApp', ['ngMaterial', 'ngMessages', 'ngRoute', 'ngMdIcons']);
   

bioApp.controller('bioController', ['$scope', '$http', function($scope, $http) {

		//default values for hypothetical scenario
		$scope.processForm = function() {
			var email = $scope.email;
			var data = {"email" : email};
			$http.post("/output", data)
		  .success(function(data) { //data received in "~" separated values in the form of ["Column chart values"~"Pie chart values for Conventional material"~"Pie chart values for New material"~"Life Cycle Cost of conventional material"~"Life Cycle Cost of New material"]
			console.log(data.ColumnChartValues);
			if(data.ColumnChartValues == "null") {
				alert("Email id is not in database");
			} else {
				columnChartValues = JSON.parse(data.ColumnChartValues);
				columnChartValues1 = JSON.parse(data.ColumnChartValues1);
				columnChartValues2 = JSON.parse(data.ColumnChartValues2);
				columnChartValues3 = JSON.parse(data.ColumnChartValues3);
				drawChart(columnChartValues, columnChartValues1, columnChartValues2, columnChartValues3);
			}
			//google.setOnLoadCallback(drawChart);
 	    })
		.error(function(data) {
            console.log("error");
            console.log(data);
        });
		};
		

    }]);
