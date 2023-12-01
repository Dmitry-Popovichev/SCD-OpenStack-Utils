# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2023 United Kingdom Research and Innovation
import logging
import logging.handlers
import os
import sys
from iriscasttools.stats import get_iriscast_stats, parse_args


def _prep_logging():
    logger = logging.getLogger("iriscasttools")
    logger.setLevel(os.getenv("LOG_LEVEL", "INFO").upper())
    logger.addHandler(logging.StreamHandler(sys.stdout))


def main():
    _prep_logging()
    cmd_args = parse_args(sys.argv[1:])
    print(get_iriscast_stats(cmd_args.as_csv, cmd_args.include_header))


if __name__ == "__main__":
    main()
