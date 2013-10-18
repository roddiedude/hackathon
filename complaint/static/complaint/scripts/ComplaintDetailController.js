app.controller('ControlDetailController', function($scope, $http, $modal) {

	$scope.postComplaint  = function() {
		var modalInstance = $modal.open({
			templateUrl : 'addComplaint.html',
			controller : MessageCtrl,
			resolve : {
				complaint : function() {
					return $scope.complaint;
				}
			}
		});
	}
	
	$scope.addNewComment = function() {
		var new_comment = {
				comment : $scope.complaint.new_comment,
				complaint : $scope.complaint.resource_uri,
				date_entered : new Date(),
				user : $scope.current_user.resource_uri,
				user_object : $scope.current_user
			};
		
		$http({
			url : "/api/v1/comment/",
			method : 'POST',
			data : new_comment,
			headers : {
				'content-type' : 'application/json'
			}
		})
		.success(function(data) {
			$scope.complaint.new_comment = '';
			$scope.complaint.comments.push(new_comment);
		})
		.error(function(data) {
			
		});
	}
	
	$scope.upvote = function () {
		$http.get('/complaint/upvote/' + complaint_id + '/').success(
			function(data) {
				complaint.upvotes += 1;
				});
	}
	
	$scope.back = function() {
		document.location.href = document.referrer;
	}
	
	$http.get('/accounts/info').success(
		function(data){
			$scope.current_user = {}
			$scope.current_user = data[0];			
		})
	
	$http.get('/api/v1/complaint/' + complaint_id + '/?format=json').success(
			function(data) {
				$scope.complaint = {};
				$scope.complaint = data;

				$http.get($scope.complaint.user).success(function(data) {
					$scope.complaint.user_object = data;
					
					$scope.is_complained_me = $scope.current_user.resource_uri == $scope.complaint.user;
				})
				
				$http.get($scope.complaint.category).success(function(data) {
					$scope.complaint.category_object = data;
				})
				
				$http.get($scope.complaint.locality).success(function(data){
					$scope.complaint.locality_object = data;
				})
				
				$http.get('/complaint/comments/'+ complaint_id).success(function(data){					
					$scope.complaint.comments = data;
					$scope.complaint.comments.forEach(function(comment){
						$http.get(comment.user).success(function(data) {
							comment.user_object = data;
						});												
					});
				})			
			})		
})


app.controller("ComplaintController", function($scope, $http) {
	
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
	
	$scope.updateComplaint = function() {

		$http({
			url : "/api/v1/complaint/" + $scope.complaint.id,
			method : 'put',
			data : $scope.complaint,
			headers : {
				'content-type' : 'application/json'
			}
		})
		.success(function(data) {
			$scope.cancel();
			
			$http.get($scope.complaint.category).success(function(data) {
				$scope.complaint.category_object = data;
			})
			
			$http.get($scope.complaint.locality).success(function(data){
				$scope.complaint.locality_object = data;
			})
		})
		.error(function(data) {
			
		});
	};
});

var MessageCtrl = function ($scope, $modalInstance, complaint) {

    $scope.complaint = complaint;
    
    $modalInstance.keyboard = 'static';

    $scope.ok = function () {
        $modalInstance.close();
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    }; 
};