# Rathius ComfyUI Nodes (rathius_comfyui_nodes)

Custom nodes for ComfyUI by Rathius. Includes `AddOne` (a minimal example node) and demonstrates the recommended layout for custom node packages.

## Quick Start

There are two ways to install this package:

1. Install the package in development mode:

```bash
# From ComfyUI directory
git clone https://github.com/Rathius-Saranoth/rathius-comfyui-nodes custom_nodes/rathius-comfyui-nodes
cd custom_nodes/rathius-comfyui-nodes
pip install -e .
```

1. Or install directly in ComfyUI's custom_nodes/:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Rathius-Saranoth/rathius-comfyui-nodes
```

## Package Info

- Name: `rathius_comfyui_nodes` (snake_case for Python)
- Author: `Rathius`

Structure

- `__init__.py` — the Python module loaded by ComfyUI's custom-node loader. It should expose `NODE_CLASS_MAPPINGS` or a `comfy_entrypoint()`.
- `README.md` — this file: quick instructions and notes.
- (optional) `example_workflows/` — JSON files with ComfyUI workflows for users to load from the UI.
- (optional) `web/` — static frontend assets your node exposes (registered automatically if present or declared in `pyproject.toml`).

How to extend

1. Add new node classes to `__init__.py` or split into modules inside the package and import them from `__init__.py`.
2. Each node should follow the node class pattern used by ComfyUI:
   - classmethod `INPUT_TYPES()` returning a dict of `required` and `optional` inputs.
   - `RETURN_TYPES` tuple.
   - `FUNCTION` string naming the instance method that performs the work.
   - Optionally `CATEGORY`, `DESCRIPTION`, `DEPRECATED`, `OUTPUT_NODE`, and `IS_CHANGED`/`VALIDATE_INPUTS` helpers.
3. Add the mapping to `NODE_CLASS_MAPPINGS` in `__init__.py` so the loader can register it.

Example (already included):

```python
# in __init__.py provided here
class AddOne(ComfyNodeABC):
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"x": ("INT", {"default": 0})}}
    RETURN_TYPES = ("INT",)
    FUNCTION = "add"
    CATEGORY = "math"

    def add(self, x):
        return (x + 1,)

NODE_CLASS_MAPPINGS = {"AddOne": AddOne}
```

What is a `.toml` (pyproject.toml)?

`pyproject.toml` is a standard metadata/configuration file used for Python packaging and build-system configuration. In the context of ComfyUI custom nodes it can also be used to declare project-level metadata that the loader may read (via the optional `comfy_config` helper) — for example, to register a `web/` folder automatically.

Minimal `pyproject.toml` snippet that the loader can use (optional):

```toml
[project]
name = "rathius-comfyui-nodes"

[tool.comfy]
web = "web" # relative folder name containing frontend assets
```

Notes about publishing
- You do not need to publish a package to use custom nodes — placing the folder under `custom_nodes/` is enough.
- If you plan to publish to PyPI or distribute as a package, `pyproject.toml` becomes useful: it holds package metadata and build-system configuration (PEP 621 / PEP 517). Use snake_case names for package/module compatibility.

Demo & example workflows — what they entail

- Demo (optional): a small web UI or readme-guided demo showing how the node behaves. This can be a simple `web/` folder containing a static HTML page that demonstrates node usage or documents inputs/outputs. If present, the loader will register the `web/` assets and the frontend can include them as extensions.
- Example workflows: JSON files saved by ComfyUI that show how to wire your node into a graph. Place these under `example_workflows/` or `examples/` (the loader searches several common names). Each file should be a ComfyUI workflow export so users can click "Load workflow" in the UI and try the node in context.

Example `example_workflows/` content (what to include):
- A minimal txt2img workflow that wires `AddOne` into a debug/meta node (or uses it in a small helper graph). Since `AddOne` is a toy example the workflow can show a small usage pattern with comments.
- Larger demos can include a README and multiple `.json` workflows showcasing different options, batch runs, and expected outputs.

Testing & verification

- Unit tests: include a test in `tests-unit/` that imports this module directly and exercises node behavior. The repository already contains a minimal test `tests-unit/test_rathius_nodes.py`.
- Runtime verification: when ComfyUI starts, the custom node loader will import this package and register the nodes so they show up in the UI.

If you want, I can also add:
- a short `pyproject.toml` (example) in this folder for packaging metadata,
- one or two example workflow JSON files under `example_workflows/` to demonstrate practical usage,
- a tiny `web/` demo page (static) that documents inputs and provides a quick UX for users.

If you'd like any of those additions, tell me which ones and I'll create them. If not, this README is ready and saved in the package.

---
Generated and maintained for Rathius — use `Rathius` as the author display name in any docs or packaging metadata.
