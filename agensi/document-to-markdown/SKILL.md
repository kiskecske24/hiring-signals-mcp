---
name: document-to-markdown
description: Convert documents at a URL into clean Markdown or plain text for reading, summarising, RAG and LLM use - PDF, Word (DOCX), PowerPoint (PPTX), Excel (XLSX / XLS), CSV, HTML, EPUB, OpenDocument, RTF and scanned images or PDFs (OCR). Keeps headings, lists and tables, adds page markers for citations, and can split the result into chunks. Use when the user gives a link to a PDF, report, slide deck, spreadsheet or scanned document and wants it read, summarised, quoted with page numbers, searched, turned into Markdown, or chunked for a knowledge base.
---

# Document to Markdown: PDF, Office and scanned files to clean text

The `document-to-markdown` MCP server gives you one tool. It downloads each file from its URL, converts it in the cloud and returns Markdown (or plain text) with tables, page markers and optional chunks. Scanned pages are read with OCR.

## If the tools are not available yet

If you cannot see the `document-to-markdown` tool, the MCP server is not connected. Tell the user, briefly, how to connect it in their agent (it takes about 3 minutes and needs a free Apify account, apify.com):

- Server URL: `https://mcp.apify.com/?tools=Kadi_Bence/document-to-markdown`
- Transport: Streamable HTTP. Auth: OAuth (the agent opens an Apify login) or header `Authorization: Bearer <Apify API token>`.
- Claude Code: `claude mcp add --transport http document-to-markdown "<server URL>"`, then `/mcp` > document-to-markdown > Authenticate.
- Cursor / VS Code / other clients: add an HTTP MCP server named `document-to-markdown` with the URL above.

Then stop and wait.

If the document is already a local file you can read directly, or a short HTML page you can fetch, you do not need this tool. Use it for remote PDFs and Office files, scanned documents, long files and batches.

Tool names can carry a client prefix (for example `mcp__document-to-markdown__kadi_bence--document-to-markdown`); match on the part after the prefix.

| Tool | What it does | Input / limit |
|---|---|---|
| `kadi_bence--document-to-markdown` | Converts PDF, DOCX, PPTX, XLSX / XLS, CSV, HTML, EPUB, ODT / ODS / ODP, RTF and images to Markdown or text; OCR for scanned pages | `urls` (direct file links); one charge per document per started 20 pages, plus one per OCR page. `maxPagesPerDocument` (default 200) |

## Build the input

- `urls`: direct links to the files (`https://arxiv.org/pdf/2401.18059`). A link to a viewer page (Google Drive preview, Dropbox page) is not a file; ask for the direct download link.
- `outputFormat`: `markdown` (default, best for reading and LLMs), `text`, or `both`.
- `pageRange` (`"1-5, 8, 20-"`) or `maxPagesPerDocument` to convert only what the user needs from a long file.
- `includePageMarkers` (default on) adds `<!-- Page 3 -->` before each page; keep it on when the user wants page citations.
- `chunkSize` (for example 1500) and `chunkOverlap` (default 200) when the user wants chunks for a vector database or knowledge base.
- OCR: `ocrMode: "auto"` (default) reads only pages without a text layer; `ocrLanguages` (for example `["eng", "deu"]`) must match the document's language. `ocrMode: "off"` skips scanned pages.
- `pdfPassword` for an encrypted PDF the user has the password for. Do not ask for it in chat unless the run fails with an encryption error.

## Keep runs small and cheap

Each document (per started 20 pages) and each OCR page is a paid event on the user's Apify account (fractions of a cent each; see the Actor's Store page for the current price). Files above `maxFileSizeMb` (default 50) are skipped and not charged.

- For a summary of the opening sections of a long report, use `pageRange` instead of converting the whole file.
- Before converting more than about 20 documents, or a document with several hundred scanned pages, say roughly what it will process and ask the user to confirm.

## Read the results

The tool returns a run summary: `status`, item count, the `datasetId` and the list of available fields. It does not return the rows themselves. Call `get-dataset-items` with that `datasetId`, using `limit`, `offset` and `fields`. Large files take longer; if the summary says the run is still running, call `get-actor-run` with the `runId` and `waitSecs` (max 45), then read the dataset.

One item per document: `url`, `fileName`, `format`, `title`, `pages`, `pagesConverted`, `wordCount`, `tableCount`, `ocrUsed`, `ocrPages`, `ocrConfidence`, `markdown`, `text`, `pageContents` (optional), `chunks` (optional; each with its heading path), `metadata`, `truncated`, `warnings`, `error`. First read the small fields (`url,title,pages,pagesConverted,wordCount,tableCount,ocrUsed,truncated,error`), then fetch `markdown` for one document at a time so the response stays small.

## Answer the question

- Do what the user asked with the content (summary, answer, extraction, comparison), not a dump of the Markdown. Give the full Markdown only when the user wants the converted file.
- Cite page numbers from the page markers when you quote or summarise.
- Say when a document was `truncated`, partly OCR'd (low `ocrConfidence` means the text may contain errors) or failed (`error`).

## Don't

- Don't convert documents the user is not allowed to access or share; the tool only downloads public URLs or files the user uploaded to their own Apify storage.
- Don't run the same document again in one conversation; reuse the dataset with `get-dataset-items`.
