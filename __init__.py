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
