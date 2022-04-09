#!/bin/bash
set -e

# Run tests
pytest atpthings -x
pytest tests -x
