import argparse
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("stan_file", help="path of the stan file to compile", type=str)

args = parser.parse_args()
f_stan = os.path.join(os.getcwd(), args.stan_file)
cmdstanpath = os.path.join(os.getenv("HOME"), "local", "cmdstan")

print(cmdstanpath)
print(f"{f_stan[:-5]}")
with subprocess.Popen(
    ["make", f"{f_stan[:-5]}"],
    cwd=cmdstanpath,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
) as process:
    stdout, stderr = process.communicate()
    print(stdout.decode("utf-8"))
    print(stderr.decode("utf-8"))
