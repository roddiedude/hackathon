app.controller("ComplaintController", function($scope, $http) {

	$scope.complaint = {
			date_entered : new Date()
	},
	
	$http.get('/api/v1/category/?format=json')
		.success(function(data) {
			$scope.categories = data.objects;
		})
	
	$scope.postComplaints = function(e) {
		
		$http({
            url: "/api/v1/complaint/",
            method: 'POST',
            data: $scope.complaint,
            headers: { 'content-type': 'application/json' }
        }).success(function (data) {
            if (data.message == 'success') {
                //document.location.href = data.redirect
            }
            else {
                //$scope.incorrectCredentials = true;
            }
        }).error(function (data) {
            //$scope.incorrectCredentials = true;
        });		

		console.log($scope.complaint);
	},
	

	$scope.onFileSelect = function($files) {
		// $files: an array of files selected, each file has name, size, and
		// type.
		for ( var i = 0; i < $files.length; i++) {
			var $file = $files[i];
			$http.uploadFile({
				url : 'server/upload/url', // upload.php script, node.js route,
				// or
				// servlet upload url
				// headers: {'optional', 'value'}
				data : {
					myObj : $scope.myModelObj
				},
				file : $file
			}).progress(
					function(evt) {
						console.log('percent: '
								+ parseInt(100.0 * evt.loaded / evt.total));
					}).then(function(data, status, headers, config) {
				// file is uploaded successfully
				console.log(data);
			});
		}
	}
})
