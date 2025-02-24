$('#tree-container').jstree({
  core : {
    data: function(node, callback) {
      const url = "{% url 'locations_api:location-list' %}?parent_key" + (node.id === '#' ? '__isnull=True' : '=' + node.id)
      $.ajax({
        url: url
      }).done(function(data) {
        let nodeData = [];
        data.results.forEach(location => {
          location.names.forEach(name => {
            if (name.preferred) {
              nodeData.push({id: location.location_key, text: name.item_name, children: true});
            }
          });

        });
        callback(nodeData);
      });
    },
  },
  types : {
    'default' : {
        'icon' : 'far fa-folder'
    },
    'open' : {
        'icon' : 'far fa-folder-open'
    },
    'closed' : {
        'icon' : 'far fa-folder'
    }
  },
  "plugins" : [ "types" ]
});

$('#tree-container')
  // listen for event
  .on('select_node.jstree', function (e, data) {
    $.ajax({
      url: "/locations/" + data.node.id,
      success : function(data) {
        $('#selection-pane').html(data);
        const point = [$('#map-long').val(), $('#map-lat').val()];
        const marker = new ol.Feature(new ol.geom.Point(ol.proj.fromLonLat(point)));
        const view = recorder.map.getView();
        recorder.markerLayer.getSource().addFeature(marker);
        view.setCenter(ol.proj.fromLonLat(point));
        view.setZoom(9);
      }
    });
  });