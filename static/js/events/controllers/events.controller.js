(function () {
    'use strict';

    angular.module('application.events.controllers')
        .controller('EventsController', function (Events, $window) {
            var vm = this;
            vm.events = Events.query();

            vm.new = {};

            vm.saveEvent = function () {
                var event = Events.save(vm.new);
                $window.location = '/events';
            };

            vm.deleteEvent = function (index) {
                var eventId = vm.events[index].id;
                vm.events.splice(index, 1);
                Events.delete({eventId: eventId});
            };

            vm.currentEvent = null;

            vm.setCurrentEvent = function (event) {
                vm.currentEvent = (JSON.parse(JSON.stringify(event)))
            };

            vm.updateEvent = function () {
                Events.update({eventId: vm.currentEvent.id}, vm.currentEvent);
                $window.location = "/events"
            }
        })
})();
