(function () {
    'use strict';

    angular.module('application.knowledges', [
        'application.knowledges.controllers',
        'application.knowledges.services'
    ]);

    angular.module('application.knowledges.controllers', []);
    angular.module('application.knowledges.services', ['ngResource']);
})();
