/**
 * Created by Kirov on 19/11/15.
 */
(function () {
    'use strict';

    angular.module('application.auth.services').
    factory('Actions', function ($resource) {
        return $resource('api/v1/actions/:actionId/', null,
            {
                'update': {method: 'PUT'}
            },
            {
                stripTrailingSlashes: false
            });
    });
})();
