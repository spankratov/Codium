(function () {
    'use strict';

    angular.module('application.attributes.services').
    factory('Attributes', function ($resource) {
        return $resource('api/v1/attributes/:attributeId/', null,
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
