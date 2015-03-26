'use strict';

describe('Controller: CreatehappinstanceCtrl', function () {

  // load the controller's module
  beforeEach(module('dashboardApp'));

  var CreatehappinstanceCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    CreatehappinstanceCtrl = $controller('CreatehappinstanceCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
