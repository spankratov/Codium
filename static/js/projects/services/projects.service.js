(function () {
    'use strict';

    angular.module('application.projects.services').
    factory('Projects', function ($resource) {
        return $resource('api/v1/projects/:projectId/', null,
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
