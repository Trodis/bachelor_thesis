from cx_Freeze import setup, Executable

includefiles = ['sirrix_logo.png', 'BitBox.ico']
includes = []
excludes = []
packages = []

setup(
    name = "BitBox_PolicyTool",
    version = "0.1",
    description = "Policy Configuration Tool for BitBox Standalone",
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables = [Executable("policytool.py")]
)
