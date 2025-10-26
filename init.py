 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/src/cratesai_pro/__init__.py b/src/cratesai_pro/__init__.py
new file mode 100644
index 0000000000000000000000000000000000000000..823cb806db89321ff26dfadea67c56b95a0631f4
--- /dev/null
+++ b/src/cratesai_pro/__init__.py
@@ -0,0 +1,5 @@
+"""CratesAI Pro - macOS DJ library analyzer & organizer."""
+from __future__ import annotations
+
+__all__ = ["__version__"]
+__version__ = "0.1.0"
 
EOF
)
