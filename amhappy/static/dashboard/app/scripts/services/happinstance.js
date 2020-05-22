'use strict';

/**
 * @ngdoc service
 * @name dashboardApp.Happinstance
 * @description
 * # Happinstance
 * Factory in the dashboardApp.
 */
angular.module('dashboardApp')
.factory('Happinstance', function ($resource, service_root, happinstance_url) {
  return $resource(
    `${service_root}${happinstance_url}/:application/:name`,
    {},
    {query: {method: 'GET', isArray: false}, changeStatus: {method: 'PUT'}})
})
