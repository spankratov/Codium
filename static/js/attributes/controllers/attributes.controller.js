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
        .controller('CharacterAttributesController', function (CharacterAttributes, $window, $scope, $routeParams) {

            var vm = this;


            vm.attributes = CharacterAttributes.query({characterId: $routeParams.characterId});

            vm.body = true;

            vm.update = function (index) {
                vm.attributes[index].copyValue = angular.copy(vm.attributes[index]);
                CharacterAttributes.update({
                    characterId: $routeParams.characterId, attributeId: vm.attributes[index].id
                }, vm.attributes[index]).$promise.then(function (response) {
                    vm.attributes[index].isRequestSent = true;
                    if (response.$status == 200) {
                        vm.attributes[index].status = true;
                        vm.attributes[index].result = "Attribute was updated."
                    } else {
                        vm.attributes[index].status = false;
                        vm.attributes[index].result = JSON.parse(angular.toJson(response));
                    }
                });
            };
            vm.reset = function (index) {
                CharacterAttributes.get({
                    characterId: $routeParams.characterId, attributeId: vm.attributes[index].id
                }, function (response) {
                    vm.attributes[index] = JSON.parse(angular.toJson(response));
                })
            }


        })

})();
