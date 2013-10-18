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