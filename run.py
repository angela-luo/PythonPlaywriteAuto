"""
File: run.py
Creator: Angel
Created: 2025-06-05
Description: Main script to execute tests and generate reports
"""

import os
import pytest
import subprocess
import argparse
from config.config import Config


def run_tests(modules=None, levels=None, parallel=False):
    """
    Execute test cases
    :param modules: Module to run (login, register)
    :param levels: Test level (P0, P1, P2, P3)
    :param parallel: Whether to run in parallel
    """
    # Build pytest command
    pytest_args = [
        # "pytest",
        f"--alluredir={Config.ALLURE_RESULTS_DIR}",
        "--clean-alluredir"
    ]



    # Build marker expression
    markers = []
    if modules:
        # markers.append(module)
        module_expr = " or ".join(modules)
        markers.append(f"({module_expr})")

    if levels:
        # construct the precedence expression: P0 or P1 or P2
        level_expr = " or ".join(levels)
        markers.append(f"({level_expr})")

    if markers:
        marker_expr = " and ".join(markers)
        pytest_args.extend(["-m", marker_expr])

    # Add parallel execution
    if parallel:
        pytest_args.extend(["-n", "auto"])

    #  Execute pytest
    exit_code = pytest.main(pytest_args)

    results_files = os.listdir(Config.ALLURE_RESULTS_DIR)

    # Generate Allure report
    subprocess.run([
        Config.ALLURE_BIN_PATH, "generate",
        Config.ALLURE_RESULTS_DIR,
        "-o", Config.ALLURE_REPORT_DIR,
        "--clean"
    ], check=True)


    # # Open Allure report
    # subprocess.run([
    #     Config.ALLURE_BIN_PATH, "open",
    #     Config.ALLURE_REPORT_DIR
    # ], check=True)

    return exit_code


if __name__ == "__main__":
    #  Command line argument parsing
    parser = argparse.ArgumentParser(description="Run PetStore test suite")
    parser.add_argument("-m", "--modules", nargs="+", choices=["login", "register"], help="Test module")
    # parser.add_argument("-l", "--test_level", choices=["P0", "P1", "P2", "P3"], help="Test level")
    parser.add_argument(
        "-l", "--levels",
        nargs="+",
        choices=["P0", "P1", "P2", "P3"],
        help="Test levels to include (e.g., P0 P1)"
    )
    parser.add_argument("-p", "--parallel", action="store_true", help="Run tests in parallel")
    args = parser.parse_args()

    # Run tests
    run_tests(modules=args.modules, levels=args.levels, parallel=args.parallel)




# example usage:
# # Run all tests of both the login and register modules
# python run.py --modules login register
#
# # Run P0 tests for the login and register modules
# python run.py --modules login register --levels P0
#
# # Run P0 and P1 tests for all modules
# python run.py --levels P0 P1