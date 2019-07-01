var overviewMapControl = new ol.control.OverviewMap({
    // see in overviewmap-custom.html to see the custom CSS used
    className: 'ol-overviewmap ol-custom-overviewmap',
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    collapseLabel: '\u00BB',
    label: '\u00AB',
    collapsed: false
});
var scaleLineControl = new ol.control.ScaleLine();
var map = new ol.Map({
    controls: ol.control.defaults(({ zoom: false })).extend([
        overviewMapControl, scaleLineControl
    ]),
    interactions: ol.interaction.defaults().extend([
        new ol.interaction.DragRotateAndZoom()
    ]),
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    target: 'map',
    view: new ol.View({
        center: [2000000, 6900000],
        zoom: 7
    })
});

debugger

function zoomin() {
    var current = map.getView().getZoom();
    map.getView().setZoom(current + 1);
}

function zoomout() {
    var current = map.getView().getZoom();
    map.getView().setZoom(current - 1);
}

// jQuery(document).ready(function(){
//     jQuery(".data-grid-openar").click(function(){
//         jQuery(".dada-grid").toggleClass("show");
//     });
// });

function showDataGrid() {
    var element = document.getElementById("dada-grid");
    element.classList.toggle("show");
}

jQuery(document).ready(function () {
    // reset modal if it isn't visible
    if (!(jQuery('.modal.in').length)) {
        jQuery('.modal-dialog').css({
            top: 0,
            left: 0
        });
    }
    jQuery('.modal').modal({
        backdrop: false,
        show: false
    });

    jQuery('.modal-dialog').draggable({
        handle: ".modal-header"
    });
});