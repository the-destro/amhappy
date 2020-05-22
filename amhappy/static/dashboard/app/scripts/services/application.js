'use strict';

/**
 * @ngdoc service
 * @name dashboardApp.Application
 * @description
 * # Application
 * Factory in the dashboardApp.
 */
angular.module('dashboardApp')
.factory('Application', function ($resource, service_root, application_url) {
    return $resource(
      `${service_root}${application_url}/:application`,
      {},
      {query: {method: 'GET', isArray: true}}
    )
  }
)
