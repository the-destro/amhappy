'use strict';

/**
 * @ngdoc service
 * @name dashboardApp.vhosts
 * @description
 * # vhosts
 * Service in the dashboardApp.
 */
angular.module('dashboardApp')
.service('Vhosts', function ($resource, service_root, vhosts_url) {
  return $resource(
    `${service_root}${vhosts_url}/:application`,
    {},
    {query: {method: 'GET'}})
})
