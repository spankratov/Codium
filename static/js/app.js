/**
 * Created by Kirov on 19/11/15.
 */
(function () {
    'use strict';

    angular.module('application', [
        'application.config',
        'application.routes',
        'application.auth',
        'application.actions',
        'application.attributes'
    ]);
    angular.module('application.config', ['ngResource']);
    angular.module('application.routes', ['ngRoute']);
})();
