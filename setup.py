import cx_Freeze
import cx_Freeze.executable

executaveis = [cx_Freeze.Executable(script="main.py")]
cx_Freeze.setup(
    name = "Iron Man" ,
    options={
        "build_axe":{
            "packages":["pygame"],
            "include_files":["assets"]
        }
    }, executables = executaveis
)