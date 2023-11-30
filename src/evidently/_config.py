import os


TELEMETRY_ADDRESS = "https://telemetry-321112.ew.r.appspot.com/post_data"
TELEMETRY_ENABLED = os.getenv("EVIDENTLY_DISABLE_TELEMETRY", "0") != "1"
