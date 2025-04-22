import logging
import json
import os
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

# Ensuring the logs directory exists
LOGS_DIR = 'logs'
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

logger = logging.getLogger(__name__)

class RequestResponseLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        log_data = {
            'method': request.method,
            'path': request.path,
            'headers': dict(request.headers),
            'body': request.body.decode('utf-8', errors='ignore') if request.body else None,
        }
        logger.info(f"Request: {json.dumps(log_data)}")
        return None

    def process_response(self, request, response):
        log_data = {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content_length': len(response.content),
            'content': response.content.decode('utf-8', errors='ignore')[:500] + "..." if len(response.content) > 500 else response.content.decode('utf-8', errors='ignore'), 
        }
        logger.info(f"Response: {json.dumps(log_data)}")
        return response