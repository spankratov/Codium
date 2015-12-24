(function () {
    'use strict';

    angular.module('application.users.controllers')
        .controller('UsersController', function (Users, $window) {
            var vm = this;
            Users.query(function (response) {
                vm.users = JSON.parse(angular.toJson((response)));
            });

            vm.newUser = {};

            vm.addUser = function () {
                delete vm.newUser.errors;
                delete vm.newUser.message;

                Users.save(vm.newUser, function (response) {
                    vm.newUser.isRequestSent = true;
                    var result = JSON.parse(angular.toJson(response));
                    if (response.$status >= 500) {
                        vm.newUser.status = false;
                        vm.newUser.message = "Server Error";
                        delete vm.newUser.errors
                    } else if (response.$status >= 400) {
                        vm.newUser.status = false;
                        vm.newUser.message = "New User was NOT added.";
                        vm.newUser.errors = result;
                    } else if (response.$status >= 200) {
                        vm.users.push(result);
                        vm.newUser.status = true;
                        vm.newUser.message = "New User was added.";
                        delete vm.newUser.errors;
                    }
                });
            };

            vm.resetNewUser = function () {
                vm.newUser = {}
            };

            vm.deleteUser = function (index) {
                var userId = vm.users[index].id;
                vm.users.splice(index, 1);
                Users.delete({userId: userId});
            };


        })
})();
