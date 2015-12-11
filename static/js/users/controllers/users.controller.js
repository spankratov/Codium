(function () {
    'use strict';

    angular.module('application.users.controllers')
        .controller('UsersController', function (Users, $window) {
            var vm = this;
            vm.users = Users.query();

            vm.new = {};

            vm.saveUser = function () {
                var user = Users.save(vm.new);
                $window.location = '/users';
            };

            vm.deleteUser = function (index) {
                var userId = vm.users[index].id;
                vm.users.splice(index, 1);
                Users.delete({userId: userId});
            };


        })
})();
