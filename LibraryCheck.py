import importlib

required = {
    "numpy": "pip install numpy",
    "PIL": "pip install pillow",
    "matplotlib": "pip install matplotlib"
}

print("\n=== Checking Required Libraries for Image Segmentation Demo ===\n")

for module, install_cmd in required.items():
    try:
        importlib.import_module(module)
        print(f"[OK] {module} is installed.")
    except ImportError:
        print(f"[MISSING] {module} is NOT installed.")
        print(f"          → Install using: {install_cmd}\n")

print("\nCheck complete.\n")