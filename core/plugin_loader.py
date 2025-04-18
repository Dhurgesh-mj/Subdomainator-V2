import os 
import importlib

def load_plugins():
    plugins = []
    plugins_dir = "plugins"
    for file in os.listdir(plugins_dir):
        if file.endswith(".py") and file !="__init__.py":
            module_name = f'plugins.{file[:-3]}'
            try :
                mod = importlib.import_module(module_name)
                plugins.append(mod)
            except Exception as e :
                print("unable to load the plugins")
    return plugins