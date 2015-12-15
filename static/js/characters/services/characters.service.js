(function () {
    'use strict';

    angular.module('application.characters.services').
    factory('Characters', function ($resource) {
        return $resource('api/v1/characters/:characterId/', null,
            {
                update: {
                    method: 'PUT',
                    interceptor: {
                        response: function (response) {
                            var result = response.resource;
                            result.$status = response.status;
                            return result;
                        }
                    }
                },
                partial_update: {
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
                    isArray: true,
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
