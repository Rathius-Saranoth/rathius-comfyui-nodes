from comfy.comfy_types import ComfyNodeABC


class AddOne(ComfyNodeABC):
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"x": ("INT", {"default": 0})}}

    RETURN_TYPES = ("INT",)
    FUNCTION = "add"
    CATEGORY = "math"

    def add(self, x):
        # simple, deterministic example node used for testing and docs
        return (x + 1,)


NODE_CLASS_MAPPINGS = {
    "AddOne": AddOne,
}


class DisplayValue(ComfyNodeABC):
    @classmethod
    def INPUT_TYPES(cls):
        # Accept any input and coerce to string for display
        return {"required": {"value": ("*", {"default": ""})}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "display"
    CATEGORY = "utility"
    DESCRIPTION = "Simple node that returns a string representation of its input for display/testing."

    def display(self, value):
        # Coerce to string and return as a single STRING output
        return (str(value),)


# register display node as well
NODE_CLASS_MAPPINGS["DisplayValue"] = DisplayValue
