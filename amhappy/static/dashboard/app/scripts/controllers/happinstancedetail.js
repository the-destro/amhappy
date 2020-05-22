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
  function ($scope, $routeParams, $location, Happinstance, PortInfo) {
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
    $scope.port_info = PortInfo.get(happinstance);
    console.log("GOT NEW PORT INFO???", $scope.port_info);

    $scope.toJson = angular.toJson;
    $scope.toggleStatus = (status) => {
      const toggled = status === 'on' ? 'off' : 'on';
      console.log(
        "NOT CHANGING STATUS, BUT HERE IS THE PORT INFO:", $scope.port_info);
      // Happinstance.changeStatus(happinstance, {action: toggled}, refresh_callback);
    }

    $scope.delete = () =>
      Happinstance.delete(happinstance, () => $location.url('/'));
  });
