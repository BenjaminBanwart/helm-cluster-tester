{{/* Helper functions */}}
{{- define "cluster-tester.name" -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}