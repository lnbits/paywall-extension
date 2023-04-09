from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles

from lnbits.db import Database
from lnbits.helpers import template_renderer

db = Database("ext_paywall")

paywall_ext: APIRouter = APIRouter(prefix="/paywall", tags=["Paywall"])

paywall_static_files = [
    {
        "path": "/paywall/static",
        "app": StaticFiles(directory="lnbits/extensions/paywall/static"),
        "name": "paywall_static",
    }
]


def paywall_renderer():
    return template_renderer(["lnbits/extensions/paywall/templates"])


from .views import *  # noqa: F401,F403
from .views_api import *  # noqa: F401,F403
