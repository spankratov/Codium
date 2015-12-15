(function () {
    'use strict';

    angular.module('application.users.controllers')
        .controller('ProfileController', function (Users, Characters, $window, $routeParams) {
            var vm = this;


            Users.get({userId: $routeParams.userId}, function (response) {
                vm.user = JSON.parse(angular.toJson(response));;
                Characters.get({characterId: vm.user.character}, function (response) {
                    vm.character = JSON.parse(angular.toJson(response));;
                });
            });

/*
            vm.userUpdate = function () {
                Users.partial_update({userId: vm.user.id}, {username: vm.user.username},
                    function (response) {
                        vm.user.isRequestSent = true;
                        var result = JSON.parse(angular.toJson(response));
                        if (response.$status >= 500) {
                            vm.user.status = false;
                            vm.user.message = "Server Error";
                        } else if (response.$status >= 400) {
                            vm.user.status = false;
                            vm.user.errors = result;
                            vm.user.message = "User was NOT updated.";
                        } else if (response.$status >= 200) {
                            vm.user.status = true;
                            vm.user.message = "User was updated.";
                            delete vm.user.errors;
                        }

                    });
            };*/

            vm.resetUser = function () {
                Users.get({userId: $routeParams.userId}, function (response) {
                    vm.user = JSON.parse(angular.toJson(response));
                })
            };

            vm.resetCharacter = function () {
                Characters.get({characterId: vm.character.id}, function (response) {
                    vm.character = JSON.parse(angular.toJson(response));
                })
            };


            vm.userDelete = function () {
                Users.delete({userId: vm.user.id});
                $window.location = '/users/';
            };

            vm.partial_update = function (obj, resource, params, data) {
                resource.partial_update(params, data,
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

            vm.update = function (obj, resource, params, data) {
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

            vm.userUpdate = function () {
                vm.partial_update(vm.user, Users, {userId: vm.user.id}, {username: vm.user.username});
            };


            vm.characterUpdate = function () {
                vm.update(vm.character, Characters, {characterId: vm.character.id}, vm.character);
                console.log(vm.character);
            };

            vm.characterDelete = function () {
                Characters.delete({characterId: vm.character.data.id});
                vm.character.data = null;
            }
        })
})();
