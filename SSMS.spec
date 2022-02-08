# -*- mode: python ; coding: utf-8 -*-
#打包为目录结构


block_cipher = None


a = Analysis(['main.py','package\\__init__.py','package\\login.py','package\\path.py','package\\student.py','package\\user.py','package\\encrypt.py','package\\imexport.py'],#项目所有包含的py文件
             pathex=['D:\\Code\\Workspace\\Python\\STUSF\\SSMS_cmd\\V1.2'],#项目绝对路径
             binaries=[],
             datas=[('file\\SU\\student.txt','file'),('file\\SU\\user.txt','file'),('file\\import','file'),('file\\export','file')],#资源文件
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='SAMS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,#运行时显示控制台
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='SSMS V1.2')
