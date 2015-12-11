(function () {
    'use strict';

    angular.module('application.attributes.services').
    factory('Attributes', function ($resource) {
        return $resource('api/v1/attributes/:attributeId/', null,
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

    angular.module('application.attributes.services').
    factory('CharacterAttributes', function ($resource) {
        return $resource('api/v1/characters/:characterId/attributes/:attributeId/', null,
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

})();
