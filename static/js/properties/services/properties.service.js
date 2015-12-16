(function () {
    'use strict';

    angular.module('application.properties.services').
    factory('Properties', function ($resource) {
        return $resource('api/v1/properties/:propertyId/', null,
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
    
    angular.module('application.properties.services').
    factory('CharacterProperties', function ($resource) {
        return $resource('api/v1/characters/:characterId/properties/:propertyId/', null,
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
