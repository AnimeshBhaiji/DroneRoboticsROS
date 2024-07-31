
"use strict";

let KeyValue = require('./KeyValue.js');
let GeoPoint = require('./GeoPoint.js');
let GeoPointStamped = require('./GeoPointStamped.js');
let RouteNetwork = require('./RouteNetwork.js');
let GeoPose = require('./GeoPose.js');
let GeographicMap = require('./GeographicMap.js');
let RouteSegment = require('./RouteSegment.js');
let BoundingBox = require('./BoundingBox.js');
let RoutePath = require('./RoutePath.js');
let GeoPoseWithCovariance = require('./GeoPoseWithCovariance.js');
let WayPoint = require('./WayPoint.js');
let GeoPoseWithCovarianceStamped = require('./GeoPoseWithCovarianceStamped.js');
let GeoPoseStamped = require('./GeoPoseStamped.js');
let GeoPath = require('./GeoPath.js');
let MapFeature = require('./MapFeature.js');
let GeographicMapChanges = require('./GeographicMapChanges.js');

module.exports = {
  KeyValue: KeyValue,
  GeoPoint: GeoPoint,
  GeoPointStamped: GeoPointStamped,
  RouteNetwork: RouteNetwork,
  GeoPose: GeoPose,
  GeographicMap: GeographicMap,
  RouteSegment: RouteSegment,
  BoundingBox: BoundingBox,
  RoutePath: RoutePath,
  GeoPoseWithCovariance: GeoPoseWithCovariance,
  WayPoint: WayPoint,
  GeoPoseWithCovarianceStamped: GeoPoseWithCovarianceStamped,
  GeoPoseStamped: GeoPoseStamped,
  GeoPath: GeoPath,
  MapFeature: MapFeature,
  GeographicMapChanges: GeographicMapChanges,
};
