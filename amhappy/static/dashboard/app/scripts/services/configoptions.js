'use strict';

/**
 * @ngdoc service
 * @name dashboardApp.ConfigInfo
 * @description
 * # ConfigInfo
 * Factory in the dashboardApp.
 */
angular.module('dashboardApp')
.factory('ConfigOptions', function ($resource, service_root, config_url) {
    console.log("FETCHING " + service_root + config_url);
    return $resource(service_root + config_url)
  }
)

