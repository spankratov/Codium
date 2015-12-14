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

            Jobs.query(function (response) {
                vm.allJobs = JSON.parse(angular.toJson(response));
                CharacterJobs.query({characterId: $routeParams.characterId}, function (response) {
                    vm.jobs = JSON.parse(angular.toJson(response));
                    vm.availableJobs = [];

                    for (var i in vm.allJobs) {
                        var found = false;
                        for (var j in vm.jobs) {
                            if (vm.allJobs[i].id == vm.jobs[j].id) {
                                found = true;
                                break;
                            }
                        }
                        if (!found) {
                            vm.availableJobs.push(vm.allJobs[i]);
                        }
                    }
                });
            });


            vm.showForm = false;

            vm.toggleForm = function () {
                vm.showForm = !vm.showForm;
            };

            vm.body = true;

            vm.update = function (index) {

                var copy = angular.copy(vm.jobs[index]);

                CharacterJobs.update({
                    characterId: $routeParams.characterId, jobId: vm.jobs[index].id
                }, {
                    finished: copy.finished,
                    taking_date: copy.taking_date
                }, function (response) {

                    vm.jobs[index].isRequestSent = true;
                    var result = JSON.parse(angular.toJson(response));
                    if (response.$status >= 500) {
                        vm.jobs[index].status = false;
                        vm.jobs[index].message = "Server Error";
                    } else if (response.$status >= 400) {
                        vm.jobs[index].status = false;
                        vm.jobs[index].errors = result;
                        vm.jobs[index].message = "Job was NOT updated.";
                    } else if (response.$status >= 200) {
                        vm.jobs[index].status = true;
                        vm.jobs[index].message = "Job was updated.";
                        delete vm.jobs[index].errors;
                    }
                });
            };

            vm.resetJob = function (index) {
                CharacterJobs.get({
                    characterId: $routeParams.characterId, jobId: vm.jobs[index].id
                }, function (response) {
                    vm.jobs[index] = JSON.parse(angular.toJson(response));
                })
            };

            vm.newJob = {};
            vm.resetNewJob = function () {
                vm.newJob = {};
            };

            vm.deleteAvailableJob = function (id) {
                for (var i = 0; i < vm.availableJobs.length; i++) {
                    if (vm.availableJobs[i].id == id) {
                        vm.availableJobs.splice(i, 1);
                        break;
                    }
                }
            };

            vm.addAvailableJob = function (id) {
                for (var i = 0; i < vm.allJobs.length; i++) {
                    if (vm.allJobs[i].id == id) {
                        vm.availableJobs.push(vm.allJobs[i]);
                        break;
                    }
                }
            };

            vm.add = function () {
                CharacterJobs.save({characterId: $routeParams.characterId}, vm.newJob, function (response) {
                    if (vm.newJob.isRequestSent) {
                        vm.resetNewJob();
                    }
                    vm.newJob.isRequestSent = true;
                    var result = JSON.parse(angular.toJson(response));
                    if (response.$status >= 500) {
                        vm.newJob.status = false;
                        vm.newJob.message = "Server Error";
                    } else if (response.$status >= 400) {
                        vm.newJob.status = false;
                        vm.newJob.message = "New Job was NOT added.";
                        vm.newJob.errors = result;
                    } else if (response.$status >= 200) {
                        vm.deleteAvailableJob(result.id);
                        vm.jobs.push(result);
                        vm.newJob.status = true;
                        vm.newJob.message = "New Job was added.";
                    }
                })
            };

            vm.delete = function (index) {
                var id = vm.jobs[index].id;
                vm.addAvailableJob(id);
                vm.jobs.splice(index, 1);
                CharacterJobs.delete({characterId: $routeParams.characterId, jobId: id});
            };
        });

})();
