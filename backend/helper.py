
# ------------ Helper functions ------------

MEDIA_TYPES = [
    {
        'endswith': '.gif',
        'mime': 'image/gif',
        'text': 'Bild'
    },{
        'endswith': '.png',
        'mime': 'image/png',
        'text': 'Bild'
    },{
        'endswith': '.jpg',
        'mime': 'image/jpeg',
        'text': 'Bild'
    },{
        'endswith': '.geojson',
        'mime': 'application/vnd.geo+json',
        'text': 'Geodaten'
    },{
        'endswith': '.ipynb',
        'contains': 'jupyter',
        'mime': 'application/ipynb+json',
        'text': 'Notebook'
    },{
        'endswith': 'datapackage.json',
        'mime': 'application/vnd.datapackage+json',
        'text': 'Data Package'
    },{
        'startswith': 'http',
        'mime': 'application/html',
        'text': 'Website'
    }
]

MEDIA_NONE = {
    'mime': 'unknown',
    'text': 'Unbekannt'
}

def media_type(filename, default=None):
    if default is None: default=MEDIA_NONE
    if type(default) is str:
        default = { 'mime':default, 'text':default }
    if filename is None: return default
    for mt in MEDIA_TYPES:
        if 'endswith' in mt and filename.endswith(mt['endswith']):
            return mt
        if 'startswith' in mt and filename.startswith(mt['startswith']):
            return mt
        if 'contains' in mt and mt['contains'] in filename:
            return mt
    for mt in MEDIA_TYPES:
        if default in mt['mime']:
            return mt
    return default

def media_mime(filename, default=None):
    return media_type(filename, default)['mime']

def media_name(filename, default=None):
    return media_type(filename, default)['text']


def features_geojson(name, objs):
    if objs is None:
        return {}
    features = [{'type': 'Feature',
        'geometry': to_shape(o),
        'properties': {'name': name}
    } for o in objs]
    return geojson.dumps(
        {'type': 'FeatureCollection', 'features': features}
    )

def slugify(title):
    return title.lower().strip().replace(' ', '-')
