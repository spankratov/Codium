(function () {
    'use strict';

    angular.module('application.users.services').
    factory('Users', function ($resource) {
        return $resource('api/v1/users/:userId/', null,
            {
                update: {method: 'PUT'},
                partial_update: {method: 'PATCH'},
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
