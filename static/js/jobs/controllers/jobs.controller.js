(function () {
    'use strict';

    angular.module('application.jobs.controllers')
        .controller('JobsController', function (Jobs, $window) {
            var vm = this;
            vm.jobs = Jobs.query();

            vm.new = {};

            vm.saveJob = function () {
                var job = Jobs.save(vm.new);
                $window.location = '/jobs';
            };

            vm.deleteJob = function (index) {
                var jobId = vm.jobs[index].id;
                vm.jobs.splice(index, 1);
                Jobs.delete({jobId: jobId});
            };

            vm.currentJob = null;

            vm.setCurrentJob = function (job) {
                vm.currentJob = (JSON.parse(JSON.stringify(job)))
            };

            vm.updateJob = function () {
                Jobs.update({jobId: vm.currentJob.id}, vm.currentJob);
                $window.location = "/jobs"
            }
        });

    angular.module('application.jobs.controllers')
        .controller('CharacterJobsController', function (CharacterJobs, Jobs, $window, $scope, $routeParams) {

            var vm = this;

            vm.allJobs = Jobs.query();


            vm.jobs = CharacterJobs.query({characterId: $routeParams.characterId});

            vm.body = true;

            vm.update = function (index) {
                CharacterJobs.update({
                    characterId: $routeParams.characterId, jobId: vm.jobs[index].id
                }, {
                    finished: vm.jobs[index].finished,
                    taking_date: vm.jobs[index].taking_date
                }).$promise.then(function (response) {
                    if (response.$status == 200) {
                        vm.jobs[index].class = "glyphicon glyphicon-ok";
                    } else {
                        vm.jobs[index].class = "glyphicon glyphicon-remove";
                    }
                });
            };

            vm.newJob = {};
            vm.add = function () {
                CharacterJobs.save({characterId: $routeParams.characterId}, vm.newJob);
                $window.location.reload();
            };

            vm.delete = function (index) {
                var id = vm.jobs[index].id;
                vm.jobs.splice(index, 1);
                CharacterJobs.delete({characterId: $routeParams.characterId, jobId: id});
            };


        })

})();
