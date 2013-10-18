app.config(function ($routeProvider) {
    $routeProvider
        .when('/home',
            {
                controller: 'HomeController',
                templateUrl: '/accounts/home'
            })
        .when('/signup',
            {
                controller: 'SignupController',
                templateUrl: '/accounts/sign-up'
            })
        .when('/edit',
    		{
        		controller: 'EditAccountController',
        		templateUrl: '/accounts/edit'
    		})
        .otherwise({ redirectTo: '/home' });
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
                 document.location.href = data.redirect
             }
        }).error(function (data) {
            console.log('error occurred while creating user.')
        });
    };
});

app.controller('EditAccountController', function($scope, $http) {
	
    $scope.isSaveDisabled = function () {
        return $scope.signUpForm.$invalid || $scope.user.password != $scope.user.confirmPassword;
    };
	
	$http.get('/accounts/info')
		.success(function(data) {
			$scope.user = data[0];
			$scope.user.password="";
		});
	
	$scope.updateUser = function() {
		delete $scope.user.confirmPassword;
		
        $http({
            url: $scope.user.resource_uri,
            method: 'PUT',
            data: $scope.user,
            headers: { 'content-type': 'application/json' }
        })
        .success(function (data) {
        	document.location.href = '/landing';
        })
        .error(function (data) {
            console.log('error.');
        });
	};
});
