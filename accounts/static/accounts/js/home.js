app.controller('HomeController', function($scope, $http, $modal) {
	$scope.postComplaint = function() {
		var modalInstance = $modal.open({
			templateUrl : 'addComplaint.html',
			controller : MessageCtrl,
			resolve : {
				messageText : function() {
					return $scope.messageText;
				}
			}
		});
	}
});

var MessageCtrl = function ($scope, $modalInstance, messageText) {

    $scope.messageBody = messageText;
    
    $modalInstance.keyboard = 'static';

    $scope.ok = function () {
        $modalInstance.close();
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
};
