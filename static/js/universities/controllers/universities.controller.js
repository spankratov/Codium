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

    angular.module('application.universities.controllers')
        .controller('UniversitiesController', function (Universities, $window) {
            var vm = this;
            Universities.query(function (response) {
                vm.universities = JSON.parse(angular.toJson(response));
            });

            vm.new = {};

            vm.saveUniversity = function () {
                Universities.save(vm.new, function (response) {
                    vm.universities.push(JSON.parse(angular.toJson(response)));
                });
            };

            vm.deleteUniversity = function (index) {
                var universityId = vm.universities[index].id;
                vm.universities.splice(index, 1);
                Universities.delete({universityId: universityId});
            };

            vm.university = null;

            vm.setCurrentUniversity = function (university) {
                vm.university = university;
            };

            vm.updateUniversity = function () {
                update(vm.university, Universities, {universityId: vm.university.id}, vm.university);
            };

            vm.resetUniversity = function () {
                Universities.get({
                    universityId: vm.university.id
                }, function (response) {
                    vm.university = JSON.parse(angular.toJson(response));
                })
            };
        });
    
    angular.module('application.universities.controllers')
        .controller('CharacterUniversitiesController', function (CharacterUniversities, Universities, $window, $scope, $routeParams) {

            var vm = this;

            Universities.query(function (response) {
                vm.allUniversities = JSON.parse(angular.toJson(response));
                CharacterUniversities.query({characterId: $routeParams.characterId}, function (response) {
                    vm.universities = JSON.parse(angular.toJson(response));
                    vm.availableUniversities = [];

                    for (var i in vm.allUniversities) {
                        var found = false;
                        for (var j in vm.universities) {
                            if (vm.allUniversities[i].id == vm.universities[j].id) {
                                found = true;
                                break;
                            }
                        }
                        if (!found) {
                            vm.availableUniversities.push(vm.allUniversities[i]);
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

                var copy = angular.copy(vm.universities[index]);

                CharacterUniversities.update({
                    characterId: $routeParams.characterId, universityId: vm.universities[index].id
                }, {
                    finished: copy.finished,
                    entering_date: copy.entering_date
                }, function (response) {

                    vm.universities[index].isRequestSent = true;
                    var result = JSON.parse(angular.toJson(response));
                    if (response.$status >= 500) {
                        vm.universities[index].status = false;
                        vm.universities[index].message = "Server Error";
                    } else if (response.$status >= 400) {
                        vm.universities[index].status = false;
                        vm.universities[index].errors = result;
                        vm.universities[index].message = "University was NOT updated.";
                    } else if (response.$status >= 200) {
                        vm.universities[index].status = true;
                        vm.universities[index].message = "University was updated.";
                        delete vm.universities[index].errors;
                    }
                });
            };

            vm.resetUniversity = function (index) {
                CharacterUniversities.get({
                    characterId: $routeParams.characterId, universityId: vm.universities[index].id
                }, function (response) {
                    vm.universities[index] = JSON.parse(angular.toJson(response));
                })
            };

            vm.newUniversity = {};
            vm.resetNewUniversity = function () {
                vm.newUniversity = {};
            };

            vm.deleteAvailableUniversity = function (id) {
                for (var i = 0; i < vm.availableUniversities.length; i++) {
                    if (vm.availableUniversities[i].id == id) {
                        vm.availableUniversities.splice(i, 1);
                        break;
                    }
                }
            };

            vm.addAvailableUniversity = function (id) {
                for (var i = 0; i < vm.allUniversities.length; i++) {
                    if (vm.allUniversities[i].id == id) {
                        vm.availableUniversities.push(vm.allUniversities[i]);
                        break;
                    }
                }
            };

            vm.add = function () {
                CharacterUniversities.save({characterId: $routeParams.characterId}, vm.newUniversity, function (response) {
                    if (vm.newUniversity.isRequestSent) {
                        vm.resetNewUniversity();
                    }
                    vm.newUniversity.isRequestSent = true;
                    var result = JSON.parse(angular.toJson(response));
                    if (response.$status >= 500) {
                        vm.newUniversity.status = false;
                        vm.newUniversity.message = "Server Error";
                    } else if (response.$status >= 400) {
                        vm.newUniversity.status = false;
                        vm.newUniversity.message = "New University was NOT added.";
                        vm.newUniversity.errors = result;
                    } else if (response.$status >= 200) {
                        vm.deleteAvailableUniversity(result.id);
                        vm.universities.push(result);
                        vm.newUniversity.status = true;
                        vm.newUniversity.message = "New University was added.";
                    }
                })
            };

            vm.delete = function (index) {
                var id = vm.universities[index].id;
                vm.addAvailableUniversity(id);
                vm.universities.splice(index, 1);
                CharacterUniversities.delete({characterId: $routeParams.characterId, universityId: id});
            };
        });
    
})();
