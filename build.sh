#!/usr/bin/env bash
# TA-Lib kurulumu
curl -L https://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz | tar xvz
cd ta-lib
./configure --prefix=/usr
make
make install
cd ..
