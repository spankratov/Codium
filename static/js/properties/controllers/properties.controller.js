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
        });

    angular.module('application.properties.controllers')
        .controller('CharacterPropertiesController', function (CharacterProperties, Properties, $window, $scope, $routeParams) {

            var vm = this;

            Properties.query(function (response) {
                vm.allProperties = JSON.parse(angular.toJson(response));
                CharacterProperties.query({characterId: $routeParams.characterId}, function (response) {
                    vm.properties = JSON.parse(angular.toJson(response));
                    vm.availableProperties = [];

                    for (var i in vm.allProperties) {
                        var found = false;
                        for (var j in vm.properties) {
                            if (vm.allProperties[i].id == vm.properties[j].id) {
                                found = true;
                                break;
                            }
                        }
                        if (!found) {
                            vm.availableProperties.push(vm.allProperties[i]);
                        }
                    }
                });
            });


            vm.showForm = false;

            vm.toggleForm = function () {
                vm.showForm = !vm.showForm;
            };

            vm.body = false;

            vm.update = function (index) {

                CharacterProperties.update({
                    characterId: $routeParams.characterId, propertyId: vm.properties[index].id
                }, {
                    purchase_date: vm.properties[index].purchase_date,
                }, function (response) {

                    vm.properties[index].isRequestSent = true;
                    var result = JSON.parse(angular.toJson(response));
                    if (response.$status >= 500) {
                        vm.properties[index].status = false;
                        vm.properties[index].message = "Server Error";
                    } else if (response.$status >= 400) {
                        vm.properties[index].status = false;
                        vm.properties[index].errors = result;
                        vm.properties[index].message = "Property was NOT updated.";
                    } else if (response.$status >= 200) {
                        vm.properties[index].status = true;
                        vm.properties[index].message = "Property was updated.";
                        delete vm.properties[index].errors;
                    }
                });
            };

            vm.resetProperty = function (index) {
                CharacterProperties.get({
                    characterId: $routeParams.characterId, propertyId: vm.properties[index].id
                }, function (response) {
                    vm.properties[index] = JSON.parse(angular.toJson(response));
                })
            };

            vm.newProperty = {};
            vm.resetNewProperty = function () {
                vm.newProperty = {};
            };

            vm.deleteAvailableProperty = function (id) {
                for (var i = 0; i < vm.availableProperties.length; i++) {
                    if (vm.availableProperties[i].id == id) {
                        vm.availableProperties.splice(i, 1);
                        break;
                    }
                }
            };

            vm.addAvailableProperty = function (id) {
                for (var i = 0; i < vm.allProperties.length; i++) {
                    if (vm.allProperties[i].id == id) {
                        vm.availableProperties.push(vm.allProperties[i]);
                        break;
                    }
                }
            };

            vm.add = function () {
                CharacterProperties.save({characterId: $routeParams.characterId}, vm.newProperty, function (response) {
                    vm.newProperty.isRequestSent = true;
                    var result = JSON.parse(angular.toJson(response));
                    if (response.$status >= 500) {
                        vm.newProperty.status = false;
                        vm.newProperty.message = "Server Error";
                        delete vm.newProperty.errors
                    } else if (response.$status >= 400) {
                        vm.newProperty.status = false;
                        vm.newProperty.message = "New Property was NOT added.";
                        vm.newProperty.errors = result;
                    } else if (response.$status >= 200) {
                        vm.deleteAvailableProperty(result.id);
                        vm.properties.push(result);
                        vm.newProperty.status = true;
                        vm.newProperty.message = "New Property was added.";
                        delete vm.newProperty.errors;
                    }
                })
            };

            vm.delete = function (index) {
                var id = vm.properties[index].id;
                vm.addAvailableProperty(id);
                vm.properties.splice(index, 1);
                CharacterProperties.delete({characterId: $routeParams.characterId, propertyId: id});
            };
        });


})();
