'use strict';

/**
 * @ngdoc service
 * @name dashboardApp.ConfigInfo
 * @description
 * # ConfigInfo
 * Factory in the dashboardApp.
 */
angular.module('dashboardApp')
.service('ConfigOptions', function ($resource, service_root, config_url) {
  return $resource(`${service_root}${config_url}`)
})

