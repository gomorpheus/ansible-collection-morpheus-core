# Morpheus Tasks

## Variables

`morpheus_url` - Morpheus URL eg. `https://morpheus.example.com`

`morpheus_token` - Morpheus Access Token

`morpheus_tasks` - Task list, examples in `defaults/main.yml`

## Export Existing Tasks

`export.sh` is included to export existing tasks from Morpheus.  

Usage: `TASKID=<task id> ./export.sh`

NOTE: Manual indenting is required for script exports.  Meant more for a rough dumping script than direct usable output.

## Task Codes
This role requires a task type code.  Below is a mapping of the current task types and codes as of Morpheus 5.3.1

```
name: "Ansible Playbook" 
code: "ansibleTask"

name: "Ansible Tower Job" 
code: "ansibleTowerTask"

name: "Chef bootstrap" 
code: "chefTask"

name: "Email" 
code: "email"

name: "Groovy Script" 
code: "groovyTask"

name: "HTTP" 
code: "httpTask"

name: "Javascript" 
code: "javascriptTask"

name: "jRuby Script" 
code: "jrubyTask"

name: "Library Script" 
code: "containerScript"

name: "Library Template" 
code: "containerTemplate"

name: "Local Shell Script" 
code: "localScript"

name: "Powershell Script" 
code: "winrmTask"

name: "Puppet Agent Install" 
code: "puppetTask"

name: "Python Script" 
code: "jythonTask"

name: "Restart" 
code: "restartTask"

name: "Shell Script" 
code: "script"

name: "SSH Script" 
code: "sshTask"

name: "vRealize Orchestrator Workflow" 
code: "vro"
```