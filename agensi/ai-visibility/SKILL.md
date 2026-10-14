---
name: ai-visibility
description: Check whether ChatGPT, Perplexity, Gemini and Claude mention and cite a brand when people ask them buying questions (AI search visibility, GEO / AEO, LLM share of voice). Use when the user asks if AI assistants recommend their product, how visible a brand is in ChatGPT answers, which competitors AI answers mention instead, which websites the AI cites as sources, wants an AI visibility score or share of voice for a list of prompts, or wants to track changes in AI answers over time.
---

# AI visibility: does ChatGPT, Perplexity, Gemini or Claude mention your brand?

The `ai-visibility` MCP server gives you one tool. It asks the AI assistants the user's prompts through their official APIs (with web search, like ChatGPT search does), then checks each answer for the brand, its position, the competitors named and the sources cited.

## If the tools are not available yet

If you cannot see the `ai-visibility-tracker` tool, the MCP server is not connected. Tell the user, briefly, how to connect it in their agent (it takes about 3 minutes and needs a free Apify account, apify.com):

- Server URL: `https://mcp.apify.com/?tools=Kadi_Bence/ai-visibility-tracker`
- Transport: Streamable HTTP. Auth: OAuth (the agent opens an Apify login) or header `Authorization: Bearer <Apify API token>`.
- Claude Code: `claude mcp add --transport http ai-visibility "<server URL>"`, then `/mcp` > ai-visibility > Authenticate.
- Cursor / VS Code / other clients: add an HTTP MCP server named `ai-visibility` with the URL above.

Then stop and wait. Do not answer the visibility question from your own knowledge: your answer is not what other assistants say to real users.

Tool names can carry a client prefix (for example `mcp__ai-visibility__kadi_bence--ai-visibility-tracker`); match on the part after the prefix.

| Tool | What it does | Input / limit |
|---|---|---|
| `kadi_bence--ai-visibility-tracker` | Asks ChatGPT (OpenAI), Perplexity, Gemini and / or Claude each prompt and analyses the answers | `prompts` and `brandName` (required); one charge per prompt x provider x run |

## Build the check

1. `prompts`: the questions a customer would type, in their words ("What are the best CRM tools for small agencies?", "Which accounting software do freelancers in Germany use?"). 5-10 prompts are a good first check. If the user gives only a brand, suggest 5 buying-intent prompts for its category and confirm them before running.
2. `brandName` plus `brandAliases` (product names, old names, abbreviations) and `brandDomains` (`["hubspot.com"]`; any subdomain counts as a citation). Set `caseSensitive: true` for brands that are common words (Notion, Box).
3. `competitors`: one per line as `Name | domain.com | Alias`, for example `"Pipedrive | pipedrive.com"`. Ask the user for 3-5 competitors if they did not name any.
4. `providers`: default `["openai"]`, which works without any API key (the AI cost is included in the price). Perplexity, Gemini and Claude need the user's own API key (`perplexityApiKey`, `geminiApiKey`, `anthropicApiKey`); OpenAI with the user's own `openaiApiKey` is cheaper per check. Never ask the user to paste a key into the chat; tell them to set it in the Actor input on Apify Console or to keep OpenAI only.
5. Optional: `country` (2-letter code for the searcher's location), `language`, `runsPerPrompt` (2-3 for a more reliable percentage, since answers vary), `webSearch` (default on; off = model knowledge only, no citations).
6. For tracking over time: `monitoring: true` and a `monitoringId` per client or market; each row then gets a `change` field (new / changed / unchanged).

## Keep runs small and cheap

Each check (one prompt, one provider, one run) is a paid event on the user's Apify account: about one cent with the user's own key and a few cents on the hosted OpenAI key (see the Actor's Store page for the current price). The number of checks is prompts x providers x `runsPerPrompt`.

- Start with OpenAI only and `runsPerPrompt: 1`. Add providers or runs only when the user asks.
- Before a run with more than about 30 checks, say how many checks it will make and ask the user to confirm.
- Set `answerMaxChars: 0` if the user does not need the answer text.

## Read the results

The tool returns a run summary: `status`, item count, the `datasetId` and the list of available fields. It does not return the rows themselves. Call `get-dataset-items` with that `datasetId`, using `limit`, `offset` and `fields`. Web-search answers take 10-60 s each; if the summary says the run is still running, call `get-actor-run` with the `runId` and `waitSecs` (max 45), then read the dataset.

One item per check: `prompt`, `provider`, `model`, `run`, `brandMentioned`, `brandPosition` (1 = first brand named), `mentionCount`, `brandCited`, `brandCitationRank`, `sentiment`, `shareOfVoice`, `mentionedBrands`, `competitors` (per competitor: mentioned, position, cited), `citedUrls`, `citedDomains`, `answer`, `change`, `error`. Useful `fields`: `prompt,provider,brandMentioned,brandPosition,brandCited,shareOfVoice,sentiment,competitors,citedDomains,error`.

## Answer the question

Summarise for the user, do not dump raw rows:

- Visibility: in how many of the answers the brand was mentioned (for example "mentioned in 4 of 10 answers, cited as a source in 2"), and its average position when mentioned.
- Per prompt: a compact table of mentioned yes / no, position and the competitors named ahead of the brand.
- Competitors: share of voice ranked, so the user sees who the AI recommends instead.
- Sources: the domains cited most often; these are the pages to get listed on or to improve.
- Note that AI answers vary between calls, so one run per prompt is a snapshot; suggest 2-3 runs or monitoring for decisions.

## Don't

- Don't invent or guess AI answers. Only report what the checks returned.
- Don't ask for or repeat API keys in the chat.
- Don't run the same prompts again in one conversation; reuse the dataset with `get-dataset-items`.
