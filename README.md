# Introduction
Mobile-first ss-panel based on django 2, support [ssmanager-nopanel](https://github.com/fzinfz/ssmanager-nopanel).

# Docker demo

    docker run  --net host --rm -it \
        -e "SECRET_KEY=your_secret_key" \
        -e "DEBUG=true" \
        -v $(pwd)/tsadmin:/tsadmin/data \
        fzinfz/ss-panel:py-django-tsadmin /bin/bash
    ./init.sh