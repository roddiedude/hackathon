app.config(function ($routeProvider) {
    $routeProvider
        .when('/home',
            {
                controller: 'HomeController',
                templateUrl: '../partials/home.html'
            })
        .when('/signup',
            {
                controller: 'SignupController',
                templateUrl: '../partials/sign-up.html'
            })
        .otherwise({ redirectTo: '/signup' });
});

app.controller('HomeController', function($scope) {
	console.log('Home controller activated.');
});

app.controller('LoginController', function ($scope, $http, $location) {

    $scope.login = function () {
        $http({
            url: '/login',
            method: 'POST',
            data: $scope.user,
            headers: { 'content-type': 'application/json' }
        }).success(function (data) {
            if (data.message == 'success') {
                document.location.href = data.redirect
            }
            else {
                $scope.incorrectCredentials = true;
            }
        }).error(function (data) {
            $scope.incorrectCredentials = true;
        });
    };
});

app.controller('SignupController', function($scope, $http, $location) {
	
    $scope.isSaveDisabled = function () {
        return $scope.signUpForm.$invalid;
    };
	
    $scope.signup = function () {
        $http({
            url: '/signup',
            method: 'POST',
            data: $scope.user,
            headers: { 'content-type': 'application/json' }
        }).success(function (data) {
            if (data.message == 'success') {
                document.location.href = '/landingPage';
            }
        }).error(function (data) {
            console.log('error occurred while creating user.')
        });
    };
});


