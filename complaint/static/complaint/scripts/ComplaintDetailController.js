app.controller('ControlDetailController', function($scope, $http, $modal) {

	$scope.can_followed = true;
	$scope.can_upvote = true;
	
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
			window.refresh();			
		})
		.error(function(data) {
			
		});
	}
	
	$scope.upvote = function () {
		$http.get('/complaint/upvote/' + complaint_id + '/').success(
			function(data) {
				$scope.complaint.upvotes += 1;
				});
	}
	
	$scope.follow_complaint = function(){
		$http({
			url : "/api/v1/following/",
			method : 'POST',
			data : {
				date_followed : new Date(),
				complaint : $scope.complaint.resource_uri,
				user:$scope.current_user.resource_uri
			},
			headers : {
				'content-type' : 'application/json'
			}
		}).success(function(data){
			$scope.can_followed = false;
			$scope.can_upvote = false;
		})
	}
	

	$scope.update_complaint_status = function () {
		$http({
			url : "/api/v1/complaint/" + $scope.complaint.id,
			method : 'put',
			data : $scope.complaint,
			headers : {
				'content-type' : 'application/json'
			}
		})
		.success(function(data) {
			console.log(data);
		})
		.error(function(err){
			console.log(err);
		});
	}

	window.fbAsyncInit = function () {
		FB.init({ appId: '659521847413677', //change the appId to your appId
		status: true, 
		cookie: true,
		xfbml: true,
		oauth: true});
	}
	
	$scope.postInFacebook = function () {
		FB.login(function(response) {
			if (response.authResponse) {
				FB.api('/me', function(info) {
					console.log(response);
					console.log(info);
					
					showStream()
				});	   
			}
		})
		
		function showStream(){
			FB.api('/me', function(response) {
				//console.log(response.id);
				streamPublish($scope.complaint.title, $scope.complaint.information, 'hrefTitle', 'http://www.globalscholar.com/', "Post your complaints here.");
			});
		}
		
		function streamPublish(name, description, hrefTitle, hrefLink, userPrompt){
			FB.ui(
			{
				method: 'stream.publish',
				message: '',
				attachment: {
					name: name,
					caption: '',
					description: (description),
					href: hrefLink
				},
				action_links: [
					{ text: hrefTitle, href: hrefLink }
				],
				user_prompt_message: userPrompt
			},
			function(response) {
			});

		}		
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
					$scope.can_followed = $scope.can_upvote = $scope.can_followed && !$scope.is_complained_me;
					 
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