"""Static checks for the deployable MultiPost website root."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
CORE_PAGES = (
    "index.html",
    "features.html",
    "how-it-works.html",
    "download.html",
    "support.html",
    "privacy-policy/index.html",
    "terms-of-service/index.html",
)
FORBIDDEN_SOURCE_TEXT = (
    "MultiPost Desktop",
    "ovtom22.github.io/multipost-desktop",
    "GitHub Pages media location",
    "does not operate a central database or cloud account service",
    "does not operate a posting backend",
)


class References(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []
        self.has_h1 = False
        self.has_viewport = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "a" and data.get("href"):
            self.references.append(data["href"] or "")
        if tag in {"img", "script"} and data.get("src"):
            self.references.append(data["src"] or "")
        if tag == "link" and data.get("href"):
            self.references.append(data["href"] or "")
        if tag == "h1":
            self.has_h1 = True
        if tag == "meta" and (data.get("name") or "").lower() == "viewport":
            self.has_viewport = True


def local_target(page: Path, reference: str) -> Path | None:
    parsed = urlparse(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("#", "mailto:", "tel:")):
        return None
    path = parsed.path
    if not path:
        return None
    target = (page.parent / path).resolve()
    if path.endswith("/"):
        target /= "index.html"
    return target


def main() -> int:
    errors: list[str] = []
    pages = sorted(path for path in ROOT.rglob("*.html") if "commercial-preview" not in path.parts)
    for relative in CORE_PAGES:
        page = ROOT / relative
        if not page.is_file():
            errors.append(f"missing core page: {relative}")
    for page in pages:
        content = page.read_text(encoding="utf-8")
        for phrase in FORBIDDEN_SOURCE_TEXT:
            if phrase.lower() in content.lower():
                errors.append(f"legacy source claim in {page.relative_to(ROOT)}: {phrase}")
        parser = References()
        parser.feed(content)
        if page.relative_to(ROOT).as_posix() in CORE_PAGES:
            if not parser.has_viewport:
                errors.append(f"missing viewport: {page.relative_to(ROOT)}")
            if not parser.has_h1:
                errors.append(f"missing h1: {page.relative_to(ROOT)}")
        for reference in parser.references:
            target = local_target(page, reference)
            if target is not None and not target.is_file():
                errors.append(f"broken local reference in {page.relative_to(ROOT)}: {reference}")

    if errors:
        print("SITE CHECK FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"SITE CHECK PASSED: {len(pages)} HTML pages checked; {len(CORE_PAGES)} core pages verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
