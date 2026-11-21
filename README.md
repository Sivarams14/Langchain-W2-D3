# LangChain + LangSmith: Windows VS Code setup

This follows the Week 2, Day 3 assignment. All Python application code is in
`traced_app.py`. It calls ChatOpenAI three times with fictional insurance examples.
It contains no LangSmith imports, callbacks, decorators, or tracing configuration.

## 1. Open the folder

Extract the ZIP. In VS Code choose File > Open Folder and select the folder
containing `traced_app.py` and `requirements.txt`.
Install Microsoft's Python extension if needed. Open Terminal > New Terminal,
and select PowerShell. Commands below run from this project folder.

Use Python 3.11 or newer. Check your installation:

```powershell
py --version
```

If `py` is unavailable but `python --version` works, use `python -m venv venv`
instead of the next command.

## 2. Create the environment and install

```powershell
py -m venv venv
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

Activation is unnecessary: these commands explicitly use the virtual environment's
Python, so PowerShell execution policy does not block them.

Press Ctrl+Shift+P > Python: Select Interpreter > Enter interpreter path.
Choose `venv\Scripts\python.exe` inside your project.

## 3. Get your two API keys

- OpenAI: https://platform.openai.com/api-keys
- LangSmith: https://smith.langchain.com/ > Settings > API Keys.

OpenAI API billing is separate from your ChatGPT subscription. Ensure your API
project has available billing/credits. Do not paste your keys into the Python file,
GitHub, screenshots, or messages.

## 4. Set environment variables in the same PowerShell terminal

Replace both placeholders with your real keys locally:

```powershell
$env:OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
$env:LANGSMITH_API_KEY="YOUR_LANGSMITH_API_KEY"
$env:LANGSMITH_TRACING="true"
$env:LANGSMITH_PROJECT="caie-week2"
```

These settings last for this terminal session. Set them again after opening a new
terminal. Run from this terminal rather than a separate Code Runner/debug session.
A `.env` file alone is not loaded by this app.

For non-US LangSmith accounts, set `LANGSMITH_ENDPOINT` to the API endpoint shown
in your account's setup instructions. For an EU account, for example:

```powershell
$env:LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"
```

For a key associated with multiple workspaces, you may also need:

```powershell
$env:LANGSMITH_WORKSPACE_ID="YOUR_WORKSPACE_ID"
```

The assignment uses a project-based workspace. If your LangSmith account uses the
newer agent-based interface, create/select an agent and its Local environment;
copy its agent ID and set the following instead of using LANGSMITH_PROJECT:

```powershell
Remove-Item Env:LANGSMITH_PROJECT -ErrorAction SilentlyContinue
$env:LANGSMITH_AGENT_ID="YOUR_AGENT_ID"
$env:LANGSMITH_AGENT_ENVIRONMENT="local"
```

Name the agent `caie-week2` and explain the interface difference in your submission
if the course requires the older projects screen.

## 5. Check configuration without printing either key

```powershell
Write-Host "Tracing enabled:" ($env:LANGSMITH_TRACING -eq "true")
Write-Host "OpenAI key present:" (-not [string]::IsNullOrWhiteSpace($env:OPENAI_API_KEY))
Write-Host "LangSmith key present:" (-not [string]::IsNullOrWhiteSpace($env:LANGSMITH_API_KEY))
Write-Host "Project:" $env:LANGSMITH_PROJECT
```

The first three checks should print `True`. These checks only verify local
configuration; a visible completed trace confirms successful remote ingestion.

## 6. Run

```powershell
.\venv\Scripts\python.exe traced_app.py
```

Wait for Python to exit normally. You should see three prompts, answers, elapsed
times, and token counts. Actual responses and measurements vary. Terminal elapsed
time includes client overhead/retries and may differ from LangSmith latency.

## 7. Inspect LangSmith

Open https://smith.langchain.com/ and select the correct workspace and tracing
project `caie-week2`. Refresh if necessary; clear restrictive time filters.
For an agent-based account, open the agent's Local environment instead.

The app makes three independent top-level model calls. Their default run name may
be `ChatOpenAI`; open Inputs to distinguish them by prompt.

Open one run and record:

| Field | What to capture |
| --- | --- |
| Input | Exact user message/prompt sent to the model |
| Output | Model answer |
| Latency | Duration shown by LangSmith |
| Tokens | Input, output, and total tokens |
| Cost, if available | Estimated dollar cost shown by LangSmith |

The third prompt requests a longer answer, so it is expected to use more output
tokens. Compare actual cost where available: input and output tokens can have
different prices, and total tokens alone do not establish exact dollar cost.

## 8. Submit

1. Screenshot the three runs listed in the named project/destination.
2. Screenshot one opened run showing its input, output, latency, and token counts.
   Use more than one screenshot if necessary to make all fields readable.
3. Upload `traced_app.py`, `requirements.txt`, `README.md`, and `.gitignore` to
   your GitHub repository. Do not upload the virtual environment or secrets.
4. Share the GitHub link and community video as instructed by your course.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| `ModuleNotFoundError` | Install with the venv Python and run with the same executable. |
| OpenAI 401 | Check/recreate your OpenAI API key. |
| OpenAI 429 | Check the error: insufficient quota needs billing/credits; rate limiting needs a retry after the indicated delay. |
| LangSmith authentication error | Check the LangSmith key, account region endpoint, and workspace ID. |
| Answers print but no runs appear | Verify tracing in the same terminal; check workspace, project/agent, region, filters, and upload errors in terminal. An answer alone does not prove tracing worked. |
| PowerShell blocks Activate.ps1 | Use `.\venv\Scripts\python.exe` directly as shown above. |
| Model unavailable | Use a supported model you can access; update `model=` and check supported parameters for that model. |

## References

- https://docs.langchain.com/langsmith/trace-with-langchain
- https://docs.langchain.com/oss/python/integrations/chat/openai
- https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform

Prepared code was checked for Python syntax. A live API run and dashboard
verification require your own credentials and were not performed here.
