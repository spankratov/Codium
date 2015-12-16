(function () {
    'use strict';

    angular.module('application.universities.services').
    factory('Universities', function ($resource) {
        return $resource('api/v1/universities/:universityId/', null,
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

    angular.module('application.universities.services').
    factory('CharacterUniversities', function ($resource) {
        return $resource('api/v1/characters/:characterId/universities/:universityId/', null,
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
