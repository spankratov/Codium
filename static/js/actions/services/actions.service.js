(function () {
    'use strict';

    angular.module('application.actions.services').
    factory('Actions', function ($resource) {
        return $resource('api/v1/actions/:actionId/', null,
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
