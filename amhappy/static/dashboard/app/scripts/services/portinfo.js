'use strict';

/**
 * @ngdoc service
 * @name dashboardApp.portinfo
 * @description
 * # portinfo
 * Factory in the dashboardApp.
 */
angular.module('dashboardApp')
.factory('PortInfo', function ($resource, service_root, portinfo_url) {
  $resource(`${service_root}${portinfo_url}/:application/:name`)
});
