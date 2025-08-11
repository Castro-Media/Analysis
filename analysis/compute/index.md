---
layout: default
title: Compute
description: Catalogues estimated int8 compute accessible to different actors.
---

# Compute

This project catalogues estimated int8 compute accessible to different actors. You will notice that OpenAI is absent; they don't own any hardware, they rent it from Microsoft. This is a list of people/groups who own and control decisions about how ai compute is used.

The chart compares relative compute power of different classes of entities, versus stakeholder counts:

- [Amazon](./entities/amazon.md)
- [Apple](./entities/apple.md)
- [California State University](./entities/california-state-university.md)
- [Elon Musk](./entities/elon-musk.md)
- [iPhone 16](./entities/iphone-16.md)
- [Meta](./entities/meta.md)
- [Microsoft](./entities/microsoft.md)
- [United States Federal Government](./entities/united-states-federal-government.md)
- [University of California](./entities/university-of-california.md)

<a href="chart.svg"><img src="chart.svg" alt="Comparison of relative compute power of different classes of entities, versus stakeholder counts." style="width: 100%; height: 100%;"></a>

<div id="data-table"></div>

<script>
$(document).ready(function () {
    loadCsv();
});

function loadCsv() {
    $.get('data.csv', function (text) {
        renderTable(text);
    });
}

function renderTable(text) {
    const rows = text.trim().split('\n');
    const headers = rows[0].split(',');
    const table = $('<table id="mmlu-table" class="tablesorter"></table>');
    const thead = $('<thead></thead>');
    const tbody = $('<tbody></tbody>');
    const headerRow = $('<tr></tr>');

    headers.forEach(function (header) {
        headerRow.append($('<th></th>').text(header));
    });
    
    thead.append(headerRow);
    table.append(thead);

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].split(',');
        const row = $('<tr></tr>');

        cells.forEach(function (cell) {
            row.append($('<td></td>').text(cell));
        });

        tbody.append(row);
    }

    table.append(tbody);
    $('#data-table').empty().append(table);
    $('#mmlu-table').tablesorter();
    $('#mmlu-table').addClass('tablesorter');
    $('#mmlu-table').addClass('tablesorter-ice');
}
</script>