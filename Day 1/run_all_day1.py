"""
run_all_day1.py
Simple runner to execute Day_1 examples in order. Interactive files will be skipped by default
unless the user agrees to run them (so the script can be used non-interactively).

Run: python .\run_all_day1.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent

files = [
    "1First_program.py",
    "2Data_type.py",
    "3Type_of_operator.py",
    "4Input_in_python.py",  # interactive examples
    "5Practice.py",
]

interactive = {"4Input_in_python.py"}

def run_file(path: Path):
    print("\n" + "=" * 60)
    print(f"Running: {path.name}")
    print("=" * 60)
    try:
        subprocess.run([sys.executable, str(path)], check=True)
    except subprocess.CalledProcessError as exc:
        print(f"{path.name} exited with code {exc.returncode}")

def confirm(prompt: str) -> bool:
    ans = input(prompt + " [y/N]: ").strip().lower()
    return ans in ("y", "yes")

def main():
    for fname in files:
        path = ROOT / fname
        if not path.exists():
            print(f"Skipping missing file: {fname}")
            continue

        if fname in interactive:
            print(f"\nFile `{fname}` contains interactive input() calls.")
            if confirm("Run it now (you will be prompted for input)?"):
                run_file(path)
            else:
                print(f"Skipped {fname}")
        else:
            run_file(path)

    print("\nAll done.")

if __name__ == '__main__':
    main()
