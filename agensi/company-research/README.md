# Company Research skill

Ask your AI agent what a company's website is built with and get a screenshot of any page. Detects CMS, ecommerce platform, analytics and marketing tags, frameworks, CDN, hosting and payment providers (7,600+ fingerprints), captures pages as PNG, JPEG, WebP or PDF on desktop or mobile, looks up domain WHOIS / RDAP (age, registrar, expiry, DNS, e-mail provider, SPF / DMARC) and runs an SEO audit with a 0-100 score, broken links and fix hints for every page.

Example prompts:
- "What is allbirds.com built with? Which analytics and marketing tools do they use?"
- "Which of these 30 prospect sites run on Shopify or WooCommerce?"
- "How old are these 50 competitor domains, when do they expire and which e-mail provider do they use?"
- "Run an SEO audit of the first 50 pages of our site and list the broken links and the top 5 fixes."
- "Take a mobile screenshot of stripe.com/pricing and compare it with ramp.com/pricing."

## Setup (about 3 minutes)
1. Put this folder in your agent's skills directory (Claude Code: `~/.claude/skills/company-research/`).
2. Create a free Apify account: https://console.apify.com/sign-up
3. Connect the MCP server:
   - URL: `https://mcp.apify.com/?tools=Kadi_Bence/tech-stack-detector,Kadi_Bence/website-screenshot,Kadi_Bence/domain-whois-lookup,Kadi_Bence/seo-site-audit`
   - Transport: Streamable HTTP; auth via OAuth or `Authorization: Bearer <Apify API token>`
   - Claude Code: `claude mcp add --transport http company-research "<URL>"`, then `/mcp` > Authenticate.
4. Ask a question.

## Also listed
Official MCP Registry: `io.github.kiskecske24/company-research` (also Smithery and Glama).

## Costs
The tools run on your Apify account and bill per website analysed, screenshot, domain looked up or page audited (fractions of a cent each; failed sites are not charged), so checking one company costs well under one cent. Apify's free plan includes monthly credit.

## Privacy
Only public web pages and official registry data. No personal data is collected; robots.txt is respected for screenshots and SEO crawls.

## Custom versions
Need bulk stack checks for a lead list, a weekly competitor screenshot feed or a Google Sheet export? Email bence.kadi@gmail.com or see https://apify.com/kadi_bence
