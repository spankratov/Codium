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
        })
})();
