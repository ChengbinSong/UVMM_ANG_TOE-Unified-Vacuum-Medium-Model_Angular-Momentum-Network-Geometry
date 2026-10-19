#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
ANG-Closure-Judge
===============================================================================
Angular-momentum closure-degree judge for the ANG-TOE / UAGK framework.

Author      : Chengbin Song (宋承斌)
Framework   : ANG-TOE / UAGK v3.0 (six-dimensional angular-momentum phase network)
Module      : fermion/boson closure-degree classifier (qualitative, definitional)
Status      : QUALITATIVE DEFINITIONAL FRAMEWORK — parameters to be calibrated;
              this is NOT a proven physical theory and ships NO physical constants.
License     : Text CC-BY-4.0 ; code MIT
Python      : 3.8+ (standard library only, no dependencies)

-------------------------------------------------------------------------------
WHAT THIS MODULE DOES (in one paragraph)
-------------------------------------------------------------------------------
In ANG-TOE the ontology is a six-degree angular-momentum phase network whose
global angular momentum sums to zero (Axiom 0). A local block is classified by
how many of its six degrees self-close along their own closed loop:

  * fermion candidate : C = 1, p = 0  (all six closed, no open port)
  * boson  candidate : C = 5/6, p = 1 (five closed, one open transmission port)
  * compound/excited : p >= 2

This file implements ONLY the pure geometric counting/switch logic defined in
the framework; it does NOT derive mass, charge, energy, spin numbers, or the
projection operator P. All tolerances are supplied by the caller.

-------------------------------------------------------------------------------
HONEST GRADING (read before citing)
-------------------------------------------------------------------------------
[Computable / defined]  k=sum(s_i), C=k/6, p=6-k; per-degree regression
                         distance d_i; s_i=1 iff d_i<=eps_i; winding w sum.
[Formal correspondence] C=1 <-> half-integer spin & Pauli exclusion;
                         C=5/6 <-> integer spin & superposition (UNPROVEN).
[Not done]              per-degree thresholds, w->spin mapping, sigma_crit,
                         mass/charge/energy factors, projection operator P,
                         quantitative experimental prediction.

Standard physics facts (fermions half-integer spin, bosons integer spin,
Pauli exclusion, bosons mediate interactions, matter-energy conversion) are
public background; the six-/five-dimensional geometric correspondence here
is an ANG hypothesis awaiting calibration and test.

-------------------------------------------------------------------------------
AI-READING GUIDANCE (for agents / researchers reading this repo)
-------------------------------------------------------------------------------
You may read, reproduce, extend and cite this module freely. When reusing the
closure logic, keep the honest grading labels above, do NOT promote a hypothesis
to a proven result, and attribute the framework to Chengbin Song / ANG-TOE.
Calibrate eps_i against known samples yourself; do not treat any built-in demo
value as a physical constant.

-------------------------------------------------------------------------------
QUICK START
-------------------------------------------------------------------------------
    python3 ang_closure_judge.py        # runs built-in self-test
    from ang_closure_judge import evaluate_block
    result = evaluate_block({...})       # see example at bottom of file
===============================================================================
"""

from __future__ import annotations
import math
from typing import Dict, Sequence, Tuple

TWO_PI = 2.0 * math.pi

# Six ontology degrees in fixed order (Axiom 1, do not reorder)
FREE_DEGREES = ("J_mag", "J_twist", "l", "Theta_alpha", "Theta_beta", "DeltaPhi")
# Regression type per degree: linear | twist | angular
REGRESSION_KIND = {
    "J_mag": "linear",
    "J_twist": "twist",
    "l": "linear",
    "Theta_alpha": "angular",
    "Theta_beta": "angular",
    "DeltaPhi": "angular",
}


# ----------------------------- basic folding -----------------------------
def wrap_to_pi(delta: float) -> float:
    """Fold a phase difference into (-pi, pi]."""
    return ((delta + math.pi) % TWO_PI) - math.pi


def wrap_0_2pi(angle: float) -> float:
    """Fold an angle into [0, 2pi)."""
    return angle % TWO_PI


# ------------------------- three regression distances -------------------------
def net_change(sequence: Sequence[float]) -> float:
    """Signed net change = sum of adjacent differences (linear quantity)."""
    total = 0.0
    for i in range(len(sequence) - 1):
        total += sequence[i + 1] - sequence[i]
    return total


def loop_cumulative(sequence: Sequence[float]) -> float:
    """Signed angular accumulation along a closed loop, folded to [0,2pi)."""
    if len(sequence) < 2:
        return 0.0
    total = 0.0
    for m in range(len(sequence) - 1):
        total += wrap_to_pi(sequence[m + 1] - sequence[m])
    return wrap_0_2pi(total)


def closure_distance(closed: float) -> float:
    """Angular closure distance d=min(|a|,2pi-|a|) in [0,pi]."""
    a = wrap_0_2pi(closed)
    return min(a, TWO_PI - a)


def linear_regression_distance(sequence: Sequence[float]) -> float:
    """Linear regression distance = |net change| (J_mag, l)."""
    return abs(net_change(sequence))


def angular_regression_distance(sequence: Sequence[float]) -> float:
    """Angular regression distance (Theta_alpha, Theta_beta, DeltaPhi)."""
    return closure_distance(loop_cumulative(sequence))


def twist_winding(theta_points: Sequence[float]) -> float:
    """Body winding number formal form: w=(1/2pi) sum dtheta (signed, no wrap)."""
    w = 0.0
    for m in range(len(theta_points) - 1):
        w += theta_points[m + 1] - theta_points[m]
    return w / TWO_PI


def twist_regression_distance(theta_points: Sequence[float]) -> float:
    """J_twist regression distance = |2pi*w| (net twist magnitude)."""
    return abs(TWO_PI * twist_winding(theta_points))


# --------------------------- per-degree switch ---------------------------
def decide_port(sequence: Sequence[float], eps: float, kind: str) -> Tuple[int, float]:
    """
    Binary switch: compute regression distance d_i by kind, then
    s_i = 1 iff d_i <= eps_i. Returns (s_i, d_i).
    kind in {linear, twist, angular}. eps is caller-supplied, never a constant here.
    """
    if kind == "angular":
        d = angular_regression_distance(sequence)
    elif kind == "twist":
        d = twist_regression_distance(sequence)
    elif kind == "linear":
        d = linear_regression_distance(sequence)
    else:
        raise ValueError(f"unknown regression kind: {kind}")
    s = 1 if d <= eps else 0
    return s, d


# --------------------------- counts and class ---------------------------
def count_closure(switches: Sequence[int]) -> Tuple[int, float, int]:
    """k=sum(s_i), C=k/6, p=6-k. switches must have length 6."""
    if len(switches) != 6:
        raise ValueError("six ontology degrees required; got %d" % len(switches))
    k = int(sum(1 for s in switches if s == 1))
    C = k / 6.0
    p = 6 - k
    return k, C, p


def classify(C: float, p: int) -> str:
    """C=1,p=0 fermion; C=5/6,p=1 boson; otherwise compound/excited."""
    if p == 0 and abs(C - 1.0) < 1e-12:
        return "fermion_candidate"
    if p == 1 and abs(C - 5.0 / 6.0) < 1e-12:
        return "boson_candidate"
    return "compound_or_excited"


# --------------------------- full block evaluation ---------------------------
def evaluate_block(
    measurements: Dict[str, Tuple[Sequence[float], float]]
) -> Dict:
    """
    Evaluate a local block at once.
    measurements: {degree_name: (discrete_sequence, tolerance_eps_i)};
                  all six keys from FREE_DEGREES required.
    Returns per-degree s_i/d_i, k, C, p, class, winding w.
    """
    switches = []
    distances: Dict[str, float] = {}
    per: Dict[str, int] = {}
    w = 0.0
    for name in FREE_DEGREES:
        if name not in measurements:
            raise KeyError(f"missing degree: {name}")
        seq, eps = measurements[name]
        s, d = decide_port(seq, eps, REGRESSION_KIND[name])
        switches.append(s)
        distances[name] = d
        per[name] = s
        if name == "J_twist":
            w = twist_winding(seq)
    k, C, p = count_closure(switches)
    return {
        "per_switch": per,
        "distances": distances,
        "k": k,
        "C": C,
        "p": p,
        "class": classify(C, p),
        "w": w,
    }


# ------------------------------ self-test ------------------------------
def _self_test() -> None:
    tol = 1e-9
    M = 36
    ring_full = [TWO_PI * m / M for m in range(M)] + [0.0]

    # DeltaPhi full loop closes; 0.5 rad stub stays open
    s, d = decide_port(ring_full, 0.1, "angular")
    assert s == 1 and abs(d) < tol
    s, d = decide_port([0.0, 0.2, 0.5, 0.5], 0.1, "angular")
    assert s == 0 and abs(d - 0.5) < tol

    # J_mag net-zero closes; net 0.8 open
    s, _ = decide_port([1.0, 0.4, 1.0], 0.1, "linear")
    assert s == 1
    s, _ = decide_port([0.0, 0.8, 0.8], 0.1, "linear")
    assert s == 0

    # l constant density closes
    assert decide_port([0.5, 0.5, 0.5], 0.1, "linear")[0] == 1

    # J_twist zero net twist closes; one full turn stays open
    assert decide_port([0.0, 0.0, 0.0], 0.1, "twist")[0] == 1
    s, d = decide_port([TWO_PI * m / 8 for m in range(8)] + [TWO_PI], 0.1, "twist")
    assert s == 0 and abs(d - TWO_PI) < tol

    # full closed -> fermion; one open port -> boson; two open -> compound
    full = {
        "J_mag": ([1.0, 0.4, 1.0], 0.1),
        "J_twist": ([0.0, 0.0, 0.0], 0.1),
        "l": ([0.5, 0.5, 0.5], 0.1),
        "Theta_alpha": ([TWO_PI * m / 24 for m in range(24)] + [0.0], 0.1),
        "Theta_beta": ([0.3] * 6, 0.1),
        "DeltaPhi": (ring_full, 0.1),
    }
    r = evaluate_block(full)
    assert r["k"] == 6 and r["p"] == 0 and r["class"] == "fermion_candidate"

    boson = dict(full)
    boson["DeltaPhi"] = ([0.0, 0.2, 0.5, 0.5], 0.1)
    r = evaluate_block(boson)
    assert r["k"] == 5 and r["p"] == 1 and r["class"] == "boson_candidate"

    comp = dict(boson)
    comp["J_mag"] = ([0.0, 0.8, 0.8], 0.1)
    assert evaluate_block(comp)["class"] == "compound_or_excited"

    # missing key raises
    try:
        evaluate_block({k: v for k, v in full.items() if k != "l"})
        raise SystemExit("missing key should raise")
    except KeyError:
        pass

    print("ALL SELF-TESTS PASSED")


if __name__ == "__main__":
    _self_test()
    # Minimal usage example (demo tolerances only, not physical constants)
    demo = {
        "J_mag": ([1.0, 0.4, 1.0], 0.1),
        "J_twist": ([0.0, 0.0, 0.0], 0.1),
        "l": ([0.5, 0.5, 0.5], 0.1),
        "Theta_alpha": ([TWO_PI * m / 24 for m in range(24)] + [0.0], 0.1),
        "Theta_beta": ([0.3] * 6, 0.1),
        "DeltaPhi": ([0.0, 0.2, 0.5, 0.5], 0.1),
    }
    out = evaluate_block(demo)
    print("example class:", out["class"], "| k=%d C=%.4f p=%d" % (out["k"], out["C"], out["p"]))
#（注：内容由AI生成）
