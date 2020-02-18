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

function testSeveralEntries(){
    ts1 = 1537131015
    ts2 = 1537131014.49
    jd1 = new Date(ts1 * 1000)
    jd2 = new Date(ts2 * 1000)
    var result = chart.chartData([{timestamp: ts1, value: 26},{timestamp: ts2, value: 25.67}]);
    assert(result.label == ('Temperature ' + jd1)); 
    assert(result.labels.length == 2);
    assert(result.labels[0] == jd1.getHours() + ':50:14'); 
    assert(result.labels[1] == jd2.getHours() + ':50:15'); 
    assert(result.values.length == 2); 
    assert(result.values[0] == 25.67); 
    assert(result.values[1] == 26); 
}

function testSomeDataMissing(){
    ts1 = 1537131015
    ts2 = 1537131014.49
    jd1 = new Date(ts1 * 1000)
    var result = chart.chartData([{timestamp: ts1, value: null},{timestamp: ts2, value: 25.67}]);
    assert(result.label == 'Temperature ' + jd1 + ' (some data is missing)'); 
    assert(result.labels.length == 1); 
    assert(result.labels[0] == jd1.getHours() + ':50:14'); 
    assert(result.values.length == 1); 
    assert(result.values[0] == 25.67); 
}

testEmpty();
testSeveralEntries();
testSomeDataMissing();