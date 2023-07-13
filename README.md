
# EnviroStream
**A Stream Reasoning Benchmark for Environmental and Climate Monitoring**

This repository contains datasets, queries and a generator for the _EnviroStream_, a benchmark for Stream Reasoning (SR) systems. SR focuses on applying inference to dynamic data streams and has applications in various domains such as IoT, Smart Cities, Emergency Management, and Healthcare.

_EnviroStream_ focuses on weather and environmental data from two European cities.

## Table of Contents
- [Datasets](#datasets)
- [Queries](#queries)
- [Scalable Datasets Generator](#scalable-datasets-generator)
- [Web Application for Continuous Online Reasoning](#web-application-for-continuous-online-reasoning)
- [Links](#links)

## Datasets
The repository includes two datasets in different formats and size:
- EnviroStream-small.csv: A CSV file containing weather data from the two European cities (3h log).
- EnviroStream-large.csv: A CSV file containing weather data from the two European cities (full log).
- EnviroData-small.json: A JSON file containing weather data from the two European cities (3h log).
- EnviroData-large.json: A JSON file containing weather data from the two European cities (full log).

You can download the datasets from the [GitHub repository](https://github.com/DeMaCS-UNICAL/EnviroStream). Additionally, real-time data visualization is available through the [EnviroStream website](https://experiments.demacs.unical.it/).

To cite the datasets, please refer to the Zenodo record:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8142369.svg)](https://doi.org/10.5281/zenodo.8142369)

## Queries
The repository provides a folder with pre-modeled queries. These queries can be used to evaluate SR systems using the _EnviroStream_ benchmark. We have used _I-DLV-sr_, a recently released SR system based on Answer Set Programming, as a baseline experiment.

The queries are modeled using the input language of _I-DLV-sr_. The readme file in the queries folder provides detailed instructions on how to execute the queries and reports the evaluation times.

## Scalable Datasets Generator
We have also included a dataset generator in the repository. This generator allows you to generate scalable datasets based on the _EnviroStream_ benchmark. You can use this tool to create larger datasets for testing and evaluating SR systems.

## Web Application for Continuous Online Reasoning
In addition to the benchmark datasets and queries, we have developed a web application that enables continuous online reasoning. This application demonstrates how SR systems can perform real-time inference on streaming data. You can access the application through the _EnviroStream_ website.

## Links
- [GitHub Repository](https://github.com/DeMaCS-UNICAL/EnviroStream)
- [EnviroStream Website](https://experiments.demacs.unical.it/)

For more details about the benchmark and the datasets, please refer to the [Zenodo dataset record](https://doi.org/10.5281/zenodo.8142369).

## Dataset Citing
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8142369.svg)](https://doi.org/10.5281/zenodo.8142369)
