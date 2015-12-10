(function () {
    'use strict';

    angular.module('application.properties.controllers')
        .controller('PropertiesController', function (Properties, $window) {
            var vm = this;
            vm.properties = Properties.query();

            vm.new = {};

            vm.saveProperty = function () {
                var property = Properties.save(vm.new);
                $window.location = '/properties';
            };

            vm.deleteProperty = function (index) {
                var propertyId = vm.properties[index].id;
                vm.properties.splice(index, 1);
                Properties.delete({propertyId: propertyId});
            };

            vm.currentProperty = null;

            vm.setCurrentProperty = function (property) {
                vm.currentProperty = (JSON.parse(JSON.stringify(property)))
            };

            vm.updateProperty = function () {
                Properties.update({propertyId: vm.currentProperty.id}, vm.currentProperty);
                $window.location = "/properties"
            }
        })
})();
