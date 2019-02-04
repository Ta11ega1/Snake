import cx_Freeze

executables = [cx_Freeze.Executable("serpiente.py", base = "Win32GUI")]

build_exe_options = {"packages": ["pygame"], "include_files":["arial_narrow_7.ttf",
                                                              "25.jpg",
                                                              "icon.png","29.jpg",
                                                              "Fondo jp-01.png",
                                                              "song.ogg",
                                                              "Sonig.ogg"]}

cx_Freeze.setup(
    name = "serpiente",
    version = "1.0",
    description = "Juego de atrapar la manzana con una serpiente",
    options={"build_exe": build_exe_options},
    executables = executables
    )
