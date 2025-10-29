 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/app/core/tags.py b/app/core/tags.py
new file mode 100644
index 0000000000000000000000000000000000000000..21750834ca351ff687a49a4a5b60248b93054b0d
--- /dev/null
+++ b/app/core/tags.py
@@ -0,0 +1,8 @@
+"""Tag management helpers."""
+
+from typing import Iterable, Mapping
+
+
+def apply_tags(tracks: Iterable[Mapping[str, object]]) -> list[Mapping[str, object]]:
+    """Apply tagging rules to tracks (stub)."""
+    raise NotImplementedError("Tag application has not been implemented yet.")
 
EOF
)
