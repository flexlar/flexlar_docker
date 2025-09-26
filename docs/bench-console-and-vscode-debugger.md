Add the following configuration to `launch.json` `configurations` array to start bench console and use debugger. Replace `development.localhost` with appropriate site. Also replace `flexlar-bench` with name of the bench directory.

```json
{
  "name": "Bench Console",
  "type": "python",
  "request": "launch",
  "program": "${workspaceFolder}/flexlar-bench/apps/flexlar/flexlar/utils/bench_helper.py",
  "args": ["flexlar", "--site", "development.localhost", "console"],
  "pythonPath": "${workspaceFolder}/flexlar-bench/env/bin/python",
  "cwd": "${workspaceFolder}/flexlar-bench/sites",
  "env": {
    "DEV_SERVER": "1"
  }
}
```
