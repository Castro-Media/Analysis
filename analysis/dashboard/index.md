---
layout: default
title: Data Source Dashboard
description: Reports the latest fetch time and item count for every configured news feed.
dependencies:
  - data/news
---

## News Feed Dashboard

A report of every configured RSS, XML, or publisher API feed. `item_count` is the number of entries in the feed's current `latest.json`; `latest_status` distinguishes populated, empty, missing, and unreadable outputs.

<div id="dashboard-table"></div>
<script>
function loadCsvTable(sel, csvPath){
  fetch(csvPath)
    .then(r => r.text())
    .then(text => {
      const rows = csvToObjects(text);
      const table = ArrTabler(rows);
      $(sel).html(table);
      new DataTable(sel + ' table', {
        order: [[0, 'desc']],
        columnDefs: [
          { targets: '_all', className: 'dt-head-left dt-body-left' }
        ]
      });
    })
    .catch(() => {
      $(sel).text('Unable to load data.');
    });
}

document.addEventListener('DOMContentLoaded', function(){
  loadCsvTable('#dashboard-table', './latest.csv');
});
</script>

## File Versions:
{% assign csv_files = site.static_files | where:"extname", ".csv" | where_exp:"f","f.path contains 'analysis/dashboard/'" | sort: 'name' | reverse %}
<ol>
  <li><a href="./latest.csv">Latest version</a></li>
  {% for file in csv_files %}
    {% unless file.name == 'latest.csv' %}
  <li><a href="./{{ file.name }}">{{ file.name }}</a></li>
    {% endunless %}
  {% endfor %}
</ol>
