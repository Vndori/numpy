from collections.abc import Sequence
from typing import Any, Literal as L, SupportsIndex, TypeAlias

from numpy._typing import ArrayLike, NDArray

__all__ = ["histogram", "histogramdd", "histogram_bin_edges"]

_BinKind: TypeAlias = L[
    "stone",
    "auto",
    "doane",
    "fd",
    "rice",
    "scott",
    "sqrt",
    "sturges",
]

def histogram_bin_edges(
    a: ArrayLike,
    bins: _BinKind | SupportsIndex | ArrayLike = ...,
    range: tuple[float, float] | None = ...,
    weights: ArrayLike | None = ...,
) -> NDArray[Any]: ...

def histogram(
    a: ArrayLike,
    bins: _BinKind | SupportsIndex | ArrayLike = ...,
    range: tuple[float, float] | None = ...,
    density: bool = ...,
    weights: ArrayLike | None = ...,
) -> tuple[NDArray[Any], NDArray[Any]]: ...

def histogramdd(
    sample: ArrayLike,
    bins: SupportsIndex | ArrayLike = ...,
    range: Sequence[tuple[float, float]] = ...,
    density: bool | None = ...,
    weights: ArrayLike | None = ...,
) -> tuple[NDArray[Any], tuple[NDArray[Any], ...]]: ...
