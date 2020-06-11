import os


def export_vars(request):
    data = {
        'PROJECT_NAME': os.getenv('APP_NAME'),
        'HOSTNAME': "localhost:8000" if os.getenv('SETTINGS') == "DEV" else os.getenv('WEB_HOST'),
        'URL_SCHEME': "http" if os.getenv('SETTINGS') == "DEV" else "https",
    }
    return data
