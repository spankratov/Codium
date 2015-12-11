(function () {
    'use strict';

    angular.module('application.characters', [
        'application.characters.controllers',
        'application.characters.services'
    ]);

    angular.module('application.characters.controllers', []);
    angular.module('application.characters.services', ['ngResource']);
})();
