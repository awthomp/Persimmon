# -*- mode: python -*-

from kivy.deps import sdl2, angle#, glew
from PyInstaller.utils.hooks import collect_submodules

from glob import iglob
from itertools import chain
from os.path import dirname
import pathlib

non_py_files = chain.from_iterable((iglob('whitewater/**/*.{}'.format(ext), recursive=True)
	                            for ext in ['kv', 'png', 'ini']))


non_py_files = [(file, dirname(file)) for file in non_py_files]

block_cipher = None

a = Analysis(['whitewater\\__main__.py'],
             pathex=['.\\whitewater'],
             binaries=None,
             datas=non_py_files,
             hiddenimports=collect_submodules('scipy') + collect_submodules('sklearn') + ['win32timezone'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['jinja2.asyncsupport','jinja2.asyncfilters'],  # Python 3.5 bug
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + angle.dep_bins)],#+ glew.dep_bins)],
          name='whitewater',
          debug=False,
          strip=False,
          upx=True,
          console=False)
