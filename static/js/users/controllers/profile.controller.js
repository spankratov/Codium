(function () {
    'use strict';

    angular.module('application.users.controllers')
        .controller('ProfileController', function (Users, Characters, $window, $routeParams) {
            var vm = this;


            Users.get({userId: $routeParams.userId}).$promise.then(function (data) {
                vm.user = data;
                Characters.get({characterId: vm.user.character}).$promise.then(function (data) {
                    vm.character = data;
                });
            });


            vm.userUpdate = function () {
                Users.partial_update({userId: vm.user.data.id}, {username: vm.user.data.username});
                $window.location = '/users/' + vm.user.data.id;
            };

            vm.userDelete = function () {
                Users.delete({userId: vm.user.data.id});
                $window.location = '/users/';
            };

            vm.characterUpdate = function () {
                Characters.update({characterId: vm.character.data.id}, vm.character.data);
                $window.location = '/users/' + vm.user.data.id;
            };

            vm.characterDelete = function () {
                Characters.delete({characterId: vm.character.data.id});
                vm.character.data = null;
            }
        })
})();
