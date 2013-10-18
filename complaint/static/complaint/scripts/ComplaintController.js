app.controller("ComplaintController", function($scope, $http) {

	$scope.complaint = {
		date_entered : new Date()
	};

	$http.get('/api/v1/location/?format=json')
		.success(function(data) {
			$scope.locations = data.objects;
	});
	
	$http.get('/api/v1/category/?format=json')
	.success(function(data) {
		$scope.categories = data.objects;
	});
	
	$http.get('/accounts/info')
		.success(function(data) {
			$scope.complaint.user = data[0].resource_uri;
	});
	
	$scope.postComplaint = function() {

		$http({
			url : "/api/v1/complaint/",
			method : 'POST',
			data : $scope.complaint,
			headers : {
				'content-type' : 'application/json'
			}
		})
		.success(function(data) {
			$scope.cancel();
		})
		.error(function(data) {
			
		});
	};
});

app.controller('MyComplaintsController', function($scope, $http) {
	$http.get('/complaint/').success(function(data) {
		$scope.complaints = data;

		if ($scope.complaints && $scope.complaints.length > 0)
			for (var i = 0; i < $scope.complaints.length; i++) {
				var complaint = $scope.complaints[i];
				$http.get('/complaint/' + complaint.id + '/followers')
					.success(function(followers) {
						complaint.followers = followers;
				});
				$http.get(complaint.locality)
					.success(function(locality) {
						complaint.location = locality.name;
				});
			};
	});
	
	$http.get('/complaint/localcomplaints/').success(function(data) {
		$scope.localityComplaints = data;
	});
	
	$scope.upvote = function(complaint) {
		$http.get('/complaint/upvote/'+complaint.id + '/')
		.success(function(data) {
			complaint.upvotes += 1;
		});
	};
});

