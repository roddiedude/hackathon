app.controller("ComplaintController", function($scope, $http) {

	$scope.complaint = {
		date_entered : new Date()
	};

	$http.get('/api/v1/location/?format=json').success(function(data) {
		$scope.locations = data.objects;
	});

	$http.get('/api/v1/category/?format=json').success(function(data) {
		$scope.categories = data.objects;
	});

	$http.get('/accounts/info').success(function(data) {
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
		}).success(function(data) {
			$scope.cancel();
			window.refresh();
			document.location.reload(true);
		}).error(function(data) {
			
		});
	};
});

app.controller('MyComplaintsController', function($scope, $http) {
	
	$http.get('/complaint/').success(
			function(data) {
				
				$scope.complaints = data;

				if ($scope.complaints && $scope.complaints.length > 0) {
					for ( var i = 0; i < $scope.complaints.length; i++) {
											
						var complaint = $scope.complaints[i];

						$http.get(complaint.locality).success(
								function(locality) {
									complaint.location = locality.name;
								});
					}
					
					for ( var i = 0; i < $scope.complaints.length; i++) {

						var complaint = $scope.complaints[i];
						
						$http.get('/complaint/' + complaint.id + '/followers')
								.success(function(followers) {
									complaint.followers = followers;
								})
								.error(function(followers) {
									complaint.followers = [];
								});
					}
				}
			});

	$http.get('/complaint/localcomplaints/')
		.success( function(data) {
			$scope.localityComplaints = data;
		
			if (data && data.length > 0) {
				
				for ( var i = 0; i < data.length; i++) {
					
					var complaint = data[i];
					
					$http.get(complaint.locality).success(
							function(c) {
								var fn = function (locality) {
									c.location = locality.name;
								};
								return fn;
							}(complaint));
				};
				
				for ( var i = 0; i < $scope.localityComplaints.length; i++) {
					
					var complaint = $scope.localityComplaints[i];
					
					complaint.followers = [];
									
					$http.get('/complaint/' + complaint.id + '/followers').success(
							function(c) {
								var fn = function (followers) {
									c.followers = followers;
								};
								return fn;
							}(complaint));
				};
			}
	}).error(function(data) {
		$scope.localityComplaints = [];
	});	

	$scope.upvote = function(complaint) {
		$http.get('/complaint/upvote/' + complaint.id + '/').success(
				function(data) {
					complaint.upvotes += 1;
				});
	};
});

app.controller('AdminComplaintsController', function($scope, $http) {
	$http.get('/complaint/top-complaints/')
	.success(function(data) {
		
		$scope.topComplaints = data;
		if ($scope.topComplaints && $scope.topComplaints.length > 0) {
			for ( var i = 0; i < $scope.topComplaints.length; i++) {
									
				var complaint = $scope.topComplaints[i];

				$http.get(complaint.locality).success(
						function(locality) {
							complaint.location = locality.name;
						});
			}
			
			for ( var i = 0; i < $scope.topComplaints.length; i++) {

				var complaint = $scope.topComplaints[i];
				
				$http.get('/complaint/' + complaint.id + '/followers')
						.success(function(followers) {
							complaint.followers = followers;
						})
						.error(function(followers) {
							complaint.followers = [];
						});
			}
		}
	})
	.error(function(data) {
		$scope.topComplaints = [];
	});

	$http.get('/complaint/recent-complaints/')
	.success(function(data) {
		
		$scope.recentComplaints = data;
	})
	.error(function(data) {
		$scope.recentComplaints = [];
	});

	$http.get('/complaint/all-complaints/')
	.success(function(data) {
		$scope.allComplaints = data;
	})
	.error(function(data) {
		$scope.allComplaints = [];
	});
});
