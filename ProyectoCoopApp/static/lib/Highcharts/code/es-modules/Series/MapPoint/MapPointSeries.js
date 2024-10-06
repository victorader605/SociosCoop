/* *
 *
 *  (c) 2010-2024 Torstein Honsi
 *
 *  License: www.highcharts.com/license
 *
 *  !!!!!!! SOURCE GETS TRANSPILED BY TYPESCRIPT. EDIT TS FILE ONLY. !!!!!!!
 *
 * */
'use strict';
import H from '../../Core/Globals.js';
const { noop } = H;
import MapPointPoint from './MapPointPoint.js';
import MapPointSeriesDefaults from './MapPointSeriesDefaults.js';
import SeriesRegistry from '../../Core/Series/SeriesRegistry.js';
const { map: MapSeries, scatter: ScatterSeries } = SeriesRegistry.seriesTypes;
import SVGRenderer from '../../Core/Renderer/SVG/SVGRenderer.js';
import U from '../../Core/Utilities.js';
const { extend, fireEvent, isNumber, merge } = U;
import '../../Core/Defaults.js';
import '../Scatter/ScatterSeries.js';
/* *
 *
 *  Class
 *
 * */
/**
 * @private
 * @class
 * @name Highcharts.seriesTypes.mappoint
 *
 * @augments Highcharts.Series
 */
class MapPointSeries extends ScatterSeries {
    constructor() {
        /* *
         *
         *  Static Properties
         *
         * */
        super(...arguments);
        this.clearBounds = MapSeries.prototype.clearBounds;
        /* eslint-enable valid-jsdoc */
    }
    /* *
     *
     *  Functions
     *
     * */
    /* eslint-disable valid-jsdoc */
    drawDataLabels() {
        super.drawDataLabels();
        if (this.dataLabelsGroup) {
            this.dataLabelsGroup.clip(this.chart.clipRect);
        }
    }
    /**
     * Resolve `lon`, `lat` or `geometry` options and project the resulted
     * coordinates.
     *
     * @private
     */
    projectPoint(pointOptions) {
        const mapView = this.chart.mapView;
        if (mapView) {
            const { geometry, lon, lat } = pointOptions;
            let coordinates = (geometry &&
                geometry.type === 'Point' &&
                geometry.coordinates);
            if (isNumber(lon) && isNumber(lat)) {
                coordinates = [lon, lat];
            }
            if (coordinates) {
                return mapView.lonLatToProjectedUnits({
                    lon: coordinates[0],
                    lat: coordinates[1]
                });
            }
        }
    }
    translate() {
        const mapView = this.chart.mapView;
        if (!this.processedXData) {
            this.processData();
        }
        this.generatePoints();
        if (this.getProjectedBounds && this.isDirtyData) {
            delete this.bounds;
            this.getProjectedBounds(); // Added point needs bounds(#16598)
        }
        // Create map based translation
        if (mapView) {
            const mainSvgTransform = mapView.getSVGTransform(), { hasCoordinates } = mapView.projection;
            this.points.forEach((p) => {
                let { x = void 0, y = void 0 } = p;
                const svgTransform = (isNumber(p.insetIndex) &&
                    mapView.insets[p.insetIndex].getSVGTransform()) || mainSvgTransform;
                const xy = (this.projectPoint(p.options) ||
                    (p.properties &&
                        this.projectPoint(p.properties)));
                let didBounds;
                if (xy) {
                    x = xy.x;
                    y = xy.y;
                    // Map bubbles getting geometry from shape
                }
                else if (p.bounds) {
                    x = p.bounds.midX;
                    y = p.bounds.midY;
                    if (svgTransform && isNumber(x) && isNumber(y)) {
                        p.plotX = x * svgTransform.scaleX +
                            svgTransform.translateX;
                        p.plotY = y * svgTransform.scaleY +
                            svgTransform.translateY;
                        didBounds = true;
                    }
                }
                if (isNumber(x) && isNumber(y)) {
                    // Establish plotX and plotY
                    if (!didBounds) {
                        const plotCoords = mapView.projectedUnitsToPixels({ x, y });
                        p.plotX = plotCoords.x;
                        p.plotY = hasCoordinates ?
                            plotCoords.y :
                            this.chart.plotHeight - plotCoords.y;
                    }
                }
                else {
                    p.y = p.plotX = p.plotY = void 0;
                }
                p.isInside = this.isPointInside(p);
                // Find point zone
                p.zone = this.zones.length ? p.getZone() : void 0;
            });
        }
        fireEvent(this, 'afterTranslate');
    }
}
MapPointSeries.defaultOptions = merge(ScatterSeries.defaultOptions, MapPointSeriesDefaults);
/* *
 *
 * Extra
 *
 * */
/* *
 * The mapmarker symbol
 */
const mapmarker = (x, y, w, h, options) => {
    const isLegendSymbol = options && options.context === 'legend';
    let anchorX, anchorY;
    if (isLegendSymbol) {
        anchorX = x + w / 2;
        anchorY = y + h;
        // Put the pin in the anchor position (dataLabel.shape)
    }
    else if (options &&
        typeof options.anchorX === 'number' &&
        typeof options.anchorY === 'number') {
        anchorX = options.anchorX;
        anchorY = options.anchorY;
        // Put the pin in the center and shift upwards (point.marker.symbol)
    }
    else {
        anchorX = x + w / 2;
        anchorY = y + h / 2;
        y -= h;
    }
    const r = isLegendSymbol ? h / 3 : h / 2;
    return [
        ['M', anchorX, anchorY],
        ['C', anchorX, anchorY, anchorX - r, y + r * 1.5, anchorX - r, y + r],
        // A rx ry x-axis-rotation large-arc-flag sweep-flag x y
        ['A', r, r, 1, 1, 1, anchorX + r, y + r],
        ['C', anchorX + r, y + r * 1.5, anchorX, anchorY, anchorX, anchorY],
        ['Z']
    ];
};
SVGRenderer.prototype.symbols.mapmarker = mapmarker;
extend(MapPointSeries.prototype, {
    type: 'mappoint',
    axisTypes: ['colorAxis'],
    forceDL: true,
    isCartesian: false,
    pointClass: MapPointPoint,
    searchPoint: noop,
    useMapGeometry: true // #16534
});
SeriesRegistry.registerSeriesType('mappoint', MapPointSeries);
/* *
 *
 *  Default Export
 *
 * */
export default MapPointSeries;
/* *
 *
 *  API Options
 *
 * */
''; // Adds doclets above to transpiled file
