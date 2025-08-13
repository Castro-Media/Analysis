---
layout: default
title: Compute
description: Catalogues estimated int8 compute accessible to different actors.
---

# Compute

This project catalogues estimated int8 compute accessible to different actors. You will notice
that OpenAI is absent; they don't own any hardware, they rent it from Microsoft. This is a
list of people or groups who own and control decisions about how AI compute is used.

<a href="chart.svg"><img src="chart.svg" alt="Comparison of relative compute power of different classes of entities, versus counts of stakeholders." style="width: 100%; height: 100%;"></a>

## Cluster shapes

This figure outlines DBSCAN clusters for compute versus stakeholder counts. 
It looks for groups of entities with similar characteristics which are 
sufficiently separate from other groups to be considered distinct.
Learn more about the DBSCAN analytical technique [here](https://cjtrowbridge.com/ai).

<a href="cluster_shapes.svg"><img src="cluster_shapes.svg" alt="DBSCAN cluster shapes for compute versus stakeholder counts." style="width: 100%; height: 100%;"></a>

<h2>Entity List</h2>
This is the list of the data from all the entity files when the analysis was last run, along with their estimated
int8 compute capcaity and number of stakeholders. You can sort the table by clicking on the column headers.
You can edit the data in the appropriate entity file, linked below.

<div id="data-table"></div>

<div class="row">
    <div class="col-md-6">
        <div class="card mb-3">
            <div class="card-body">
                <h2 class="card-title">Entities</h2>
                <ul class="list-unstyled mb-0">
                    {% assign entity_pages = site.pages | where_exp: "page", "page.path contains 'analysis/compute/entities/'" | sort: "title" %}
                    {% for entity in entity_pages %}
                    <li><a href="{{ entity.url | relative_url }}">{{ entity.title }}</a></li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
    <div class="col-md-6">
        <div class="card mb-3">
            <div class="card-body">
                <h2 class="card-title">Files</h2>
                <ul class="list-unstyled mb-0">
                    <li><a href="{{ '/analysis/compute/' | relative_url }}">index.md</a></li>
                    {% assign compute_files = site.static_files | where_exp: 'file', "file.path contains '/analysis/compute/'" %}
                    {% for file in compute_files %}
                    {% unless file.path contains '/analysis/compute/entities/' %}
                    <li><a href="{{ file.path | relative_url }}">{{ file.name }}</a></li>
                    {% endunless %}
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
</div>

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
