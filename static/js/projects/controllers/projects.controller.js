(function () {
    'use strict';

    angular.module('application.projects.controllers')
        .controller('ProjectsController', function (Projects, $window) {
            var vm = this;
            vm.projects = Projects.query();

            vm.new = {};

            vm.saveProject = function () {
                var project = Projects.save(vm.new);
                $window.location = '/projects';
            };

            vm.deleteProject = function (index) {
                var projectId = vm.projects[index].id;
                vm.projects.splice(index, 1);
                Projects.delete({projectId: projectId});
            };

            vm.currentProject = null;

            vm.setCurrentProject = function (project) {
                vm.currentProject = (JSON.parse(JSON.stringify(project)))
            };

            vm.updateProject = function () {
                Projects.update({projectId: vm.currentProject.id}, vm.currentProject);
                $window.location = "/projects"
            }
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


            vm.showForm = true;

            vm.toggleForm = function () {
                vm.showForm = !vm.showForm;
            };

            vm.body = true;

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
