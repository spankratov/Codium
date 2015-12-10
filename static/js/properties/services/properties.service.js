(function () {
    'use strict';

    angular.module('application.properties.services').
    factory('Properties', function ($resource) {
        return $resource('api/v1/properties/:propertyId/', null,
            {
                'update': {method: 'PUT'},
                query: {
                    method: 'GET',
                    isArray: true
                }
            },
            {
                stripTrailingSlashes: false
            });
    });
})();
