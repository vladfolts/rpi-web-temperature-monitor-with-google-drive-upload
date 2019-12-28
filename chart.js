function dtFromSecs(secs){
    return new Date(secs * 1000);
}

function secsToLabel(secs){
    t = dtFromSecs(secs);
    return t.getHours() + ':' + t.getMinutes() + ':' + t.getSeconds();
}

function chartData(response){
    var labels = [];
    var values = [];
    var missed_timestamps = [];
    for(var i = 0; i < response.length; ++i){
        var item = response[i];
        var v = item.value;
        var t = item.timestamp;
        if (v == null)
            missed_timestamps.push(t);
        else {
            values.unshift(v);
            labels.unshift(secsToLabel(t));
        }
    }

    var label = 'Temperature';
    if (response.length)
        label += ' ' + dtFromSecs(response[0].timestamp);
    if (missed_timestamps.length)
        label += ' (some data is missing)';
    
    return {label: label, labels: labels, values: values};
}

if (typeof exports != 'undefined')
    exports.chartData = chartData;