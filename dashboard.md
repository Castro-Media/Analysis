---
layout: default
title: Repository Dashboard
---

## Analyses

<table id="analysis-table" class="table table-striped">
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
      <th>Last Updated</th>
      <th>Dependencies</th>
    </tr>
  </thead>
  <tbody>
{% assign pages = site.pages | where: "name", "index.md" | sort: "folder" %}
{% for p in pages %}
{% if p.path contains 'analysis/' %}
    <tr>
      <td><a href="{{ p.url }}">{{ p.title }}</a></td>
      <td>{{ p.description | default: '' }}</td>
      <td>{{ p.date | default: '' }}</td>
      <td>{% if p.dependencies %}{{ p.dependencies | join: ', ' }}{% endif %}</td>
    </tr>
{% endif %}
{% endfor %}
  </tbody>
</table>

## Data Sources

<table id="data-table" class="table table-striped">
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
      <th>Last Fetched</th>
      <th>Cadence</th>
      <th>Filetype</th>
    </tr>
  </thead>
  <tbody>
{% for p in pages %}
{% if p.path contains 'data/' %}
    <tr>
      <td><a href="{{ p.url }}">{{ p.title }}</a></td>
      <td>{{ p.description | default: '' }}</td>
      <td>{{ p.last_fetched | default: p.date | default: '' }}</td>
      <td>{{ p.cadence | default: '' }}</td>
      <td>{{ p.filetype | default: '' }}</td>
    </tr>
{% endif %}
{% endfor %}
  </tbody>
</table>

<script>
  document.addEventListener('DOMContentLoaded', function(){
    new DataTable('#analysis-table');
    new DataTable('#data-table');
  });
</script>
