/**
 * Created by Kirov on 19/11/15.
 */
(function () {
	'use strict';

	angular.module('application', [
		'application.config',
		'application.routes',
		'application.auth'
	]);
	angular.module('application.config', []);
	angular.module('application.routes', ['ngRoute']);
})();
