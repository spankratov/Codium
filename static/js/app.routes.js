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
            }).when('/attributes', {
                controller: 'AttributesController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/attributes/index.html'
            }).when('/events', {
                controller: 'EventsController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/events/index.html'
            }).when('/properties', {
                controller: 'PropertiesController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/properties/index.html'
            }).when('/universities', {
                controller: 'UniversitiesController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/universities/index.html'
            }).when('/projects', {
                controller: 'ProjectsController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/projects/index.html'
            }).when('/jobs', {
                controller: 'JobsController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/jobs/index.html'
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
