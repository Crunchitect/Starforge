# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/HOME_USE/PycharmProjects/StarForge/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/HOME_USE/PycharmProjects/StarForge/venv/Lib/site-packages/direct', 'direct/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/venv/Lib/site-packages/noise', 'noise/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/venv/Lib/site-packages/noise-1.2.2.dist-info', 'noise-1.2.2.dist-info/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/venv/Lib/site-packages/numpy', 'numpy/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/venv/Lib/site-packages/numpy-1.24.2.dist-info', 'numpy-1.24.2.dist-info/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/venv/Lib/site-packages/panda3d', 'panda3d/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/venv/Lib/site-packages/panda3d-1.10.13.dist-info', 'panda3d-1.10.13.dist-info/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/venv/Lib/site-packages/pygame', 'pygame/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/venv/Lib/site-packages/pygame-2.3.0.dist-info', 'pygame-2.3.0.dist-info/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/venv/Lib/site-packages/ursina', 'ursina/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/venv/Lib/site-packages/ursina-5.2.0.dist-info', 'ursina-5.2.0.dist-info/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/Fonts', 'Fonts/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/Scripts', 'Scripts/'), ('C:/Users/HOME_USE/PycharmProjects/StarForge/Sprites', 'Sprites/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
