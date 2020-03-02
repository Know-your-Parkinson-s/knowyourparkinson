from flask import Flask, request, render_template
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://47f7844dd9d34a1d9b28d4dc906dea58@sentry.io/3394112",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

from app import routes, errors
