FROM alpine:edge

ENV base_dir /srv/music

RUN apk --no-cache --update add bash make ca-certificates \
    && apk --no-cache --update add python uwsgi uwsgi-python py2-pip py-psycopg2 py-pillow \

    # cleanup
    && rm -rf /var/cache/apk/* \

    # prepare
    && mkdir -p $base_dir/requirements

WORKDIR ${base_dir}

ADD ./requirements $base_dir/requirements

RUN pip install -r requirements/base.txt \
    && rm -rf /root/.cache/pip/

ADD . $base_dir

EXPOSE 8000
VOLUME /srv/music/src/static
VOLUME /srv/music/src/media
CMD sh docker-entrypoint.sh
