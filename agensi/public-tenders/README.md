# Public Tenders skill

Ask your AI agent for public procurement opportunities in Europe. Searches TED (Tenders Electronic Daily, the EU's official tenders journal) by keyword, CPV code, country, region, value and deadline, and returns open calls for tenders and contract awards with buyer, value, deadline and winners.

Example prompts:
- "Find open IT services tenders in Germany and Austria with a deadline in the next 30 days."
- "Which cleaning contracts above EUR 500k were published in France this week?"
- "Who won the last 10 hospital equipment contracts in Italy, and for how much?"

## Setup (about 3 minutes)
1. Put this folder in your agent's skills directory (Claude Code: `~/.claude/skills/public-tenders/`).
2. Create a free Apify account: https://console.apify.com/sign-up
3. Connect the MCP server:
   - URL: `https://mcp.apify.com/?tools=Kadi_Bence/ted-tenders-scraper`
   - Transport: Streamable HTTP; auth via OAuth or `Authorization: Bearer <Apify API token>`
   - Claude Code: `claude mcp add --transport http public-tenders "<URL>"`, then `/mcp` > Authenticate.
4. Ask a question.

## Costs
The tool runs on your Apify account and bills per saved notice (fractions of a cent; default 20 notices per search, so a typical question costs well under one cent). Apify's free plan includes monthly credit.

## Coverage
EU and EEA countries plus Switzerland, the Western Balkans, Türkiye, Ukraine, Moldova and Georgia; notices above the EU thresholds. Not included: small national tenders, US federal (SAM.gov) and post-2020 UK tenders.

## Privacy
Only official public procurement notices from the TED open-data API. No personal data is collected.

## Custom versions
Need a daily tender alert for your CPV codes, other national portals or a Google Sheet export? Email bence.kadi@gmail.com or see https://apify.com/kadi_bence
