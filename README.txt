CZO-IML: HOBO stream stage data
===============================

Authors
~~~~~~~
- Tim Hodson (tohodson@illinois.edu)
- Laura Keefer (lkeefer@illinois.edu)

Revision: 0.1
Dataset Location: Sangamon Watershed, Illinois
Temporal Coverage: 2014 - 2017

Data overview
~~~~~~~~~~~~~
This dataset contains stage records from HOBO Water Level Loggers deployed at number of sites along the Sangamon Watershed.

|   Sites                      | Atmospheric Station | Offset       | Lat       | Lon        |
----------------------------------------------------------------------------------------------
| Saybrook                     | Saybrook            | 3.2734       | 40.437239 | -88.554944 |
| Big Ditch                    | Saybrook            | 1.3          | 40.280303 | -88.346718 |          
| Wildcat                      | Saybrook            | 5.835        | 40.280303 | -88.346718 |
| Camp Creek                   | Bucks Pond Rd       | 5.03         | 40.054329 | -88.531266 |
| Goose Creek @ Bucks Pond Rd  | Bucks Pond Rd       | 4.489 (4.276)| 40.054299 | -88.582921 |
| Goose Creek @ CR 600         | Bucks Pond Rd       | 4.2757       | 40.094392 | -88.630968 |
----------------------------------------------------------------------------------------------

Methods
~~~~~~~
HOBO Water Level Loggers measure absolute pressure, which is the combination of the weight of the water above the sensore
and the atmospheric pressure acting on the water surface. To convert absolute pressure to water pressure, the atmospheric
component is subtracted using parallel measurements from a nearby station. In this case, the stations are HOBO loggers
placed within a few meters above the local water table. CZO has two such barometric loggers: one at Saybrook and another
at Bucks Pond.  Files collected by these HOBOS are given an 'atm' suffix, whereas water level HOBOS have the 'h2o' suffix.

After removing atmospheric pressure, water pressure is converted to depth by:

                     h = P/ (rho * g)

where h is depth, P is corrected water pressure, g is the acceleration due to gravity, and rho is the density of water 
approximated by:

                     rho = 1 g/cm^3                                        #TODO FIND A TEMPERATURE BASED FORMULA

where T_w is the water temperature in C.

Finally water depth is converted to stage by:

                     stage (m) = 100 - offset + depth 

where offsets are listed in the table above.


Other Notes
~~~~~~~~~~~
1. A median filter (kernel width = 5 samples) was applied to help remove spikes that occur during while the sensor is out
of the water during deployment and recovery. Any remaining spikes were cleaned manually. 

2. During, 2014 and 2015 the atmospheric logger at Bucks Pond malfunctioned and the missing record was filled
using the record from Saybrook by calculating a linear fit between the two sites using the 2016 data:
                P_goosecreek = 1.044 * P_saybrook - 3.897

3. After 2015, the water level logger at Bucks Pond was moved 20m downstream. New offset shown in (). 
