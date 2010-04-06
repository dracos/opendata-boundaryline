function init(wkt_url) {
    var map = new OpenLayers.Map('map', {
        controls: [
            new OpenLayers.Control.Navigation(),
            new OpenLayers.Control.PanZoom()
        ]
    });

    var osm = new OpenLayers.Layer.OSM.Mapnik('OpenStreetMap');
    map.addLayer(osm);

    /* There appears to be a bug in OpenLayers.Strategy.Fixed when the server
     * returns just one feature. So just do it manually for the mo */
    var http = new OpenLayers.Protocol.HTTP({
        url: wkt_url,
        format: new OpenLayers.Format.WKT(),
        callback: function(r) {
            var layer = new OpenLayers.Layer.Vector("Council");
            layer.addFeatures(r.features);
            map.addLayer(layer);
            b = new OpenLayers.Bounds();
            if (r.features.length) {
                for (var i=0; i<r.features.length; i++) {
                    b.extend(r.features[i].geometry.getBounds());
                }
            } else {
                b.extend(r.features.geometry.getBounds());
            }
            map.zoomToExtent(b);
        }
    });
    http.read();
}

