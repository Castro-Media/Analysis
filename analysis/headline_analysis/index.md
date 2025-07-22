---
layout: default
title: Headline Analysis
date: 2025-07-22
category: analysis
folder: headline_analysis
description: Collects all news headlines and produces time-based summaries.
columns:
  - pubdate
  - source
  - headline
  - link
dependencies:
  - data/news
---

## Headline Analysis

This project gathers the latest headlines from every news source and organizes them by publication time.

<div id="headlines-table"></div>
<script>
document.addEventListener('DOMContentLoaded', function(){
  loadJsonTable('#headlines-table', './headlines.json');
});
</script>

## File Versions:
{% assign files = site.static_files | where_exp:'f','f.path contains "analysis/headline_analysis"' %}
<ol>
  <li><a href="./headlines.json">Latest headlines</a></li>
  {% for file in files %}
    {% unless file.name == 'headlines.json' and file.path contains '/archive/' %}
  <li><a href="./{{ file.name }}">{{ file.name }}</a></li>
    {% endunless %}
  {% endfor %}
</ol>
