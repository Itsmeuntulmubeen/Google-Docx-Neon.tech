# Docs: Collaborative Document Editor

A lightweight Google Docs-inspired editor built as a full stack take-home assignment for Ajaia.

**Live demo:** https://google-docs-clone-jade-eight.vercel.app/
**Repository:** https://github.com/Itsmeuntulmubeen/Google-Docx-Neon.tech

## Demo accounts

| Email | Password |
|---|---|
| alice@demo.com | demo1234 |
| bob@demo.com | demo1234 |
| carol@demo.com | demo1234 |

<!-- TODO: confirm these match your seed script. Delete this section if the app has no login. -->

### Quick sharing demo
1. Log in as **alice**, create a document, write some text.
2. Click **Share**, add `bob@demo.com` as **Viewer**.
3. Log out, log in as **bob**. The document appears under **Shared with me** and is read-only.
4. Log back in as alice and change bob's role to **Editor**. Bob can now edit.

## Features

- **Create, rename and open documents**, saved and available after refresh
- **Rich-text editing:** bold, italic, underline, headings, bulleted and numbered lists, undo/redo
- **Autosave** with a visible save status
- **File import:** upload `.txt`, `.md` or `.docx` to create a new editable document
- **Sharing:** document owner can share with another user as Viewer or Editor
- **Owned vs shared:** dashboard clearly separates "My documents" and "Shared with me"
- **Persistence:** documents and sharing data stored in PostgreSQL (Neon)

<!-- TODO: remove any line above that does not work in the live app. -->

## Supported upload types

`.txt`, `.md`, `.docx` only, max 2 MB. Other file types are rejected with an error message.

## Tech stack

- Next.js (App Router) + TypeScript
- Tailwind CSS
- TipTap rich-text editor
- PostgreSQL on Neon, accessed with Prisma
- `mammoth` (.docx import), `marked` (.md import)
- Zod for input validation
- Vitest for tests
- Deployed on Vercel

<!-- TODO: edit this list to match what you actually used. -->

## Local setup

### Prerequisites
- Node.js 18 or 20
- A PostgreSQL database (free [Neon](https://neon.tech) project works)

### Steps

```bash
git clone https://github.com/Itsmeuntulmubeen/Google-Docx-Neon.tech.git
cd Google-Docx-Neon.tech
npm install
cp .env.example .env        # Windows PowerShell: copy .env.example .env
```

Edit `.env` and set your values (see below), then:

```bash
npx prisma migrate dev      # create tables
npm run db:seed             # create demo users
npm run dev                 # http://localhost:3000
```

### Environment variables

| Variable
