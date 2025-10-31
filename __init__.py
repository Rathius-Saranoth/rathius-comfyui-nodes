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
        # Use permissive input but validate at runtime. Accept INT or STRING.
        return {"required": {"value": ("*", {"default": 0})}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "display"
    CATEGORY = "utility"
    DESCRIPTION = "Simple node that returns a string representation of its input for display/testing."
    OUTPUT_NODE = True

    def display(self, value):
        # Coerce to string and return as a single STRING output
        return (str(value),)

    @classmethod
    def VALIDATE_INPUTS(cls, inputs):
        """Ensure the incoming value is INT or STRING (or coercible to int)."""
        v = inputs.get("value")
        if v is None:
            return
        if isinstance(v, (int, str)):
            return
        # try coercion
        try:
            int(v)
            return
        except Exception:
            raise RuntimeError("DisplayValue input must be INT or STRING")


# register display node as well
NODE_CLASS_MAPPINGS["DisplayValue"] = DisplayValue
