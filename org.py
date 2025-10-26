 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/src/cratesai_pro/organizer/organizer.py b/src/cratesai_pro/organizer/organizer.py
new file mode 100644
index 0000000000000000000000000000000000000000..c07d531b0f060b9f9de3f9ebacbf9fa26b5cb188
--- /dev/null
+++ b/src/cratesai_pro/organizer/organizer.py
@@ -0,0 +1,39 @@
+"""Utilities for copying or moving analyzed tracks into normalized folders."""
+from __future__ import annotations
+
+import shutil
+from pathlib import Path
+from typing import Iterable
+
+from ..models import TrackAnalysis
+
+
+class Organizer:
+    """Move or copy analyzed tracks into destination folders."""
+
+    def __init__(self, destination: Path, mode: str = "copy") -> None:
+        if mode not in {"copy", "move"}:
+            raise ValueError("mode must be 'copy' or 'move'")
+        self.destination = destination
+        self.mode = mode
+
+    def organize(self, tracks: Iterable[TrackAnalysis]) -> list[Path]:
+        self.destination.mkdir(parents=True, exist_ok=True)
+        result_paths: list[Path] = []
+        for track in tracks:
+            genre = (track.genre or "Unknown").strip() or "Unknown"
+            safe_title = _sanitize(track.title)
+            safe_artist = _sanitize(track.artist or "Unknown Artist")
+            target_dir = self.destination / genre
+            target_dir.mkdir(parents=True, exist_ok=True)
+            target_path = target_dir / f"{safe_artist} - {safe_title}{track.source_path.suffix}"
+            if self.mode == "copy":
+                shutil.copy2(track.source_path, target_path)
+            else:
+                shutil.move(track.source_path, target_path)
+            result_paths.append(target_path)
+        return result_paths
+
+
+def _sanitize(value: str) -> str:
+    return "".join(char for char in value if char.isalnum() or char in {" ", "-", "_"}).strip() or "Unknown"
 
EOF
)
