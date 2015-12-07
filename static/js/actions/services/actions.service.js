(function () {
    'use strict';

    angular.module('application.actions.services').
    factory('Actions', function ($resource) {
        return $resource('api/v1/actions/:actionId/', null,
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
