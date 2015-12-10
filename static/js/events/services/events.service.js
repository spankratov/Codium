(function () {
    'use strict';

    angular.module('application.events.services').
    factory('Events', function ($resource) {
        return $resource('api/v1/events/:eventId/', null,
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
