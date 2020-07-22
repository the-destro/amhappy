'use strict';

/**
 * @ngdoc service
 * @name dashboardApp.portinfo
 * @description
 * # portinfo
 * Factory in the dashboardApp.
 */
angular.module('dashboardApp')
.service('PortInfo', function ($resource, service_root, portinfo_url) {
  return $resource(`${service_root}${portinfo_url}/:application/:name`)
})
