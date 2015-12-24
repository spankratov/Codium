(function () {
    'use strict';

    angular.module('application.projects.services').
    factory('Projects', function ($resource) {
        return $resource('api/v1/projects/:projectId/', null,
            {
                'update': {
                    method: 'PUT',
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
                }
            },
            {
                stripTrailingSlashes: false
            });
    });
    
    angular.module('application.projects.services').
    factory('CharacterProjects', function ($resource) {
        return $resource('api/v1/characters/:characterId/projects/:projectId/', null,
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
