from dataclasses import dataclass
from typing import Optional


@dataclass
class ToyConfig:
    """Configuration for ToyNet model."""
    hidden_size: int = 64
    output_size: int = 10
    activation: str = "relu"
    use_bias_hidden: bool = True
    use_bias_output: bool = False
    dropout_rate: Optional[float] = None
    seed: int = 42


@dataclass
class DummyConfig:
    """Configuration for DummyNet model."""
    n_hidden: int = 3
    hidden_size: int = 64
    output_size: int = 10
    activation: str = "relu"
    use_bias_input: bool = True
    use_bias_hidden: bool = True
    use_bias_output: bool = False
    dropout_rate: Optional[float] = None
    seed: int = 42