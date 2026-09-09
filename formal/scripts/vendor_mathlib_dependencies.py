"""Archive mathlib's official transitive sources, with exact commits and licenses.

Read-only on the source cache. The destination is formal/vendor.
No project code from the owner of the source cache is copied.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import posixpath
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[1]

def git(directory, *args):
    return subprocess.check_output(["git", "-C", str(directory), *args])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("packages", type=Path)
    args = parser.parse_args()
    manifest = json.loads((args.packages / "mathlib/lake-manifest.json").read_text(encoding="utf-8"))
    records = []
    for entry in manifest["packages"]:
        name, revision = entry["name"], entry["rev"]
        source = args.packages / name
        assert git(source, "rev-parse", "HEAD").decode().strip() == revision
        raw = git(source, "archive", "--format=tar", revision)
        target = ROOT / "vendor" / name
        target.mkdir(parents=True, exist_ok=True)
        links = []
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:") as archive:
            for item in archive.getmembers():
                resolved = (target / item.name).resolve()
                assert resolved.is_relative_to(target.resolve()), item.name
                if item.issym() or item.islnk():
                    linkpath = posixpath.normpath(posixpath.join(
                        posixpath.dirname(item.name) if item.issym() else "", item.linkname))
                    assert (target / linkpath).resolve().is_relative_to(target.resolve())
                    referent = archive.getmember(linkpath)
                    assert referent.isfile(), (item.name, linkpath)
                    links.append(dict(path=item.name, original_target=item.linkname,
                                      materialized_from=linkpath))
            archive.extractall(target, members=[
                m for m in archive.getmembers() if not (m.issym() or m.islnk())], filter="data")
            for link in links:
                destination = target / link["path"]
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(archive.extractfile(link["materialized_from"]).read())
        files = []
        for file in sorted(target.rglob("*")):
            if file.is_file() and ".lake" not in file.parts:
                data = file.read_bytes()
                files.append(dict(path=file.relative_to(target).as_posix(),
                                  bytes=len(data), sha256=hashlib.sha256(data).hexdigest()))
        licenses = [f["path"] for f in files if any(
            word in Path(f["path"]).name.upper() for word in ("LICENSE", "COPYING", "NOTICE"))]
        assert licenses, name
        records.append(dict(name=name, url=entry["url"], revision=revision,
                            archive_sha256=hashlib.sha256(raw).hexdigest(),
                            license_files=licenses, materialized_symlinks=links, files=files))
        print(name, revision, len(files), flush=True)
    (ROOT / "vendor/manifest.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
