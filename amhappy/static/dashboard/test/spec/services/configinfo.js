'use strict';

describe('Service: ConfigInfo', function () {

  // load the service's module
  beforeEach(module('dashboardApp'));

  // instantiate service
  var ConfigInfo;
  beforeEach(inject(function (_ConfigInfo_) {
    ConfigInfo = _ConfigInfo_;
  }));

  it('should do something', function () {
    expect(!!ConfigInfo).toBe(true);
  });

});
