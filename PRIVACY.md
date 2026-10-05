# Privacy notice: Hiring Signals

Last updated: 2026-10-05

**What this plugin is.** A configuration that connects your AI assistant to Apify's hosted MCP server (`mcp.apify.com`), limited to two Apify Actors that read public job postings from company career sites. The plugin has no server, database, analytics or telemetry of its own, and the author receives no data from it.

**What data flows where.**
- Your questions stay between you and your AI assistant. When the assistant calls a tool, it sends the tool input (company names, URLs, filters) to Apify's MCP server, which runs the Actor on your Apify account.
- The Actors fetch public job postings from the companies' career sites and return them to your assistant. They do not collect personal data and remove e-mail addresses and phone numbers from job descriptions by default.
- Run inputs and results are stored in your own Apify account under Apify's retention rules. You can delete them in Apify Console.

**Authentication.** You sign in to Apify with OAuth, or give your MCP client your own Apify API token. The plugin does not read credentials or files from your machine.

**Third parties.** Apify (runs the Actors and the MCP server): <https://apify.com/privacy-policy>. As with any Apify Store Actor, the author sees only aggregate usage statistics (such as numbers of users and runs), not your inputs or results.

**Contact.** Open an issue at <https://github.com/kiskecske24/hiring-signals-mcp/issues>.
