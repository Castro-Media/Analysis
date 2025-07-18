---
layout: default
title: Latest Headlines
date: 2025-06-05
category: analysis
folder: headlines
description: All the current headlines from all the rss feeds we are monitoring, sorted by pubdate, deduplicated.
columns:
  - pubdate
  - source
  - title
  - link
dependencies:
  - data/news
---

## Latest Headlines

All the current headlines from all the rss feeds we are monitoring, sorted by pubdate, deduplicated.

<div id="headline-table"></div>
<script>
document.addEventListener('DOMContentLoaded', function(){
  HeadlinesLister($('#headline-table'));
});
</script>

## File Versions:
{% assign csv_files = site.static_files | where:"extname", ".csv" | where_exp:"f","f.path contains 'analysis/headlines/'" | sort: 'name' | reverse %}
<ol>
  <li><a href="./latest.csv">Latest version</a></li>
  {% for file in csv_files %}
    {% unless file.name == 'latest.csv' %}
  <li><a href="./{{ file.name }}">{{ file.name }}</a></li>
    {% endunless %}
  {% endfor %}
</ol>
