/**
 * Created by Kirov on 19/11/15.
 */
(function () {
    'use strict';

    angular.module('application.actions', [
        'application.actions.controllers',
        'application.actions.services'
    ]);

    angular.module('application.actions.controllers', []);
    angular.module('application.actions.services', ['ngResource']);
})();
