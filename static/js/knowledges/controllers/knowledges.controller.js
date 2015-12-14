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

            vm.allKnowledges = Knowledges.query();


            vm.knowledges = CharacterKnowledges.query({characterId: $routeParams.characterId});

            vm.body = true;

            vm.update = function (index) {
                CharacterKnowledges.update({
                    characterId: $routeParams.characterId, knowledgeId: vm.knowledges[index].id
                }, {
                    finished: vm.knowledges[index].finished,
                    taking_date: vm.knowledges[index].taking_date
                }).$promise.then(function (response) {
                    if (response.$status == 200) {
                        vm.knowledges[index].class = "glyphicon glyphicon-ok";
                    } else {
                        vm.knowledges[index].class = "glyphicon glyphicon-remove";
                    }
                });
            };

            vm.newKnowledge = {};
            vm.add = function () {
                CharacterKnowledges.save({characterId: $routeParams.characterId}, vm.newKnowledge);
                $window.location.reload();
            };

            vm.delete = function (index) {
                var id = vm.knowledges[index].id;
                vm.knowledges.splice(index, 1);
                CharacterKnowledges.delete({characterId: $routeParams.characterId, knowledgeId: id});
            };


        })

})();
