import os
import importlib.util
import pytest


def load_nodes_module():
    """Helper to load the nodes module for testing without importing ComfyUI."""
    module_path = os.path.join(os.getcwd(), "__init__.py")
    spec = importlib.util.spec_from_file_location("rathius_comfyui_nodes", module_path)
    spec = importlib.util.spec_from_file_location("rathius_comfyui_nodes", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not find module or loader at {module_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_node_registration():
    """Test that nodes are properly registered in NODE_CLASS_MAPPINGS."""
    mod = load_nodes_module()
    assert hasattr(mod, "NODE_CLASS_MAPPINGS"), "Module must expose NODE_CLASS_MAPPINGS"
    assert "AddOne" in mod.NODE_CLASS_MAPPINGS, "AddOne must be registered"
    assert "DisplayValue" in mod.NODE_CLASS_MAPPINGS, "DisplayValue must be registered"
    
    node_cls_addone = mod.NODE_CLASS_MAPPINGS["AddOne"]
    assert hasattr(node_cls_addone, "INPUT_TYPES"), "AddOne node must declare INPUT_TYPES"
    assert hasattr(node_cls_addone, "RETURN_TYPES"), "AddOne node must declare RETURN_TYPES"
    assert hasattr(node_cls_addone, "FUNCTION"), "AddOne node must declare FUNCTION"

    input_types_addone = node_cls_addone.INPUT_TYPES()
    assert "required" in input_types_addone, "AddOne node must declare required inputs"
    assert "x" in input_types_addone["required"], "AddOne node must accept 'x' input"
    assert input_types_addone["required"]["x"][0] == "INT", "AddOne input 'x' must be INT type"

    node_cls_displayvalue = mod.NODE_CLASS_MAPPINGS["DisplayValue"]
    assert hasattr(node_cls_displayvalue, "INPUT_TYPES"), "DisplayValue node must declare INPUT_TYPES"
    assert hasattr(node_cls_displayvalue, "RETURN_TYPES"), "DisplayValue node must declare RETURN_TYPES"
    assert hasattr(node_cls_displayvalue, "FUNCTION"), "DisplayValue node must declare FUNCTION"

    input_types_displayvalue = node_cls_displayvalue.INPUT_TYPES()
    assert "required" in input_types_displayvalue, "DisplayValue node must declare required inputs"
    assert "value" in input_types_displayvalue["required"], "DisplayValue node must accept 'value' input"
    assert input_types_displayvalue["required"]["value"][0] == ("INT", "STRING"), "DisplayValue input 'value' must be (INT, STRING) type"


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


def test_display_value_basic():
    """Test basic DisplayValue node functionality."""
    mod = load_nodes_module()
    node_cls = mod.NODE_CLASS_MAPPINGS["DisplayValue"]
    node = node_cls()

    assert node.display(123) == ("123",), "Integer input should be converted to string"
    assert node.display("hello") == ("hello",), "String input should remain string"
    assert node.display(123.45) == ("123.45",), "Float input should be converted to string"
    assert node.display(True) == ("True",), "Boolean input should be converted to string"
    assert node.display(None) == ("None",), "None input should be converted to string"
