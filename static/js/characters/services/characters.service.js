(function () {
    'use strict';

    angular.module('application.characters.services').
    factory('Characters', function ($resource) {
        return $resource('api/v1/characters/:characterId/', null,
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
