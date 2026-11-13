# Run with a .NET-enabled Godot 4.5 editor from the project directory.
# This preserves the generated PNG pixels and saves a loadable ImageTexture.
extends SceneTree
func _initialize():
    var image = Image.load_from_file("res://WowWatcher/images/wah_watcher.png")
    if image == null:
        quit(1)
        return
    var texture = ImageTexture.create_from_image(image)
    var result = ResourceSaver.save(texture, "res://WowWatcher/images/wah_watcher.res")
    quit(0 if result == OK else 1)
