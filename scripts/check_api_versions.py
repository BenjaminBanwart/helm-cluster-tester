#!/usr/bin/env python3
from kubernetes import client, config
import sys

def check_api_versions(apis_to_test=None):
    if apis_to_test is None:
        apis_to_test = ["monitoring.coreos.com/v1", "apps/v1"]  # Default APIs

    try:
        # Load kubeconfig
        config.load_kube_config()
        api_client = client.ApiClient()

        # Get all API versions
        api_resources = api_client.call_api('/apis', 'GET', _preload_content=False)
        api_data = api_resources[0].data.decode('utf-8')

        # Check each API
        for api in apis_to_test:
            if api in api_data:
                print(f"{api}: AVAILABLE")
            else:
                print(f"{api}: NOT AVAILABLE")
    except Exception as e:
        print(f"Error connecting to cluster: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Accept optional command-line arguments for APIs to test
    apis = sys.argv[1:] if len(sys.argv) > 1 else None
    check_api_versions(apis)