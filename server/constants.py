import os

CONSTANTS = {
    'PORT': os.environ.get('PORT', 3001),
    'COSMOS': {
        'COLLECTION': 'ListItems'
    },
    'HTTP_STATUS': {
        '404_NOT_FOUND': 404,
    },
    'ENDPOINT': {
        'MASTER_DETAIL': '/api/masterdetail',
        'GRID': '/api/grid',
    }
}
