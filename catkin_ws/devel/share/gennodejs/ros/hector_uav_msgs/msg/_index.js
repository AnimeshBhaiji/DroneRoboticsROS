
"use strict";

let AttitudeCommand = require('./AttitudeCommand.js');
let MotorPWM = require('./MotorPWM.js');
let HeightCommand = require('./HeightCommand.js');
let RuddersCommand = require('./RuddersCommand.js');
let RC = require('./RC.js');
let YawrateCommand = require('./YawrateCommand.js');
let MotorCommand = require('./MotorCommand.js');
let Compass = require('./Compass.js');
let ServoCommand = require('./ServoCommand.js');
let VelocityXYCommand = require('./VelocityXYCommand.js');
let VelocityZCommand = require('./VelocityZCommand.js');
let RawRC = require('./RawRC.js');
let PositionXYCommand = require('./PositionXYCommand.js');
let RawImu = require('./RawImu.js');
let ControllerState = require('./ControllerState.js');
let ThrustCommand = require('./ThrustCommand.js');
let RawMagnetic = require('./RawMagnetic.js');
let Altimeter = require('./Altimeter.js');
let HeadingCommand = require('./HeadingCommand.js');
let Supply = require('./Supply.js');
let MotorStatus = require('./MotorStatus.js');

module.exports = {
  AttitudeCommand: AttitudeCommand,
  MotorPWM: MotorPWM,
  HeightCommand: HeightCommand,
  RuddersCommand: RuddersCommand,
  RC: RC,
  YawrateCommand: YawrateCommand,
  MotorCommand: MotorCommand,
  Compass: Compass,
  ServoCommand: ServoCommand,
  VelocityXYCommand: VelocityXYCommand,
  VelocityZCommand: VelocityZCommand,
  RawRC: RawRC,
  PositionXYCommand: PositionXYCommand,
  RawImu: RawImu,
  ControllerState: ControllerState,
  ThrustCommand: ThrustCommand,
  RawMagnetic: RawMagnetic,
  Altimeter: Altimeter,
  HeadingCommand: HeadingCommand,
  Supply: Supply,
  MotorStatus: MotorStatus,
};
