(function () {
    'use strict';

    angular.module('application.actions.controllers')
        .controller('ActionsController', function (Actions, $window) {
            var vm = this;
            vm.actions = Actions.query();

            vm.new = {};

            vm.saveAction = function () {
                var action = Actions.save(vm.new);
                $window.location = '/actions';
            };

            vm.deleteAction = function (index) {
                var actionId = vm.actions[index].id;
                vm.actions.splice(index, 1);
                Actions.delete({actionId: actionId});
            };

            vm.currentAction = null;

            vm.setCurrentAction = function (action) {
                vm.currentAction = (JSON.parse(JSON.stringify(action)))
            };

            vm.updateAction = function () {
                Actions.update({actionId: vm.currentAction.id}, vm.currentAction);
                $window.location = "/actions"
            }
        })
})();
