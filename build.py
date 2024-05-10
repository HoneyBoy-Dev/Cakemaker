from cx_Freeze import setup, Executable
setup(
    name="MiAplicacion",
    version="1.0",
    description="Descripción de mi aplicación",
    executables=[Executable("main.py")]
)
