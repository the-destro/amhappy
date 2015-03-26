'use strict';

describe('Controller: HeadercontrollerCtrl', function () {

  // load the controller's module
  beforeEach(module('dashboardApp'));

  var HeadercontrollerCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    HeadercontrollerCtrl = $controller('HeadercontrollerCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
