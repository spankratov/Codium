(function () {
    'use strict';

    angular.module('application.universities.controllers')
        .controller('UniversitiesController', function (Universities, $window) {
            var vm = this;
            vm.universities = Universities.query();

            vm.new = {};

            vm.saveUniversity = function () {
                var university = Universities.save(vm.new);
                $window.location = '/universities';
            };

            vm.deleteUniversity = function (index) {
                var universityId = vm.universities[index].id;
                vm.universities.splice(index, 1);
                Universities.delete({universityId: universityId});
            };

            vm.currentUniversity = null;

            vm.setCurrentUniversity = function (university) {
                vm.currentUniversity = (JSON.parse(JSON.stringify(university)))
            };

            vm.updateUniversity = function () {
                Universities.update({universityId: vm.currentUniversity.id}, vm.currentUniversity);
                $window.location = "/universities"
            }
        })
})();
