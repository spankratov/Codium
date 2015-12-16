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

    angular.module('application.projects.controllers')
        .controller('ProjectsController', function (Projects, $window) {
            var vm = this;
            Projects.query(function (response) {
                vm.projects = JSON.parse(angular.toJson(response));
            });

            vm.new = {};

            vm.saveProject = function () {
                Projects.save(vm.new, function (response) {
                    vm.projects.push(JSON.parse(angular.toJson(response)));
                });
            };

            vm.deleteProject = function (index) {
                var projectId = vm.projects[index].id;
                vm.projects.splice(index, 1);
                Projects.delete({projectId: projectId});
            };

            vm.project = null;

            vm.setCurrentProject = function (project) {
                vm.project = project;
            };

            vm.updateProject = function () {
                update(vm.project, Projects, {projectId: vm.project.id}, vm.project);
            };

            vm.resetProject = function () {
                Projects.get({
                    projectId: vm.project.id
                }, function (response) {
                    vm.project = JSON.parse(angular.toJson(response));
                })
            };
        });

    angular.module('application.projects.controllers')
        .controller('CharacterProjectsController', function (CharacterProjects, Projects, $window, $scope, $routeParams) {

            var vm = this;

            Projects.query(function (response) {
                vm.allProjects = JSON.parse(angular.toJson(response));
                CharacterProjects.query({characterId: $routeParams.characterId}, function (response) {
                    vm.projects = JSON.parse(angular.toJson(response));
                    vm.availableProjects = [];

                    for (var i in vm.allProjects) {
                        var found = false;
                        for (var j in vm.projects) {
                            if (vm.allProjects[i].id == vm.projects[j].id) {
                                found = true;
                                break;
                            }
                        }
                        if (!found) {
                            vm.availableProjects.push(vm.allProjects[i]);
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

                CharacterProjects.update({
                    characterId: $routeParams.characterId, projectId: vm.projects[index].id
                }, {
                    finished: vm.projects[index].finished,
                    taking_date: vm.projects[index].taking_date,
                    name: vm.projects[index].name
                }, function (response) {

                    vm.projects[index].isRequestSent = true;
                    var result = JSON.parse(angular.toJson(response));
                    if (response.$status >= 500) {
                        vm.projects[index].status = false;
                        vm.projects[index].message = "Server Error";
                    } else if (response.$status >= 400) {
                        vm.projects[index].status = false;
                        vm.projects[index].errors = result;
                        vm.projects[index].message = "Project was NOT updated.";
                    } else if (response.$status >= 200) {
                        vm.projects[index].status = true;
                        vm.projects[index].message = "Project was updated.";
                        delete vm.projects[index].errors;
                    }
                });
            };

            vm.resetProject = function (index) {
                CharacterProjects.get({
                    characterId: $routeParams.characterId, projectId: vm.projects[index].id
                }, function (response) {
                    vm.projects[index] = JSON.parse(angular.toJson(response));
                })
            };

            vm.newProject = {};
            vm.resetNewProject = function () {
                vm.newProject = {};
            };

            vm.deleteAvailableProject = function (id) {
                for (var i = 0; i < vm.availableProjects.length; i++) {
                    if (vm.availableProjects[i].id == id) {
                        vm.availableProjects.splice(i, 1);
                        break;
                    }
                }
            };

            vm.addAvailableProject = function (id) {
                for (var i = 0; i < vm.allProjects.length; i++) {
                    if (vm.allProjects[i].id == id) {
                        vm.availableProjects.push(vm.allProjects[i]);
                        break;
                    }
                }
            };

            vm.add = function () {
                CharacterProjects.save({characterId: $routeParams.characterId}, vm.newProject, function (response) {
                    if (vm.newProject.isRequestSent) {
                        vm.resetNewProject();
                    }
                    vm.newProject.isRequestSent = true;
                    var result = JSON.parse(angular.toJson(response));
                    if (response.$status >= 500) {
                        vm.newProject.status = false;
                        vm.newProject.message = "Server Error";
                    } else if (response.$status >= 400) {
                        vm.newProject.status = false;
                        vm.newProject.message = "New Project was NOT added.";
                        vm.newProject.errors = result;
                    } else if (response.$status >= 200) {
                        vm.deleteAvailableProject(result.id);
                        vm.projects.push(result);
                        vm.newProject.status = true;
                        vm.newProject.message = "New Project was added.";
                    }
                })
            };

            vm.delete = function (index) {
                var id = vm.projects[index].id;
                vm.addAvailableProject(id);
                vm.projects.splice(index, 1);
                CharacterProjects.delete({characterId: $routeParams.characterId, projectId: id});
            };
        });


})();
