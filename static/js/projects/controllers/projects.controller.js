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
        })
})();
