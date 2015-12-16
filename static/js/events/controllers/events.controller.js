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

    angular.module('application.events.controllers')
        .controller('EventsController', function (Events, $window) {
            var vm = this;
            Events.query(function (response) {
                vm.events = JSON.parse(angular.toJson(response));
            });

            vm.new = {};

            vm.saveEvent = function () {
                Events.save(vm.new, function (response) {
                    vm.events.push(JSON.parse(angular.toJson(response)));
                });
            };

            vm.deleteEvent = function (index) {
                var eventId = vm.events[index].id;
                vm.events.splice(index, 1);
                Events.delete({eventId: eventId});
            };

            vm.event = null;

            vm.setCurrentEvent = function (event) {
                vm.event = event;
            };

            vm.updateEvent = function () {
                update(vm.event, Events, {eventId: vm.event.id}, vm.event);
            };

            vm.resetEvent = function () {
                Events.get({
                    eventId: vm.event.id
                }, function (response) {
                    vm.event = JSON.parse(angular.toJson(response));
                })
            };
        })
})();
