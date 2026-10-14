# AI Visibility skill

Ask your AI agent whether ChatGPT, Perplexity, Gemini and Claude recommend your brand. The skill sends your customers' questions to the assistants through their official APIs (with web search), then reports whether your brand is mentioned, in which position, which competitors are named instead and which websites are cited as sources.

Example prompts:
- "Does ChatGPT recommend us (acme.io) when people ask for the best project management tools for agencies? Compare with Asana, Monday and ClickUp."
- "Which websites does ChatGPT cite when people ask about the best CRM for small businesses?"
- "Run our 10 tracking prompts again and tell me what changed since last week."

## Setup (about 3 minutes)
1. Put this folder in your agent's skills directory (Claude Code: `~/.claude/skills/ai-visibility/`).
2. Create a free Apify account: https://console.apify.com/sign-up
3. Connect the MCP server:
   - URL: `https://mcp.apify.com/?tools=Kadi_Bence/ai-visibility-tracker`
   - Transport: Streamable HTTP; auth via OAuth or `Authorization: Bearer <Apify API token>`
   - Claude Code: `claude mcp add --transport http ai-visibility "<URL>"`, then `/mcp` > Authenticate.
4. Ask a question.

## Costs
The tool runs on your Apify account and bills per check (one prompt answered by one assistant). ChatGPT works without any API key, with the AI cost included (a few cents per check); with your own OpenAI, Perplexity, Gemini or Anthropic key it is about one cent per check plus the provider's own token cost. A 10-prompt ChatGPT check costs well under one dollar. Apify's free plan includes monthly credit.

## Privacy
Only your prompts and brand names are sent to the AI providers. Your own API keys are stored encrypted in your Apify account and never logged. No personal data is collected.

## Custom versions
Need a weekly AI visibility report for several clients, more assistants or a Google Sheet export? Email bence.kadi@gmail.com or see https://apify.com/kadi_bence
