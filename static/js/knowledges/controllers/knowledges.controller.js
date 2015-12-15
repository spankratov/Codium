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

    angular.module('application.knowledges.controllers')
        .controller('KnowledgesController', function (Knowledges, $window) {
            var vm = this;
            Knowledges.query(function (response) {
                vm.knowledges = JSON.parse(angular.toJson(response));
            });

            vm.new = {};

            vm.saveKnowledge = function () {
                if (!vm.new.hasOwnProperty('parents')) {
                    vm.new.parents = [];
                }
                if (!vm.new.hasOwnProperty('children')) {
                    vm.new.children = [];
                }
                Knowledges.save(vm.new, function (response) {
                    vm.knowledges.push(JSON.parse(angular.toJson(response)));
                });
            };

            vm.deleteKnowledge = function (index) {
                var knowledgeId = vm.knowledges[index].id;
                vm.knowledges.splice(index, 1);
                Knowledges.delete({knowledgeId: knowledgeId});
            };

            vm.knowledge = null;

            vm.setCurrentKnowledge = function (knowledge) {
                vm.knowledge = knowledge;
            };

            vm.updateKnowledge = function () {
                if (!vm.knowledge.hasOwnProperty('parents')) {
                    vm.knowledge.parents = [];
                }
                if (!vm.knowledge.hasOwnProperty('children')) {
                    vm.knowledge.children = [];
                }
                update(vm.knowledge, Knowledges, {knowledgeId: vm.knowledge.id}, vm.knowledge);
            };

            vm.resetKnowledge = function () {
                Knowledges.get({
                    knowledgeId: vm.knowledge.id
                }, function (response) {
                    vm.knowledge = JSON.parse(angular.toJson(response));
                })
            };
        });

    angular.module('application.knowledges.controllers')
        .controller('CharacterKnowledgesController', function (CharacterKnowledges, Knowledges, $window, $scope, $routeParams) {

            var vm = this;

            Knowledges.query(function (response) {
                vm.allKnowledges = JSON.parse(angular.toJson(response));
            });


            CharacterKnowledges.query({characterId: $routeParams.characterId}, function (response) {
                vm.knowledges = JSON.parse(angular.toJson(response));
            });

            vm.body = false;

            vm.update = function (index) {

                CharacterKnowledges.update({
                    characterId: $routeParams.characterId, knowledgeId: vm.knowledges[index].id
                }, {
                    level: vm.knowledges[index].level
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
                })
            };
        })

})
();
