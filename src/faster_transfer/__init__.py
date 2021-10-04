from mcdreforged.api.all import *
import speedcopy

def on_load(server: PluginServerInterface, old):
    speedcopy.patch_copyfile()

def on_unload(server: PluginServerInterface):
    try:
        speedcopy.unpatch_copyfile()
    except AttributeError:
        pass
