(function () {
    'use strict';

    angular.module('application', [
        'application.config',
        'application.routes',
        'application.auth',
        'application.actions',
        'application.attributes',
        'application.events',
        'application.properties',
        'application.universities',
        'application.projects',
        'application.jobs',
        'application.users',
        'application.characters'
    ]);
    angular.module('application.config', ['ngResource']);
    angular.module('application.routes', ['ngRoute']);
})();
