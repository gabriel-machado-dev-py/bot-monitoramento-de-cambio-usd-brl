from cx_Freeze import setup, Executable
import sys

configuracao = Executable(
    script="app.py",
    base=None
)

setup(
    name="App",
    version="1.0",
    description="App",
    executables=[configuracao],
    options={
        "build_exe": {
          'include_msvcr': True
        },
    }
)