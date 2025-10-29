 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/build_app.sh b/build_app.sh
new file mode 100755
index 0000000000000000000000000000000000000000..10f5cea8d9c6eff345a62c7c6413ace9e81d1bb0
--- /dev/null
+++ b/build_app.sh
@@ -0,0 +1,5 @@
+#!/usr/bin/env bash
+set -euo pipefail
+
+# Placeholder build script for File Organizer MAC.
+python -m PyInstaller FileOrganizerMAC.spec
 
EOF
)
