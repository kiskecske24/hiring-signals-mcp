@echo off
rem Publishes server.json to the official MCP Registry (registry.modelcontextprotocol.io).
rem Run AFTER this folder is pushed to https://github.com/kiskecske24/hiring-signals-mcp
cd /d "%~dp0.."
if not exist registrymcp-publisher.exe (
  curl -L -o registrymcp-publisher.tar.gz https://github.com/modelcontextprotocol/registry/releases/download/v1.8.1/mcp-publisher_windows_amd64.tar.gz || goto :err
  tar -xzf registrymcp-publisher.tar.gz -C registry mcp-publisher.exe || goto :err
  del registrymcp-publisher.tar.gz
)
echo.
echo Step 1/2: log in with GitHub (account kiskecske24). Follow the code shown below.
registrymcp-publisher.exe login github || goto :err
echo.
echo Step 2/2: publish server.json
registrymcp-publisher.exe publish || goto :err
echo.
echo Done. Check: https://registry.modelcontextprotocol.io/v0/servers?search=io.github.kiskecske24/hiring-signals
pause
exit /b 0
:err
echo FAILED - copy the error above to Claude.
pause
exit /b 1
