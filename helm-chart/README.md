# Cluster Tester Helm Chart

A Helm chart to test Kubernetes cluster API compatibility.

## Usage
1. Install the chart:
   ```bash
   helm install test-release ../helm-chart --namespace default
    ```
2. Check the logs of the pod:
    ```bash
    kubectl get configmap test-release-api-test -o yaml
    ```
3. Modify `values.yaml` to test additional APIs.

    ### Values
    | Key | Type | Default | Description |
    |-----|------|---------|-------------|
    | testApis | list | `["monitoring.coreos.com/v1", "apps/v1"]` | List of APIs to test. |
    | namespace | string | `default` | Namespace to run the tests in. |