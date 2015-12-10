(function () {
    'use strict';

    angular.module('application.projects', [
        'application.projects.controllers',
        'application.projects.services'
    ]);

    angular.module('application.projects.controllers', []);
    angular.module('application.projects.services', ['ngResource']);
})();
