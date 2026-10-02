import subprocess
import sys
from pathlib import Path

import mini_hako


def test_mini_hako_module_and_public_exports():
    assert mini_hako.Hako is not None
    assert mini_hako.FakeModelClient is not None
    assert not hasattr(mini_hako, "MiniAgent")
    result = subprocess.run([sys.executable, "-m", "mini_hako", "--help"], capture_output=True, text=True, check=True)
    assert "Teaching-sized Hako agent harness" in result.stdout


def test_readme_main_mapping_points_to_existing_files():
    repo_root = Path(__file__).resolve().parents[3]
    main_files = [
        "hako/cli.py",
        "hako/runtime.py",
        "hako/agent_loop.py",
        "hako/context_manager.py",
        "hako/providers/clients.py",
        "hako/tool_executor.py",
        "hako/tools.py",
        "hako/task_state.py",
        "hako/run_store.py",
        "hako/workspace.py",
    ]
    for path in main_files:
        assert (repo_root / path).exists()
