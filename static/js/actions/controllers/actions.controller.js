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

    angular.module('application.actions.controllers')
        .controller('ActionsController', function (Actions, $window) {
            var vm = this;
            Actions.query(function (response) {
                vm.actions = JSON.parse(angular.toJson(response));
            });

            vm.new = {};

            vm.saveAction = function () {
                Actions.save(vm.new, function (response) {
                    vm.actions.push(JSON.parse(angular.toJson(response)));
                });
            };

            vm.deleteAction = function (index) {
                var actionId = vm.actions[index].id;
                vm.actions.splice(index, 1);
                Actions.delete({actionId: actionId});
            };

            vm.action = null;

            vm.setCurrentAction = function (action) {
                vm.action = action;
            };

            vm.updateAction = function () {
                update(vm.action, Actions, {actionId: vm.action.id}, vm.action);
            };

            vm.resetAction = function () {
                Actions.get({
                    actionId: vm.action.id
                }, function (response) {
                    vm.action = JSON.parse(angular.toJson(response));
                })
            };
        })
})();
