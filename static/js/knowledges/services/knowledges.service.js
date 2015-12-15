(function () {
    'use strict';

    angular.module('application.knowledges.services').
    factory('Knowledges', function ($resource) {
        return $resource('api/v1/knowledges/:knowledgeId/', null,
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

    angular.module('application.knowledges.services').
    factory('CharacterKnowledges', function ($resource) {
        return $resource('api/v1/characters/:characterId/knowledges/:knowledgeId/', null,
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
                }
            },
            {
                stripTrailingSlashes: false
            });
    });

})();
