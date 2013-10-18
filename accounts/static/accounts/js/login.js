app.controller('LoginController', function ($scope, $http, $location) {

    $scope.login = function () {
        $http({
            url: '/login',
            method: 'POST',
            data: $scope.user,
            headers: { 'content-type': 'application/json' }
        }).success(function (data) {
            if (data.message == 'success') {
                document.location.href = '../../Index.htm';
            }
            else {
                $scope.incorrectCredentials = true;
            }
        }).error(function (data) {
            $scope.incorrectCredentials = true;
        });
    };
});