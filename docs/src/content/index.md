---
title: Data Engineering Environment
description: Documentation for the Data Engineering Development Environment
---

# Data Engineering Environment Documentation

## Overview

This documentation covers the setup and usage of our data engineering environment, which includes:

- Dagster for orchestration
- dbt for transformations
- DuckDB for data storage
- Jupyter notebooks for exploration

## Getting Started

1. Environment Setup
2. Running Pipelines
3. Creating Transformations
4. Querying Data

## Components

### Dagster Assets

Our Dagster implementation includes assets for:
- Loading raw sales data
- Processing daily metrics
- Generating reports

### dbt Models

The dbt project includes models for:
- Daily sales aggregations
- Product analytics
- Revenue metrics

### Data Storage

We use DuckDB as our local data warehouse, with tables for:
- Raw sales data
- Processed metrics
- Aggregated reports 