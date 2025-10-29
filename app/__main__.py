 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/app/__main__.py b/app/__main__.py
new file mode 100644
index 0000000000000000000000000000000000000000..e555e431597e3ea30722fa688fa7727b7ca63afb
--- /dev/null
+++ b/app/__main__.py
@@ -0,0 +1,12 @@
+"""Entry point for the File Organizer MAC application."""
+
+from .gui.main_window import launch_app
+
+
+def main() -> None:
+    """Launch the graphical application."""
+    launch_app()
+
+
+if __name__ == "__main__":
+    main()
 
EOF
)
