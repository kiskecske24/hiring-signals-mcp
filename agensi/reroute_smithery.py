"""Points every agensi skill at its Smithery-hosted gateway (traffic shows up in Smithery Observability)."""
import re

SLUGS = ["hiring-signals", "company-research", "public-tenders", "job-market-data"]

for slug in SLUGS:
    gw = f"https://{slug}--bence-kadi.run.tools"
    page = f"https://smithery.ai/servers/bence-kadi/{slug}"

    path = f"{slug}/SKILL.md"
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"it takes about 3 minutes and needs a free Apify account, apify\.com\)",
               "it takes about 3 minutes: a Smithery login plus a free Apify account)", t)
    t = re.sub(r"- Server URL: `https://mcp\.apify\.com/\?tools=[^`]+`",
               f"- Server URL: `{gw}` (hosted on Smithery: {page})", t)
    t = re.sub(r"- Transport: Streamable HTTP\. Auth: OAuth \(the agent opens an Apify login\) or header `Authorization: Bearer <Apify API token>`\.",
               "- Transport: Streamable HTTP. Auth: OAuth. The agent opens a Smithery login; Smithery then asks the user to connect their free Apify account (apify.com), where the scrapers run.", t)
    open(path, "w", encoding="utf-8", newline="\n").write(t)

    path = f"{slug}/README.md"
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"   - URL: `https://mcp\.apify\.com/\?tools=[^`]+`",
               f"   - URL: `{gw}` (hosted on Smithery: {page})", t)
    t = re.sub(r"   - Transport: Streamable HTTP; auth via OAuth or `Authorization: Bearer <Apify API token>`",
               "   - Transport: Streamable HTTP; auth via OAuth (log in with Smithery, then connect your Apify account)", t)
    open(path, "w", encoding="utf-8", newline="\n").write(t)

    for p in (f"{slug}/SKILL.md", f"{slug}/README.md"):
        s = open(p, encoding="utf-8").read()
        print(p, "apify-url-left" if "mcp.apify.com" in s else "ok", s.count(gw))
