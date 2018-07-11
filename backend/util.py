
def get_media_type(filename):
    if filename.endswith('.gif'):
        return 'image/gif'
    if filename.endswith('.png'):
        return 'image/png'
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        return 'image/jpeg'
    if filename.endswith('.geojson') or filename.endswith('.json'):
        return 'application/vnd.geo+json'
    if filename.endswith('datapackage.json'):
        return 'application/vnd.datapackage+json'
    if filename.startswith('http'):
        return 'application/html'
    return None

def get_features_geojson(name, objs):
    if objs is None:
        return {}
    features = [{'type': 'Feature',
        'geometry': to_shape(o),
        'properties': {'name': name}
    } for o in objs]
    return geojson.dumps(
        {'type': 'FeatureCollection', 'features': features}
    )
