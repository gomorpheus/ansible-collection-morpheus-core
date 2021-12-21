#!/usr/bin/env bash

morpheus workflows get "$WFID" --json | 
jq -r '.taskSet | "  - name: "+ .name, "    description: "+ .description,"    type: "+ .type'
echo '    optionTypeNames:'
morpheus workflows get "$WFID" --json | 
jq -r '.taskSet | .optionTypes | "      - "+ .[].name'
echo '    taskNames:'
morpheus workflows get "$WFID" --json | 
jq -rc '.taskSet | .taskSetTasks[] | @base64' | while IFS='' read -r task; do
  name=$(echo "$task" | base64 --decode | jq -r '.task.name')
  phase=$(echo "$task" | base64 --decode | jq -r '.taskPhase')
  echo "      - name: $name"
  echo "        phase: $phase"
done
