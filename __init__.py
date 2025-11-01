from comfy.comfy_types import ComfyNodeABC

NODE_CLASS_MAPPINGS = {}

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

class DisplayValue(ComfyNodeABC):
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (("INT", "STRING"), {"default": 0})}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "display"
    CATEGORY = "utility"
    OUTPUT_NODE = True

    def display(self, value):
        return (str(value),)


NODE_CLASS_MAPPINGS["DisplayValue"] = DisplayValue
NODE_CLASS_MAPPINGS["AddOne"] = AddOne
