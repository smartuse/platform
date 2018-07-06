
def get_media_type(fmt):
    if fmt == 'png': return 'image/png'
    if fmt == 'jpg': return 'image/jpeg'
    if fmt == 'geojson': return 'application/vnd.geo+json'
    if fmt == 'datapackage': return 'application/vnd.datapackage+json'
    if fmt == 'embed': return 'application/html'
    return fmt

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
