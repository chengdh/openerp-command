import argparse

from .call import Call
from .client import Open, Show, ConsumeNothing, ConsumeMemory, LeakMemory, ConsumeCPU
from .benchmarks import Bench, BenchRead, BenchFieldsViewGet, BenchDummy, BenchLogin
from .bench_sale_mrp import BenchSaleMrp
from . import common

from . import conf # Not really server-side (in the `for` below).
from . import drop
from . import initialize
from . import model
from . import module
from . import read
from . import run_tests
from . import scaffold
from . import uninstall
from . import update

def main_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    # Server-side commands.
    for x in (conf, drop, initialize, model, module, read, run_tests, scaffold, uninstall, update,):
        x.add_parser(subparsers)
    # Client-side commands. TODO one per .py file.
    for x in (Call, Open, Show, ConsumeNothing, ConsumeMemory, LeakMemory, ConsumeCPU,
        Bench, BenchRead, BenchFieldsViewGet, BenchDummy, BenchLogin,
        BenchSaleMrp):
        x(subparsers)
    return parser
