# Helm Cluster Tester

A project to test Helm chart functionality and Kubernetes cluster compatibility.

## Features
- Helm chart to test API version availability.
- Python script to programmatically check cluster APIs.

## Prerequisites
- Helm 3.x
- Python 3.x with `kubernetes` package (`pip install kubernetes`)
- A Kubernetes cluster with `kubectl` configured

## Usage
1. Install the chart:
   ```bash
   helm install test-release ./helm-chart
   ```

2. Test with Python script:
   ```bash
    ./scripts/check_api_versions.py
    # Or specify APIs:
    ./scripts/check_api_versions.py monitoring.coreos.com/v1 apps/v1
   ```