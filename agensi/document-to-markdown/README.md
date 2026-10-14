# Document to Markdown skill

Give your AI agent a link to a PDF, Word file, slide deck, spreadsheet or scanned document and it gets clean Markdown back: headings, lists and tables kept, page markers for citations, optional chunks for a knowledge base, and OCR for scanned pages.

Example prompts:
- "Summarise this 80-page annual report and cite page numbers: <PDF link>"
- "Turn these 12 slide decks into Markdown and list the pricing tables in each."
- "Convert this scanned German contract to text and translate the termination clause."

## Setup (about 3 minutes)
1. Put this folder in your agent's skills directory (Claude Code: `~/.claude/skills/document-to-markdown/`).
2. Create a free Apify account: https://console.apify.com/sign-up
3. Connect the MCP server:
   - URL: `https://mcp.apify.com/?tools=Kadi_Bence/document-to-markdown`
   - Transport: Streamable HTTP; auth via OAuth or `Authorization: Bearer <Apify API token>`
   - Claude Code: `claude mcp add --transport http document-to-markdown "<URL>"`, then `/mcp` > Authenticate.
4. Ask a question.

## Formats
PDF (text and scanned), DOCX, PPTX, XLSX / XLS, CSV, HTML, EPUB, ODT / ODS / ODP, RTF, and images (Tesseract OCR, many languages).

## Costs
The tool runs on your Apify account and bills per document (per started 20 pages) and per OCR page, fractions of a cent each, so a normal report costs well under one cent. Files that are too large or fail are not charged. Apify's free plan includes monthly credit.

## Privacy
Files are downloaded and converted inside your own Apify account; nothing is shared with third parties. Passwords for encrypted PDFs are stored as secrets.

## Custom versions
Need a bulk conversion pipeline, a different output format or a Google Drive integration? Email bence.kadi@gmail.com or see https://apify.com/kadi_bence
