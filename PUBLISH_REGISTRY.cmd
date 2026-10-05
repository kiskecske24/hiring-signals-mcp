@echo off
rem Publishes server.json to the official MCP Registry (registry.modelcontextprotocol.io).
rem Run AFTER this folder is pushed to https://github.com/kiskecske24/hiring-signals-mcp
cd /d "%~dp0"
if not exist mcp-publisher.exe (
  curl -L -o mcp-publisher.tar.gz https://github.com/modelcontextprotocol/registry/releases/download/v1.8.1/mcp-publisher_windows_amd64.tar.gz || goto :err
  tar -xzf mcp-publisher.tar.gz mcp-publisher.exe || goto :err
  del mcp-publisher.tar.gz
)
echo.
echo Step 1/2: log in with GitHub (account kiskecske24). Follow the code shown below.
mcp-publisher.exe login github || goto :err
echo.
echo Step 2/2: publish server.json
mcp-publisher.exe publish || goto :err
echo.
echo Done. Check: https://registry.modelcontextprotocol.io/v0/servers?search=io.github.kiskecske24/hiring-signals
pause
exit /b 0
:err
echo FAILED - copy the error above to Claude.
pause
exit /b 1
