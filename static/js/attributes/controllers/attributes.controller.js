(function () {
    'use strict';

    angular.module('application.attributes.controllers')
        .controller('AttributesController', function (Attributes, $window) {
            var vm = this;
            vm.attributes = Attributes.query();

            vm.new = {};

            vm.saveAttribute = function () {
                var attribute = Attributes.save(vm.new);
                $window.location = '/attributes';
            };

            vm.deleteAttribute = function (index) {
                var attributeId = vm.attributes[index].id;
                vm.attributes.splice(index, 1);
                Attributes.delete({attributeId: attributeId});
            };

            vm.currentAttribute = null;

            vm.setCurrentAttribute = function (attribute) {
                vm.currentAttribute = (JSON.parse(JSON.stringify(attribute)))
            };

            vm.updateAttribute = function () {
                Attributes.update({attributeId: vm.currentAttribute.id}, vm.currentAttribute);
                $window.location = "/attributes"
            }
        });

    angular.module('application.attributes.controllers')
        .controller('CharacterAttributesController', function (CharacterAttributes, $window, $scope) {

            var vm = this;

            vm.init = function (id) {
                vm.characterId = id;
                vm.attributes = CharacterAttributes.query({characterId: id});
            };

            vm.body = false;

            vm.update = function (index) {
                CharacterAttributes.update({
                    characterId: vm.characterId, attributeId: vm.attributes[index].id
                }, vm.attributes[index]).$promise.then(function (response) {
                    if (response.$status == 200) {
                        vm.attributes[index].is_updated = true;
                        vm.attributes[index].class = "glyphicon glyphicon-ok";
                    } else {
                        vm.attributes[index].is_updated = true;
                        vm.attributes[index].class = "glyphicon glyphicon-remove";
                    }
                });
            }


        })

})();
