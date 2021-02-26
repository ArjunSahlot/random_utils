#!/bin/bash

download_link=https://github.com/ArjunSahlot/random_utils/archive/main.zip
temporary_dir=$(mktemp -d) \
&& curl -LO $download_link \
&& unzip -d $temporary_dir main.zip \
&& rm -rf main.zip \
&& mv $temporary_dir/random_utils-main $1/random_utils \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/random_utils[0m"
