(function () {
    'use strict';

    angular.module('application.knowledges.controllers')
        .controller('KnowledgesController', function (Knowledges, $window) {
            var vm = this;
            vm.knowledges = Knowledges.query();

            vm.new = {};

            vm.saveKnowledge = function () {
                var knowledge = Knowledges.save(vm.new);
                $window.location = '/knowledges';
            };

            vm.deleteKnowledge = function (index) {
                var knowledgeId = vm.knowledges[index].id;
                vm.knowledges.splice(index, 1);
                Knowledges.delete({knowledgeId: knowledgeId});
            };

            vm.currentKnowledge = null;

            vm.setCurrentKnowledge = function (knowledge) {
                vm.currentKnowledge = (JSON.parse(JSON.stringify(knowledge)))
            };

            vm.updateKnowledge = function () {
                Knowledges.update({knowledgeId: vm.currentKnowledge.id}, vm.currentKnowledge);
                $window.location = "/knowledges"
            }
        });

    angular.module('application.knowledges.controllers')
        .controller('CharacterKnowledgesController', function (CharacterKnowledges, Knowledges, $window, $scope, $routeParams) {

            var vm = this;

            Knowledges.query(function (response) {
                vm.allKnowledges = JSON.parse(angular.toJson(response));
            });


            CharacterKnowledges.query({characterId: $routeParams.characterId}, function (response) {
                vm.knowledges = JSON.parse(angular.toJson(response));
                for (var i in vm.knowledges) {
                    vm.addExtrFields(i);
                }
            });

            vm.addExtrFields = function (i) {
                vm.knowledges[i].extParents = [];
                vm.knowledges[i].extChildren = [];
                for (var j in vm.allKnowledges) {

                    for (var k in vm.knowledges[i].parents) {
                        if (vm.knowledges[i].parents[k] == vm.allKnowledges[j].id) {
                            vm.knowledges[i].extParents.push(vm.allKnowledges[j]);
                        }
                    }
                    for (var k in vm.knowledges[i].children) {
                        if (vm.knowledges[i].children[k] == vm.allKnowledges[j].id) {
                            vm.knowledges[i].extChildren.push(vm.allKnowledges[j]);
                        }
                    }
                }
            };

            vm.body = true;

            vm.update = function (index) {

                var copy = angular.copy(vm.knowledges[index]);

                var newParents = [];
                var newChildren = [];

                for (var i in copy.extChildren) {
                    newChildren.push(copy.extChildren[i])
                }
                for (var i in copy.extParents) {
                    newParents.push(copy.extParents[i])
                }

                CharacterKnowledges.update({
                    characterId: $routeParams.characterId, knowledgeId: vm.knowledges[index].id
                }, {
                    level: copy.level
                }, function (response) {

                    vm.knowledges[index].isRequestSent = true;
                    var result = JSON.parse(angular.toJson(response));
                    if (response.$status >= 500) {
                        vm.knowledges[index].status = false;
                        vm.knowledges[index].message = "Server Error";
                    } else if (response.$status >= 400) {
                        vm.knowledges[index].status = false;
                        vm.knowledges[index].errors = result;
                        vm.knowledges[index].message = "Knowledge was NOT updated.";
                    } else if (response.$status >= 200) {
                        vm.knowledges[index].status = true;
                        vm.knowledges[index].message = "Knowledge was updated.";
                        delete vm.knowledges[index].errors;
                    }
                });
            };

            vm.resetKnowledge = function (index) {
                CharacterKnowledges.get({
                    characterId: $routeParams.characterId, knowledgeId: vm.knowledges[index].id
                }, function (response) {
                    vm.knowledges[index] = JSON.parse(angular.toJson(response));
                    vm.addExtrFields(index);
                })
            };


        })

})
();
