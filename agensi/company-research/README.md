# Company Research skill

Ask your AI agent what a company's website is built with and get a screenshot of any page. Detects CMS, ecommerce platform, analytics and marketing tags, frameworks, CDN, hosting and payment providers (7,600+ fingerprints), and captures pages as PNG, JPEG, WebP or PDF on desktop or mobile.

Example prompts:
- "What is allbirds.com built with? Which analytics and marketing tools do they use?"
- "Which of these 30 prospect sites run on Shopify or WooCommerce?"
- "Take a mobile screenshot of stripe.com/pricing and compare it with ramp.com/pricing."

## Setup (about 3 minutes)
1. Put this folder in your agent's skills directory (Claude Code: `~/.claude/skills/company-research/`).
2. Create a free Apify account: https://console.apify.com/sign-up
3. Connect the MCP server:
   - URL: `https://mcp.apify.com/?tools=Kadi_Bence/tech-stack-detector,Kadi_Bence/website-screenshot`
   - Transport: Streamable HTTP; auth via OAuth or `Authorization: Bearer <Apify API token>`
   - Claude Code: `claude mcp add --transport http company-research "<URL>"`, then `/mcp` > Authenticate.
4. Ask a question.

## Also listed
Official MCP Registry: `io.github.kiskecske24/company-research` (also Smithery and Glama).

## Costs
The tools run on your Apify account and bill per website analysed or per screenshot (fractions of a cent each; failed sites are not charged), so checking one company costs well under one cent. Apify's free plan includes monthly credit.

## Privacy
Only public web pages. No personal data is collected; robots.txt is respected for screenshots by default.

## Custom versions
Need bulk stack checks for a lead list, a weekly competitor screenshot feed or a Google Sheet export? Email bence.kadi@gmail.com or see https://apify.com/kadi_bence
