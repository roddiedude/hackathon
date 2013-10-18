app.controller('HomeController', function($scope, $http, $modal) {
	$scope.postComplaint = function() {
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
