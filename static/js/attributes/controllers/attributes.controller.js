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
        })
})();
