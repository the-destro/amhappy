'use strict';

/**
 * @ngdoc function
 * @name dashboardApp.controller:CreatehappinstanceCtrl
 * @description
 * # CreatehappinstanceCtrl
 * Controller of the dashboardApp
 */
angular.module('dashboardApp')
.controller('CreatehappinstanceCtrl',
  function ($scope, $location, Application, Happinstance, ConfigOptions, Vhosts) {
    Application.query((applications) => $scope.applications = applications);
    $scope.environments = {};
    $scope.selectedApplication = '';
    $scope.happinstanceName = '';
    $scope.toJson = angular.toJson;
    $scope.isDefined = angular.isDefined;
    $scope.configs = ConfigOptions.get();
    console.log("Is this a promise?", $scope.configs);

    // Strip chars from name
    $scope.$watch(
      () => $scope.happinstanceName,
      (name) => $scope.happinstanceName = name.replace(/[^a-zA-Z.]/g, '')
    );

    $scope.$watch(
      () => $scope.selectedApplication,
      (selectedApplication) => {
        if (selectedApplication === "") return;
        console.log("Configs? " , $scope.configs);
        $scope.sourceCodeDirs = $scope.configs.source_code_dirs;

        if ($scope.happinstanceName === '') {
          $scope.happinstanceName = $scope.selectedApplication;
        }
        const query = {application: selectedApplication}
        console.log("Selected application is ", selectedApplication);
        $scope.happConfig = Application.get(query);
        $scope.vhosts = Vhosts.get(query);

      });
    $scope.submit = () => {
      angular.forEach($scope.environments, (variables, image) => {
        variables.forEach(
          (value, variable) => {
            console.log(`Setting {$image}:{$variable} to {$value}`);
            $scope.happConfig[image]['environment'][variable] = value
          }
        )
      });
      Happinstance.save(
        {application: $scope.selectedApplication, name: $scope.happinstanceName},
        $scope.happConfig,
        () => $location.url('/'));

    }
  });
