var app = angular.module("app", ['ui.bootstrap', 'angularFileUpload']);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
