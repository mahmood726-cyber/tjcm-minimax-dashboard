"""Static contracts for the TJCM dashboard shell."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = REPO_ROOT / "index.html"
README = REPO_ROOT / "README.md"
PROTOCOL = REPO_ROOT / "E156-PROTOCOL.md"


def test_readme_and_protocol_align_with_dashboard() -> None:
    html = INDEX_HTML.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    protocol = PROTOCOL.read_text(encoding="utf-8")

    assert "# TJCM 12.0" in readme
    assert "Topological Jensen-Compensated Meta-Variance" in readme
    assert "Launch Dashboard" in readme
    assert "<title>TJCM 12.0" in html
    assert "Epistemic Minimax" in html
    assert "TJCM" in protocol


def test_dashboard_exposes_expected_controls_and_metrics() -> None:
    html = INDEX_HTML.read_text(encoding="utf-8")

    expected_markers = [
        'id="advection"',
        'id="sparsity"',
        'id="coupling"',
        'id="naive-val"',
        'id="clbe-val"',
        'id="cti-val"',
        'id="dof-val"',
        "Causal Transport Index",
        "Kinetic DoF",
    ]
    for marker in expected_markers:
        assert marker in html


def test_script_targets_defined_dom_nodes() -> None:
    html = INDEX_HTML.read_text(encoding="utf-8")

    assert "document.getElementById('dof-val')" in html
    assert "document.getElementById('cti-val')" not in html or 'id="cti-val"' in html
    assert "requestAnimationFrame(update);" in html
    assert "No External CDNs | Strictly Offline Capable" in html
