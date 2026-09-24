"""Add conventional PDF document-information fields after the Pandoc build.

The LaTeX hyperxmp package writes the authoritative Creative Commons rights
statement and licence URL to the XMP metadata stream. This post-processing step
also exposes the author and keywords through conventional PDF readers that only
inspect the document-information dictionary.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: set-pdf-info.py <pdf-path>")

    pdf_path = Path(sys.argv[1]).resolve()
    temporary_path = pdf_path.with_name(f"{pdf_path.stem}.metadata.tmp.pdf")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter()
    writer.pdf_header = reader.pdf_header
    writer.clone_document_from_reader(reader)

    metadata = dict(reader.metadata or {})
    metadata.update(
        {
            "/Title": "Spatial Catastrophe Risk Intelligence",
            "/Author": "Nevil Maloba",
            "/Subject": (
                "Crowd intelligence, artificial intelligence and actuarial "
                "modelling for continuous catastrophe underwriting in Kenya"
            ),
            "/Keywords": (
                "Kenya, catastrophe, flood, drought, wildfire, locust, "
                "landslide, heat, AI, actuarial, insurance, resilience finance"
            ),
        }
    )
    writer.add_metadata(metadata)

    xmp_reference = writer._root_object.get("/Metadata")
    if xmp_reference is not None:
        xmp_stream = xmp_reference.get_object()
        xmp_bytes = xmp_stream.get_data()
        updated_xmp, replacements = re.subn(
            rb"<xmpTPg:NPages>\d+</xmpTPg:NPages>",
            f"<xmpTPg:NPages>{len(reader.pages)}</xmpTPg:NPages>".encode("ascii"),
            xmp_bytes,
            count=1,
        )
        if replacements != 1:
            raise RuntimeError("Could not update the XMP page-count field")
        xmp_stream.set_data(updated_xmp)

    try:
        with temporary_path.open("wb") as output_file:
            writer.write(output_file)
        os.replace(temporary_path, pdf_path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
