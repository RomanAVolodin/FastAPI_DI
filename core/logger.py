LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # noqa: WPS323
LOG_DEFAULT_HANDLERS = ['console']  # noqa: WPS407

LOGGING = {  # noqa: WPS407
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {'format': LOG_FORMAT},
        'default': {
            '()': 'uvicorn.logging.DefaultFormatter',
            'fmt': '%(levelprefix)s %(message)s',  # noqa: WPS323
            'use_colors': None,
        },
        'access': {
            '()': 'uvicorn.logging.AccessFormatter',
            'fmt': "%(levelprefix)s %(client_addr)s - '%(request_line)s' %(status_code)s",  # noqa: WPS323
        },
    },
    'handlers': {
        'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'verbose', },
        'default': {'formatter': 'default', 'class': 'logging.StreamHandler', 'stream': 'ext://sys.stdout', },
        'access': {'formatter': 'access', 'class': 'logging.StreamHandler', 'stream': 'ext://sys.stdout', },
    },
    'loggers': {
        "": {'handlers': LOG_DEFAULT_HANDLERS, 'level': 'INFO'},
        'uvicorn.error': {'level': 'INFO'},
        'uvicorn.access': {'handlers': ['access'], 'level': 'INFO', 'propagate': False, },
    },
    'root': {'level': 'INFO', 'formatter': 'verbose', 'handlers': LOG_DEFAULT_HANDLERS, },
}
