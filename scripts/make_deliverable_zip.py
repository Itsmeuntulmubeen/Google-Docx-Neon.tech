"""Build a single complete deliverable zip under download/.

Layout inside the zip (mirrors download/):
  ajaia-doc-editor/          <- repo files (no node_modules/.next/.git/.env)
  ajaia-docs-git.bundle      <- full 13-commit history for GitHub push
  screenshots/               <- proof screenshots
"""
import os
import zipfile

DOWNLOAD = "/home/z/my-project/download"
REPO = os.path.join(DOWNLOAD, "ajaia-doc-editor")
OUT = os.path.join(DOWNLOAD, "ajaia-docs-complete.zip")

EXCLUDE_DIRS = {"node_modules", ".next", ".git", ".vercel", "__pycache__"}
EXCLUDE_FILES = {".env"}

if os.path.exists(OUT):
    os.remove(OUT)

zf = zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED)
count = 0

for root, dirs, files in os.walk(REPO):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    for f in sorted(files):
        if f in EXCLUDE_FILES:
            continue
        p = os.path.join(root, f)
        arc = os.path.join("ajaia-doc-editor", os.path.relpath(p, REPO))
        zf.write(p, arc)
        count += 1

bundle = os.path.join(DOWNLOAD, "ajaia-docs-git.bundle")
zf.write(bundle, "ajaia-docs-git.bundle")

shots = os.path.join(DOWNLOAD, "screenshots")
for f in sorted(os.listdir(shots)):
    if f.endswith(".png"):
        zf.write(os.path.join(shots, f), os.path.join("screenshots", f))

zf.close()

# verify
vz = zipfile.ZipFile(OUT)
bad = vz.testzip()
names = vz.namelist()
leaks = [n for n in names if n.endswith("/.env") or n == ".env"
         or "node_modules" in n or n.startswith(".next") or n.startswith(".git/")]
print(f"written: {OUT} ({os.path.getsize(OUT)} bytes)")
print(f"repo files: {count} | total entries: {len(names)} | corrupt: {bad}")
print(f"leaks (.env/build dirs): {leaks or 'NONE'}")
for key in ["ajaia-doc-editor/README.md", "ajaia-doc-editor/package.json",
            "ajaia-doc-editor/src/middleware.ts",
            "ajaia-doc-editor/prisma/migrations/",
            "ajaia-doc-editor/.env.example", "ajaia-doc-editor/docker-compose.yml",
            "ajaia-docs-git.bundle", "screenshots/01-login.png"]:
    ok = any(n == key or n.startswith(key) for n in names)
    print(f"  {'OK ' if ok else 'MISSING'} {key}")
