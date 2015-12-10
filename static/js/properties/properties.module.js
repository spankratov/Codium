(function () {
    'use strict';

    angular.module('application.properties', [
        'application.properties.controllers',
        'application.properties.services'
    ]);

    angular.module('application.properties.controllers', []);
    angular.module('application.properties.services', ['ngResource']);
})();
