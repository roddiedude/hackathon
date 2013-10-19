app.config(function($routeProvider) {
	$routeProvider.when('/home', {
		controller : 'HomeController',
		templateUrl : '/accounts/home'
	}).when('/signup', {
		controller : 'SignupController',
		templateUrl : '/accounts/sign-up'
	}).when('/edit', {
		controller : 'EditAccountController',
		templateUrl : '/accounts/edit'
	}).otherwise({
		redirectTo : '/home'
	});
});

app.controller('HomeController', function($scope) {
	$scope.myInterval = 3000;
	var slides = $scope.slides = [];

	$scope.addSlide = function() {
		var newWidth = 200 + ((slides.length + (25 * slides.length)) % 150);
		slides.push({
			image : 'static/img/Electricity-and-Power-Supply.jpg',
			text : 'Electricity and power supply'
		});
		slides.push({
			image : 'static/img/rainwaterDrain.jpg',
			text : 'Rain water drain'
		});
		slides.push({
			image : 'static/img/CrimeandSafety.jpg',
			text : 'Crime and Safety'
		});
		slides.push({
			image : 'static/img/Drinking-Water.jpg',
			text : 'Drinking water'
		});
		slides.push({
			image : 'static/img/Civil-Supplies.jpg',
			text : 'Civil Supplies'
		});
		slides.push({
			image : 'static/img/Sanitation.jpg',
			text : 'Sanitation'
		});
		slides.push({
			image : 'static/img/Sewage.jpg',
			text : 'Sewage'
		});
		slides.push({
			image : 'static/img/Traffic.jpg',
			text : 'Traffic'
		});
	};
	
	$scope.addSlide();
});

app.controller('LoginController', function($scope, $http, $location) {

	$scope.login = function() {
		$http({
			url : '/login',
			method : 'POST',
			data : $scope.user,
			headers : {
				'content-type' : 'application/json'
			}
		}).success(function(data) {
			if (data.message == 'success') {
				document.location.href = data.redirect
			} else {
				$scope.incorrectCredentials = true;
			}
		}).error(function(data) {
			$scope.incorrectCredentials = true;
		});
	};
});

app.controller('SignupController', function($scope, $http, $location) {

	$scope.isSaveDisabled = function() {
		return $scope.signUpForm.$invalid;
	};

	$scope.signup = function() {
		$http({
			url : '/signup',
			method : 'POST',
			data : $scope.user,
			headers : {
				'content-type' : 'application/json'
			}
		}).success(function(data) {
			if (data.message == 'success') {
				document.location.href = data.redirect
			}
		}).error(function(data) {
			console.log('error occurred while creating user.')
		});
	};
});

app.controller('EditAccountController', function($scope, $http) {

	$scope.isSaveDisabled = function() {
		return $scope.signUpForm.$invalid
				|| $scope.user.password != $scope.user.confirmPassword;
	};

	$http.get('/accounts/info').success(function(data) {
		$scope.user = data[0];
		$scope.user.password = "";
	});
	
	$http.get('/accounts/userInfo').success(function(data) {
		$scope.userInfo = data[0];
	});
	
	$http.get('/api/v1/location/?format=json').success(function(data) {
		$scope.locations = data.objects;
	});

	$scope.updateUser = function() {
		delete $scope.user.confirmPassword;

		$http({
			url : $scope.user.resource_uri,
			method : 'PUT',
			data : $scope.user,
			headers : {
				'content-type' : 'application/json'
			}
		}).success(function(data) {
			document.location.href = '/landing';
		}).error(function(data) {
			console.log('error.');
		});		
		
	};
	
	$scope.updateUser = function() {
		$scope.userInfo.user = $scope.user.resource_uri;
		
		$scope.userInfo.location_id = $scope.userInfo.location
		
		if ($scope.userInfo.id) {
			
			$http({
				url : $scope.userInfo.resource_uri,
				method : 'PUT',
				data : $scope.userInfo,
				headers : {
					'content-type' : 'application/json'
				}
			}).success(function(data) {
				document.location.href = '/landing';
			}).error(function(data) {
				console.log('error.');
			});
		} else {
			$http({
				url : "/api/v1/userinfo/",
				method : 'POST',
				data : $scope.userInfo,
				headers : {
					'content-type' : 'application/json'
				}
			}).success(function(data) {
				document.location.href = '/landing';
			}).error(function(data) {
				console.log('error.');
			});
		}
		
	};
});

