(function () {
    'use strict';

    angular.module('application.attributes', [
        'application.attributes.controllers',
        'application.attributes.services'
    ]);

    angular.module('application.attributes.controllers', []);
    angular.module('application.attributes.services', ['ngResource']);
})();
