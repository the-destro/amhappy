'use strict';

/**
 * @ngdoc function
 * @name dashboardApp.controller:HeaderCtrl
 * @description
 * # HeaderCtrl
 * Controller of the dashboardApp
 */
angular.module('dashboardApp')
  .controller('HeaderCtrl', function ($scope, $location) {
    $scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    };
  });
