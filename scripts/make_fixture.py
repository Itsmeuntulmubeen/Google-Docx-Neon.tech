#!/usr/bin/env python3
"""Generate a minimal .docx fixture for the import conversion tests.

Builds a WordprocessingML package by hand (a .docx is just a zip of XML parts),
so no Python dependencies are needed. Contents mirror what the tests assert:
a Heading 1, a Heading 2, bold/italic runs, and plain paragraphs.
"""

import zipfile

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

def p(style, runs):
    parts = []
    if style:
        parts.append(f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>')
    for text, bold, italic in runs:
        rpr = ""
        if bold or italic:
            props = ("<w:b/>" if bold else "") + ("<w:i/>" if italic else "")
            rpr = f"<w:rPr>{props}</w:rPr>"
        parts.append(f"<w:r>{rpr}<w:t xml:space=\"preserve\">{text}</w:t></w:r>")
    return f"<w:p>{''.join(parts)}</w:p>"

body = "".join(
    [
        p("Heading1", [("Project Phoenix", False, False)]),
        p(None, [("This word is ", False, False), ("bold", True, False), (" and this is ", False, False), ("italic", False, True), (".", False, False)]),
        p("Heading2", [("Overview", False, False)]),
        p(None, [("Plain paragraph with a few details about the project.", False, False)]),
        '<w:sectPr/>',
    ]
)

DOCUMENT = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    f'<w:document xmlns:w="{W}"><w:body>{body}</w:body></w:document>'
)

OUT = "/home/z/my-project/download/ajaia-doc-editor/tests/fixtures/sample.docx"

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", CONTENT_TYPES)
    z.writestr("_rels/.rels", RELS)
    z.writestr("word/document.xml", DOCUMENT)

print("wrote", OUT)
