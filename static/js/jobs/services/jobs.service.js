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

    angular.module('application.jobs.services').
    factory('CharacterJobs', function ($resource) {
        return $resource('api/v1/characters/:characterId/jobs/:jobId/', null,
            {
                'update': {
                    method: 'PATCH',
                    interceptor: {
                        response: function (response) {
                            var result = response.resource;
                            result.$status = response.status;
                            return result;
                        }
                    }
                },
                query: {
                    method: 'GET',
                    isArray: true
                },
                save: {
                    method: 'POST',
                    interceptor: {
                        response: function (response) {
                            var result = response.resource;
                            result.$status = response.status;
                            return result;
                        }
                    }
                }
            },
            {
                stripTrailingSlashes: false
            });
    });
})();
