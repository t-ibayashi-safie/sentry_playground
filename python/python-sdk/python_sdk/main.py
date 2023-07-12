import os
import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

SENTRY_DSN = os.environ.get('SENTRY_DSN')
if SENTRY_DSN is None:
    raise Exception('SENTRY_DSN is not set')

sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[
        sentry_logging,
    ],
)

logger = logging.getLogger(__name__)
logger.info("SENTRY_DSN: %s", SENTRY_DSN)

"""
ロギングによるエラー通知
"""
def log():
    logger.error("test error bbbb: %s", id, stack_info=True)
    # sentry_sdk.capture_message("hello", level="error", stack_trace=True)
    # logger.error("test error bbbb: %s", id, exc_info=True, stack_info=True)
    # try:
    #     raise Exception("test error")
    # except Exception as e:
    #     logger.error("test error bbbb: %s", id, exc_info=True, stack_info=True)

def fingerprint():
    try:
        raise Exception("test error")
    except Exception as e:
        with sentry_sdk.push_scope() as scope:
            scope.fingerprint = ["foo", "hoge","{{ default }}"]
            sentry_sdk.capture_exception(e)

def main():
    fingerprint()
    
if __name__ == '__main__':
    main()
    
