'use strict';

/**
 * @ngdoc function
 * @name dashboardApp.controller:HappinstancedetailCtrl
 * @description
 * # HappinstancedetailCtrl
 * Controller of the dashboardApp
 */
angular.module('dashboardApp')
.controller('HappinstancedetailCtrl',
  function ($scope, $routeParams, Happinstance, PortInfo, $location) {
    const happinstance = {
      application: $routeParams.application,
      name: $routeParams.name
    }
    console.log("Happinstance Info: ", happinstance);
    const refresh_callback = () => {
      $scope.detail = Happinstance.get(happinstance);
      $scope.port_info = PortInfo.get(happinstance);
    }
    $scope.name = $routeParams.name;
    $scope.application = $routeParams.application;
    $scope.detail = Happinstance.get(happinstance);
    $scope.port_info = PortInfo.get(happinstance).$promise.then(refresh_callback);

    $scope.toJson = angular.toJson;
    $scope.toggleStatus = (status) => {
      const toggled = status === 'on' ? 'off' : 'on';
      Happinstance.changeStatus(happinstance, {action: toggled}, refresh_callback);
    }

    $scope.delete = () =>
      Happinstance.delete(happinstance, () => $location.url('/'));
  });
