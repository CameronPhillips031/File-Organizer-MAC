 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/app/webviews/spotify_view.py b/app/webviews/spotify_view.py
new file mode 100644
index 0000000000000000000000000000000000000000..be61bc992b6017bbaef363ab9e338ef6d0f7fbe1
--- /dev/null
+++ b/app/webviews/spotify_view.py
@@ -0,0 +1,6 @@
+"""Web view integrations for Spotify."""
+
+
+def open_spotify_view() -> None:
+    """Open the Spotify embedded view (stub)."""
+    raise NotImplementedError("Spotify web view has not been implemented yet.")
 
EOF
)
