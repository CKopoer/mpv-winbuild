"""Select the maintained mpv fork before configuring the Windows toolchain."""
from pathlib import Path
path = Path("packages/mpv.cmake")
text = path.read_text()
old = "GIT_REPOSITORY https://github.com/mpv-player/mpv.git"
if text.count(old) != 1:
    raise SystemExit("Review the mpv toolchain source contract before building")
text = text.replace(old, "GIT_REPOSITORY https://github.com/CKopoer/mpv.git\n    GIT_TAG 88eb9f2e73945d8bc9c133a2f67babaa9af34680")
path.write_text(text)
