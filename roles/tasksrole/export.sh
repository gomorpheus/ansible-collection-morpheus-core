#!/usr/bin/env bash

morpheus tasks get "$TASKID" --json |
jq -r '.task | "- name: "+ .name, "  code: "+.code,"  resultType: "+.resultType, "  executeTarget: "+.executeTarget,"  taskType:\n    code: "+.taskType.code, "  file:\n    sourceType: "+.file.sourceType, "    content: |\n      "+.file.content'

echo -------------------
echo -------------------

morpheus tasks get "$TASKID" --json |
jq -r '.task | "- name: "+ .name, "  code: "+.code,"  resultType: "+.resultType, "  executeTarget: "+.executeTarget,"  taskType:\n    code: "+.taskType.code, "  file:\n    sourceType: "+.file.sourceType, "    content: |\n      "+.taskOptions.script'