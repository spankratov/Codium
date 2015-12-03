/**
 * Created by Kirov on 19/11/15.
 */
(function () {
    'use strict';
    angular.module('application.routes')
        .config(function ($routeProvider) {
            $routeProvider.when('/', {
                templateUrl: '/static/templates/index.html'
            }).when('/login', {
                controller: 'AuthController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/auth/login.html'
            }).when('/actions', {
                controller: 'ActionsController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/actions/index.html'
            }).otherwise({
                redirectTo: '/'
            });
        }).run(function ($rootScope, $location, Auth) {
        $rootScope.$on("$routeChangeStart", function (event, next, current) {
            if (Auth.getToken() == null) {
                if ((next.templateUrl === "/static/templates/auth/register.html") ||
                    (next.templateUrl === "/static/templates/auth/login.html")) {
                } else {
                    // no logged user, redirect to /login
                    if (next.templateUrl === "/static/templates/auth/login.html") {
                    } else {
                        $location.path("/login");
                    }
                }
            } else {
                if ((next.templateUrl === "/static/templates/auth/register.html") ||
                    (next.templateUrl === "/static/templates/auth/login.html")) {
                    $location.path("/");
                }
            }
        })
    });
})();
