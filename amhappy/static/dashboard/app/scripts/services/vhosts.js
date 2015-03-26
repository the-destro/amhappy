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
    var service_url = service_root + vhosts_url + '/:application';
        return $resource(service_url, {}, {
      query: {method:'GET'}
    });
  });
