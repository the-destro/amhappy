'use strict';

describe('Service: Happinstance', function () {

  // load the service's module
  beforeEach(module('dashboardApp'));

  // instantiate service
  var Happinstance;
  beforeEach(inject(function (_Happinstance_) {
    Happinstance = _Happinstance_;
  }));

  it('should do something', function () {
    expect(!!Happinstance).toBe(true);
  });

});
