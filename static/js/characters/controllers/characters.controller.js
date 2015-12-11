(function () {
    'use strict';

    angular.module('application.characters.controllers')
        .controller('CharacterController', function (Characters, $window) {
            var vm = this;
            vm.init = function (characterId) {
                if (characterId) {
                    Characters.get({characterId: characterId}).$promise.then(function (data) {
                        vm.character = data;
                    })
                }
            };

            vm.new = {};

            vm.saveCharacter = function () {
                var character = Characters.save(vm.new);
                alert("Привет!");
                $window.location = '/characters';
            };

            vm.deleteCharacter = function (index) {
                var characterId = vm.characters[index].id;
                vm.characters.splice(index, 1);
                Characters.delete({characterId: characterId});
            };


            vm.updateCharacter = function () {
                Characters.partial_update({characterId: vm.currentCharacter.id}, {charactername: vm.currentCharacter.charactername});
                $window.location = '/characters';
            }
        })
})();
