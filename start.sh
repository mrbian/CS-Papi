#!/bin/bash
export PATH="/usr/lib/lightdm/lightdm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/mysql/bin:/opt/android-sdk-linux/tools:/opt/android-sdk-linux/platform-tools:~/usr/lib/jvm/jdk-6/bin"

dir="$(dirname $0)"

env=${dir}/.env/bin/activate
source ${env}

entry_file="${dir}/index.py"
python ${entry_file}