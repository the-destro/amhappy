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
    // Service logic
    // ...
    var service_url = service_root + happinstance_url + '/:application/:name';
    return $resource(service_url, {}, {
      query: {method:'GET', isArray:false},
      changeStatus: {method:'PUT'}
    });
  });
