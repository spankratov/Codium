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
                templateUrl: '/static/templates/actions/content/index.html'
            }).when('/attributes', {
                controller: 'AttributesController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/attributes/content/index.html'
            }).when('/events', {
                controller: 'EventsController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/events/content/index.html'
            }).when('/properties', {
                controller: 'PropertiesController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/properties/content/index.html'
            }).when('/universities', {
                controller: 'UniversitiesController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/universities/content/index.html'
            }).when('/projects', {
                controller: 'ProjectsController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/projects/content/index.html'
            }).when('/jobs', {
                controller: 'JobsController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/jobs/content/index.html'
            }).when('/users', {
                controller: 'UsersController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/users/index.html'
            }).when('/users/:userId/', {
                controller: 'ProfileController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/profile/index.html'
            }).when('/docs/', {
                controller: function () {
                    window.location.replace('http://127.0.0.1:8000/docs/');
                },
                template: "<div></div>"
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
