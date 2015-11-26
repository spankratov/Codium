/**
 * Created by Kirov on 19/11/15.
 */
(function () {
	'use strict';

	angular.module('application.auth.services').
	service('Auth', function ($http, $location, $q, $window) {
		var Auth = {
			getToken: function () {
				return $window.localStorage.getItem('token');
			},

			setToken: function (token) {
				$window.localStorage.setItem('token', token);
			},

			setEmail: function (email) {
				$window.localStorage.setItem('email', email);
			},

			setUserId: function (id) {
				$window.localStorage.setItem('id', id);
			},

			getUserId: function () {
				return $window.localStorage.getItem('id');
			},

			deleteUserId: function () {
				$window.localStorage.removeItem('id');
			},


			getEmail: function () {
				return $window.localStorage.getItem('email');
			},
			deleteToken: function () {
				$window.localStorage.removeItem('token');
			},
			deleteEmail: function () {
				$window.localStorage.removeItem('email');
			},
			login: function (username, password) {
				var deferred = $q.defer();

				$http.post('/api/v1/auth/login/', {
					username: username, password: password
				}).success(function (response, status, headers, config) {
					if (response.token) {
						Auth.setToken(response.token);
						Auth.setEmail(response.email);
						Auth.setUserId(response.id);
					}
					$window.location = '/';
					deferred.resolve(response, status, headers, config);


				}).error(function (response, status, headers, config) {
					deferred.reject(response, status, headers, config);
				});

				return deferred.promise;
			},
			logout: function () {
				Auth.deleteToken();
				Auth.deleteEmail();
				Auth.deleteUserId();
				$window.location = '/';
			}
		};

		return Auth;
	});
})();
