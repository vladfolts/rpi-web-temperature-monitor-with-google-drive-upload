module.paths.push('..')

var chart = require('chart.js')

function assert(cond){
    if (!cond)
        throw new Error('assertion failed');
}

function testEmpty(){
    var result = chart.chartData([]);
    assert(result.label == 'Temperature'); 
    assert(result.labels.length == 0); 
    assert(result.values.length == 0); 
}

function normLabel(label){
    return label.replace("Central Daylight Time", "CDT")
}

function testSeveralEntries(){
    var result = chart.chartData([{timestamp: 1537131015, value: 26},{timestamp: 1537131014.49, value: 25.67}]);
    label = normLabel(result.label);
    assert(label == 'Temperature Sun Sep 16 2018 15:50:15 GMT-0500 (CDT)'); 
    assert(result.labels.length == 2);
    assert(result.labels[0] == '15:50:14'); 
    assert(result.labels[1] == '15:50:15'); 
    assert(result.values.length == 2); 
    assert(result.values[0] == 25.67); 
    assert(result.values[1] == 26); 
}

function testSomeDataMissing(){
    var result = chart.chartData([{timestamp: 1537131015, value: null},{timestamp: 1537131014.49, value: 25.67}]);
    label = normLabel(result.label);
    assert(label == 'Temperature Sun Sep 16 2018 15:50:15 GMT-0500 (CDT) (some data is missing)'); 
    assert(result.labels.length == 1); 
    assert(result.labels[0] == '15:50:14'); 
    assert(result.values.length == 1); 
    assert(result.values[0] == 25.67); 
}

testEmpty();
testSeveralEntries();
testSomeDataMissing();