 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/FileOrganizerMAC.spec b/FileOrganizerMAC.spec
new file mode 100644
index 0000000000000000000000000000000000000000..de189db0c09f829ccdf0f79366fc04c081d36aa1
--- /dev/null
+++ b/FileOrganizerMAC.spec
@@ -0,0 +1,49 @@
+# -*- mode: python ; coding: utf-8 -*-
+"""PyInstaller specification placeholder for File Organizer MAC."""
+
+block_cipher = None
+
+
+a = Analysis(
+    [],
+    pathex=[],
+    binaries=[],
+    datas=[("assets/camelot_wheel.png", "assets")],
+    hiddenimports=[],
+    hookspath=[],
+    hooksconfig={},
+    runtime_hooks=[],
+    excludes=[],
+    win_no_prefer_redirects=False,
+    win_private_assemblies=False,
+    cipher=block_cipher,
+    noarchive=False,
+)
+pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
+exe = EXE(
+    pyz,
+    a.scripts,
+    [],
+    exclude_binaries=True,
+    name="FileOrganizerMAC",
+    debug=False,
+    bootloader_ignore_signals=False,
+    strip=False,
+    upx=True,
+    console=False,
+    disable_windowed_traceback=False,
+    argv_emulation=True,
+    target_arch=None,
+    codesign_identity=None,
+    entitlements_file=None,
+)
+coll = COLLECT(
+    exe,
+    a.binaries,
+    a.zipfiles,
+    a.datas,
+    strip=False,
+    upx=True,
+    upx_exclude=[],
+    name="FileOrganizerMAC",
+)
 
EOF
)
