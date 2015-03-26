'use strict';

describe('Service: vhosts', function () {

  // load the service's module
  beforeEach(module('dashboardApp'));

  // instantiate service
  var vhosts;
  beforeEach(inject(function (_vhosts_) {
    vhosts = _vhosts_;
  }));

  it('should do something', function () {
    expect(!!vhosts).toBe(true);
  });

});
