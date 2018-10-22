module.paths.push('..')

var chart = require('chart.js')

function assert(cond){
    if (!cond)
        throw new Error('assertion failed');
}

function test_empty(){
    var result = chart.chartData([]);
    assert(result.label == 'Temperature'); 
    assert(result.labels.length == 0); 
    assert(result.data.length == 0); 
}

function test_several_entries(){
    var result = chart.chartData([{timestamp: 1537131015, value: 26},{timestamp: 1537131014.49, value: 25.67}]);
    assert(result.label == 'Temperature Sun Sep 16 2018 15:50:15 GMT-0500 (Central Daylight Time)'); 
    assert(result.labels.length == 2);
    assert(result.labels[0] == '50:14'); 
    assert(result.labels[1] == '50:15'); 
    assert(result.data.length == 2); 
    assert(result.data[0] == 25.67); 
    assert(result.data[1] == 26); 
}

function test_some_data_missing(){
    var result = chart.chartData([{timestamp: 1537131015, value: null},{timestamp: 1537131014.49, value: 25.67}]);
    assert(result.label == 'Temperature Sun Sep 16 2018 15:50:15 GMT-0500 (Central Daylight Time) (some data is missing)'); 
    assert(result.labels.length == 1); 
    assert(result.labels[0] == '50:14'); 
    assert(result.data.length == 1); 
    assert(result.data[0] == 25.67); 
}

test_empty();
test_several_entries();
test_some_data_missing();