 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/app/core/settings.py b/app/core/settings.py
new file mode 100644
index 0000000000000000000000000000000000000000..3c868a257ad93add9df5c48aa3da81fc08d2bf23
--- /dev/null
+++ b/app/core/settings.py
@@ -0,0 +1,12 @@
+"""Configuration primitives for the File Organizer MAC project."""
+
+from dataclasses import dataclass
+
+
+@dataclass
+class AppSettings:
+    """Placeholder settings container."""
+
+    library_path: str = ""
+    enable_spotify: bool = False
+    enable_soundcloud: bool = False
 
EOF
)
