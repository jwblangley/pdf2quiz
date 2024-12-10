import pymupdf
import math

REDACT_COLOR = (1, 0, 0)


def redact_from_page(page, text_to_redact, occurrences=math.inf):
    areas = page.search_for(text_to_redact)
    for i, area in enumerate(areas):
        if i >= occurrences:
            break
        page.add_redact_annot(area, text=" ", fill=REDACT_COLOR)

    page.apply_redactions()


if __name__ == "__main__":
    doc = pymupdf.open("pdfs/AGEP1 cell bio review.pdf")
    page = doc[3]
    redact_from_page(page, "and")
    pix = page.get_pixmap()
    pix.save("test.png")
