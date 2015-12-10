(function () {
    'use strict';

    angular.module('application.jobs.services').
    factory('Jobs', function ($resource) {
        return $resource('api/v1/jobs/:jobId/', null,
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
