 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/src/cratesai_pro/__main__.py b/src/cratesai_pro/__main__.py
new file mode 100644
index 0000000000000000000000000000000000000000..4b8174cc06af4ec0f04a91a3523ddb3a3a39ca27
--- /dev/null
+++ b/src/cratesai_pro/__main__.py
@@ -0,0 +1,8 @@
+"""Module entry point for ``python -m cratesai_pro``."""
+from __future__ import annotations
+
+from .app import main
+
+
+if __name__ == "__main__":
+    raise SystemExit(main())
 
EOF
) 
