function clean_data(data_server){
    var data = [];
        data_server.data.forEach(function(row){
            tmp = {};
            for(var i=0; i< data_server.columns.length; i++){
                tmp[data_server.columns[i]] = row[i];
            }
            data.push(tmp);
        })

    return data;
}

// Discussion groups- how many times the student participate on discussion groups (numeric:0-100)'
$.get( "/api/product", function( data_server ) {
    data = clean_data(data_server);    
    var visualization = d3plus.viz()
        .container("#viz")
        .data(data)
        .type("bar")
        .id("name")
        .x("name")
        .y("value")
        .title('Valor total importado por produto.')
        .draw()

});

