'use strict';

/**
 * @ngdoc overview
 * @name dashboardApp
 * @description
 * # dashboardApp
 *
 * Main module of the application.
 */
angular
  .module('dashboardApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'mgcrea.ngStrap'
  ])
  .config(function ($routeProvider, $locationProvider) {
    $locationProvider.hashPrefix('');
    $routeProvider
      .when('/', {
            templateUrl: 'views/main.html',
            controller: 'MainCtrl',
            resolve: {
                happinstances: (Happinstance) => Happinstance.query().$promise
            }
        })
        .when('/happinstance_detail/:application/:name', {
            templateUrl: 'views/happinstancedetail.html',
            controller: 'HappinstancedetailCtrl'
        })
        .when('/create_happinstance', {
            templateUrl: 'views/createhappinstance.html',
            controller: 'CreatehappinstanceCtrl'
        })
        .when('/manage_vhosts', {
            templateUrl: 'views/managevhosts.html',
            controller: 'ManagevhostsCtrl'
        })
      .otherwise({
        redirectTo: '/'
      });
  });
