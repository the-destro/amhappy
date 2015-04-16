'use strict';

describe('Service: portinfo', function () {

  // load the service's module
  beforeEach(module('dashboardApp'));

  // instantiate service
  var portinfo;
  beforeEach(inject(function (_portinfo_) {
    portinfo = _portinfo_;
  }));

  it('should do something', function () {
    expect(!!portinfo).toBe(true);
  });

});
