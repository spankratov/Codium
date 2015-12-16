(function () {
    'use strict';

    var update = function (obj, resource, params, data) {
        resource.update(params, data,
            function (response) {
                obj.isRequestSent = true;
                var result = JSON.parse(angular.toJson(response));
                if (response.$status >= 500) {
                    obj.status = false;
                    obj.message = "Ошибка на сервере";
                } else if (response.$status >= 400) {
                    obj.status = false;
                    obj.errors = result;
                    obj.message = "Изменения не сохранены.";
                } else if (response.$status >= 200) {
                    obj.status = true;
                    obj.message = "Изменения сохранены";
                    delete obj.errors;
                }
            });
    };

    angular.module('application.attributes.controllers')
        .controller('AttributesController', function (Attributes, $window) {
            var vm = this;
            Attributes.query(function (response) {
                vm.attributes = JSON.parse(angular.toJson(response));
            });

            vm.new = {};

            vm.saveAttribute = function () {
                Attributes.save(vm.new, function (response) {
                    vm.attributes.push(JSON.parse(angular.toJson(response)));
                });
            };

            vm.deleteAttribute = function (index) {
                var attributeId = vm.attributes[index].id;
                vm.attributes.splice(index, 1);
                Attributes.delete({attributeId: attributeId});
            };

            vm.attribute = null;

            vm.setCurrentAttribute = function (attribute) {
                vm.attribute = attribute;
            };

            vm.updateAttribute = function () {
                update(vm.attribute, Attributes, {attributeId: vm.attribute.id}, vm.attribute);
            };

            vm.resetAttribute = function () {
                Attributes.get({
                    attributeId: vm.attribute.id
                }, function (response) {
                    vm.attribute = JSON.parse(angular.toJson(response));
                })
            };
        });

    angular.module('application.attributes.controllers')
        .controller('CharacterAttributesController', function (CharacterAttributes, $window, $scope, $routeParams) {

            var vm = this;


            vm.attributes = CharacterAttributes.query({characterId: $routeParams.characterId});

            vm.body = false;

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
