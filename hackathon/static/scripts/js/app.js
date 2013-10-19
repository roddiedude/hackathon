var app = angular.module("app", ['ui.bootstrap', 'ui.bootstrap.carousel']);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
