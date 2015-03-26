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
    // Service logic
    // ...
    var service_url = service_root + application_url + '/:application';
    return $resource(service_url, {}, {
      query: {method:'GET', isArray:true}
    });
  });
