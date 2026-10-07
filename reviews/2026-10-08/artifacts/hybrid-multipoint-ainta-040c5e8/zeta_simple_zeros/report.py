"""Stable JSON/text reports for certificate runs."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class VerificationReport:
    certificate: str
    verified: bool
    target: str
    grid: int
    precision_bits: int
    kernel_table_sha256: str
    nodes: int
    pruned: int
    splits: int
    maximum_depth: int
    initial_boxes: int
    elapsed_seconds: float
    details: Dict[str, Any]

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, sort_keys=True)

    def to_text(self) -> str:
        lines = [
            f"certificate={self.certificate}",
            f"verified={str(self.verified).lower()}",
            f"target={self.target}",
            f"grid={self.grid}",
            f"precision_bits={self.precision_bits}",
            f"kernel_table_sha256={self.kernel_table_sha256}",
            f"initial_boxes={self.initial_boxes}",
            f"nodes={self.nodes}",
            f"pruned={self.pruned}",
            f"splits={self.splits}",
            f"maximum_depth={self.maximum_depth}",
            f"elapsed_seconds={self.elapsed_seconds:.6f}",
        ]
        for key in sorted(self.details):
            lines.append(f"{key}={self.details[key]}")
        return "\n".join(lines)
