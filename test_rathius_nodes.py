import os
import importlib.util


def test_rathius_addone():
    # Load the custom node module directly (avoid importing heavy top-level `nodes` module)
    module_path = os.path.join(os.getcwd(), "custom_nodes", "rathius_comfyui_nodes", "__init__.py")
    spec = importlib.util.spec_from_file_location("rathius_comfyui_nodes", module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert hasattr(mod, "NODE_CLASS_MAPPINGS")
    assert "AddOne" in mod.NODE_CLASS_MAPPINGS
    node_cls = mod.NODE_CLASS_MAPPINGS["AddOne"]
    node = node_cls()
    result = node.add(41)
    assert result == (42,)
