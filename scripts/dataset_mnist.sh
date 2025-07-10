#!/bin/bash

set -e

MNIST_TMP_DIR="./tmp/mnist"
MNIST_URL_BASE="http://yann.lecun.com/exdb/mnist"
FILES=(
  "train-images-idx3-ubyte.gz"
  "train-labels-idx1-ubyte.gz"
  "t10k-images-idx3-ubyte.gz"
  "t10k-labels-idx1-ubyte.gz"
)

mkdir -p "$MNIST_TMP_DIR"

for file in "${FILES[@]}"; do
    if [ -f "$MNIST_TMP_DIR/$file" ]; then
        echo "$file already exists in $MNIST_TMP_DIR, skipping download."
    else
        echo "Downloading $file..."
        wget -q --show-progress "$MNIST_URL_BASE/$file" -P "$MNIST_TMP_DIR"
    fi
done

echo "All MNIST files are in $MNIST_TMP_DIR"
