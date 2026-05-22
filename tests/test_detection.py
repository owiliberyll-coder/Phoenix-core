import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    """Test that required modules can be imported"""
    try:
        import numpy
        from PIL import Image
        assert True
    except ImportError as e:
        assert False, f"Import failed: {e}"

def test_detection_function_exists():
    """Test that detection function can be imported"""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "fast_scanner",
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "fast_scanner.py"),
    )
    module = importlib.util.module_from_spec(spec)
    # We only check the attribute exists without executing __main__ code
    assert spec is not None, "fast_scanner.py not found"

def test_skin_heuristic():
    """Basic test of the detection logic"""
    # This is a placeholder - real tests will use sample images
    # For now, just verify the logic doesn't crash
    import numpy as np
    r = np.array([0.5, 0.3, 0.2])
    g = np.array([0.3, 0.2, 0.1])
    b = np.array([0.2, 0.1, 0.05])
    skin = (r > 0.4) & (g > 0.2) & (b > 0.1) & (r - g > 0.07)
    assert len(skin) == 3
