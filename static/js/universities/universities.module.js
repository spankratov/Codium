(function () {
    'use strict';

    angular.module('application.universities', [
        'application.universities.controllers',
        'application.universities.services'
    ]);

    angular.module('application.universities.controllers', []);
    angular.module('application.universities.services', ['ngResource']);
})();
