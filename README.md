# Introduction
Mobile-first ss-panel based on django 2, support [ssmanager-nopanel](https://github.com/fzinfz/ssmanager-nopanel).

# Docker demo

    git clone git@github.com:fzinfz/tsadmin.git
    docker run  --net host --rm -it \
        -e "SECRET_KEY=your_secret_key" \
        -e "DEBUG=y" \
        -v $(pwd)/tsadmin:/tsadmin -w /tsadmin \
        fzinfz/tools:django2 /bin/bash
    ./init.sh