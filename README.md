# staePark
Smart Parking Prototype

## Parking Stall Data Specification

The following provides the working fields for the Parking Stall data types. All data needs to be in JSON with location data encoded in [GeoJSON](http://geojson.org/). 

### Parking Stall Data Types
The fields marked with an asterisk are already populated when you create the data source for your parking space in Stae. 

| Field | Data type | Description | Validation | Example
| ---   | --- 		| ---         | ---		   | ---
|id*    | Text      | Includes data on whether a parking stall is occupied or not. | Not empty | "Parking Stalls"
|name*  | Text      | Descriptive name of the parking to be monitored. | Not empty | "Parking Stall"
|notes* | Text 		| Description or further notes about the parking stalls. | Not empty | "Real-time Data from Flatiron"
|stall number   | Number      | Stall number in a parking structure. |  Not empty | "10"
|status   | Text      | Status of Parking Stall. |  enumeration: open, closed | "Open"
|parking_structure_name | Text 	| Name of Parking Structure | Not empty | "GCT Parking Structure"
|type| Text | Type of parking space | enumeration: general, compact, handicap, motorcycle  | "general"
|images | Array 	| List of images related to the building or location in the building | Not empty, max character length: 2048 | [https://stae.co/park1.jpg, https://stae.co/park2.jpg]
|location_point | Point 	| Location of where the Parking Stall exists. | GEOJSON format | {"type": "Point", "coordinates": [-74.0429, 40.744]}
