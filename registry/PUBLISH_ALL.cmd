@echo off
rem Publishes all 6 MCP servers (updated 2026-11-11) to the official MCP Registry. Double-click to run.
rem Uses your GitHub CLI login (account kiskecske24). Nothing is printed except results.
cd /d "%~dp0.."
for /f "delims=" %%t in ('gh auth token') do set GHT=%%t
registry\mcp-publisher.exe login github --token %GHT% || goto :err
set GHT=
for %%d in (. servers\job-market-data servers\public-tenders servers\company-research servers\startup-funding-leads servers\ai-search-visibility) do (
  echo.
  echo == %%d
  pushd %%d
  "%~dp0mcp-publisher.exe" publish
  popd
)
echo.
echo Done. Check: https://registry.modelcontextprotocol.io/v0/servers?search=io.github.kiskecske24
pause
exit /b 0
:err
echo FAILED - copy the error above to Claude.
pause
exit /b 1
