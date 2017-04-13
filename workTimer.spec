# -*- mode: python -*-

block_cipher = None


a = Analysis(['workTimer.py'],
             pathex=['E:\\mywork_lzd\\python_space\\workScript'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['.'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='workTimer',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='loadIcon.ico')
