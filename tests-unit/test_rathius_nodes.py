import os
import importlib.util
import pytest


def load_nodes_module():
    """Helper to load the nodes module for testing without importing ComfyUI."""
    module_path = os.path.join(os.getcwd(), "custom_nodes", "rathius_comfyui_nodes", "__init__.py")
    spec = importlib.util.spec_from_file_location("rathius_comfyui_nodes", module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_node_registration():
    """Test that nodes are properly registered in NODE_CLASS_MAPPINGS."""
    mod = load_nodes_module()
    assert hasattr(mod, "NODE_CLASS_MAPPINGS"), "Module must expose NODE_CLASS_MAPPINGS"
    assert "AddOne" in mod.NODE_CLASS_MAPPINGS, "AddOne must be registered"
    
    node_cls = mod.NODE_CLASS_MAPPINGS["AddOne"]
    assert hasattr(node_cls, "INPUT_TYPES"), "Node must declare INPUT_TYPES"
    assert hasattr(node_cls, "RETURN_TYPES"), "Node must declare RETURN_TYPES"
    assert hasattr(node_cls, "FUNCTION"), "Node must declare FUNCTION"

    input_types = node_cls.INPUT_TYPES()
    assert "required" in input_types, "Node must declare required inputs"
    assert "x" in input_types["required"], "Node must accept 'x' input"
    assert input_types["required"]["x"][0] == "INT", "Input 'x' must be INT type"


def test_addone_basic():
    """Test basic AddOne node functionality."""
    mod = load_nodes_module()
    node_cls = mod.NODE_CLASS_MAPPINGS["AddOne"]
    node = node_cls()
    
    # Test with various inputs
    assert node.add(0) == (1,), "0 + 1 = 1"
    assert node.add(41) == (42,), "41 + 1 = 42"
    assert node.add(-1) == (0,), "-1 + 1 = 0"
    assert node.add(999) == (1000,), "999 + 1 = 1000"


def test_addone_validation():
    """Test input validation and error cases."""
    mod = load_nodes_module()
    node_cls = mod.NODE_CLASS_MAPPINGS["AddOne"]
    node = node_cls()

    # Test that node handles invalid inputs appropriately
    with pytest.raises(TypeError):
        node.add("not a number")  # should raise TypeError
    
    with pytest.raises(TypeError):
        node.add(None)  # should raise TypeError

    with pytest.raises(TypeError):
        node.add([1, 2, 3])  # should raise TypeError
