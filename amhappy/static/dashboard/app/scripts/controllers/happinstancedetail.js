'use strict';

/**
 * @ngdoc function
 * @name dashboardApp.controller:HappinstancedetailCtrl
 * @description
 * # HappinstancedetailCtrl
 * Controller of the dashboardApp
 */
angular.module('dashboardApp')
  .controller('HappinstancedetailCtrl', function ($scope, $routeParams, $location, Happinstance) {
        var location = {application:$routeParams.application,
                        name:$routeParams.name},
            detail_refresh = function() {
                $scope.detail = Happinstance.get(location);
            };
        $scope.name = $routeParams.name;
        $scope.application = $routeParams.application;
        $scope.toJson = angular.toJson;
        $scope.toggleStatus = function(status) {
            if (status == 'on'){
                Happinstance.changeStatus(location, {action:'off'}, detail_refresh);
            }
            else {
                Happinstance.changeStatus(location, {action:'on'}, detail_refresh);
            }
        };
        $scope.detail = Happinstance.get(location);
        $scope.delete = function(){
            Happinstance.delete(location, function() {
                $location.url('/');
            })
        }
  });
