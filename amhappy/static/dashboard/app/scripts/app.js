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
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
            templateUrl: 'views/main.html',
            controller: 'MainCtrl',
            resolve: {
                happinstances: function (Happinstance) {
                    return Happinstance.query().$promise;
                }
            }
        }
    )
        .when('/happinstance_detail/:application/:name', {
            templateUrl: 'views/happinstancedetail.html',
            controller: 'HappinstancedetailCtrl'
        })
        .when('/create_happinstance', {
            templateUrl: 'views/createhappinstance.html',
            controller: 'CreatehappinstanceCtrl'
        })
      .otherwise({
        redirectTo: '/'
      });
  });
