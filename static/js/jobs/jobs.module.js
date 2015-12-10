(function () {
    'use strict';

    angular.module('application.jobs', [
        'application.jobs.controllers',
        'application.jobs.services'
    ]);

    angular.module('application.jobs.controllers', []);
    angular.module('application.jobs.services', ['ngResource']);
})();
