/**
 * Created by Kirov on 19/11/15.
 */
(function () {
    'use strict';

    angular.module('application.actions.controllers')
        .controller('ActionsController', function (Actions) {
            var vm = this;

            vm.actions = Actions.query();

            vm.new = {};

            vm.save = function () {
                Actions.save(vm.new);
            }

        })
})();
