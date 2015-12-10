(function () {
    'use strict';

    angular.module('application.universities.services').
    factory('Universities', function ($resource) {
        return $resource('api/v1/universities/:universityId/', null,
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
