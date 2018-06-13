from django.conf import settings

from django_hosts import patterns, host


host_patterns = patterns(
    '',

    host(
        r'second\.test\.net',
        'dhtest.secondurls',
        name='second'
    ),

    host(
        r'(\w+)',
        'dhtest.urls',
        name='default'
    ),
)
