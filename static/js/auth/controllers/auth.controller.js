/**
 * Created by Kirov on 19/11/15.
 */
(function () {
    'use strict';

    angular.module('application.auth.controllers')
        .controller('AuthController', function (Auth) {
            var vm = this;

            vm.isLoggedIn = !!Auth.getToken();

            vm.login = function () {
                Auth.login(vm.username, vm.password);
            };

            vm.logout = function () {
                Auth.logout();
            };

            vm.ngViewClasses = function () {
                if (vm.isLoggedIn) {
                    return "col-sm-9 col-md-10";
                } else {
                    return "col-sm-4 col-md-4 col-sm-offset-4 col-md-offset-4";
                }
            }


        })
})();
