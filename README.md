# Introduction
Mobile-first ss-panel based on django 2.

# Docker demo

    docker run  --net host --rm -it \
        -v $(pwd)/tsadmin:/tsadmin/data \
        fzinfz/ss-panel:py-django-tsadmin /bin/bash
    ./init.sh