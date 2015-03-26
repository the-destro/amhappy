'use strict';

/**
 * @ngdoc function
 * @name dashboardApp.controller:ManagevhostsCtrl
 * @description
 * # ManagevhostsCtrl
 * Controller of the dashboardApp
 */
angular.module('dashboardApp')
  .controller('ManagevhostsCtrl', function ($scope, Application, Vhosts) {
        Application.query(function(applications) {
            $scope.applications = applications;
        });
        $scope.name = '';
        $scope.selectedApplication = '';
        $scope.$watch(function () {return $scope.selectedApplication;},
            function(selectedApplication) {
                if (selectedApplication != "") {
                    $scope.vhosts = Vhosts.get({'application': selectedApplication});
                }
            });
         $scope.submit = function(){
             Vhosts.save({application:$scope.selectedApplication}, {name: $scope.name});
         }
  });
