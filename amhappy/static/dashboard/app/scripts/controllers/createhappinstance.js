'use strict';

/**
 * @ngdoc function
 * @name dashboardApp.controller:CreatehappinstanceCtrl
 * @description
 * # CreatehappinstanceCtrl
 * Controller of the dashboardApp
 */
angular.module('dashboardApp')
  .controller('CreatehappinstanceCtrl', function ($scope, $location, Application, Happinstance, ConfigOptions, Vhosts) {
        Application.query(function(applications) {
            $scope.applications = applications;
        });
        $scope.environments = {};
        $scope.selectedApplication = '';
        $scope.name = '';
        $scope.toJson = angular.toJson;
        $scope.isDefined = angular.isDefined;
        $scope.config_options = ConfigOptions.get();
        $scope.$watch(function () {return $scope.selectedApplication;},
            function(selectedApplication) {
                if (selectedApplication != "") {
                    $scope.config = Application.get({application: selectedApplication});
                    $scope.vhosts_available = Vhosts.get({'application': selectedApplication});
                }
            });
        $scope.submit = function(){
            angular.forEach($scope.environments, function(variables, image) {
                angular.forEach(variables, function(value, variable){
                  $scope.config[image]['environment'][variable] = value;
                })
            });
            Happinstance.save({application:$scope.selectedApplication, name:$scope.name}, $scope.config, function(){
                $location.url('/');
            });

        }
  });
