function ArrTabler(arr){
    // Create a table element
    var table = document.createElement('table');
    //Get a list of column names from the first object
    var columns = Object.keys(arr[0]);
    // Create thead element
    var thead = document.createElement('thead');
    // Create a row for the header
    var headerRow = document.createElement('tr');
    // Create and append th elements for each column
    columns.forEach(function(column) {
        var th = document.createElement('th');
        th.textContent = column;
        headerRow.appendChild(th);
    });
    // Append the header row to thead
    thead.appendChild(headerRow);
    // Append thead to the table
    table.appendChild(thead);


    // Create tbody element
    var tbody = document.createElement('tbody');
    // Iterate over each object in the array
    arr.forEach(function(item) {
        // Create a row for each object
        var row = document.createElement('tr');
        // Create and append td elements for each property in the object
        columns.forEach(function(column) {
            var td = document.createElement('td');
            td.textContent = item[column];
            row.appendChild(td);
        });
        // Append the row to tbody
        tbody.appendChild(row);
    });
    // Append tbody to the table
    table.appendChild(tbody);

    // create tfoot element
    var tfoot = document.createElement('tfoot');
    // Create a row for the footer
    var footerRow = document.createElement('tr');
    // Create and append th elements for each column
    columns.forEach(function(column) {
        var th = document.createElement('th');
        th.textContent = column;
        footerRow.appendChild(th);
    });
    // Append the footer row to tfoot
    tfoot.appendChild(footerRow);
    // Append tfoot to the table
    table.appendChild(tfoot);

    // Set the class for the table
    table.className = 'tablesorter tablesorter-ice';

    return table;
}

function FREDTable($container){
    fetch('./latest.json')
        .then(r => r.json())
        .then(d => {
            if (d.observations){
                var arr = d.observations.map(o => ({ date: o.date, value: o.value }));
                var table = ArrTabler(arr);
                $container.append(table);
                $(table).tablesorter();
            } else {
                $container.text("This source isn't supported for tables yet.");
            }
        })
        .catch(() => {
            $container.text("This source isn't supported for tables yet.");
        });
}