## IC Compiler™ II   Graphical User Interface User Guide

Version X-2025.06-SP1, August 2025

<!-- image -->

## Copyright and Proprietary Information Notice

© 2025 Synopsys, Inc. This Synopsys software and all associated documentation are proprietary to Synopsys, Inc. and may only be used pursuant to the terms and conditions of a written license agreement with Synopsys, Inc. All other use, reproduction, modification, or distribution of the Synopsys software or the associated documentation is strictly prohibited.

## Destination Control Statement

All technical data contained in this publication is subject to the export control laws of the United States of America. Disclosure to nationals of other countries contrary to United States law is prohibited. It is the reader's responsibility to determine the applicable regulations and to comply with them.

## Disclaimer

SYNOPSYS, INC., AND ITS LICENSORS MAKE NO WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, WITH REGARD TO THIS MATERIAL, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

## Trademarks

https://www.synopsys.com/company/legal/trademarks-brands.html. All other product or company names may be trademarks of their respective owners.

Synopsys and certain Synopsys product names are trademarks of Synopsys, as set forth at

## Free and Open-Source Licensing Notices

If applicable, Free and Open-Source Software (FOSS) licensing notices are available in the product installation.

## Third-Party Links

Any links to third-party websites included in this document are for your convenience only. Synopsys does not endorse and is not responsible for such websites and their practices, including privacy practices, availability, and content.

[www.synopsys.com](https://www.synopsys.com/)

## Contents

|    | New in This Release . . . . . . . . . . . . . . . . . . . . . . . . . .       | .12   |
|----|-------------------------------------------------------------------------------|-------|
|    | Related Products, Publications, and Trademarks . . . .                        | .13   |
|    | Conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | .13   |
|    | Customer Support . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . 14  |
| 1. | Getting Started With the GUI . . . . . . . . . . . . . . . . . .              | . 15  |
|    | Starting the GUI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . 16  |
|    | Closing the GUI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | .17   |
|    | Exiting the Tool From the GUI . . . . . . . . . . . . . . . . . . .           | . 18  |
|    | Running the GUI in Batch Mode Without an X Server                             | . 18  |
|    | Determining Whether the GUI is Running in a Script .                          | .19   |
|    | Using GUI Windows . . . . . . . . . . . . . . . . . . . . . . . . . . .       | . 20  |
|    | Menu Bar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | 21    |
|    | Toolbars . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    | .21   |
|    | Status Bar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . 21  |
|    | View Windows . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | .22   |
|    | Panels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    | . 23  |
|    | Capturing a Screenshot of the Tool Window . . . . . . . .                     | . 23  |
|    | Working With Image View Window . . . . . . . . . . . .                        | 24    |
|    | Working With the Console . . . . . . . . . . . . . . . . . . . . . .          | . 26  |
|    | Viewing the Session Log . . . . . . . . . . . . . . . . . . . .               | . 27  |
|    | Viewing the History View . . . . . . . . . . . . . . . . . . . .              | . 29  |
|    | Setting Application Preferences . . . . . . . . . . . . . . . . . .           | . 30  |
|    | Using Command Search . . . . . . . . . . . . . . . . . . . . . . .            | .32   |
|    | Using the Command Dialog . . . . . . . . . . . . . . . . .                    | . 34  |
|    | Using Topic Search . . . . . . . . . . . . . . . . . . . . . . . . . . .      | .36   |
|    | Viewing the Tip of the Day . . . . . . . . . . . . . . . . . . . . .          | . 39  |
|    | Creating Reference Methodology Scripts . . . . . . . . . .                    | . 39  |
|    | Viewing and Editing Application Options . . . . . . . . . . .                 | . 39  |
|    | Viewing Application Options . . . . . . . . . . . . . . . . .                 | . 40  |
|    | Editing Application Options . . . . . . . . . . . . . . . . . .               | .42   |

<!-- image -->

## Contents

2.

<!-- image -->

| Working in the Block Window . . . . . . . . . . . . . . . . . . . . . . .         | .43    |
|-----------------------------------------------------------------------------------|--------|
| Changing the View of the Physical Design . . . . . . . . . . . . .                | . .43  |
| Setting and Saving View Properties . . . . . . . . . . . . . . .                  | .44    |
| Saving and Restoring View Settings . . . . . . . . . . .                          | . 48   |
| Applying Predefined View Settings . . . . . . . . . . . . .                       | . 48   |
| Displaying Grid Lines in a Layout View . . . . . . . . . . . .                    | . 50   |
| Drawing Timing Rulers in a Layout View . . . . . . . . . . .                      | . 50   |
| Drawing Physical Rulers in a Layout View . . . . . . . . . .                      | . .51  |
| Drawing Circular Rulers . . . . . . . . . . . . . . . . . . . . . . . .           | . 53   |
| Using Strokes to Activate Commands . . . . . . . . . . . . .                      | . 53   |
| Editing the Physical Layout . . . . . . . . . . . . . . . . . . . . . . . . .     | . .55  |
| Editing Objects Interactively . . . . . . . . . . . . . . . . . . . . .           | . 57   |
| Moving, Modifying, Creating, and Removing Objects                                 | . 58 . |
| Expanding and Rotating Objects . . . . . . . . . . . . . .                        | 60     |
| Working in the Editing Environment . . . . . . . . . . . . . . .                  | .61    |
| Using the Editor Toolbox . . . . . . . . . . . . . . . . . . . . . . . .          | . 61   |
| Using the Edit in Place Functionality . . . . . . . . . . . . . .                 | . 66   |
| Viewing Metal Fill Data . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . 71   |
| Using Toolbars and the Selection List . . . . . . . . . . . . . .                 | . 72   |
| Using the Query Tool . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . 72   |
| Using the Customize Query Toolbar . . . . . . . . . . . . . . .                   | . 74   |
| Using the Attribute Group Manager . . . . . . . . . . . . . . .                   | . 75   |
| Using the Attribute Group Editor . . . . . . . . . . . . . . . . . .              | . 76   |
| Using the Recent Menu Button . . . . . . . . . . . . . . . . . . . . . .          | . .76  |
| Using the Script Editor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 77   |
| Using the Select By Name Toolbar . . . . . . . . . . . . . . . . . . .            | . .78  |
| Entering Search Terms for Multiple Objects . . . . . . . . .                      | . .79  |
| Searching by Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . .       | . 80   |
| Using the Overview Toolbar . . . . . . . . . . . . . . . . . . . . . . . . .      | . 81   |
| Using the Selection List and Work List . . . . . . . . . . . . . . . .            | . .83  |
| Using User Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | .85    |
| Creating a User Table . . . . . . . . . . . . . . . . . . . . . . . . . .         | . .86  |
| Saving and Reloading a User Table . . . . . . . . . . . . . . .                   | . .87  |
| Analyzing Data in a User Table . . . . . . . . . . . . . . . . . .                | . 87   |
| Creating a Report Summary . . . . . . . . . . . . . . . . . . . . .               | . .88  |

## Contents

|    | Automatically Selecting Objects in a User Table . . . . . . . . . . . . . . . .        | . . 88   |
|----|----------------------------------------------------------------------------------------|----------|
|    | Improved Bus Compression . . . . . . . . . . . . . . . . . .                           | . . 89   |
|    | Viewing the Data as a Chart or Plot . . . . . . . . . . . . . . . . . .                | . 91     |
| 3. | Using UPF and Power Analysis Tools . . . . . . . . . . . . . . . . . .                 | . 93     |
|    | Viewing the UPF Power Intent . . . . . . . . . . . . . . . . . . . . . . . . . .       | . . 93   |
|    | Viewing the Power State Table . . . . . . . . . . . . . . . . . . . . . . . . . .      | . .96    |
| 4. | Using GUI Assistant Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . .98    |
|    | Using the Task Assistant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . .98    |
|    | Starting the Tasks Toolbar and Task Assistant . . . . . . . . . . .                    | . .98    |
|    | Navigating the Tasks in the Task Assistant Dialog Box . . . .                          | . . 99   |
|    | Previewing, Capturing, and Issuing Commands . . . . . . . . . .                        | .101     |
|    | Using Overview Pages . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . 102    |
|    | Editing Data in Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | .102     |
|    | Using the Design Assistant . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | .103     |
|    | Listing and Selecting Objects . . . . . . . . . . . . . . . . . . . . . . . .          | .104     |
|    | Selecting Objects Using the Select Menu . . . . . . . . . . . . . .                    | 105      |
|    | Configuring Columns in the Design Assistant . . . . . . . . . . .                      | 105      |
|    | Changing Property Settings for Multiple Objects . . . . . . . . .                      | . 108    |
|    | Applying the Changes Automatically . . . . . . . . . . . . . . . . . .                 | 109      |
|    | Synchronizing the Selection With the Global Selection . . . .                          | . 110    |
|    | Performing Related Tasks . . . . . . . . . . . . . . . . . . . . . . . . . .           | .111     |
|    | Using the Constraints Editor . . . . . . . . . . . . . . . . . . . . . . . . .         | .112     |
|    | Highlighting Objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | 114      |
|    | Reading and Writing Object Selection Scripts . . . . . . . . . . .                     | . 114    |
|    | Setting Constraints With the Relative Location Constraints Tool                        | 115      |
|    | Manually Creating Relative Location Constraints . . . . . . . . .                      | .115     |
|    | Automatically Creating Relative Location Constraints . . . . .                         | . 116    |
|    | Placing Macros Using Relative Location Constraints . . . . . .                         | .117     |
|    | Removing Relative Location Constraints . . . . . . . . . . . . . . .                   | . 117    |
|    | Writing Out Relative Location Constraints . . . . . . . . . . . . . .                  | . 117    |
|    | Writing Out Port Relative Location Constraints . . . . . . . . . .                     | 118      |
|    | Reading In Relative Location Constraints . . . . . . . . . . . . . .                   | 118      |
|    | Changing the Color of the Constraint Flylines . . . . . . . . . . .                    | . 119    |
|    | Using the Netlist Tracer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 119      |

<!-- image -->

## Contents

|    | Using the Track Assistant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | . 119   |
|----|---------------------------------------------------------------------------------------------|---------|
|    | Displaying Tracks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       | . 121   |
|    | Displaying Track Information in Specific Regions . . . . . . . . . .                        | 121     |
|    | Displaying Obstructed or Unobstructed Tracks . . . . . . . . . . . .                        | 123     |
|    | Setting Track Assistant Options . . . . . . . . . . . . . . . . . . . . . . .               | . 124   |
| 5. | Using Design Planning Tools . . . . . . . . . . . . . . . . . . . . . . . . . . .           | .125    |
|    | Hierarchy Browser . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | .125    |
|    | Filtering Information in the Hierarchy Browser . . . . . . . . . . . .                      | .129    |
|    | Name Based Hierarchy Browser . . . . . . . . . . . . . . . . . . . . . . . . . .            | .131    |
|    | What-if Channel Congestion . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | . 133   |
|    | Performing Global Routing for What-if Channel Congestion .                                  | 134     |
|    | Viewing Congestion Information . . . . . . . . . . . . . . . . . . . . . . .                | .134    |
|    | Filtering by Minimum Channel Dimension . . . . . . . . . . . . . . .                        | 135     |
|    | Displaying Channel Segments . . . . . . . . . . . . . . . . . . . . . . . .                 | . 136   |
|    | Specifying the Region for Analysis . . . . . . . . . . . . . . . . . . . . .                | .136    |
|    | Scaling the Congestion Color Mapping . . . . . . . . . . . . . . . . .                      | 136     |
|    | Correcting Congestion Problems . . . . . . . . . . . . . . . . . . . . . .                  | . 137   |
|    | Updating the Placement . . . . . . . . . . . . . . . . . . . . . . .                        | .138    |
|    | . . . Showing Nets in a Channel . . . . . . . . . . . . . . . . . .                         | . 138   |
|    | . . . . . Removing the Congestion Map . . . . . . . . . . . . . . . . . . . .               | . 139   |
|    | Hierarchy Exploration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 139     |
|    | Creating Module Boundaries . . . . . . . . . . . . . . . . . . . . . . . . . .              | 139     |
|    | Expanding, Collapsing, and Removing Module Boundaries . .                                   | .141    |
|    | Coloring Module Boundaries . . . . . . . . . . . . . . . . . . . . . . . . . .              | 141     |
|    | Placing Module Boundaries . . . . . . . . . . . . . . . . . . . . . . . . . .               | 141     |
|    | Hierarchy Exploration and Module Color . . . . . . . . . . . . . . . .                      | . 142   |
|    | What-if Partitioning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . 144   |
|    | Topological Pin Constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | .146    |
|    | Working With Pin Constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | . 147   |
|    | Performing Topology Interconnect Planning . . . . . . . . . . . . . . . . .                 | . 148   |
|    | Using the Topology Toolbox . . . . . . . . . . . . . . . . . . . . . . . . . .              | . 149   |
|    | Customizing the Topology Toolbox . . . . . . . . . . . . . . . . . .                        | 151     |
|    | Using the Create Topology Layout Tool . . . . . . . . . . . . . . . . .                     | . 151   |
|    | Using Custom Symbols to Represent Topology Nodes . . . . .                                  | . 154   |
|    | Using the Move Topology Object Tool . . . . . . . . . . . . . . . . . .                     | . 155   |
|    | Attaching Topology Nodes With Valid Overlapped Objects . .                                  | 156     |

<!-- image -->

## Contents

|    | Daisy Chaining Topology Nodes . . . . . . . . . . . . . . . . . . . . . . . . . .                                 | 157   |
|----|-------------------------------------------------------------------------------------------------------------------|-------|
|    | Setting Topology Edge Shape Layers . . . . . . . . . . . . . . . . . . . . . .                                    | . 158 |
|    | Working With Topology Groups and Topology Plans . . . . . . . . . . .                                             | . 159 |
|    | Setting the Current Topology Group . . . . . . . . . . . . . . . . . . . .                                        | . 162 |
|    | Removing Topology Groups . . . . . . . . . . . . . . . . . . . . . . . . . . .                                    | .162  |
|    | Viewing and Editing Aggregate Attributes of Topology Groups . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 162 |
|    | Uniquifying Topology Plans                                                                                        | . 164 |
|    | Automatically Select Topology Plans . . . . . . . . . . . . . . . . . . . . . .                                   | . 164 |
|    | Merging Stacked Topology Nodes . . . . . . . . . . . . . . . . . . . .                                            | . 165 |
|    | Working With Bundle Objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             | .165  |
|    | Viewing Estimate Topology Timing Results in GUI . . . . . . . . . . . .                                           | 167   |
| 6. | Using Flyline Analysis Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                        | . 169 |
|    | Net Connections Flylines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | 169   |
|    | Flyline Display Modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                       | .171  |
|    | Setting Flyline Display Options . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           | .172  |
|    | Displaying Connections to Route Corridors . . . . . . . . . . . . . . . . . .                                     | . 174 |
|    | Net Connections Explorer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                          | .174  |
|    | Path Analyzer Flylines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | .176  |
|    | Viewing Timing Paths by Number of Connections . . . . . . . . . . . . .                                           | . 178 |
|    | Viewing Timing Paths by Criticality . . . . . . . . . . . . . . . . . . . . . . . .                               | 180   |
|    | Changing the Flyline Display . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                            | . 180 |
|    | Filtering by Design Object and Other Constraints . . . . . . . . . . . . .                                        | . 181 |
|    | Checking Timing Paths Info in Table . . . . . . . . . . . . . . . . . . . . . . .                                 | . 181 |
|    | Path Analyzer Flylines Best Practices . . . . . . . . . . . . . . . . . . . . . .                                 | . 182 |
|    | Data Flow Flylines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | .182  |
|    | Computing Data Flow Flylines . . . . . . . . . . . . . . . . . . . . . . . . . . . .                              | . 184 |
|    | Tracing Flylines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | .184  |
|    | Setting Tracing Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                         | . 184 |
|    | Viewing Flyline Details and Filtering Flylines . . . . . . . . . . . . . . . . .                                  | . 186 |
|    | Data Flow Flylines Pin and Net Filters . . . . . . . . . . . . . . . . . . . . . .                                | .188  |
|    | Using Tcl Commands to Analyze Data Flow Flylines . . . . . . . . . . .                                            | .189  |
|    | Saving and Restoring Data Flow Flylines Connection Data . . . . . .                                               | .190  |
|    | Register Tracing Flylines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | .191  |
|    | Displaying Flylines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     | . 192 |
|    | Clock Trunk Planning Flylines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     | .193  |
|    | Loading Clock Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                        | . 194 |
|    | Changing Clock Trunk Highlighting . . . . . . . . . . . . . . . . . . . . . . . .                                 | . 195 |

<!-- image -->

## Contents

|    | Adding and Removing Clock Trunk Cells . . .                                | .196   |
|----|----------------------------------------------------------------------------|--------|
|    | . . . . Displaying Timing Flylines Between Blocks . .                      | .197   |
| 7. | Using Map and Visual Modes . . . . . . . . . . . . . . . . . .             | . 198  |
|    | Map Mode Overview . . . . . . . . . . . . . . . . . . . . . . . . . .      | .199   |
|    | Configuring the Histogram . . . . . . . . . . . . . . . . . .              | . 202  |
|    | Map Mode Preset . . . . . . . . . . . . . . . . . . . . . . . . .          | . 203  |
|    | Changing the Transparency . . . . . . . . . . . . . . . . .                | . 204  |
|    | Configuring Map Options . . . . . . . . . . . . . . . . . . .              | . 206  |
|    | Global Route Congestion Map . . . . . . . . . . . . . . . . . .            | . 207  |
|    | Refining the Global Route Congestion Map . . . . .                         | .207   |
|    | Congestion Map Calculations . . . . . . . . . . . . . . . .                | .208   |
|    | Examining Cells in Congested Areas . . . . . . . . . .                     | .209   |
|    | Cross-Probing Cells in Congested Areas . . . .                             | . 211  |
|    | Channel Congestion Map . . . . . . . . . . . . . . . . . . . . . .         | . 211  |
|    | Cell, Pin, Block Pin, and Power Density Maps . . . . . .                   | .212   |
|    | Effective Voltage Areas Map . . . . . . . . . . . . . . . . . . . .        | .213   |
|    | Effective Site Arrays Map . . . . . . . . . . . . . . . . . . . . . .      | . 214  |
|    | Wire Utilization Map . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 214  |
|    | Exporting and Importing Map Data . . . . . . . . . . . . . . .             | .216   |
|    | Visual Mode Overview . . . . . . . . . . . . . . . . . . . . . . . . .     | . 223  |
|    | Snapshot Visual Mode . . . . . . . . . . . . . . . . . . . . . . . . .     | . 224  |
|    | Highlight Visual Mode . . . . . . . . . . . . . . . . . . . . . . . . .    | . 225  |
|    | Clock Tree Visual Mode . . . . . . . . . . . . . . . . . . . . . . .       | . 227  |
|    | Tracing Clock Tree . . . . . . . . . . . . . . . . . . . . . . . .         | . 228  |
|    | Examining Clock Tree Overlaps . . . . . . . . . . . . . .                  | .232   |
|    | Viewing User-Defined Skew Groups . . . . . . . . . . .                     | . 233  |
|    | Viewing Full or Partial Clock Tree Graph . . . . . . .                     | .235   |
|    | Scan Chain Visual Mode . . . . . . . . . . . . . . . . . . . . . . .       | . .237 |
|    | Net Connections in Area Visual Mode . . . . . . . . . . . .                | . 239  |
|    | Relative Placement (RP) Groups Visual Mode . . . . . .                     | .242   |
|    | Relative Placement (RP) Net Connection Visual Mode                         | . 243  |
|    | Hierarchy Visual Mode . . . . . . . . . . . . . . . . . . . . . . . . .    | . 245  |
|    | Cell Slack Visual Mode . . . . . . . . . . . . . . . . . . . . . . . .     | .246   |

<!-- image -->

## Contents

|     | Imported Path Pins Visual Mode . . . . . . . . . . . . . . .              | . 248   |
|-----|---------------------------------------------------------------------------|---------|
|     | Voltage Areas Visual Mode . . . . . . . . . . . . . . . . . . . .         | . .249  |
|  8. | Viewing Schematics . . . . . . . . . . . . . . . . . . . . . . . .        | . 251   |
|     | Schematic View . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | .251    |
|     | WordView in the Schematic View . . . . . . . . . . . . . . .              | .252    |
|     | Annotating Attributes on the Schematic View . . . . . .                   | . .255  |
|     | Adding Pin Markers to the Schematic View . . . . . . .                    | . 257   |
|  9. | Timing Analysis Using the GUI . . . . . . . . . . . . . . .               | . 259   |
|     | Opening the Timing Analysis Window . . . . . . . . . . .                  | . 259   |
|     | Displaying the Timing Analysis Endpoint Summary .                         | . 260   |
|     | Creating Path Collections . . . . . . . . . . . . . . . . . . . . .       | . 261   |
|     | Getting Timing Paths . . . . . . . . . . . . . . . . . . . . .            | . 262   |
|     | Saving and Loading Timing Path Data . . . . . . .                         | . .264  |
|     | Analyzing Timing Path Collections . . . . . . . . . . . . . .             | . 264   |
|     | Analyzing Logic Levels . . . . . . . . . . . . . . . . . . . . . . .      | . 266   |
| 10. | Using the Error Browser . . . . . . . . . . . . . . . . . . . .           | . 268   |
|     | Error Browser Overview . . . . . . . . . . . . . . . . . . . . . .        | . 268   |
|     | Loading and Saving Error Data . . . . . . . . . . . . . . . .             | . 270   |
|     | Managing the Error Hierarchy . . . . . . . . . . . . . . . . .            | . .271  |
|     | Managing the Error List and Viewing Error Details .                       | . .271  |
|     | Using Error Filters . . . . . . . . . . . . . . . . . . . . . . . . . . . | .272    |
|     | Highlighting Errors . . . . . . . . . . . . . . . . . . . . . . . . . . . | .273    |
|     | Marking Errors as Fixed and Changing Error Status                         | . 274   |
|     | Writing Out DRC Error Data . . . . . . . . . . . . . . . . . . .          | . 274   |
|     | DRC Error Waiver and Container . . . . . . . . . . . . . . .              | . 276   |
| 11. | Using the Message Browser . . . . . . . . . . . . . . . . .               | . 278   |
|     | Preparing the EMS Database . . . . . . . . . . . . . . . . . .            | .278    |
|     | Message Browser Layout . . . . . . . . . . . . . . . . . . . . .          | . 279   |

<!-- image -->

## Contents

|     | Message Tree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | .279    |
|-----|---------------------------------------------------------------------------------------------------|---------|
|     | Message List . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | .280    |
|     | Detailed Error Message . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . 282   |
|     | Reclassifying a Message . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . 283   |
|     | Creating a Waiver . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . 283   |
|     | Merging EMS Databases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . 286   |
| 12. | Creating Charts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . 287   |
|     | Creating a Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    | .287    |
|     | Checking the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . 289   |
|     | Adding or Deleting Data From the Model . . . . . . . . . . . . . . . . .                          | .290    |
|     | Creating a Plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 291   |
| 13. | Using the PG Pattern Viewer . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . 294   |
|     | Selecting a PG Pattern Template . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . 295   |
|     | Previewing a Template PG Pattern . . . . . . . . . . . . . . . . . . . . . . . . .                | .298    |
|     | Previewing Existing Pattern and Strategy Definitions . . . . . . . . . . . .                      | .299    |
|     | Highlighting Individual Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | .300    |
| 14. | Creating Routes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | .302    |
|     | Creating Routes Interactively . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . 302   |
|     | Performing Interactive Design Rule Checking on Routes . . . . . . . .                             | .315    |
|     | Diagnosing Design Rule Violations Using the Editor DRC tool .                                     | . 315   |
|     | Verifying Route Edits Interactively . . . . . . . . . . . . . . . . . . . .                       | . 316   |
|     | Verifying Edited Nets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | . 316   |
|     | Setting Editor DRC Options . . . . . . . . . . . . . . . . . . . . . . . . .                      | . 316 . |
|     | Examining Errors Reported by Editor DRC . . . . . . . . . . . . .                                 | 317     |
|     | Creating Route Trunks With Tcl Commands or GUI . . . . . . . . . . . . .                          | .318    |
|     | Creating Route Segments in One Direction . . . . . . . . . . . . . . . .                          | .318    |
|     | Creating Route Segments on the Same Track in One Direction                                        | . 322   |
|     | Creating Routes From Pins to Existing Route Segments . . . . .                                    | .326    |
|     | Creating Routes From Pin to Pin . . . . . . . . . . . . . . . . . . . . . . . .                   | . 329   |
|     | Creating Routes From Topology Edges . . . . . . . . . . . . . . . . . . .                         | . 334   |
|     | Routing Area Bounding Box . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | .338    |
|     | Shielding Nets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | .338    |

<!-- image -->

## Contents

|     | Adding Buffers on Routes . . . . . . . . . . . . . . . . . . .          | . .343   |
|-----|-------------------------------------------------------------------------|----------|
|     | Estimating Point-to-Point Resistance . . . . . . . . . .                | . 350    |
| 15. | Creating Anchors . . . . . . . . . . . . . . . . . . . . . . . . .      | . 351    |
| 16. | Creating Cell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 353    |
|     | Creating a Hierarchical Block . . . . . . . . . . . . . . . .           | . . 353  |
| 17. | Creating Persistent Annotations . . . . . . . . . . . .                 | . . 355  |
|     | Creating Annotation Shapes . . . . . . . . . . . . . . . . .            | . . 355  |
|     | Creating Annotation Symbols . . . . . . . . . . . . . . . .             | . . 358  |
|     | Creating Annotation Text . . . . . . . . . . . . . . . . . . . .        | . .362   |
|     | Editing Persistent Annotations . . . . . . . . . . . . . . . .          | . 365    |
|     | Removing Persistent Annotations . . . . . . . . . . . . .               | . .366   |
| 18. | Working With Manufacturing Objects . . . . . . . .                      | . .368   |
|     | Selecting a Manufacturing Object . . . . . . . . . . . . .              | . .369   |
|     | Querying Manufacturing Objects . . . . . . . . . . . . . .              | . .370   |
|     | Viewing the Properties of a Manufacturing Object                        | . . 370  |
|     | Editing a Manufacturing Object . . . . . . . . . . . . . . .            | . .370   |
| 19. | Extending the Graphical User Interface . . . . . .                      | . . 371  |
|     | Creating Menu Items . . . . . . . . . . . . . . . . . . . . . . .       | . .371   |
|     | Creating Toolbars and Toolbar Items . . . . . . . . . .                 | . 374    |
|     | Creating Mouse Palette . . . . . . . . . . . . . . . . . . . . .        | . .378   |
|     | Adding Buttons to the Favorites Palette . . . . . . . .                 | . . 380  |
|     | Highlighting Objects With Tcl Commands . . . . . . .                    | . .380   |
|     | Creating Annotations . . . . . . . . . . . . . . . . . . . . . . .      | . .381   |
|     | Saving Annotations . . . . . . . . . . . . . . . . . . . . . . . .      | . . 385  |
|     | Creating New Visual Modes . . . . . . . . . . . . . . . . .             | . . 387  |

<!-- image -->

## About This User Guide

The Synopsys IC Compiler II tool provides a complete netlist-to-GDSII design solution, which combines proprietary design planning, physical synthesis, clock tree synthesis, and routing for logical and physical design implementations throughout the design flow.

This guide describes the IC Compiler II implementation and integration flow. For more information about the IC Compiler II tool, see the following companion volumes:

- Library Manager User Guide
- IC Compiler II Implementation User Guide
- IC Compiler II Design Planning User Guide
- IC Compiler II Data Model User Guide
- IC Compiler II Timing Analysis User Guide

This user guide is for design engineers who use the IC Compiler II tool to implement designs.

To use the IC Compiler II tool, you need to be skilled in physical design and synthesis and be familiar with the following:

- Physical design principles
- The Linux or UNIX operating system
- The tool command language (Tcl)

This preface includes the following sections:

- New in This Release
- Related Products, Publications, and Trademarks
- Conventions
- Customer Support

## New in This Release

Information about new features, enhancements, and changes, known limitations, and resolved Synopsys Technical Action Requests (STARs) is available in the IC Compiler II Release Notes on the SolvNetPlus site.

<!-- image -->

## Related Products, Publications, and Trademarks

For additional information about the IC Compiler II tool, see the documentation on the Synopsys SolvNetPlus support site at the following address:

[https://solvnetplus.synopsys.com](https://solvnetplus.synopsys.com/)

You might also want to see the documentation for the following related Synopsys products:

- Design Compiler ®
- IC Validator
- PrimeTime ® Suite
- StarRC™

## Conventions

The following conventions are used in Synopsys documentation.

| Convention     | Description                                                                                                                                                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Courier        | Indicates syntax, such as write_file                                                                                                                                  |
| Courier italic | Indicates a user-defined value in syntax, such as write_file design_list                                                                                              |
| Courier bold   | Indicates user input-text you type verbatim-in examples, such as prompt> write_file top                                                                               |
| Purple         | • Within an example, indicates information of special interest. • Within a command-syntax section, indicates a default, such as include_enclosing = true &#124; false |
| [ ]            | Denotes optional arguments in syntax, such as write_file [-format fmt ]                                                                                               |
| ...            | Indicates that arguments can be repeated as many times as needed, such as pin1 pin2 ... pinN .                                                                        |
| &#124;         | Indicates a choice among alternatives, such as low &#124; medium &#124; high                                                                                          |
| \              | Indicates a continuation of a command line.                                                                                                                           |
| /              | Indicates levels of directory structure.                                                                                                                              |

<!-- image -->

<!-- image -->

| Convention   | Description                                                                               |
|--------------|-------------------------------------------------------------------------------------------|
| Bold         | Indicates a graphical user interface (GUI) element that has an action associated with it. |
| Edit > Copy  | Indicates a path to a menu command, such as opening the Edit menu and choosing Copy .     |
| Ctrl+C       | Indicates a keyboard combination, such as holding down the Ctrl key and pressing C.       |

## Customer Support

Customer support is available through SolvNetPlus.

## Accessing SolvNetPlus

The SolvNetPlus site includes a knowledge base of technical articles and answers to frequently asked questions about Synopsys tools. The SolvNetPlus site also gives you access to a wide range of Synopsys online services including software downloads, documentation, and technical support.

To access the SolvNetPlus site, go to the following address:

## [https://solvnetplus.synopsys.com](https://solvnetplus.synopsys.com/)

If prompted, enter your user name and password. If you do not have a Synopsys user name and password, follow the instructions to sign up for an account.

If you need help using the SolvNetPlus site, click REGISTRATION HELP in the top-right menu bar.

## Contacting Customer Support

To contact Customer Support, go to https://solvnetplus.synopsys.com.

1

## Getting Started With the GUI

The IC Compiler II GUI provides a flexible working environment with multiple windows for performing different tasks. The GUI windows operate independently in your X windows environment, but they share the block and global selection data in the tool.

The following topics describe how to work with the GUI:

- Starting the GUI
- Closing the GUI
- Exiting the Tool From the GUI
- Running the GUI in Batch Mode Without an X Server
- Determining Whether the GUI is Running in a Script
- Using GUI Windows
- Capturing a Screenshot of the Tool Window
- Working With the Console
- Setting Application Preferences
- Using Command Search
- Using Topic Search
- Viewing the Tip of the Day
- Creating Reference Methodology Scripts
- Viewing and Editing Application Options
- Working in the Block Window
- Changing the View of the Physical Design
- Editing the Physical Layout
- Viewing Metal Fill Data

<!-- image -->

## Starting the GUI

The IC Compiler II GUI provides both menu commands and a CLI. It is an advanced analysis and physical editing tool. The IC Compiler II tool can perform certain tasks, such as accurately displaying a block and providing visual analysis tools, only from the GUI. The look and feel of the IC Compiler II GUI is consistent with the look and feel of other Synopsys GUIs.

The IC Compiler II GUI uses the DISPLAY environment variable to determine the display location. Before using the GUI, ensure that this variable is set to the name of your UNIX or Linux system display. Make sure the path to the bin directory is included in your PATH variable.

To start the IC Compiler II tool in the GUI mode,

- Enter the icc2\_shell command with the -gui option in a UNIX or Linux shell.
- % icc2\_shell -gui

To start the GUI for the Library Manager tool, use the icc2\_lm\_shell command with the -gui option as follows.

- % icc2\_lm\_shell -gui

You can include other options on the command line when you start the IC Compiler II GUI. For example, you can use

- -help to display a list of all available options
- -f script\_file\_name to execute a script
- -x command to execute an icc2\_shell command

When you start the GUI, the tool

1. Runs the commands in the setup files

The IC Compiler II tool loads the .synopsys\_icc2.setup and .synopsys\_icc2\_gui/ setup.tcl setup files; the Library Manager tool loads the .synopsys\_icc2\_lm.setup and .synopsys\_icc2\_lm\_gui/setup.tcl setup files. The tool first runs the setup files in your home directory followed by the files in the local directory where you ran the icc2\_shell or icc2\_lm\_shell command.

2. Runs the command specified by the -x option or the script specified by the -f option
3. Opens a main window that displays the splash screen

By default, the console appears attached (docked) to the main window above the status bar.

<!-- image -->

<!-- image -->

The IC Compiler II tool performs the same startup tasks when you start the tool in the CLI and open a block.

If you start either tool without the GUI, you can open the GUI by entering the gui\_start command at the command prompt.

```
gui_start
```

To execute a script before opening the GUI, use the -file option. For example,

```
gui_start -file my_gui_setup.tcl
```

If you open a block at the icc2\_shell prompt and then open the GUI, the IC Compiler II tool automatically opens a block window and displays the block in the layout view. If you have multiple blocks open when you open the GUI, the IC Compiler II tool opens a separate block window for each block. The active window (the window that has the mouse focus) is the window with the current block.

The IC Compiler II GUI provides menu commands and dialog boxes for most graphic features, such as viewing, selecting, and highlighting objects in layout views. Menu commands are grouped by function on the menus in each GUI window.

## Closing the GUI

You can open or close the GUI at any time during the session. For example, if you need to conserve system resources, you can close the GUI and continue the session in icc2\_shell or icc2\_lm\_shell.

To close the GUI, do one of the following:

- Choose File &gt; Close GUI in the block window.
- Enter the gui\_stop command.

```
gui_stop
```

When you are ready to use the GUI again, enter the gui\_start command on the command line.

## Exiting the Tool From the GUI

You can end the session and exit the IC Compiler II or Library Manager tool at any time. To exit the tool, enter the exit or quit command or choose File &gt; Exit . Enter the quit! command to exit and ignore any prompts issued by the tool.

When the GUI is open, the tool behavior depends on whether there are unsaved changes to any open block.

- If there are unsaved changes in any open block, the Exit IC Compiler II dialog box or Exit Library Manager dialog box appears, which allows you to save the changes to the modified blocks.
- If there are no unsaved block changes, a message box appears instead of the Exit IC Compiler II dialog box or Exit Library Manager dialog box . If you see this message box, click OK to exit.

## Note:

The tool does not save view settings when you exit. If you have changed view settings for layout or schematic views and want to save them, do so before exiting the tool, as explained in Setting and Saving View Properties.

## Running the GUI in Batch Mode Without an X Server

The tool supports a mode that allows you to run GUI-related commands without running an X server. When you run the icc2\_shell command with the -batch option, the GUI can run in a 'headless' mode that does not require an X server or display window when you specify the -gui option or the start\_gui command. In this mode, you supply Tcl commands to the tool in a script file specified with the -file option or by specifying the commands on the command line with the -x option.

For example, the following script loads a design, creates a screenshot of the layout, and exits the tool:

```
# capture_layout.tcl open_block ./orca:orca.design start_gui gui_write_window_image -file ./layout.png -size {1000 1000} \ -window [gui_get_current_window -types Layout -mru] -format png quit! To run the script in headless mode, specify the -batch option followed by the -f or -x option as shown in the following examples: % icc2_shell -batch -f capture_layout.tcl % icc2_shell -batch -x "source capture_layout.tcl" % icc2_shell -batch \
```

<!-- image -->

<!-- image -->

```
-x 'open_block ./orca:orca.design; start_gui; \ gui_write_window_image -file ./layout.png -format png; \ quit! '
```

Instead of using the -batch option, you can use the following commands and options to run the tool in headless mode:

- Specify the -offscreen 1 option with the gui\_start command.
- Set the gui.batch\_x\_display application option to offscreen .

```
# capture_layout.tcl using gui_start -offscreen 1 open_block ./orca:orca.design start_gui -offscreen 1 gui_write_window_image -file ./layout.png -size {1000 1000} \ -window [gui_get_current_window -types Layout -mru] -format png quit!
```

```
# capture_layout.tcl using gui.batch_x_display offscreen open_block ./orca:orca.design set_app_options -list {gui.batch_x_display offscreen} start_gui gui_write_window_image -file ./layout.png -size {1000 1000} \ -window [gui_get_current_window -types Layout -mru] -format png quit!
```

In each example, the tool runs the commands without displaying a GUI window and does not require a running X server.

## Determining Whether the GUI is Running in a Script

If you are planning to execute commands in the GUI from a script, use the in\_gui\_session application variable to determine if the GUI is active or not. The variable is true when the GUI is active and false when inactive as shown in the following example.

```
icc2_shell> gui_start icc2_shell> get_app_var in_gui_session true icc2_shell> gui_stop To restart the GUI, type 'gui_start'. icc2_shell> get_app_var in_gui_session false
```

## Using GUI Windows

Each top-level GUI window displays design information in view windows and provides menus and dialog boxes (with keyboard shortcuts), toolbars and panels, interactive mouse button tools, a command console (with a command-line interface), and a status bar.

The IC Compiler II GUI provides the following types of windows:

- Block window
- Clock tree analysis window
- Message browser window
- Relative placement (RP) window
- Timing analysis window

Each top-level GUI window is independent of other GUI windows. The title bar displays the product name (IC Compiler II), the window name (BlockWindow.1 for the window that appears when you start the GUI), the current task, and the name of the current library and block. Design objects you select in one window are automatically selected in the other windows.

You can open and close GUI windows, and you can open multiple instances of each window to work with different block settings. Each window instance has a unique name that includes an incremented number.

To open a new instance of a GUI window, choose Window &gt; window-type .

To close a GUI window, choose Window &gt; Close Window in the window you want to close.

## Note:

If you close all the open GUI windows, you end the GUI session but you remain in the icc2\_shell and your blocks remain open. You can reopen the GUI by using the gui\_start command.

You can move, resize, minimize, or maximize GUI windows by using the window management tools on your UNIX or Linux desktop.

The following topics describe the GUI window components:

- Menu Bar
- Toolbars
- Status Bar

<!-- image -->

- View Windows
- Panels

## Menu Bar

The menu bar at the top of a GUI window contains menus with common tasks and commands. You can display a brief message in the status bar about the action that a menu command performs by holding the pointer over the command. For menu commands that can also be used by clicking a toolbar button or pressing a keyboard shortcut, the menus show representations of those alternatives.

## Note:

If a window is not wide enough to display all the menu names on the menu bar, the window displays all the menu names that fit, from left to right, followed by an overflow button ( ). To access the other menus, click the overflow button.

## Toolbars

Each top-level window provides toolbars with buttons you can use to quickly perform frequently used operations or tasks. To determine the function of a toolbar button, hold the pointer over the button. A tooltip displays the name of the button, and the status bar displays a brief description of its use. You cannot disable these messages.

Toolbars are always attached to a window edge. If a window edge is not long enough to display all the toolbars attached to it, the GUI displays the full toolbars that fit and shortened versions of the other toolbars. A shortened toolbar displays an overflow button ( ). To access the other buttons on a shortened toolbar, click the overflow button.

You can move a toolbar to another location by dragging the double bars on one of its sides. You can also disable a toolbar, hiding it from view.

To display or hide a toolbar or panel, choose View &gt; Toolbars &gt; toolbar\_name . A check mark beside the name of a toolbar on the Toolbars menu indicates that the toolbar is visible.

## Status Bar

By default, each GUI window displays a status bar at the bottom of the window. The status bar displays the following information:

- Status information such as the number and type of selected objects
- Information about the action performed by the toolbar button, menu command, or workspace tab under the pointer

<!-- image -->

<!-- image -->

If you hold the pointer over a menu command, a toolbar button, or a tab in the workspace, the status bar displays a brief message about the action that the command, button, or tab performs.

- The relative coordinates of the pointer position over an active layout view (block windows only)

<!-- image -->

To quickly display the list of selected objects in the Selection List dialog box, click the button at the right end of the status bar.

To display or hide the status bar, choose View &gt; Status Bar . A check mark next to the Status Bar command on the View menu indicates that the status bar is visible.

## View Windows

The IC Compiler II tool displays design information in view windows, which are child windows that open within the workspace area of a GUI window. View windows display specific graphic or textual design information.

Most menu commands and toolbar buttons in a GUI window operate in the active view, which is the view window that has the mouse focus. Some view windows contain two or more panes, with a view in each pane. You can drag the split bars between two panes to adjust their relative sizes within the window.

You can resize a view window or move it to another location inside the workspace area of its parent window.

To change the size of a view window,

1. Ensure that the window is restored (it does not take up the entire workspace area).

If the view window is maximized, click the Restore Down button at the far right of the menu bar to restore it.

2. Hold the pointer over an edge or corner of the window until the pointer changes shape.
3. Drag the edge or corner to resize the window.

To move a view window,

1. Move the pointer over the title bar.
2. Drag the window to a different location.

You can organize view windows by tiling them within the workspace area. To tile the view windows in the workspace area, choose Window &gt; Tile Views .

You can also minimize individual view windows, or maximize a view window to fill the workspace area.

<!-- image -->

In most views, you can use navigation keys (the arrow keys, Page Up, Page Down, Home, and End) to scroll through and navigate the view.

## Panels

Panels are enhanced toolbars that open within the workspace area of a top-level window to provide tools or views for performing particular tasks. Most panels are associated with a particular view window and operate on the active view (the view window that has the mouse focus). An exception is the console, which contains a command line and its own views.

Some panels contain tabs that you can click to access different tools or views. The first time that you open a panel during a session, it displays the tools or view for its default tab.

Move a panel to another location on or off the parent window by dragging the double bars on one of its sides. You can also dock a panel (attach it to a window edge) or let it float where you leave it.

Disable a panel to hide it. (A panel that is associated with a particular view is automatically hidden when you close the view window).

To display or hide a toolbar or panel, choose View &gt; Toolbars &gt; panel\_name . A check mark beside the name of a panel on the Toolbars menu indicates that the panel is visible.

## Capturing a Screenshot of the Tool Window

To capture a screenshot of the tool window, you can use the GUI control or run the gui\_write\_window\_image command from the console.

To capture a screenshot using GUI control,

1. Choose File &gt; Save Window Image .
2. In the dialog box that opens, choose a location to save the screenshot.
3. (Optional) Select the Grab screenshot of view window only check box to capture a screenshot of just the current view; for example, the layout view without the whole application window (views, toolbars, palettes, menus, status bar, and so on).
4. Enter a file name.

If you do not provide an extension, by default, the screenshot is saved in PNG format.

5. Click Open.

The screenshot is saved to current directory unless a fully qualified file name is specified.

<!-- image -->

To capture a screenshot using the gui\_write\_window\_image command, run this command on the tool prompt. For example, the following command, captures the currently active window and saves it in a file named my\_file.png.

```
icc2_shell> gui_write_window_image \ -window $view -format png -file my_file.png
```

The supported image formats are PNG, XPM, JPG, IDF, and BMP, which you can specify by using the -format option.

To specify the size of the screen to capture, use the -size option. For example,

```
icc2_shell> gui_write_window_image \ -size {100 100} -file my_file.png
```

If you have multiple windows open, use the -window option to capture a specific window.

To save the image data file (.idf) containing the location and metadata of the image, use the -data\_file option. Use the -report string option to specify a short description of the image data.

To specify extra name value pairs to be added to the data file, use the -data\_values option.

The following example writes an image data file with metadata on map mode with the screenshot of the Layout.1 view referenced by it.

```
icc2_shell> gui_write_window_image -window Layout.1 -data_file 1 \ -data_values {{map_mode congestion}} -report {congestion map}
```

## Working With Image View Window

To display the set of images from the GUI, click View &gt; Image Viewer .

In the dialog box that opens, click the Add button or right-click on the image and choose Images &gt; Add from the context menu option. You can run the gui\_add\_image\_view\_file command on the tool prompt to load the image files. The following example adds the image\_view.idf file to the current image view.

```
icc2_shell> set view [gui_get_current_window -type ImageView] icc2_shell> gui_add_image_view_file -window $view -file image_view.idf
```

To remove an existing image or all images from the image view, right-click on the image and choose Images &gt; Remove Selected / Remove / Remove All from the context menu option. You can run the gui\_remove\_image\_view\_file command on the tool prompt to remove any image file. The following example removes image named image\_view.idf from the current image view.

and gui\_set\_image\_view\_data commands.

<!-- image -->

```
icc2_shell> set view [gui_get_current_window -type ImageView] icc2_shell> gui_remove_image_view_file -window $view -image image_view You can modify or query the view data, from tcl, using the gui_get_image_view_data
```

The following figure identifies the major features of the Image View window. The Image View window shows:

- Images - All images using horizontal, vertical, grid or stacked layout
- Diff - Shows difference between two images
- Movie - Allows user to play animation of multiple (time based) images
- Thumbnails - Shows thumbnails of all images in a horizontal scrolled area
- Data Table - Shows all images and associated data in table with sort and filter support

Figure 1 Image View Window

<!-- image -->

## Working With the Console

The console provides a command-line interface and two views, a log view that displays the session transcript (the default) and a history view that displays the command list. To open the console, choose View &gt; Toolbars &gt; Console from the menu.

You can use the console to

- Enter icc2\_shell commands on the console command line
- View either the session transcript (log view) or the command history list (history view) by clicking the Log or History tab above the command line
- Display an error message man page in the man page viewer by clicking the message number in the console log view

<!-- image -->

- Copy and edit or reuse commands
- Search for, select, and save commands or messages in the log view or the history view

You can enter any icc2\_shell command on the console command line. For example, if you enter get\_selection , the console log view displays a list of the names of all selected objects. When you enter a command on the console command line, make sure the console has the mouse focus.

To enter a command on the console command line,

1. Type the command.
2. Click the icc2\_shell&gt; prompt button or press Enter.

You can open (or close) one console in each top-level window. When the console is open, you can dock it to the bottom or top of its parent window, or move it over or away from the window.

## Viewing the Session Log

Within the Console toolbar, the console log view in the Log tab displays a transcript of session information. The tool records the commands you entered and the tool output and messages resulting from your commands. You can use this information to check on tool status after performing functions, to troubleshoot problems you encounter, and to look up information about past functions. You can reenter commands you have already used by copying them from the log to the icc2\_shell command line.

To view the session transcript, click the Log tab in the console. The console changes to the log view, which is displayed by default whenever the console is opened.

The log view displays the commands you entered at the command prompt. Warnings and error messages are noted with 'Warning' or 'Error' as the first word. If you need to see information not currently displayed in the display area of the log view, use the scroll bars to scroll through the session information.

<!-- image -->

You can view commands in the Options menu by clicking the Options button ( ) on the right side of the console above the command line. Use the Options menu commands to find text in the transcript, copy text in the transcript, and save text from the transcript in a text file.

To find text in the transcript,

1. Click the Options button and choose Find.

The Find Text in Console dialog box appears.

2. Type the text you want to find in the Find box.

<!-- image -->

<!-- image -->

You must type the text exactly as it appears in the transcript, including uppercase and lowercase letters and blank spaces.

3. Search forward in the transcript by clicking Next, or backward by clicking Prev.

The console highlights the next or previous instance of the text. Repeat this step as needed to find additional instances of the text.

To copy text from the transcript to the command line,

1. Select the command or portion of the command that you want to copy.
2. Move your mouse to the command line and click the middle mouse button.

If you already have text on the command line, middle-click where you want to paste the selected information.

To copy text from the transcript that you want to paste somewhere else, such as in a file,

1. Select the text.

To select all the text in the transcript, choose Select All from the Options menu.

2. Choose Copy from the Options menu.

To save text from the transcript in a text file,

1. Do one of the following:
- To save the transcript, choose Save Contents As from the Options menu.
- To save selected text, select the text and choose Save Selection As from the Options menu.
- To save error and warning messages, choose Save Errors/Warnings As from the Options menu.
2. In the dialog box that appears, navigate to the directory where you want to save the file.
3. Enter the file name in the 'File name' box.
4. Click Save .

## Viewing the History View

The console history view lists shell, menu, and stroke commands you have used in the current session. You can do the following with this list:

- Review the commands you have used in this session
- Copy commands in the list
- Save the list to use at a later time

To review the command history for the current session,

- Click the History tab in the command console.

The console displays the list of commands, each with a number showing the order in which you used it.

Use the scroll bars to view information not currently in the display area of the history view. Alternatively, you can enter the history command on the command line. This displays the list of commands in the log view.

To reuse a command listed in the history view, you can do any of the following:

- Double-click the command in the history view.
- Select the command in the view and click either Execute (to immediately rerun the command) or Edit (to paste the command on the command line where you can edit it).
- Enter an exclamation point character followed by the number of the command on the icc2\_shell command line. For example, to reuse the fifth command, use the following command:

<!-- formula-not-decoded -->

You can copy commands in the list that you want to paste somewhere else, such as in a file.

To copy commands in the history list,

1. Select the text.

To select all the text in the transcript, choose Select All from the Options menu.

2. Choose Copy from the Options menu.

<!-- image -->

<!-- image -->

To save the command history list (or a portion of the list) in a text file,

1. (Optional) To save a portion of the list, select the commands you want to save.
2. Do one of the following:
- If you are saving the entire list, click the Save Contents As button or choose Save Contents As from the Options menu.

The Save Contents As dialog box appears.

- If you are saving just a portion of the list, choose Save Selection As from the Options menu.

The Save Selection As dialog box appears.

3. If necessary, navigate to the directory where you want to save the file.
4. Enter the file name in the 'File name' box.
5. Click Save .

You can set options in the Global Settings category of the Application Preferences dialog box to control which types of GUI commands are included in the history list. To open the Application Preferences dialog box, choose View &gt; Preferences .

## Setting Application Preferences

Application preferences are used to set the font, icon size, default colors and color scheme, and other display settings for the GUI. To change the application preferences, choose View &gt; Preferences to open the Application Preferences dialog box.

## Changing Icon Size

To increase the size of the toolbar icons from the default size of 16 point, choose View &gt; Preferences and select the Style Settings entry in the Categories box as shown in Figure 2. In the Icon sizes section, select a larger value in the Large icon size box. Figure 3 shows a toolbar displayed with 16, 24, and 32 point icon sizes.

Figure 2 Application Preferences for Icon Size

<!-- image -->

Figure 3 Toolbars Displayed Using 16, 24, and 32 Point Icons

<!-- image -->

## Selecting a Light or Dark Display Theme

To change the background from the default light gray theme to a dark gray theme, choose View &gt; Preferences &gt; Style Settings and select dark in the Theme box. Figure 4 shows both light and dark themes.

<!-- image -->

Figure 4 Light and Dark Themes

<!-- image -->

## Using Command Search

The IC Compiler II GUI provides a command search feature to quickly locate menu and task actions, shell commands, and application options.

To search for a command,

1. Click the magnifying glass icon ( ) on the menu bar.
2. Click one or more options in the Search for: section at the top of the form.
3. Click in the search box and type a few letters of the command name or topic, or type multiple terms separated by space characters, to return a list of matching results.

As you type, the tool returns a list of menu and task actions, shell commands, and application options related to the search term, based on the options you selected in step 2. For shell commands, the tool searches a list of command names and command options, and sorts the search results based on the quality of the match. Command name matches are placed higher in the search results than matches for command options. Move the pointer over the item in the search results to view an infotip that contains information about the result as shown in Figure 5.

<!-- image -->

<!-- image -->

Figure 5 Command Search Results

<!-- image -->

The command search supports full or partial matching of one or more search terms in the search box. For example, to search for results related to block shaping, you can enter "shape", "block", "sha bl", "shape\_blocks", and so on. If the tool returns a large number of results, a scroll bar is displayed on the right to navigate the list. Alternatively, edit your search term to narrow the search results. Finally, click the item from the list that matches your search.

Click an item in the Menu and Task Actions list to run that item. If a dialog box or panel is available for the action, the tool opens it. The tool dynamically generates a dialog box if you click an item from the Shell Commands section. For more information, see Using the Command Dialog.

If you click an item in the Application Options list, the tool opens the Application Options dialog box and displays the application option you selected. Set the value of the application option as needed and click OK to save the changes, or Cancel to leave the option unchanged. Alternatively, you can open the Application Options dialog box by choosing File &gt; Application Options from the menu bar.

As you use the command search, the tool remembers the search terms and actions you select for the current tool session. The tool displays the history of previous selections in the Recently found section, and the search terms for this session in the Recently searched section. Click an item in the Recently found section to perform the action again, or click the item in the Recently searched for section to reproduce the search.

The command search tool supports these additional features:

- Click the book icon to the right of the search box to open a Web browser with a link to search SolvNetPlus for the search term.
- Click the (X) to the right of the search box to clear any text in the search box (only if the search box contains text).
- Click the Tab key to move the focus between the search bar and three sections in the command search tool.
- Hover your pointer between the Menu and Task Actions section and Shell Commands section, or between the Shell Commands and Application Options sections, to reveal a splitter; click and drag the splitter to resize the section.
- Click and drag the bar at the bottom of the command search tool to resize the dialog box.
- Click outside the command search tool, or press the Esc key, to dismiss the tool.

## Using the Command Dialog

In the IC Compiler II tool, the graphical user interface generates dialog boxes on-the-fly for Tcl commands in the tool. When you click an item in the Shell Commands list in the command search, the tool generates a dialog box for the command as shown in Figure 6.

Figure 6 Command Dialog Box

<!-- image -->

The dialog box lists options and data entry fields in the top section, and displays status information and a command preview in the bottom section. The bottom row contains buttons to perform tasks related to this dialog box.

<!-- image -->

<!-- image -->

In the top section, required fields in the dialog box are marked with an asterisk (*). As you type in a text box, the tool validates your input. If no error is detected in your input, the tool displays your text in blue and updates the command preview. If your input contains an error, the tool displays your text in red and displays an error message in the command preview area. Click the Default button to restore the defaults in the dialog box. For more information about the purpose of a particular text box, hover the pointer over the box to view the infotip.

You can also enter Tcl expressions and variables in command dialog boxes. For example, you can enter the following in the cell text box in Figure 6:

- The actual cell name, such as "u0\_0"
- The "$cell" variable, to specify a variable that you defined which contains the cell name
- A Tcl expression, such as "[get\_cells u0\_0]"

When possible, the dialog box provides tools to select bounding boxes, layers, and enumerated values to help you specify the command. To specify a boundary, do one of the following:

- To define a rectangular bound, select the ( ) button, and either type the x- and y-coordinates for the upper-left and lower-right corners of the rectangle in the Coordinates box or drag the pointer in the layout view to form the rectangle where you need it.
- To define a rectilinear bound, select the ( ) button, and either type the x- and ycoordinates for each corner or direction change in the Coordinates box or drag the pointer in the layout view to form the sides of the polygon where you need it.
- To enter coordinates manually, click the ( ) button and type the x- and y-coordinates for the upper-left and lower-right corners of the rectangle in the Coordinates box.
- To enable or disable grid snapping, select or deselect the ( ) button.
- To select options from a list, click the ( ) button and choose an option on the menu that appears.

If the command option requires that you specify one or more layers, click the ( ) button and choose the layers. Alternatively, click the ( ) button and type the layer names.

If the command option supports multiple, enumerated values, click the ( ) button and choose an option on the menu that appears. For all other form entries, type the value in the text box.

<!-- image -->

In the bottom section, the tool provides buttons to perform different actions.

- Click OK to run the command and close the dialog box. If the dialog box contains an error, you must correct the error before clicking OK.
- Click Cancel to stop the command.
- Click Apply to run the command and keep the dialog box open.
- Click Script to copy the command to the Script Editor window without running the command.
- Click Default to restore the defaults in the dialog box.
- Click Help to open the man page for the command in the Man Page Viewer.

## Using Topic Search

The tool provides an interface for searching help topics and other documentation available in the installation directory. Searchable documents include man pages, tips-of-the-day, and help topics for GUI features that are accessed through the menu or by clicking a button. Matches are returned in the search results if the search term is contained in the command name, application option name, document title, or document keyword list. Note that the search tool does not consider online documentation available through SolvNet.

To open the search tool,

1. Choose Help &gt; Man Pages to open the man page viewer.

The first time you open the search tool, the tool displays links for viewing shell commands, application options, error messages, GUI help, and tip-of-the-day topics as shown in the following figure.

Figure 7 Man Page Viewer

<!-- image -->

2. (Optional) Click on a link to view a table of contents for that category.

<!-- image -->

<!-- image -->

3. Enter a search term in the title bar to display commands, application options, and help topics that match the term.
4. Click the down arrow at the right of the search box to view the search history.

Figure 8 Search Term

<!-- image -->

Figure 9 Search History

<!-- image -->

## Viewing the Tip of the Day

The tool provides a set of helpful hints that you can use to improve your workflow. To view the tip of the day, choose Help &gt; Tip of the Day from the menu. The tool displays a random tip of the day. Use the Prev and Next buttons to view additional tips.

## Creating Reference Methodology Scripts

The Synopsys reference methodology for the IC Compiler II tool is a set of scripts that capture the latest recommended methodology for using the tool for various vendors and process nodes. These scripts are a starting point form which you can adapt and build based on your own design requirements. The scripts contain embedded comments and alternate settings to help you customize the flow as needed.

To generate RM scripts for the IC Compiler II tool with the GUI,

1. Choose Help &gt; Generate RM Scripts from the menu.
2. Enter an output directory for the scripts. By default, the compressed tar file is written to the current directory.
3. Click the box next to ' I agree to the above Terms and Conditions .'
4. Click OK .

These steps write a compressed tar file to the directory you specified in step 2. After writing out the file, use the tar xzf filename command to extract the files. You can also create the Reference Methodology scripts with the generate\_rm command.

## Note:

Some technology nodes require additional configuration files from the foundry. Contact your Synopsys representative for help in obtaining the files.

## Viewing and Editing Application Options

The IC Compiler II tool uses application options to control the tool behavior. To manage application options, the IC Compiler II GUI provides a tool to display current application option settings, change settings, restore settings to defaults, and get help on specific application options.

To open the application options tool, choose File &gt; Application Options , or click an application option in the command search results.

<!-- image -->

Figure 10 Application Options Dialog Box

<!-- image -->

Application options use the following naming convention when specifying them in a Tcl command:

category[.subcategory].option\_name

where category is the text that generally refers to the engine affected by the application option. Some application option categories have optional subcategories to further refine the area affected by the application option.

Application options have either a global scope or a block scope.

- Block-scoped application options apply only to the block on which they are set. They are saved in the design library and are persistent across tool sessions.
- Global-scoped application options apply to all blocks, but only within the current session. They are not saved in the design library; you must specify them in each icc2\_shell session. You might want to consider adding the global settings to your .synopsys\_icc2.setup file.

## Viewing Application Options

After opening the Application Options dialog box, the tool displays the current application option names and settings. Select the scope of the application options to display by clicking the Global option, Block option, or both options. To filter the list of application options, enter a search term in the search box. As you type, the tool filters the application options and displays only the option names that contain the search term. To filter by the Value column, enter "Value:" followed by the search term. For example, enter "Value:true" to display only application options with a setting of "true" in the Value column.

<!-- image -->

<!-- image -->

To further limit the application options displayed in the list, click the filter button to the right of the search box. Deselect the 'Show if value is default' option to hide all default application option settings. Deselect the 'Show read-only' option to hide all read-only application options.

Application options which have a nondefault setting are displayed in bold font. Move the pointer over the text to display an infotip. The infotip shows the option name, option type, current setting, user default setting, system default setting, scope, and a brief description.

Figure 11 Nondefault Options

<!-- image -->

<!-- image -->

To display the man page for an application option, click the option to select it, then click near the top right of the dialog box. The tool opens the man page for the selected application option.

## Editing Application Options

To change the value of an application option,

1. Click the text for the option value.

For enumerated and Boolean options, the tool displays a list of possible settings. For integer type, float type, and text options, the tool displays an edit box.

2. Select the option from the list, or enter a new value in the text box.
3. Click OK to save the setting and close the dialog box, or click Apply to save the setting.

If you applied a nondefault setting, the tool displays the application option and setting in bold font. To revert a nondefault setting to its default,

1. Click the option value.
2. Click to the right of the edit box to set the value to its default.
3. Click OK or Apply to apply the setting.

<!-- image -->

To set an application option value that is based on a Tcl variable, use the set\_app\_options and list commands as follows:

```
icc2_shell> set scriptdir "myscriptdir" myscriptdir icc2_shell> set_app_options \ -list [list signoff.fix_drc.run_dir $scriptdir] signoff.fix_drc.run_dir myscriptdir icc2_shell> report_app_options signoff.fix_drc.run_dir **************************************** Report : app_option Design : ORCA **************************************** Name                    Type   Value ----------------------- ------ -----------signoff.fix_drc.run_dir string myscriptdir ----------------------- ------ -----------1
```

<!-- image -->

## Working in the Block Window

When you start the IC Compiler II tool and open the GUI, a block window appears. The following figure identifies the major features of the block window.

Figure 12 Block Window Features

<!-- image -->

When you open a block, it is displayed in the layout view. This is the primary block in the window. If you open additional blocks, each block is displayed in its own block window.

The block window provides the physical design working environment for the GUI. Layout views provide the focal points for viewing, analyzing, and editing blocks. For details about viewing and editing blocks, see the following topics:

- Changing the View of the Physical Design
- Editing the Physical Layout

## Changing the View of the Physical Design

Layout data can be densely packed with overlapping objects on different layers. You can control the visibility (display or hide) and selection (enable or disable) of individual object types or layers by setting options on the View Settings panel. You can also customize object or layer properties (color, fill pattern, and so forth) and set other layout and object display options. If you open multiple views, you can set different options for each view.

<!-- image -->

<!-- image -->

You can visualize the physical layout as explained in the following topics:

- Setting and Saving View Properties
- Displaying Grid Lines in a Layout View
- Drawing Timing Rulers in a Layout View
- Drawing Physical Rulers in a Layout View
- Drawing Circular Rulers
- Using Strokes to Activate Commands

## Setting and Saving View Properties

The View Settings View S t ngs pa lu h c v yo panels yout vi w V S g panel provides options you can use to set display properties in the active view. You can also save the current settings in your preferences file, or load settings from the preferences file. If you open multiple views, you can set different options for each view.

To display the View Settings panel, do one of the following

- Choose View &gt; Toolbars &gt; View Settings
- Press the F8 key

If the View Settings panel is hidden behind another panel, select the View Settings tab ( ) in the panel area.

You can use the View Settings panel to

- Control object or layer visibility and selection
- Change object or layer style properties such as colors or fill patterns
- Set display options for the view or for objects in the view

<!-- image -->

Figure 13 shows the View Settings panel for a layout view, and explains what you can do with it.

Figure 13 View Settings Panel for Objects in Layout Views

<!-- image -->

Select, reload, or change view setting presets

The default display characteristics for design objects are set for optimal viewing. These default characteristics work well for most blocks. However, you can change the display characteristics for individual object types if you need to customize your views for a particular block or working environment.

By displaying or hiding particular object types or layers, you can visually inspect just the data that you are interested in viewing while ignoring unrelated data. By enabling or disabling selection for particular object types or layers, you can control which types of objects are selected when you click or drag the pointer in a view.

You can customize how objects appear in the view by changing their style properties. Object styles set the appearance of objects in the active view. You can set the color, fill pattern, outline style, outline width, or exaggeration value for individual object types or layers.

<!-- image -->

## Note:

The exact properties that you can change depend on an object's graphic representation in the view.

You can set options individually, or you can apply a predefined set of view settings called a preset . You can apply a system preset provided by the tool or a custom preset that you create. For more information about presets, see Applying Predefined View Settings.

To change layout view display properties in the active view,

1. Set options as needed on the View Settings panel.
2. Click Apply.

By default, to change the settings, you must click Apply. If you prefer, you can set the panel to automatically apply your changes as soon as you make them.

<!-- image -->

To enable or disable the automatic apply mechanism, click the Options button ( ) and choose 'Auto apply.' To reverse unapplied changes, click the Options button and choose 'Cancel changes.'

<!-- image -->

Figure 14 shows the View Settings View S t ngs pa l y r o u v panel as it appears when you click the Layers tab to set options for layers in a layout view.

Figure 14 View Settings Panel for Layers in Layout Views

<!-- image -->

To filter the list of layers, enter a text string in the layer text filter box. As you type, the layer settings panel updates to show only layers that contain the text you entered. Only the list of layers is updated; the design shown in the block window is not affected by layer filtering. Click the (X) to the right side of the text box to clear the filter.

To sort the list of layers, click Arrange By and choose a sort option to reorder the list of layers. The tool updates the Layer panel and sorts the layers by mask, name, layer name, layer number, visibility, or selectability, based on the option you choose.

By default, the layers are sorted in ascending order. Click the (^) to the right of the Arrange By field.

<!-- image -->

Figure 15 shows the View Settings View S t ngs pa l y r o u v panel as it appears when you click the Settings tab in a layout view. The Settings panel has tabs to set display options for the view, cells, nets, pins, paths, and mask colors.

Figure 15 View Settings Panel for Settings in Layout Views

<!-- image -->

## Saving and Restoring View Settings

The tool does not save view settings when you exit the session. If you change view settings during a session and want to use the same settings in a future session, you can save them in your preferences file. You can also restore previously saved view settings by loading them from your preferences file.

To save the current settings for the active view, go to the View Settings panel, click the options button ( ) and choose Preferences &gt; Save To Preferences on the View Settings panel. To restore the most recently saved view settings, click the Options button and choose Preferences &gt; Set From Preferences on the View Settings panel.

## Applying Predefined View Settings

You can configure a view by applying a predefined set of view properties called a preset . You can apply a system preset provided by the tool, and you can create and apply your own custom presets.

<!-- image -->

By default, when you open a block window, the tool configures the view by using the view settings saved in your preferences file. To apply view settings from a preset, select the preset in the Preset list at the bottom of the View Settings panel.

For example, to apply the system preset that configures a layout view for design planning, select 'floorplan' in the Preset list.

<!-- image -->

When you change settings manually by setting options on the View Settings panel, an asterisk sign (*) appears in front of the preset name in the Preset list.

<!-- image -->

If you need to reapply the view settings from the preset, click the button. To reconfigure the view with the default view settings, select Default in the Preset list.

When you create a custom preset, you specify a preset name and the view settings that you want to include in the preset. You can create a new preset or redefine an existing custom preset. You cannot redefine a system preset.

To create a custom preset,

1. Click the button and choose 'Save preset.'

The Write Layout Setting Preset dialog box appears.

2. Select an existing preset, or type a new preset name in the 'Select or type a preset name' box.
3. Set options to control which settings you want to include.

For a layout view, by default, the object type filters and object display properties from the Objects tab, the layer type filters from the Layers tab, and the layout display settings from the Settings tab are included. You can set options to include the layer display properties from the Layers tab or the object style properties from the Objects and Layers tabs.

## 4. Click OK .

The tool saves the preset and adds the preset name to the Preset list on the View Settings panel.

You can specify a preset as the default configuration when you open a new block window or view. You can remove a custom preset but not a system preset.

## Displaying Grid Lines in a Layout View

By default, the grid lines are not displayed in the layout view. You can display the grids u e l tho ap y n lithograp y grid, splay n o h u e c lithography grid or the user grid. In addition, when the grid lines are displayed, you can cycle between the default grid spacing and ten times the default grid spacing.

- To display or hide the lithography grid, choose View &gt; Grid &gt; Show Litho Grid .
- To display or hide the user grid, choose View &gt; Grid &gt; Show User Grid .
- To display or hide the FinFET grid, choose View &gt; Grid &gt; Show Finfet Grid .
- To switch between the default grid spacing and ten times the default grid spacing, choose View &gt; Grid &gt; Cycle grid spacing .

## Drawing Timing Rulers in a Layout View

Timing rulers are used to measure timing delays between points in the layout. The timing is based on parasitic parameters set by the read\_parasitic\_tech and set\_parasitic\_parameters commands, or on net estimation rules set by the set\_net\_estimation\_rule command. A timing ruler can be composed of one or more horizontal or vertical segments. By default, the timing delays from the beginning of the ruler are labeled at the ends of each segment and at every tenth tick mark within a segment.

## Note:

Timing ruler drawing operations cannot be reversed by choosing Edit &gt; Undo .

To draw timing rulers in a layout view,

1. Click the Timing Ruler button ( ) on the Mouse Tools toolbar or choose View &gt; Mouse Tool &gt; Timing Ruler .

When you enable the Timing Ruler tool in a layout view, the Timing Ruler Tool options appear on the Mouse Tool Options toolbar and the pointer changes shape. By default, cross hair rulers appear attached to the pointer in the layout view.

2. (Optional) Set options as needed on the Mouse Tool Options toolbar.
- Select Attach to attach a point on the ruler to an object
- Click the Use option in the Net Estimation Rule section and select a rule name from the box to calculate timing. To calculate the timing based on metal layer and buffer size, leave this option deselected.
- Select the horizontal and vertical layer
- Change the utilization

<!-- image -->

- Change the buffer type and spacing
- Specify a nondefault routing rule (NDR)
- Change the grid snapping option for the ruler segments
3. Click in the layout view where you want to begin the ruler. If the Attach option is selected, objects are highlighted as you move the pointer over them; the ruler attaches to highlighted objects.
4. Click where you want to end the ruler segment.
5. (Optional) To draw another ruler segment, repeat steps 2 through 4.
6. To end the ruler, press the Enter key.
7. (Optional) To draw another ruler, repeat steps 2 through 6.

Before you click points to define the ruler, you can select or deselect the Attach option to limit the objects to which you attach the ruler. You can remove individual rulers or all rulers in the layout view, but you cannot remove or modify individual ruler segments.

For information on removing timing rulers, see Drawing Physical Rulers in a Layout View.

## Drawing Physical Rulers in a Layout View

You measure distances in a layout view by drawing physical rulers. A physical ruler can be composed of one or more horizontal, vertical, or diagonal segments. By default, the distances from the beginning of the ruler are labeled at the ends of each segment and at every tenth tick mark within a segment.

To draw rulers in a layout view,

1. Click the button on the Mouse Tools toolbar or choose View &gt; Mouse Tool &gt; Ruler .

When you enable the Ruler tool in a layout view, the Ruler Tool options appear on the Mouse Tool Options toolbar and the pointer changes shape. By default, cross hair rulers appear attached to the pointer in the layout view.

2. (Optional) Set options as needed on the Mouse Tool Options toolbar.
- Select the ruler mode

By default, the Ruler tool draws a single-segment ruler ( Two point mode). To draw a multisegment ruler, select the Multi point mode.

- Select a direction option
- Display or hide the cross hair rulers attached to the pointer when you start a new ruler, the labels that show the distance from the ruler origin to the endpoint of each

<!-- image -->

<!-- image -->

ruler segment, and the labels that show the segment length at the midpoint of each ruler segment

- Control whether the distances displayed by the ruler labels are absolute measurements from the design origin ( Coordinate ), relative measurements from the ruler origin ( Ruler Distance ), or relative measurements from each segment origin ( Segment Distance )
- Change the grid snapping option for the ruler segments
- Record the ruler segment lengths or distances in the session transcript (console log view)
3. (Optional) Select attach to attach the startpoint to an object.
4. Click in the layout view where you want to begin the ruler. If the Attach option is selected, objects are highlighted as you move the pointer over them; the ruler attaches to highlighted objects.
5. Click where you want to end the ruler segment.
6. (Optional) To draw another ruler segment, repeat steps 2 through 4.
7. To end the ruler, press the Enter key.
8. (Optional) To draw another ruler, repeat steps 2 through 6.

The rulers that you create are persistent - that is, when you save the design and reopen it again, the rulers that were saved automatically in the database are available for your use. You can perform the regular operations such as move, rotate, copy, or stretch on these persistent rulers.

You can use the following commands to perform the same operations that you can perform using the GUI:

| To do this action                                                                           | Use this command        | Example                                                                                               |
|---------------------------------------------------------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------|
| Create a new ruler                                                                          | create_ruler            | icc2_shell> create_ruler -name example_ruler \ -type ruler -color red \ -points {{123 456} {200 200}} |
| View the rulers in the design                                                               | get_rulers              | icc2_shell> get_rulers                                                                                |
| Remove rulers                                                                               | remove_rulers           | icc2_shell> remove_rulers                                                                             |
| Write a Tcl script that contains the annotations (including rulers) that are in the design. | write_annotation_shapes | icc2_shell> write_annotati on_shapes -file recreate.tcl                                               |

<!-- image -->

Before you click points to define the ruler, you can select or deselect the Attach option to limit the objects to which you attach the ruler. You can remove individual rulers or all rulers in the layout view, but you cannot remove or modify individual ruler segments.

To remove a ruler from the layout view,

1. Click the button on the Mouse Tools toolbar or choose View &gt; Mouse Tool &gt; Ruler .
2. Move the pointer over the ruler you need to remove.
3. Right-click and choose Remove Nearest Ruler .

To remove all rulers from the layout view,

- Click the button on the Mouse Tools toolbar or choose View &gt; Mouse Tool &gt; Remove All Rulers .

## Drawing Circular Rulers

You can create circular rulers in the tool by using the gui\_add\_annotation command. For more information, see Creating Annotations.

## Using Strokes to Activate Commands

You can stroke the pointer to activate preset commands in the active view. By default, the strokes are set up to activate commands that do the following: com ands tr ke

- Increase or decrease the magnification of the block
- Pan the block
- Display the entire block

You can also define your own strokes. You can define up to 72 basic strokes and many more multisegmented strokes.

A basic stroke is a single click of the middle mouse button with the pointer in the layout view. A point-to-point stroke (dragging the pointer from point to point in one of the following directions while holding down the middle mouse button).

<!-- image -->

com

ands et\_gui

r

k

b

<!-- image -->

You can activate other commands for each of these strokes by also pressing a modifier key (Shift, Ctrl, or Alt), or a combination of these keys as shown in the following figures:

<!-- image -->

In addition to the basic and modified stroke commands, you can perform multisegmented strokes. Each segment can go in any one of the eight directions used for the basic stroke commands. The following drawing shows some simple multisegmented strokes you can define:

<!-- image -->

To bind a command to a basic or multisegmented stroke, use the set\_gui rok b nd c m a

set\_gui\_stroke\_binding command. By default, the GUI is set up to use basic strokes instead of multisegmented strokes. You can change this preference by using the set\_gui rok p f nc m a d com ands et\_gui r k p f set\_gui\_stroke\_preferences command. For details about using these commands, see their man pages. set\_gui rok b nd c m a p f

## Editing the Physical Layout

The block window provides interactive tools and commands for editing the layout of blocks in a library workspace.

You can use the editing tools and commands to

- Move, resize, copy, and remove objects
- Rotate and flip objects, and change cell orientations
- Reshape objects
- Align, distribute, and spread objects
- Expand objects
- Create routing blockages, net shapes, port terminals, text objects, and vias

Typically, you select the objects that you want to edit. You can select the objects interactively with the Selection tool or by typing their names on the Select By Name toolbar. The interactive editing tools also allow you to select objects when the tool is active.

The Selection tool has three modes: Add, Replace, and Remove. Add and Replace are default modes, whereas Remove is a temporary mode. To activate any of the default modes, press any accelerator key. When you use the combo box to change the mode from Add to Replace or vice versa, the tool changes the current mode and the default mode at the same time. However, when you use the combo box to switch to Remove, only the current mode is changed and the default mode remains unchanged. Therefore, any key press or release restores the current mode to either Add or Replace.

You can access editing tools and commands by clicking buttons on the Edit or Mouse Tools toolbar or by choosing commands on the Edit or Create menu. Figure 16 shows these toolbars and the Edit menu. The toolbars group related editing functions together in lists that open when you click the down arrow button.

<!-- image -->

## Figure 16 GUI Editing Commands

<!-- image -->

<!-- image -->

<!-- image -->

For information about editing physical design objects and constraints, see the following topics:

- Editing Objects Interactively
- Working in the Editing Environment
- Using the Editor Toolbox
- Using the Edit in Place Functionality

## Editing Objects Interactively

The layout editing mouse tools allow you to interactively create, edit, or remove physical objects in a layout view. The block window provides a consistent editing environment for all the tools. You can

- Set tool options on the Mouse Tool Options toolbar
- Use keyboard shortcuts for frequent or repetitive operations
- Preview objects for selection and cycle through overlapping objects

If you need to magnify or traverse the design or measure distances when an editing tool is active, you can temporarily activate the Zoom In tool, Zoom Out tool, Pan tool, or Ruler tool without deactivating the editing tool.

When you activate a mouse tool in a layout view, the options for using the tool appear on the Mouse Tool Options toolbar.

You can perform frequent or repetitive actions by using keyboard shortcuts. Table 1 shows the standard key bindings for the interactive editing tools.

Table 1 Interactive Editing Tool Conventions

| Action                                     | Shortcut      |
|--------------------------------------------|---------------|
| Add points to perform the operation        | Click or Drag |
| Add point and apply changes                | Return        |
| Remove last point                          | Backspace     |
| Cancel pending input, if any, or exit tool | Escape        |
| Cycle forward through overlapping objects  | F1            |
| Cycle backward through overlapping objects | Shift+F1      |
| Reverse (undo) most recent operation       | Ctrl+X        |

Table 1 Interactive Editing Tool Conventions (Continued)

| Action                                         | Shortcut   |
|------------------------------------------------|------------|
| Reapply (redo) most recently applied operation | Ctrl+Y     |

Many of the editing tools operate on selected objects. You can select the objects before or after you activate a tool. If any objects are selected when you activate an editing tool, you can Ctrl-click objects to add them to the current selection and Shift-click objects to remove them from the current selection. Selected objects appear in the selection color, which is white by default.

## Note:

If you have trouble selecting or previewing small objects, try magnifying the view. In a large design, some objects or object outlines are too small to click at low magnification.

All the operations that you can perform with the interactive editing tools are log interac v p replay int c v o logged and can be replayed with the gui\_mo se t l c and com andsgui\_ e t l gui\_mouse\_tool command. Similarly, options that you set on the Mouse Tool Options toolbar are logged and can be replayed with the gui\_set mo l p n c a d com andsgui\_ et l p gui\_set\_mouse\_tool\_option command. For information about these commands and the

options for a particular tool, click the button to see the Help page for that tool.

<!-- image -->

For information about the interactive editing operations that you can perform, see the following topics:

- Moving, Modifying, Creating, and Removing Objects
- Expanding and Rotating Objects

## Moving, Modifying, Creating, and Removing Objects

You can move, resize, copy, split, reshape, create, and remove objects.

Table 2 shows the editing tools you can use to modify the physical design.

<!-- image -->

| To perform this operation   | Use this tool                                                                                    |
|-----------------------------|--------------------------------------------------------------------------------------------------|
| Move objects                | Click or choose Edit > Move , and then select the objects and click or drag to the new location. |
| Snap objects to the grid    | Choose Edit > Snap .                                                                             |

Table 2 Editing Tools for Design Objects

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

| To perform this operation                                                                                                                                                             | Use this tool                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Align objects relative to a side or center of an anchor object or location align objects m A /D r u                                                                                   | Click or choose Edit > Align > Align/Distribute Tool , click the Align tab on the Mouse Tool Options toolbar, select the objects you want to align, specify the anchor object or location, and click the toolbar button for the alignment operation you want to perform. You can set options as needed on the Mouse Tool Options toolbar.              |
| Distribute distr bu ng o jec distr bu on l object dis r u n l Align/D str bu e o to lsA ign/D r bu e mouse t l A ign/D r b objects relative to a side of an anchor object or location | Click or choose Edit > Align > Align/Distribute Tool , click the Distribute tab on the Mouse Tool Options toolbar, select the objects you want to distribute, specify the anchor object or location, and click the toolbar button for the distribution operation you want to perform. You can set options as needed on the Mouse Tool Options toolbar. |
| Resize objects resiz ng obj ct M v /R l m u Ed                                                                                                                                        | Click or choose Edit > Stretch , and then select an object and drag an edge or corner to resize.                                                                                                                                                                                                                                                       |
| Copy objects copying bje tsm u l C                                                                                                                                                    | Click or choose Edit > Copy , and then select and drag the objects.                                                                                                                                                                                                                                                                                    |
| Split objects Split o bjec s ng ha m u                                                                                                                                                | Click or choose Edit > Split , and then drag a line or rectangle across the objects where the split is to occur. You can set options as needed on the Mouse Tool Options toolbar.                                                                                                                                                                      |
| Reshape objects by cutting an area with an optional gap Reshap to l bj c r ing m u f d                                                                                                | Click or choose Edit > Cut , optionally set the gap size, and then drag a rectangle across the object where you want to cut a piece. You can set options as needed on the Mouse Tool Options toolbar.                                                                                                                                                  |
| Reshape objects by adding an area with an optional gap Reshap to l bj c r ing m u f d                                                                                                 | Click or choose Edit > Add , optionally set the gap size, and then drag a rectangle across the object where you want to add a piece. You can set options as needed on the Mouse Tool Options toolbar.                                                                                                                                                  |
| Create a bound                                                                                                                                                                        | Click or choose Create > Bound , and then click and drag a rectangle for the bound. You can set options as needed on the Mouse Tool Options toolbar.                                                                                                                                                                                                   |
| Create a routing blockage                                                                                                                                                             | Click or choose Create > Routing Blockage , and then click and drag a rectangle for the routing blockage. You can set options as needed on the Mouse Tool Options toolbar.                                                                                                                                                                             |

<!-- image -->

Table 2 Editing Tools for Design Objects (Continued)

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Table 2 Editing Tools for Design Objects (Continued)

| To perform this operation                | Use this tool                                                                                                                                                                     |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create a net shape                       | Click or choose Create > Shape , and then click and drag a rectangle for the net shape. You can set options as needed on the Mouse Tool Options toolbar.                          |
| Create a terminal                        | Click or choose Create > Terminal , specify a pin or port, and then click and drag a rectangle for the terminal. You can set options as needed on the Mouse Tool Options toolbar. |
| Create a text object                     | Click or choose Create > Text , specify the text, and then click the location for the text. You can set options as needed on the Mouse Tool Options toolbar.                      |
| Create a via or via array                | Click or choose Create > Via , and then click the location for the via or via array. You can set options as needed on the Mouse Tool Options toolbar.                             |
| Remove objects Del t o s m u bj c r ving | Click or choose Edit > Delete , and then click or drag a rectangle to delete objects.                                                                                             |

## Expanding and Rotating Objects

Table 3 explains how you can expand, rotate, and flip design objects and orient cells.

<!-- image -->

| To perform this operation                                                 | Do this                                                                                                                                                                           |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Expand selected objects to objects on one or all sides expandi gobj cts m | Click an expansion tool ( , , , , or ) or choose Edit > Expand > expansion_direction . Alternatively, you can use the expand_obj cts m com andsexp _ bj t expand_objects command. |
| Rotate selected objects 90 or 180-degrees rota ing bjec s m d             | Click a rotation tool ( , , or ) or choose Edit > Rotate > rotation . Alternatively, you can use the rota e_ bj c s m nd com andsr t e_ bj rotate_objects command.                |
| Flip selected objects on an x- or y-axis flip ng objects m a d            | Click a flip tool ( or ) or choose Edit > Rotate > axis . Alternatively, you can use the flip_objects m and com andsflip_ bje t flip_objects command.                             |

<!-- image -->

Table 3 Editing Commands for Design Objects

<!-- image -->

## Working in the Editing Environment

The editing environment provides an incremental undo and redo facility that allows you to reverse or reapply the most recent editing operation or a series of operations. You can also constrain (fix) objects during editing operations, control grid snapping, set editing options, and view and edit object properties. Table 4 explains the global operations that you can use with any editing tool or command.

Table 4 Global Editing Operations

| To perform this operation                                                                                                  | Use this tool                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Reverse the previous edit change undo c m a s rev it                                                                       | Click the button or choose Edit > Undo . Alternatively, you can use the undo c m a com andsu undo command.   |
| Reapply the subsequent edit change reap ly dits o c m n                                                                    | Click the button or choose Edit > Redo . Alternatively, you can use the redo c m an com andsre redo command. |
| Constrain (fix) selected objects to prevent changes from interactive edits locking bje ts f r d u x                        | Click the button or choose Edit > Constraints > Fix .                                                        |
| Remove (unfix) the editing constraint on selected objects to allow changes from interactive edits locking bje ts f r d u x | Click the button or choose Edit > Constraints > Unfix Edit .                                                 |
| Enable or disable grid snapping snap i g, e bl or d t                                                                      | Click the button or choose Edit > Options and select or deselect Snapping enabled on the Snapping tab.       |
| View or edit object attribute values for selected objects                                                                  | Click the button or choose Edit > Properties .                                                               |

## Using the Editor Toolbox

The Editor Toolbox provides easy access to common editing tasks such as move, rotate, align, distribute, spread, and so on. Choose View &gt; Assistants &gt; Editor Toolbox from the menu to start the Editor Toolbox. The Editor Toolbox is shown in the following figure.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Figure 17 Editor Toolbox

<!-- image -->

Additionally, you can add custom controls to the user editor toolbox by using the gui\_create\_user\_editor\_toolbox\_type command before creating the BlockWindow.

## Initially, you must define a user widget group by using the

gui\_create\_user\_widget\_group Tcl command. By using the gui\_create\_user\_widget\_item command you can populate the widget group with the required widget items. You can get the required user widget items by using the gui\_get\_user\_widget\_items and delete the user widget items from the user widget group by using the gui\_delete\_user\_widget\_item command.

The following code creates a new user editor toolbox with many basic controls by using the gui\_create\_user\_editor\_toolbox\_type command:

```
# called when text changed proc textChanged { clct } { echo "textChanged $clct"; echo [get_attribute $clct value] } # called when radio button changed proc radioChanged { clct } { echo "radioChanged $clct"; echo [get_attribute $clct value] } # called when check box changed proc checkChanged { clct } { echo "checkChanged $clct"; echo [get_attribute $clct value] } # initialization proc for toolbar proc my_editor_toolbox { clct } { echo "my_editor_toobox $clct" # create text line edit set text [gui_create_user_widget_item -type text -name text]
```

<!-- image -->

<!-- image -->

```
set_attribute $text value "Text" set_attribute $text changed_proc textChanged # create action button set window [gui_get_current_window -mru] set window_type [gui_get_window_attribute -window $window -attribute type] set menuRoot [gui_menu_root_from_window_type -window_type $window_type] set hotkeys [gui_create_user_widget_item -name hotkeys \ -type "action:${menuRoot}::Help->Report Hotkey Bindings"] # create radio button group set radio_group [\ gui_create_user_widget_group -type stamp -name radio -label Radio -layout hbox { set radio_one   [gui_create_user_widget_item -type radio -name radio_one] set radio_two   [gui_create_user_widget_item -type radio -name radio_two] set radio_three [gui_create_user_widget_item -type radio -name radio_three] set_attribute $radio_one label "One" set_attribute $radio_two label "Two" set_attribute $radio_three label "Three" gui_create_user_widget_item -type stretch -name radio_stretch }] # connect to single radio state change on radio parent group set_attribute $radio_group changed_proc radioChanged # create check box set check [gui_create_user_widget_item -type check -name check] set_attribute $check label "Check" set_attribute $check changed_proc checkChanged } #---# create editor toolbox type to add user widgets to editor toolbox palette gui_create_user_editor_toolbox_type -command my_editor_toolbox #---# start gui gui_start # show editor toolbox palette set window [gui_get_current_window -mru] gui_show_palette -parent $window -type editor_toolbox_palette
```

The resultant palette of the user editor toolbox is as shown:

<!-- image -->

## Editing Pins With the Editor Toolbox

You can use the Editor Toolbox to move, distribute, align, and perform other operations on block pins as follows:

<!-- image -->

Table 5 Pin Editing Operations

<!-- image -->

## Table 5 Pin Editing Operations (Continued)

## To perform this operation Use this tool

Disable pin editing on a block

Legalize the selected block pins, or the block pins connected to the selected nets or cells

Remove the selected terminals from the current design

Align the selected pins

Change the width of the selected pin

Change the length of the selected pin

Change the layer of the selected pin Click the button. Alternatively, you can use the set\_editability -blocks [get\_selection] -value false command.

<!-- image -->

<!-- image -->

Click the button. Alternatively, you can use the place\_pins -legalize command.

<!-- image -->

Click the button. Alternatively, you can use the remove\_terminals command.

<!-- image -->

Click the , , or , button. The second and third buttons change the layer width and layer height respectively to match the layer properties. Alternatively, you can use the align\_pins , align\_pins -change\_layer\_width , or align\_pins -change\_layer\_height command.

<!-- image -->

<!-- image -->

Enter a new width value in the Width box in the Edit section and click the checkmark button to commit the change.

Enter a new value in the Length box in the Edit section and click the checkmark button to commit the change.

Select a new layer value in the Layer box in the Edit section and click the checkmark button to commit the change.

<!-- image -->

Table 5 Pin Editing Operations (Continued)

<!-- image -->

## Using the Edit in Place Functionality

The edit in place functionality enables you to work with and edit a subblock in the context of top-level. This functionality changes the current block to the selected block. You can push down into a selected block and pop it back up. You can also set the level depth to view.

<!-- image -->

Figure 21 Edit in Place Toolbar

<!-- image -->

## To edit a subblock:

1. Select the subblock to be edited.
2. Click the Push icon in the Edit in Place toolbar.

When you perform a push, the tool runs the set\_working\_design -push command automatically. For example,

```
icc2_shell> set_working_design -push [get_cells I_ORCA_TOP/I_BLENDER_1]
```

You can verify the current block by running the current\_block command from the console.

```
icc2_shell> current_block
```

<!-- image -->

<!-- image -->

<!-- image -->

Other blocks in the design are dimmed. To adjust the level of dimness, set the dimness level as appropriate by using the dimness icon in the tool. Setting the value to 100% ensures that the surrounding blocks are not dimmed. To completely hide the surrounding blocks, set the value to Off.

<!-- image -->

3. Press the 'F' key (full screen) to zoom into the new current block for edit.

<!-- image -->

4. Perform edits on the subblock.
5. (Optional): If there are multiple levels in the design, you can push deeper into the design to work on a specific object by using the Push icon.

<!-- image -->

<!-- image -->

6. (Optional): To navigate one level up, click the Pop icon.

When you perform a pop, the tool runs the set\_working\_design -pop command automatically. For example,

```
icc2_shell> set_working_design -pop
```

You can verify the current block by running the current\_block command from the console.

```
icc2_shell> current_block
```

7. (Optional) To navigate to the top-level (that is, to level 0), click the Pop to Top icon.

When you perform a pop to top, the tool runs the set\_working\_design -pop command automatically. For example,

```
icc2_shell> set_working_design -pop -level 0
```

You can verify the current block by running the current\_block command from the console.

```
icc2_shell> current_block
```

8. (Optional) To view the complete design, press Ctrl + F.
9. Use the Edit in Place toolbar to change edit level, push down, pop up, and so on.

<!-- image -->

## Viewing Metal Fill Data

The IC Compiler II tool supports editing design and metal fill data in the same context. To enable metal fill editing, open the View Settings panel and change the metal fill settings as shown in Figure 22. Metal fill data appears as one or more fill instances within the block; the data is stored with the block in the library. To edit the metal fill data, enable the All Levels Active option in the View Settings panel.

Figure 22 Metal Fill Display Settings

1. Increase the level to 1 or greater

<!-- image -->

<!-- image -->

2. Click to open Hierarchy Settings

<!-- image -->

## Using Toolbars and the Selection List

The IC Compiler II GUI provides tools for querying information, editing and recording scripts, and performing other tasks.

The following topics describe design planning tasks supported by the GUI:

- Using the Query Tool
- Using the Recent Menu Button
- Using the Script Editor
- Using the Select By Name Toolbar
- Using the Overview Toolbar
- Using the Selection List and Work List
- Using User Tables

## Using the Query Tool

The Query panel displays information about objects in the active layout or schematic view. The panel opens automatically when you enable the Query tool as the active mouse tool. When you click an object, the attribute information for the object is displayed in the Query panel.

To activate the Query tool, choose View &gt; Mouse Tool &gt; Query tool or click the Query tool button on the Mouse Tools toolbar. The pointer becomes the Query Tool pointer and the tool opens the Query panel on the right of the layout window.

Figure 23 Query Panel

<!-- image -->

To display information for an object, click the object. The tool populates the query panel with information about the object.

To display information for an object, click the object. The tool populates the query panel with information about the object.

To display the Query tool and populate with information for selected objects, choose Select &gt; Query Selection.

To further control the display of information in the Query panel, click the Show Options button and change the option settings:

- Select 'Auto Print Text to Log' to write out the contents of the Query panel to the console each time you query a new object
- Select 'Auto Show when Query Tool is Chosen' to automatically open the Query panel when you click an object when the Query Tool is active
- Click 'Customize Text' to open the Customize Query Toolbar dialog box; see Using the Customize Query Toolbar for more information
- Select 'Warn in selection exceeds size limit' and set a limit to issue a warning if the selection exceeds the specified limit
- Select 'Show attribute group' to display the attribute group selection box in the Query panel
- Click 'Show attribute filter' to display a text filter box in the Query panel

<!-- image -->

<!-- image -->

Select an attribute group in the attribute group box to display only the attributes that belong to that group. To get additional information about which attributes are available for a specific group, click the Activate Attribute Group Manager button to the right of the attribute group box. See Using the Attribute Group Manager for more information about attribute groups.

Enter a simple text string in the filter box to display only attributes where the filter text matches a portion of the attribute name. To clear the string, click the (X) at the right of the filter text box. Click the Filter properties button at the right of the filter box and select Show Read Only Properties to display only attributes with read-only values.

Click the Name or Value column header to change the sort order for the column.

## Using the Customize Query Toolbar

To open the Customize Query Toolbar, click Customize Text in the Show Options panel in the Query Panel. The Customize Query Toolbar is shown in Figure 24.

Figure 24 Customize Query Toolbar Dialog Box

<!-- image -->

The Customize Query Toolbar displays a table of Object Classes and the attribute group in which they appear. To change the setting, click the text in the Single Object Query or Many Objects Query column and select a new value. Select All to enable the value to appear in all groups. After configuring the list, click OK or Apply to apply the changes.

By default, objects can be members of groups such as Application, Basic, QueryText, and so on. When the group name is selected in the Query Panel, the information about the object type appears in the Name and Value column of Query Panel. You can create additional groups by clicking the Attribute Groups button and using the Attribute Group Manager dialog box. See Using the Attribute Group Manager for more information.

<!-- image -->

## Using the Attribute Group Manager

Use the Attribute Group Manager to define new attribute groups and add or remove objects from an attribute group.

Figure 25 Attribute Group Manager and Attribute Group Editor

<!-- image -->

To use the Attribute Group Manager,

- Click the Create button to create a new attribute group; enter the attribute group name in the dialog box that appears and click OK to save the new attribute group
- Click an Object Class, click an Attribute Group name, and click the Modify button to change the attributes that are displayed when you query the object in the Query panel; see Using the Attribute Group Editor for more information
- Click an Attribute Group name and click the Rename button, or double-click the Attribute Group name, to rename a user-defined attribute group name; Attribute Group names defined by the system cannot be changed

<!-- image -->

- Click an Attribute Group name and click the Copy button create a new attribute group and copy the group attributes to the new attribute group
- Click the Delete button to remove the selected user-defined attribute group from the system
- Click the Save button to write out the current attribute group settings to the GUI user preferences file
- Click the Restore button to read in the attribute group settings from the GUI user preferences file
- Click the Reset to system defaults button to reset the content of the application-defined groups to their defaults; user-defined groups are not affected

## Using the Attribute Group Editor

Use the Attribute Group Editor to add or remove attributes from the list of attributes associated with a user-defined attribute group. The Attribute Group Editor is opened by clicking the Modify button in the Attribute Group Manager.

Do the following to modify the list of attributes for the selected attribute group:

- Select an attribute in the left column and click the right arrow to move the entry to the right and make it available for display with this attribute group
- Select an attribute in the right column and click the left arrow to move the entry to the left and make it unavailable for this attribute group
- Select one or more entries in the right column and click the up arrow to move the entries up in the list; use the down arrow to move the entries down
- Press Control-A to select all entries in the column
- Click OK or Cancel to save the results or exit the dialog box without saving

## Using the Recent Menu Button

The recent menu button displays icons and text that represent the most recent actions you performed in the GUI. The recent menu button is displayed by clicking the down arrow below the current mouse tool icon near the top left of the layout window as shown in Figure 26.

Figure 26 Recent Menu Button

<!-- image -->

As you perform tasks in the GUI, the tool inserts an icon and text at the top of the list of recent actions. By default, the tool shows the last five commands; you can change this number by clicking the Show Options button ( ) and selecting a new value for Maximum Commands.

The tool provides shortcut keys to access the last nine most recently used commands. Press Alt-1 to recall the most recent command, Alt-2 to recall the second most recent, and so on.

You can modify the list of most recently used commands by clicking the right mouse button and selecting one of the following options from the context menu:

- Choose Add to Favorites to add this command to the list of commands in the Favorites Toolbar.
- Click Remove to delete this command from the most recently used commands list.
- Click Exclude to delete this command and prevent it from being added to this list in the future; to remove the command from the exclude list, click the Show Options button and click Reset Excluded.
- Click Remove All to remove all commands from the most recently used command list.

Click the Show Options button to change other settings for the Recent toolbar:

- Use Maximum Commands to select a new value for the maximum number of commands to be saved in the list of recent actions.
- Click Reset Exclude to remove all commands from the exclude list; this button is only available if you have excluded one or more commands.

## Using the Script Editor

The Script Editor is an easy-to-use tool for loading, editing, running, and saving Tcl scripts in the IC Compiler II tool. Activate the Script Editor by choosing View &gt; Toolbars &gt; Script Editor or by moving your mouse to the status bar at the bottom of the layout view, clicking the right mouse key, and selecting Script Editor from the context menu.

<!-- image -->

Figure 27 Script Editor

<!-- image -->

Move the pointer over the icons to view their function in the infotip. You can perform the following operations in the Script Editor:

- Click the New button to clear the contents of the script window.
- Click the Open button and enter a file name in the Open dialog box to read in an existing script.
- Click the Save button to save the script.
- Click the Save As button to save the script by using a new file name.
- Click the Undo button to revert a change to the script.
- Click the Redo button to reverse the last undo action.
- Enter text in the search box and click the Find next button to search forward in the file; click the Find previous button to search backward in the script.
- Enter an integer value in the search box and click the Go to line button to scroll the editor to the specified line number.
- Click Run Script to save the contents of the script editor to a temporary file and run the file as Tcl commands.
- Use the mouse to select words or lines in the script editor and click Run Selection to save the selection to a file and execute it as Tcl commands.
- Edit to contents in the script editor by typing, cutting and pasting, or deleting text.

## Using the Select By Name Toolbar

The Select By Name Toolbar selects or highlights objects by object name or by a search filter expression. To activate the tool, choose Select &gt; By Name Toolbar from the menu.

Alternatively, click the Select By Name button ( ) at the lower-left corner of the layout window.

<!-- image -->

Figure 28 Select By Name Toolbar

<!-- image -->

The toolbar supports keyboard shortcuts to efficiently search for and select objects. A typical workflow using the Select By Name toolbar is as follows:

1. Press Ctrl+/ to display the Select By Name toolbar.
2. (Optional) Change the selection mode to Highlight to highlight the selected objects.
3. (Optional) Choose an object type from the Object Type list.
4. Press F3 to search by name or F4 to search by filter.
5. Enter a partial search term that matches the beginning of the object name for which you are searching; if no matches are found, the tool applies a light red color to the box.
6. Press Tab to expand the search term to the matching object name, or display all matching results if the search term matches more than one object.
7. Press Insert to toggle between Add to Selection and Replace Selection.
8. Press Enter or click Apply to select the objects.

## Entering Search Terms for Multiple Objects

The search box provides a flexible interface for finding multiple objects. To search for multiple object names, separate the search terms with a space. If the object name contains a space, use curly braces ({}) to separate the terms. Press the Tab key to search for the term preceding the text cursor. To search for the other term, move the cursor and press the Tab key again. Click the (X) to the right of the search box to clear the search term.

<!-- image -->

<!-- image -->

If the search term matches more than one object, the tool displays a scrollable search results list. Continue typing to create a longer search term and narrow the search results. Press the Up arrow key or Down arrow key to scroll up or down the list. Press Enter to select a single entry in the list, or press the Control key and click additional results to select them. Click the Select All button, or press Ctrl+A to select all results in the list. Click the Sort button to reverse the sort order of the list. Press Esc to exit the list.

After selecting multiple objects in the list, the search box shows an abbreviated search term, such as "(#4)", where "4" is the number of objects you chose. To select the objects in the layout, press the Enter key. To add additional objects to the selection, click the Add option or press the Insert key, then enter a new search term and repeat the previous steps.

## Searching by Filter

You can use the Select By Name tool to search for objects by using a filter expression as shown in the following figure.

<!-- image -->

By typing the first few letters of the search expression and pressing the Tab key, you can quickly build the filter expression. A typical workflow to build a filter search expression is as follows:

1. Type the first few letters of the search expression, for example, "a".
2. Press the Tab key to show the list of attributes which match the search expression.
3. Continue typing to narrow the search, or click the attribute in the list.
4. Press the Tab key again to display the legal operators for the attribute.
5. Continue typing to narrow the search, or click the attribute in the list.

<!-- image -->

6. Press the Tab key again; the tool displays the legal values for an attribute with enumerated values, or inserts empty quotation marks, or inserts a value of 0.0 into the search box.
7. Continue using the Tab key to repeat these steps to append additional information to the expression, or press Enter to commit the expression and perform the search.

## Using the Overview Toolbar

The Overview toolbar displays an outline of the entire layout view with a yellow highlight that shows the area currently displayed in the layout view. To activate the Overview toolbar and display the Overview panel, choose View &gt; Toolbars &gt; Overview from the menu.

To display the overview in a small pop-up window, click the Overview button ( ) at the bottom of the layout window.

<!-- image -->

Figure 30 Overview Toolbar

<!-- image -->

To change the region of the design that is displayed in the layout window, click and drag the yellow highlight region in the overview panel or window. After you release the mouse, the layout view updates to display the area within the highlight.

To change the zoom factor in the layout view, move the pointer to the boundary of the yellow highlight region. The pointer changes to allow you to resize the highlight. Click and drag the edge to zoom in or zoom out.

<!-- image -->

## Using the Selection List and Work List

The selection list displays a list of the currently selected objects in the design. If you select objects of the same type, the selection list displays the Selection List group of attributes for the objects. If the objects are not of the same type, the selection list displays the name, object\_class, and full\_name attributes for the objects.

The following figure shows the Selection List dialog box with a work list tab selected.

Figure 31 Selection List Dialog Box

<!-- image -->

The following actions are available in the selection list:

- Sort the list of objects by clicking a column header; click the header a second time to reverse the sorting order.
- Enter a filter expression to reduce the number of items in the list. For example, enter the following expression to display cells with a name that begins with 'C' and an orientation of R270.
- Click the forward and backward arrows next to the filter box to scroll forward and backward through previous filter expressions. Alternatively, click the filter menu button ( ) to view the entire filter history; click an entry in the list to filter the list by using the expression.

```
name=~C && orientation==R270
```

<!-- image -->

<!-- image -->

- Click the Toggle between filter expression button ( ) to show or hide filters for individual columns.
- Click the options button ( ) to change whether the filter expression is interpreted as a wildcard expression or a regular expression and whether expressions are ANDed or ORed.
- Select an entry in the attribute group selection box to display a new set of columns for the selected objects. By default, the selection list entry is displayed. Use the Attribute Group Manager to view or modify the list of attributes displayed for a particular attribute group.
- Click the Modify Attribute Group button ( ) to open the modify, manage, or save attribute groups.
- Click the Charts button ( ) to analyze design data in chart plots. See Charts for more information.
- Click the Export button ( ) to export the list, or the selected list data, to the User Tables import form or a comma-separated values file.

<!-- image -->

## Work List

The work list is a persistent list of objects based on the current selection and is created by clicking the Create Work List tab button; this action copies the currently selected objects to the work list. Clicking an item in a work list automatically selects the object in the current layout, schematic, or other view. The basic functions of the work list are similar to the selection list, however, the work list does not change as you select or deselect objects in the layout, schematic, or other view. You can create and manage multiple work lists in the same tool session, and each work list is available in a tab in the Selection List dialog box.

The following additional actions are available in a work list tab:

- Select one or more rows and click the Toggle Selected Items Fixed button ( ) to mark or unmark the selected items with a check mark.
- Select one or more rows and click the Show/Hide Fixed Objects in List button ( ) to show or hide the rows with the check mark annotation.
- Click the Add Global Selection button ( ) to add the currently selected items to the current work list.
- Click the Select Items to match Global Selection button ( ) to select items in the current work list that are also selected in the layout, schematic, or other view.

## Charts

To analyze design data in a chart plot, click the Charts button ( ) in the Selection List dialog box or the work list tab and choose from the following chart plots:

<!-- image -->

<!-- image -->

- Distribution plot Organizes the values of a column into bins and displays the number of values in each bin.
- Box plot

Displays the distribution of values in one or more columns based on the five-number summary: minimum, first quartile, median, third quartile, and maximum. Outliers (outside the 1.5 quartile range) are shown as individual points.

- Scatter plot

Displays values from two columns in a two-dimensional plot.

- Matrix plot

Displays an array of scatter plots, allowing you to select two or more columns to produce a matrix of plots that summarize the relationship between the columns.

Each chart plot dialog box has a context menu that allows you to perform common operations on the plot. In addition, the dialog box includes

- Plot area
- Settings panel
- Data table (not shown by default)
- Status bar

You can specify the columns to be used in the plot, column groups, plot-specific controls, and controls for the selection behavior.

## Using User Tables

User tables provide a way to import, define, interact, and save tables of data. You can save a user table to a file that exists apart from the design database and reload the file in a later tool session. User tables can be generated from a selection list or from a commaor tab-separated file.

User tables support many common spreadsheet operations, such as editing, sorting, filtering, summing, viewing distributions of column values, and so on. In addition, you can change the current selection by clicking rows in the user table.

## Creating a User Table

To create a user table from an existing selection set in the design,

1. Open the Selection List dialog box by clicking the Selection List button ( ) or choose Select &gt; Selection List from the menu.
2. Click the Export &gt; User Table button to create the user table based on the current values in the selection list.

The tool copies the values to the user table import form.

3. (Optional) Change the table name in the Table Name box.
4. Click OK to import the data and build the user table.

<!-- image -->

To create a user table by importing a comma- or tab-separated text file,

1. Choose View &gt; User Tables from the menu.
2. Click the Open button ( ) near the top of the user table form.
3. Complete the form by selecting the separator (comma or tab). Optionally, enter a table name.
4. Enter or choose a file name.
5. In the Configure Table Columns form, set the data type for each column as needed.
6. Click OK to create the user table.

<!-- image -->

## Saving and Reloading a User Table

To save a user table,

1. Choose Save in the Action box near the top of the form.
2. Enter the file name in which to save the database. User tables typically have a .utable extension.
3. Click OK .

The tool writes out the user table data to the specified file.

To load a saved user table,

1. Click the Open button ( ) near the top of the user table form.
2. Choose Open UserTable file from the Select drop-down box.
3. Enter the user table file name to be loaded.
4. Click OK .

## Analyzing Data in a User Table

After creating a user table, you can perform the following operations:

- Sort or reverse the sort of the table by right-clicking a column header and choosing the up or down arrow buttons.
- Filter the table by using one of the following methods:
- Clicking the filter button ( ).
- Entering column iterator and reduction functions in the filtering field.

The supported functions include: approx(), abs(), round(), scale(), offset(), min(), max(), sum(), count(), avg(), mean(), median(), lower\_quartile(), uppper\_quartile(), stdev(), second\_stdev(), and third\_stdev().

An example of an iterator function is Tot Power &gt; @Lkg Power, which shows all the rows where this expression is true. You refer to a column by using the @column\_name syntax.

An example of a reduction function is Lkg\ Power &gt; #mean(Tot\ Power).

In the following example, the filtering query shows all the rows where the 'Tot Power' in a given row is approximately equal to 10% of 'Lkg Power' in that same row.

<!-- image -->

## Note:

The approx() function can only appear on the right-hand side of the expression.

<!-- image -->

- Rearrange the order of columns in the table by clicking and dragging the column header. Alternatively, right-click a column header and choose More Column Options &gt; Configure Columns from the context menu to open the Configure Columns dialog box.
- Select a user table to display by clicking the Tables box near the top of the user table form and selecting a new table name.
- Change the currently selected objects in the layout or schematic view by right clicking a cell in the table, choosing Selection &gt; Toggle Auto Select Mode , and clicking a cell to select or deselect.

## Creating a Report Summary

The summary report in a user table provides basic statistics on data in the table columns. To generate a summary report for a user table, choose Report (summary) from the Action box near the top of the user table form. The tool displays statistics (min, max, average, and so on) for columns of numerical data in the table. A link to a histogram of numeric and categorical values is shown in the first row for each column.

Click any link in the first row to display the distribution report for that column. In the distribution report, click a column header to sort the table by the values in the column. Choose Report (summary) in the Action box to return to the summary report.

## Automatically Selecting Objects in a User Table

You can direct the tool to automatically select objects in a user table using the Auto Select Object drop down option.

<!-- image -->

<!-- image -->

By default, Objects defined by Column and None are selected, which means that for a given value in a column, the tool tries to select the object according to the type of object defined by its column.

If you select Objects defined by object\_class , the tool tries to find and select the object type given by the object class with the name given in the full\_name column.

## Improved Bus Compression

You can compress bus signals that match the [*] bus notation [#], \_#\_/, or \_#/ where # is some number.

This option is available

- As a column context menu option for any column that contains some sort of full name for nets, pins, cells and timing points
- In the hierarchy view and in the Child List view

<!-- image -->

<!-- image -->

<!-- image -->

This action creates a user table that contains all the signals that match the bus notation bused together.

<!-- image -->

Click on one of the links under the Show column to bring up a new 'child' table that contains the individual bused signals. From this child table, if the signals are endpoints of timing paths, you might also have links to view a child table of timing path points in the table.

<!-- image -->

Use the up and down arrows at the top left to navigate back and forth between parent and child tables that were created in the drill down analysis.

## Viewing the Data as a Chart or Plot

To view the data in a user table as a chart or plot, use the column context menu button, Select Plot . The tool button is enabled only if the data in the selected columns contains numeric values.

You can select multiple columns and then create a plot based on the data in the selected columns of the user table.

<!-- image -->

The following figure shows the generated plot.

To filter the data by the values in the columns, mouse over the resultant plot and click Filter . You can use Plot Control to customize and control various options of the plot.

<!-- image -->

<!-- image -->

To view the last viewed plot, click on the last viewed plot tool button. This button is enabled only if you previously viewed a plot for this table.

<!-- image -->

## Using UPF and Power Analysis Tools

For multivoltage designs, the IC Compiler II GUI provides a UPF viewer, power state table view, and other tools to view the UPF power intent for your design and support the analysis of your design.

The following topics describe the UPF and power analysis tools:

- Viewing the UPF Power Intent
- Viewing the Power State Table

## Viewing the UPF Power Intent

The UPF diagram presents a graphical representation of the UPF power intent for your design. The UPF diagram displays UPF power domains, supply networks, power switches, isolation and retention strategies, and other elements of your UPF power intent. The UPF diagram supports zooming and panning, object selection, and querying of objects.

To view the UPF diagram, choose View &gt; Multivoltage UPF &gt; Power Domain / Root Cell from the menu, or click the Power Domain button ( ). Figure 32 shows the GUI with the layout, UPF diagram, and view settings displayed.

<!-- image -->

Figure 32 UPF Diagram View

<!-- image -->

## Power Domain View

When you first open the UPF diagram, the tool displays the power scope hierarchy in the power domain view. The power domain view displays information organized according to the power domain hierarchy. Power domains within the top-level power domain are represented as child modules of the top-level. Click on a power domain to select it, or right-click the power domain to select related cells, macros, or voltage areas, show the supply network view, or show the power state table.

For each power domain, supply sets are displayed near the top of the rectangle; each thick orange line represents a unique supply set. Click the line to select it. Right-click the line to view the context menu, then choose Show Supply Network View or Power State Table to view additional information about the supply set. Supply nets are displayed below the supply sets; each thin orange line represents a supply net.

Use the zoom and pan tools and commands to magnify and traverse the view. Use the arrow keys to scroll vertically or horizontally through the view. Select individual objects or objects in a rectangular area by using the Selection tool. Preview object information in an infotip by holding the pointer over the object. Display object information in the Query panel by using the Query tool.

<!-- image -->

<!-- image -->

Click the UPFDiagram tab in the View Settings menu to view the mapping of object type and color used in the power domain view. Click on a color square to customize the color for that object type.

If isolation cells are present, they are displayed below the supply nets. Hold the pointer over the isolation cell to view additional information in the infotip. Click the line to select it, or right-click the line to view the context menu. Use the context menu to select related objects or show the Supply Network View or the Power State Table. Ground nets are displayed at the bottom; each thin blue line represents a ground net.

Ports are displayed along the boundaries of the power domains. Input ports are denoted with the letter "I", and output ports with the letter "O".

## Supply Network View

The supply network view provides an alternate view of the power domains in your design. The view displays the connections between different power domains, isolation cells, switch cells, and other elements of the power domain. Similar to the power domain view, the supply network view organizes the view by power scope hierarchy. Right-click anywhere in the view and choose Show Supply Network View to show the supply network view as shown in Figure 33.

Figure 33 Supply Network View

<!-- image -->

## Viewing the Power State Table

You can use the Power State Table panel with the UPF diagram view to analyze and debug your isolation and level-shifter strategies. The tool displays the states for each supply in a power state table and shows their relationship in the UPF diagram view.

Figure 34 shows the Power State Table panel.

<!-- image -->

Figure 34 Power State Table

<!-- image -->

The Power State Table panel supports the following analysis types:

- Always-on analysis compares the on-off states between power and ground supplies

Always-on analysis compares the on-off states between supplies, including both power and ground supplies. This analysis produces one of the following states: More AO, Less AO, Equally AO, and Unrelated AO.

- Multivoltage level-shifter analysis compares the voltage relationships between power supplies

Multivoltage level-shifter analysis compares the voltage relationships between supplies. This analysis produces one of the following states: LH (low to high), HL (high to low), HL\_LH (high to low and low to high), or None.

<!-- image -->

## 4

## Using GUI Assistant Tools

The IC Compiler II GUI provides many assistants, such as the Task Assistant, Net Assistant, Pin Assistant, and Design Assistant to help you manage different objects in your design. For example, the Task Assistant consolidates commonly used commands into different flows to support design planning, timing analysis, placement, and other flows. The GUI Assistant Tools can simplify the design process.

The following topics describe how to work with the GUI:

- Using the Task Assistant
- Using the Design Assistant
- Setting Constraints With the Relative Location Constraints Tool
- Using the Netlist Tracer
- Using the Track Assistant

## Using the Task Assistant

The Task Assistant is an easy-to-use tool for navigating the design planning and other flows and executing individual tasks to create your design. The following sections describe the major features of Task Assistant .

## Starting the Tasks Toolbar and Task Assistant

To open the Tasks Toolbar, choose View &gt; Toolbars &gt; Tasks from the menu. The tool displays the tasks panel to the right of the layout view, as shown in Figure 35.

<!-- image -->

Figure 35 Tasks Panel

<!-- image -->

To display the list of tasks for a new category, click the down arrow to the right of the category box. To display the Task Assistant dialog box, click the tasks button ( ) to the left of the category box. Alternatively, choose Task &gt; Task Assistant from the menu.

## Navigating the Tasks in the Task Assistant Dialog Box

The Task Assistant dialog box provides buttons to navigate to the next or previous task in the task list, or to go backward or forward in the history list. On the left of the Task Assistant window, the tool provides a navigation pane with a table of contents. In the navigation pane, select the category at the top left to load the list of tasks for the category. Click any task in the navigation pane to load the corresponding form into the Task Assistant . Click the [-] icon in the navigation pane to collapse a task subcategory, click the [+] icon to expand the subcategory. Figure 36 shows some navigation features of the Task Assistant.

<!-- image -->

Figure 36 Task Assistant Navigation

<!-- image -->

If the list of tasks is hidden as shown in Figure 37, click the arrow to open it and click the pin to display the list of tasks.

Figure 37 Pinning the Navigation Pane

<!-- image -->

<!-- image -->

Alternatively, move your pointer to the left of the Task Assistant until you see two vertical bars. Click and drag the bar to the right to display the navigation bar.

<!-- image -->

Figure 38 Showing the Navigation Bar

<!-- image -->

## Previewing, Capturing, and Issuing Commands

After you complete the form data, check the preview window near the bottom of the form and verify the command to be run, as shown in the following figure. The window updates automatically as you enter data and select options in the form. Based on the type of data allowed for a given entry, the text box might restrict you from entering incorrect information.

Figure 39 Tcl Command Preview Window

<!-- image -->

You can change the command by changing a selection or text box entry. Click the Script button to copy the command to the Script Editor in the layout window in the IC Compiler II GUI. You can use the Script Editor tools to edit and save the command as needed.

<!-- image -->

<!-- image -->

After previewing the command, click Apply to run the command. The tool issues a warning message if a problem is detected in the command syntax. If a problem occurs, correct the form and try again.

## Using Overview Pages

Some tasks in the task list are operated from panels in the GUI. For example, the Hierarchy Exploration and What-if Congestion Analysis tasks are performed from the View &gt; Assistants &gt; Hierarchy Exploration and View &gt; Map &gt; What-if Channel Congestion tools in the GUI. For these tasks, the Task Assistant provides overview pages to help you understand the tool. Figure 40 shows the overview page for What-if Channel Congestion.

Figure 40 What-if Channel Congestion Overview Page

<!-- image -->

Click the link at the top of the page, or use the menu commands as described in the page, to open the tool in the GUI. Use the instructions in the overview page to guide you in performing the task.

## Editing Data in Tables

For tasks related to setting or reviewing constraint information, the Task Assistant provides editable tables for viewing or modifying the constraint data. The following shows the list of blocks displayed for the Block Shaping &gt; Shaping Constraints task.

## Figure 41 Instance Search

<!-- image -->

To edit a constraint,

1. Double-click a cell in the table
2. Use the Backspace key to delete the current entry
3. Enter a new constraint for the table cell

The tool displays the text in red if it is incomplete or incorrect. Valid values are displayed in black.

4. Press Return to confirm the new values

Figure 42 Editing Table Cell Data

<!-- image -->

## Using the Design Assistant

The Design Assistant helps you to locate and select objects in the layout view. To start the Design Assistant, choose View &gt; Assistants &gt; Design Assistant from the menu, or click the Design Assistant button.

<!-- image -->

Figure 43 Design Assistant

<!-- image -->

The following sections describe how to use the Design Assistant.

## Listing and Selecting Objects

The Design Assistant supports a search box for listing cell, net, pin, and topology objects. To populate the list of objects,

1. Click the Cells, Nets, Pins, or Topologies tab.

The Topologies tab is available only when you select Get Topology Plans from the context menu, or use the menu commands View &gt; Topology Plans of selected or View &gt; New Topologies .

2. Enter a search term in the box.

You can specify a full string, a sub string, a wildcard expression, a Tcl command, or a Tcl variable. For example, specify any of the following entries in the search box to match the cells u0\_0, u0\_1, u0\_2, u0\_3 (and possibly other cells).

3. Press Enter.
- Strings only: 'u', 'u0' or 'u0\_'
- Wildcards: 'u0\_*', 'u0\_?'
- A Tcl command: get\_cells "*" -filter name=~"u0*"

<!-- image -->

<!-- image -->

- A Tcl variable: $my\_cells (after performing set my\_cells [get\_cells "*" -filter name=~"u0*"] in the tool)
- A selection in the GUI: get\_selection (after selecting u0\_0, u0\_1, u0\_2, and u0\_3 in the layout view or Hierarchy Browser); you can also click the Get current selection button to the right of the search box to populate the list with the selected objects

After the list is populated, click the cell instance in the list to select the cell in the layout. Click and drag the pointer to select more than one cell, or press the Shift or Control key while clicking the cell to add the cell to the selection. To clear the selection, click the (X) at the right of the search box, or delete the characters in the search box and press Enter.

## Selecting Objects Using the Select Menu

The Select menu in Design Assistant enables you to quickly view and select related objects.

Table 6 Using the Select Menu

| To do this                                                                                                                                                               | Use this feature                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Select or highlight objects by object name or by a search filter expression.                                                                                             | Select by Name                                                                             |
| Add objects to a selection list                                                                                                                                          | Add to Selection                                                                           |
| View the objects that are selected such as topology plans, topology nodes, topology begin and end nodes, topology edges, topology repeaters, and MIB topology instances. | Selection List For more information, see the Using the Selection List and Work List topic. |
| View objects that are related to the selected objects                                                                                                                    | Related Objects                                                                            |
| Clear the selection list                                                                                                                                                 | Clear                                                                                      |

## Configuring Columns in the Design Assistant

To change the columns displayed in the Design Assistant, click the down arrow in the attribute group selector box near the bottom of the dialog box and click an entry in the list that appears. The list contains available attribute groups for this object type as shown in the following figure.

<!-- image -->

Figure 44 Design Assistant Attribute Group Selector

<!-- image -->

The entries in the table can be configured by using the Attribute Group Manager. Click the Modify Attribute Group button ( ) at the bottom right of the dialog box and click Manage All to open the Attribute Group Manager. For more information on the Attribute Group Manager, see Using the Attribute Group Manager.

You can also perform the following actions on column headers in the table:

- Sort the data in the list by clicking a column header.
- Reverse the sort order by clicking the column header again.
- Change the column order by clicking a column header and dragging it to its new location as shown in the following figure.

Figure 45 Rearranging Columns in the Design Assistant

<!-- image -->

- Sort columns by right-clicking the column header and selecting Sort Increasing or Sort Decreasing.

<!-- image -->

<!-- image -->

- Fit column widths to the Design Assistant dialog box by right-clicking the column header and selecting Fit All Columns or Fit Column as shown in the following figure.

Figure 46 Fit Column Widths in the Design Assistant

<!-- image -->

## Changing Property Settings for Multiple Objects

You can apply changes to property settings for multiple objects at one time. To change the settings for a property for multiple selected objects,

1. Select multiple objects in the Design Assistant by clicking the rows in the table while holding the Shift key. Alternatively, click and hold while dragging the mouse to select multiple rows.
2. Change the property for a single object by clicking its row and changing the value.
3. Click the Apply button to apply the changes to all selected objects.

<!-- image -->

Figure 47 Apply Changes to Multiple Objects in the Design Assistant

<!-- image -->

<!-- image -->

## Applying the Changes Automatically

To apply your changes automatically to your design, click Auto Apply Changes on the Cells, Nets, Pins, and Topologies tabs.

Figure 48 Apply Changes Automatically in the Design Assistant

<!-- image -->

## Synchronizing the Selection With the Global Selection

To ensure that the corresponding objects or rows are selected in the Design Assistant window when you select the objects in the Layout window, click the Synchronize Global Selection button on the Cells, Nets, Pins, and Topologies tabs from the Design Assistant window.

<!-- image -->

Figure 49 Synchronize With the Global Selection in the Design Assistant

<!-- image -->

## Performing Related Tasks

Each tab in the Design Assistant window supports a context menu that displays the different tasks you can perform on the list of objects. Move the pointer over an entry in the list and click the right mouse button to view the context menu. The context menu displays tasks related to the selected object. For example, if you open the context menu in the Cells tab, the context menu displays the Get Nets, Get Hierarchical Nets, Get Pins, and Create Bounds tasks for the selected object. Click the item in the context menu to perform the task. After you select the task from the context menu, the tool opens the appropriate tab and displays the information. Another example is, when you open the context menu on the Topologies tab, the context menu displays the Get Nets task for the selected object. To view or hide topology plans, perform the Show Topology Plans (hierarchical) or Hide Topology Plans task, respectively.

Note that you can perform the same related actions by choosing it from the menu bar. For example, to display nets for the selected item in the Cells tab, choose Cells &gt; Get Nets from the Design Assistant menu bar. The items in the menu bar change as you select different tabs in the Design Assistant.

You can also use the context menu to highlight an object, zoom in to view the object, write a Tcl command to a script file to select the object, and perform other tasks. Click the item in the context menu to perform the action.

<!-- image -->

## Using the Constraints Editor

Use the Constraints Editor panel to display and modify net, topology, and shaping constraints. Net constraints include nondefault routing rules and routing corridors associated with objects selected in the Nets tab. Shaping constraints include target location, parent object, boundary, utilization, and so on, which are set by using the create\_shaping\_constraint command. Topology constraints include topology nodes, edges, and repeaters associated with the topology plans that are selected on the Topologies tab.

To use the panel to review and modify all constraints,

1. Choose View &gt; Toolbars &gt; Constraints Editor from the Design Assistant menu or click the Constraints Editor tab.
2. Select an object in Nets, Topologies, or Shapeable view.
3. Click an object name in the table.
4. Click the constraint type in the constraint list to view the properties for that constraint.
5. (Optional) Modify the properties for the constraint in the properties editor table.
6. (Optional) Right-click over the constraint type in the constraint table and choose Select, Select Owners, or Delete to select or delete the constraint type.
7. (Optional) Click the Options button (the gear icon) to turn on the Synchronize Global Selection mode and allow a 2-way synchronization of global and Constraints Editor selections.

However, you cannot have both options in the Design Assistant view and Constraints Editor palette enabled at the same time; they are mutually exclusive.

To use the panel to review and modify net constraints,

1. Choose View &gt; Shapeable Objects from the Design Assistant menu.
2. Choose View &gt; Toolbars &gt; Constraints Editor from the Design Assistant menu or click the Constraints Editor tab.
3. Click an object name in the table.
4. Click the [+] symbol in the constraint list to view the properties for that constraint.
5. (Optional) Modify the properties for the constraint in the properties editor table.
6. (Optional) Click the right mouse button over the constraint type in the constraint table and choose Select, Select Owners, or Delete to select or delete the constraint type.

<!-- image -->

Figure 50 Design Assistant Net Constraints

<!-- image -->

The Constraints Editor supports expression-based filtering and column filtering. Click a constraint and press the forward slash (/) key to display the filter expression box. Alternatively, click the right mouse key over a column header and click the Show/Hide Filter Control button to display the filter expression box. Enter an expression in the box and press the Enter key to filter the results.

To perform column filtering, click the Show/Hide column filter control button. The tool displays a funnel icon to the right of each column heading. Click the icon to display the column filter menu as shown in the following figure.

<!-- image -->

Figure 51 Design Assistant Column Filtering

<!-- image -->

## Highlighting Objects

To highlight objects in the layout, move the pointer over the entry in the list, click the right mouse button to view the context menu, and click Highlight to highlight the object. Alternatively, select the object in the list and choose Highlight &gt; Selected from the Design Assistant menu bar. To clear a highlight, select the object and choose Highlight &gt; Clear Selected from the menu bar. Choose Highlight &gt; Clear All to clear all highlights.

## Reading and Writing Object Selection Scripts

To save a Tcl command that returns the list of currently selected objects in the current tab, choose File &gt; Write Script from the menu bar or click the right mouse button and select Write Script from the context menu. Note that you must have at least one object selected to perform this action. Navigate to the directory in which to save the file, enter the file name and click Save to write the file. The Design Assistant writes a script that contains a get\_pins , get\_nets , or get\_cells command followed by the names of currently selected objects.

To read a Tcl script from the Design Assistant, select File &gt; Read Script or click the right mouse button and select Read Script from the context menu.

<!-- image -->

<!-- image -->

## Setting Constraints With the Relative Location Constraints Tool

The Relative Location Constraints tool helps you set, review, and remove placement constraints for hard macros. To start the tool, choose View &gt; Assistants &gt; Relative Location Constraints from the menu. The Relative Location Constraints panel appears at the bottom of the layout as shown in Figure 52. The list box displays the hard macro instances in the design together with any relative location constraints that are specified. Sort the table by clicking a column header; click again to sort in the reverse order.

Figure 52 Relative Location Constraints Panel

<!-- image -->

## Manually Creating Relative Location Constraints

To create a relative location constraint,

1. Click the Create button to begin defining the constraint.
2. (Optional) Change the Offset type and other settings in the Mouse tool options toolbar as needed.
3. Click the corner of the target macro to be constrained as shown in Figure 53 (1).
4. Click the corner of the anchor object to define the anchor corner as shown in Figure 53 (2). If you have trouble, make sure the anchor object type is selectable in the View Settings panel.

<!-- image -->

The tool displays a constraint flyline between the corners of the target macro and anchor object as shown in Figure 53 (3); the constraints table in the Relative Location Constraints panel is updated to display the new constraint.

5. (Optional) Repeat steps 2 through 4 to define additional macro relative location constraints.
6. Press Esc to exit the Create Macro Relative Location Constraint tool.

Figure 53 Manually Creating a Relative Macro Constraint

<!-- image -->

## Automatically Creating Relative Location Constraints

The tool supports automatic creation of relative location constraints. To create the constraints for a selected set of macros,

1. Select one or more macros using one of the following methods:
- Click a row in the table.
- Click a row in the table and drag to select more than one macro.

- Click in the table and press Ctrl+A to select all macros.
- Click one or more macros in the layout.
2. Click the Auto-detect button.

The tool creates relative location constraints for all selected macros.

## Placing Macros Using Relative Location Constraints

To place the macros based on relative location constraints, click the Place button and click OK in the dialog box that appears. The tool runs the create\_macro\_relative\_location\_placement command to update the macro placement based on the relative location constraints.

## Removing Relative Location Constraints

To remove one or more relative location constraints,

1. Select one or more macros.
2. Click the Remove button to delete the constraints.

Figure 54 shows a constraint table with two macros selected. In this example, clicking the Remove button removes the constraints for the selected macros.

Figure 54 Removing Relative Location Constraints

<!-- image -->

## Writing Out Relative Location Constraints

To write out relative location constraints for all macros with defined constraints, click the Write button, choose Macro relative location, and enter a file name in which to save the constraints. The tool writes out a set\_macro\_relative\_location command for each macro with a defined macro relative constraint. The following example shows two defined constraints:

<!-- image -->

<!-- image -->

```
# macro_relative_constraints.tcl set_macro_relative_location \ -target_object [get_cells u1/REG_FILE_D_RAM] \ -target_orientation R0 -target_corner tr \ -anchor_object [get_blocks ORCA] -anchor_corner tr -offset { \ -0.1594 -0.2488} -offset_type scalable \ -used_length {0.0000 0.0000} -scale_edge {0 0} set_macro_relative_location \ -target_object [get_cells u2/SD_FIFO_RAM] \ -target_orientation MXR90 -target_corner br \ -anchor_object [get_blocks ORCA] -anchor_corner br -offset { \ -0.1715 0.2576} -offset_type scalable \ -used_length {0.0000 0.0000} -scale_edge {0 0} set_attribute -objects [get_blocks test:ORCA.design] \ -name edge_number -value 4 -quiet
```

## Writing Out Port Relative Location Constraints

To write out port relative location constraints for all I/O ports, click the Write button, choose Port relative location, and enter a file name in which to save the constraints. The tool writes out a set\_individual\_pin\_constraints command for each I/O port with a defined relative constraint. An example file for a design with two defined constraints is as follows:

```
# Port relative location constraints # Generated on Feb 3 12:51:21 ... set_individual_pin_constraints -ports [get_ports pad[15]] \ -sides 2 -offset [mrl_get_offset 2 0.5] set_individual_pin_constraints -ports [get_ports pad[14]] \ -sides 2 -offset [mrl_get_offset 2 0.5] ...
```

## Reading In Relative Location Constraints

To read in relative location constraints for macros or I/O ports, click the Read button and enter the script file name that contains the macro relative location constraints or I/O port relative location constraints. The tool reads the file and applies the constraints.

## Changing the Color of the Constraint Flylines

The tool displays constraint flylines between macros and objects when a macro relative constraint is defined. To change the color of the constraint flyline,

1. Click a color bar in the Appearance section near the top of the panel.
2. Select a new color from the Select Style dialog box and click OK.
3. Click Apply to apply your changes.

The tool redisplays the constraint flylines using the new colors.

## Using the Netlist Tracer

The IC Compiler II tool supports the Netlist Tracer for tracing the path of a net through the design. Start the Netlist Tracer by choosing View &gt; Assistants &gt; Netlist Tracer from the menu. Use the Netlist Tracer to trace a net by traversing its path through the design. Begin by selecting a cell, net, pin, or port from which to trace. You can traverse the path of nets that connect to the object, highlight the path, and zoom in on related cells, nets, and pins. As you trace the path, the Netlist Tracer displays flylines between the current object and any connected object.

Figure 55 Netlist Tracer

<!-- image -->

## Using the Track Assistant

Use the Track Assistant panel to examine routing tracks in the current design. The Track Assistant shows the bounding boxes for tracks on routing layers that you select and displays a track number to indicate the track position relative to the selected regions. You can display tracks by layer, width, preferred and nonpreferred direction, and obstruction.

<!-- image -->

<!-- image -->

To start the Track Assistant, choose View &gt; Assistants &gt; Track Assistant from the menu, or click the Track Assistant button ( ). The following sections describe how to use the Track Assistant. The following figure shows the Track Assistant panel.

Figure 56 Track Assistant

<!-- image -->

## Displaying Tracks

To display tracks by using the Track Assistant,

1. Start the Track Assistant by choosing View &gt; Assistants &gt; Track Assistant from the menu.
2. Zoom to the region of the layout to examine.
3. Select the layers for which to display tracks.

The tool displays the routing track using the track width for the selected layers as shown in the following figure. By default, the tool displays both unobstructed and obstructed tracks.

Figure 57 Before and After Track Display

<!-- image -->

## Displaying Track Information in Specific Regions

Use options available in the Track Assistant to limit the track display to specific regions of the design. To display track information only for certain regions in the design,

1. Start the Track Assistant and select layers as described in the previous section.
2. Click in an empty row in the Regions section and enter the bounding box for the region to display.

<!-- image -->

<!-- image -->

Alternatively, click the Specify Rectangle button ( ) and draw the region on the layout. To clear the region, move your mouse pointer over the bounding box coordinates in the panel and click the Clear region button ( ).

3. (Optional) Repeat the previous step to draw additional regions as needed.
4. (Optional) Create a region in which to hide the track display by clicking in an empty row in the Skip regions section and entering the bounding box for the region.

Alternatively, click the Specify Rectangle button ( ) and draw the skip region on the layout.

The following figure shows the layout and Track Assistant panel displaying only a specific region together with a skip region. Note that tracks are not displayed outside the defined region.

Figure 58 Track Assistant With Normal and Skip Regions

<!-- image -->

## Displaying Obstructed or Unobstructed Tracks

When you start the Track Assistant, the tool displays both obstructed and unobstructed tracks. To display only unobstructed tracks, select the Show unobstructed option and deselect the Show obstructed option. To display only obstructed tracks, deselect the Show unobstructed option and select the Show obstructed option. To highlight the obstruction, select the Show obstruction option.

The following figure shows the panel settings and layout when displaying obstructed tracks.

<!-- image -->

Figure 59 Obstructed Tracks

<!-- image -->

## Setting Track Assistant Options

The Track Assistant panel supports the following additional options:

- Display tracks in both the preferred and nonpreferred routing directions by choosing the Include non-preferred option.
- Display the routing tracks with the same pattern as the metal layers by choosing the Use shape fill pattern option.
- Set the color for the normal or skip regions by clicking the color bar below the region list and choosing a new color from the Select Style dialog box.

<!-- image -->

## Using Design Planning Tools

The IC Compiler II GUI provides tools to support various tasks in Design Planning. The What-if Channel Congestion tool supports interactive, what-if analysis to identify congested global routing channels. The Hierarchy Exploration tool supports several tasks related to module boundaries.

The following topics describe design planning tasks supported by the GUI:

- Hierarchy Browser
- Name Based Hierarchy Browser
- What-if Channel Congestion
- Hierarchy Exploration
- Topological Pin Constraints
- Working With Pin Constraints
- Performing Topology Interconnect Planning

## Hierarchy Browser

The tool provides tools to explore your design hierarchy and determine which logical hierarchy cells to commit to physical hierarchy blocks. The hierarchy browser in the GUI displays a view of the design hierarchy and provides other information about each hierarchy cell.

To explore the design hierarchy with the Hierarchy Browser,

1. Choose View &gt; Hierarchy Browser in the GUI.
2. Expand or collapse the hierarchy by clicking the [+] symbols next to the hierarchy cells.
3. Rearrange the display by clicking the column headers.
4. Click the block name to perform additional operations on the block.

An example hierarchy as displayed in the Hierarchy Browser is shown in Figure 60.

<!-- image -->

Figure 60 Hierarchy Browser

<!-- image -->

To perform the following actions with the context menu in the Hierarchy Tree view, rightclick the mouse over a logical hierarchy to open the menu.

- Choose Partitioning &gt; Create Module Boundary to create a module boundary for the specified level of hierarchy.
- Choose Partitioning &gt; Create Bound to create a module boundary and start the Create Bound tool in the layout window. Draw the bound in the layout window to complete the task.
- Choose Partitioning &gt; Copy Macro Relative Placement to copy hard macro relative placement to the selected module.
- Choose Color by Hierarchy &gt; Set Selected Color and choose a color from the menu to change to a specific color.
- Choose Commit Block to commit a logical hierarchical cell to a physical hierarchy block.
- Choose Clear Selection to deselect all selected objects in the hierarchy.
- Choose Select Related Objects and choose an item from the list to select the connections, macros, safety core rules, safety core groups, and so on, associated with the object.

<!-- image -->

You can also view the related objects from one of the following:

- The Layout view
- The Select menu:
- Select &gt; By Name Toolbar (or)
- Select &gt; By Name (or)
- Select &gt; Related Objects (or)
- The context sensitive menu (Right click an object &gt; Select Related Objects ) For example, when you select a topology edge or a topology plan, the context menu displays:

<!-- image -->

Use the Selection List panel, the Properties panel, or the Queries panel to view more details about the selected objects.

- Choose Properties to open a dialog box that displays the properties for the selected logical hierarchy.
- Choose Expand Tree to display the sub hierarchies for the selected logical hierarchy.
- Choose Copy Text to copy the name of the selected cell. The copied text is available in both the copy buffer and the clipboard.

You can access this feature from the Hierarchy Tree and Child List views.

<!-- image -->

<!-- image -->

- Choose Find Copied Cell Text to search for a copied cell and select it in the Hierarchy Tree view.

This feature is available only when you have copied a cell name using the Copy Text feature.

- Choose Set Hierarchy Root &gt; Set Root to Current Selected Cell to change the root of the hierarchy tree and perform actions on the selected object.

Right-click the mouse over a column heading to open the context menu. You can perform the following actions from the context menu in the Child List view. Note: The context menu is available only for specific headings.

- Choose Compress Bus Objects (User Table) to export the objects with bus notation to a User Table and compress all common object names into a single bused object.
- Use the filter options from the context menu of the compressed User Table to view the bused objects, the bus contents, or return to the full bused table.

You can perform the following action from the TreeMap view:

Choose Outliers on the Hier Std Color dialog to highlight those cells in your design that fall outside of the specified range of minimum and maximum values.

## Filtering Information in the Hierarchy Browser

The hierarchy browser supports column filtering and a filter box to filter the information in the table. To display the filter expression box, do one of the following:

- Press the forward slash key (/), or
- Right-click the mouse over a column header for the filtering options.

Figure 61 Enable Filtering

<!-- image -->

Enter an expression in the expression box to display only the entries that match the expression.

<!-- image -->

Figure 62 Filter Expression

<!-- image -->

To enable column filters, click the Show/Hide Column filter control button to the right of the filter box. Alternatively, click the right mouse button over a column header and click the button in the context menu as shown in the following figure.

Figure 63 Enable Column Filters

<!-- image -->

To view the Column Filter menu, click the funnel icon. Use the options in the menu to sort the column in increasing or decreasing order, create a filter condition, or filter the column by selecting specific values in the column. The filter menu is shown in the following figure.

<!-- image -->

Figure 64 Column Filter Menu

<!-- image -->

## Name Based Hierarchy Browser

For flat designs, the tool provides the Name Based Hierarchy Browser to display the implicit hierarchy in the design and allows you to perform actions on the hierarchies. To start the Name Based Hierarchy Browser, choose View &gt; Name Based Hierarchy Browser The tool displays the browser as shown in Figure 65. If your design contains hierarchy, the selection is disabled and you cannot use this feature.

<!-- image -->

Figure 65 Name Based Hierarchy Browser

<!-- image -->

The tool extracts the hierarchy based on the setting of the

gui.name\_based\_hier\_delimiter application option. By default, the value is "/". You can convert your design to a flat design with the ungroup\_cells -all -flatten command.

Similar to the Hierarchy Browser, you can perform different actions by using the context menu; right-click the mouse over a hierarchy to display the context menu:

- Select Set Colors On Top Hierarchies to assign a color to each of the top-level hierarchies
- Select Clear All Hierarchy Colors to remove all colors from the hierarchies
- Select Set Selected Hierarchy Color and choose a color to assign a color to the selected hierarchy
- Select Clear Selected Hierarchy Color to remove the color from the currently selected Hierarchy
- Select Show Child List to split the dialog box and display a list of cells in the selected hierarchy
- Select Expand All Hierarchy Trees and select the number of levels to show the subhierarchies for all top-level hierarchies
- Select Expand Selected Hierarchy Trees and select the number of levels to show the subhierarchies for the selected hierarchy
- Select Copy Hierarchy Path to copy the instance path for the current hierarchy to the clipboard

For information on filtering results in the table, see Filtering Information in the Hierarchy Browser.

<!-- image -->

## What-if Channel Congestion

The IC Compiler II tool supports interactive, what-if analysis to identify congested global routing channels. To open the What-if Channel Congestion map mode in the layout window, select What-if Channel Congestion in the Design Planning section of the Task Assistant, or choose View &gt; Map &gt; What-if Channel Congestion . The What-if Channel Congestion map mode appears on the right of the layout window as shown in Figure 66.

<!-- image -->

Figure 66 What-if Channel Congestion Map Mode and Reload Dialog Box

<!-- image -->

<!-- image -->

## Performing Global Routing for What-if Channel Congestion

To begin what-if congestion analysis,

1. Click the Reload button to open the Calculate What-If Channel Congestion Map Data dialog box.
2. Select Whole design area or Specified area to choose the area of the design to evaluate.
3. (Optional) Change the value in the Max Channel Width box to set the size of the largest channel to display; see Filtering by Minimum Channel Dimension for more information about filtering by channel width.
4. (Optional) Change the Segment Length; see Displaying Channel Segments for more information about segment length.
5. (Optional) Select Use existing global route result to use the existing route information from the route\_global -congestion\_map\_only true command.

You can use the remove\_routes -global\_route command to remove global routes from your design.

6. Click OK to create the congestion map.

## Viewing Congestion Information

After global routing completes, the tool highlights each congested channel in the design. To display additional information about the channel, move the pointer over the channel and view the infotip. The infotip displays the demand and capacity for the channel and for each layer of metal in the preferred routing direction within the channel. Figure 67 shows the infotip displayed for a congested channel.

Figure 67 What-if Channel Congestion Infotip

<!-- image -->

## Filtering by Minimum Channel Dimension

To display only narrow channels in your design, click the Reload button, enter a channel width value in the Max channel width box, and click OK. The tool updates the display and hides channels where the smallest dimension (height or width) is greater than the specified maximum channel width value as shown in Figure 68.

<!-- image -->

Figure 68 Filtering by Minimum Channel Dimension

<!-- image -->

## Displaying Channel Segments

To perform a more detailed analysis and partition the channel into smaller segments, enter a value in the Segment length box. The tool subdivides each channel and creates segments of the specified length as shown in Figure 69. Move the pointer along the channel to view detailed congestion information for each channel segment in the infotip.

Figure 69 Channel With Segments

<!-- image -->

Note that the segment dimension might not exactly match the value you specified. In some cases, the tool grows or shrinks the segment to create segments of a uniform size.

## Specifying the Region for Analysis

By default, the tool generates a what-if congestion map for the entire design. You can speed up the congestion analysis by specifying a region in which to limit the analysis. Click

the button to the right of the Region box, draw a rectangle in the layout window, and click Apply to restrict the analysis to the drawn area. Alternatively, specify the coordinates for a bounding box in the Region box and click OK to analyze only the area you specified.

<!-- image -->

## Scaling the Congestion Color Mapping

The tool colors each channel based on the ratio of required routes to the number of available routes in the channel. By default, any channel where the ratio exceeds 1.0 (the number of required routes exceeds the number of available routes) is colored red, and a channel where the ratio is less than 0.2 is colored purple.

To change the way the channels are colored, enter values in the From: and To: boxes and click Apply. The tool redisplays the congestion map and colors the channels based on the values.

<!-- image -->

## Correcting Congestion Problems

To reduce routing congestion interactively with What-if Channel Congestion analysis, do the following:

1. Select the hard macro which abuts the congested area
2. Press M or select the Move tool from the toolbar
3. Move the hard macro with the mouse to create a wider channel in the congested area

Alternatively, press the Tab key and enter the x- and y-offset in the Delta box in the Move toolbar and press Enter. The tool moves the hard macro by the specified distance. After you move the hard macro to the new location, the tool redisplays the congestion map based on the updated placement.

Repeat these steps until you are satisfied with the congestion map and placement. The layout before and after repair is shown in Figure 70.

<!-- image -->

Figure 70 What-if Congestion Repair

<!-- image -->

## Updating the Placement

After adjusting the channel widths, update the cell placement by clicking the Place button. The tool runs the create\_placement -floorplan -effort medium command to update the placement while keeping cells near their original locations.

## Showing Nets in a Channel

To show the net connections that occupy a specific channel, click the Nets button and click in a channel. The tool displays the nets that pass through the channel and their path outside the channel. Figure 71 shows the layout before and after displaying the nets that pass through the channel. To clear the display, click anywhere outside the channel.

<!-- image -->

Figure 71 Displaying Nets in the Channel

<!-- image -->

## Removing the Congestion Map

To remove the What-if Channel Congestion map from the layout, close the What-If Channel Congestion map mode panel.

## Hierarchy Exploration

In the IC Compiler II tool, module boundaries represent uncommitted blocks in the logical hierarchy. Using module boundaries, you can quickly assess the approximate block size that is required for a given utilization for a top-level block and arrange module boundaries within the floorplan for rough estimation of block placement.

To open the Hierarchy Exploration panel in the layout window, select Hierarchy Exploration in the Design Planning section of the Task Assistant or choose View &gt; Assistants &gt; Hierarchy Exploration in the GUI. The Hierarchy Exploration panel appears on the right of the layout window.

## Creating Module Boundaries

To create module boundaries, click the Initialize button in the Hierarchy Exploration panel. The tool inserts module boundaries for the top-level modules as shown in Figure 72.

<!-- image -->

Figure 72 Initialized Module Boundaries

<!-- image -->

You can perform the same operation with the explore\_logic\_hierarchy -create\_module\_boundary command.

<!-- image -->

<!-- image -->

You can create module boundaries for selected modules using the Hierarchy Browser in the GUI. To create module boundaries with the Hierarchy Browser,

1. Choose View &gt; Hierarchy Browser
2. Select a logical hierarchy block
3. Select Create Module Boundary from the context menu, or click the Create button in the Module Boundaries section of the Hierarchy Exploration panel

## Expanding, Collapsing, and Removing Module Boundaries

To expand a module boundary into child modules, select the module boundary and click Expand. To collapse a module boundary into its parent module, select the module boundary and click Collapse. To remove one or more module boundaries, select the module boundaries and click Remove. To remove all module boundaries, click Remove All.

You can also perform these operations by using the context menu.

1. Select one or more module boundaries
2. Right-click in one of the selected module boundaries and choose the operation (Expand, Collapse, or Remove Module Boundary) from the context menu

## Coloring Module Boundaries

To apply a unique color to each module boundary, click Color. Click Color again to apply a different color scheme. To remove any coloring from the module boundaries, click Clear.

## Placing Module Boundaries

To place module boundaries into the core area,

1. Choose the placement type, rectangular or rectilinear. See Figure 73 for an example of both placement types
2. Select Use existing cell placement to place module boundaries based on the existing placement
3. Click Place All to place the module boundaries into the core area

Figure 73 Rectangular and Rectilinear Module Boundary Placements

<!-- image -->

To move inside the module boundary any hard macros that belong to a module bound, click Update Macros.

## Hierarchy Exploration and Module Color

The Hierarchy Exploration panel provides tools to add color to module boundaries and their corresponding standard cells and macros within the design boundary. The tool also draws a boundary around different hierarchies within the design. You can access these functions by choosing 'Color by Hierarchy' in the Task section at the top of the panel.

<!-- image -->

Figure 74 Color by Hierarchy in Hierarchy Exploration

<!-- image -->

## Viewing Hierarchies in the Layout

To highlight different hierarchies in the layout,

1. Choose View &gt; Assistants &gt; Hierarchy Exploration from the menu.
2. Select 'Color by Hierarchy' in the Task section of the panel.
3. Create the module boundaries by clicking Initialize in the Module Boundaries section of the panel.

The tool highlights and selects all top-level hierarchies.

<!-- image -->

<!-- image -->

4. (Optional) Change the module color by clicking Color and remove all module colors by clicking Clear.
5. (Optional) Change the hierarchies that are highlighted by opening the Hierarchy Browser and selecting one or more hierarchies.

## What-if Partitioning

What-if partitioning helps you to examine the relation between different module boundaries and organize the hierarchy of module boundaries by creating virtual groups. During what-if partitioning, you

- View the connectivity between different module boundaries by using the Net Connections or Data Flow Flylines tools
- Create virtual groups that contain connected module boundaries
- Investigate different partitioning strategies by placing, combining, or removing virtual groups
- Write out the module boundary groupings for resynthesis

To display the connectivity between module boundaries,

1. Click the Net Connections button in the Hierarchy Exploration panel.
2. Select Selected to Selected in the Connectivity Display section of the Net Connections panel.
3. Click on a module boundary, then click on one or more additional boundaries to view the connectivity between them.

To create a virtual group,

1. Select only the module boundaries or module groups that you want to combine into a new module group.
2. Click the Create button in the Virtual Grouping section of the Hierarchy Exploration panel.
3. (Optional) Ungroup a virtual group by selecting the group and clicking the Remove button.

In the left image in Figure 75, two module boundaries are selected, and net connections for the selected modules are displayed. The two modules are good candidates for grouping because they share common net connections. In the right image, the modules are grouped after clicking the Create button. You can move the pointer over the module group to display information about the group in the infotip.

Figure 75 Creating a Virtual Group of Two Modules

<!-- image -->

If your selection includes an existing virtual group and other module boundaries, the module boundaries are added to the existing virtual group.

To report the current module boundaries and groups in the layout after creating a virtual group of module boundaries, click the Groups and Boundaries button in the Report section. The tool opens the Groups and boundaries panel and displays a list of virtual groups and module boundaries in the layout. The tool also writes the information to the module\_boundary.results file as follows:

```
icc2_shell> sh cat module_boundary.results virtual group:   RISC_CORE_group I_ORCA_TOP/I_RISC_CORE I_ORCA_TOP/I_PCI_TOP I_ORCA_TOP/I_BLENDER_4 module boundary: I_CLOCK_GEN module boundary: I_ORCA_TOP/I_SDRAM_TOP ... ***** End Of Report *****
```

To create a script which contains Tcl commands to create a new level of hierarchy using the virtual group, click the To Script button in the Virtual Groups section. The tool opens the Script Editor and writes group\_cells and explore\_logic\_hierarchy commands you can use to re-create a new level of hierarchy from the virtual group. An example script is as follows:

```
### Virtual Grouping Commands For Group: RISC_CORE_group group_cells { I_ORCA_TOP/I_RISC_CORE I_ORCA_TOP/I_PCI_TOP \ I_ORCA_TOP/I_BLENDER_4 } -cell_name RISC_CORE_group if { [get_bounds -quiet RISC_CORE_group] ne {} } { explore_logic_hierarchy -virtual_ungroup RISC_CORE_group
```

<!-- image -->

<!-- image -->

```
explore_logic_hierarchy -create_module_boundary \ -cell [get_cells -quiet -hierarchical RISC_CORE_group] } ### End Virtual Grouping Commands For Group: RISC_CORE_group
```

To commit selected module boundaries to blocks, click To Blocks in the Commit section of the Hierarchy Exploration panel.

To commit selected module boundaries to bounds, click To Bounds in the Commit section of the Hierarchy Exploration panel.

## Topological Pin Constraints

The Topological Pin Constraints tool enables you to create pin constraints in the GUI by specifying a net and drawing a rectangular region in which the feedthrough must be routed. To start Topological Pin Constraints tool, choose Create &gt; Topological Pin

Constraint from the menu or click the ( ) button. To view or edit information about the pin constraint, click the button circled in Figure 76 to open the Topological Pin Constraints dialog box.

Figure 76 Topological Pin Constraints

<!-- image -->

To create topological pin constraints for a design with multiple levels of hierarchy, click the multiple levels active box in the View Settings panel as shown in the following figure.

Figure 77 Multiple Levels Active

<!-- image -->

## Working With Pin Constraints

Use Design Assistant to create, show, and modify the individual, bundle, and block pin constraints.

| To do this                                                               | Use this                                                                                                                                                                                          |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create pin constraints                                                   | 1. Design Assistant > Nets (or) Design Assistant > Pins 2.Select the nets or bundles (or) Select the ports or pins 3. Create > Pin Constraint                                                     |
| Create block constraints                                                 | In Design Assistant , choose Create > Block Pin Constraint                                                                                                                                        |
| View the pin constraints and block pin constraints in the current design | In Design Assistant , choose: • View > Pin Constraints of selected (or) • View > Block Pin Constraints of selected (or) • View > Pin Constraints (or) • View > Block Pin Constraints              |
| Show the currently defined pin constraints for selected objects          | In Design Assistant , 1.Select the nets or pins 2.Right-click and choose Get Pin Constraints (or) View > Pin Constraints of selected The pin constraints are displayed on the PinConstraints tab. |

Table 7 Supported Pin Constraints Operations From the GUI

<!-- image -->

<!-- image -->

Table 7 Supported Pin Constraints Operations From the GUI (Continued)

| To do this                                                            | Use this                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Show the currently defined block pin constraints for selected objects | In Design Assistant , 1.Select the block cells ( is_soft_macro == true ) 2.Right-click and choose Get Block Pin Constraints (or) View > Block Pin Constraints of selected The pin constraints are displayed on the BlockPinConstraints tab. |
| Delete pin and block pin constraints                                  | In Design Assistant , select Edit > Delete Pin Constraints                                                                                                                                                                                  |
| Select the objects related to the pin constraints                     | Select the pin constraints and choose Select > Related Objects to select the related bundles, nets, pins, or ports                                                                                                                          |

## Performing Topology Interconnect Planning

You can use the topology interconnect planning methodology to define and create a routing topology for large collections of bus signals. For more information, see the Topology Interconnect Planning topic in the IC Compiler II Design Planning User Guide .

In the topology interconnect planning flow, unified topology constraints provide a common constraint language and methodology for creating the routing topology for bus signals in the layout. The basic building components of UTC are topology plans, topology nodes, topology edges, topology repeaters.

The following sections describe some of the actions that you can perform on these components from the GUI.

- Using the Topology Toolbox
- Using the Create Topology Layout Tool
- Using Custom Symbols to Represent Topology Nodes
- Using the Move Topology Object Tool
- Attaching Topology Nodes With Valid Overlapped Objects
- Daisy Chaining Topology Nodes
- Setting Topology Edge Shape Layers
- Working With Topology Groups and Topology Plans

- Working With Bundle Objects
- Viewing Estimate Topology Timing Results in GUI

## Using the Topology Toolbox

You can access all topology interconnect planning-related commands and utilities from Topology Toolbox ( View &gt; Toolbars &gt; Topology Toolbox or View &gt; Assistants &gt; Topology Toolbox )

| Section   | Tool GUI   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Toolbar   |            | Includes the following buttons: • Design Assistant - To perform design planning tasks • Create Topology Layout - To create topology objects such as nodes, edges, and repeaters • Lock - To lock a selected object in its position for editing • Unlock - To unlock a selected object • Set topology objects visible • Set topology objects invisible • Set net estimation rule • Associate selected annotation shapes with topology plan - To associate a selected or current topology plan with selected annotation shapes. This action is disabled if you select more than one topology plan. After you associate an annotation shape with a topology plan, its visibility is determined by the visibility of associated topology plan in addition to the annotation shape visibility setting in the View Settings panel. |
| Plan      |            | Includes the following buttons: • Create - To create a topology plan • Characterize - To characterize a topology plan • Create Default - To create a default topology plan • Refine - To refine a topology plan • Create Group - To create a topology group • Uniquify - To uniquify a topology plan • Optimize - To optimize a topology plan • Write - To write a topology plan                                                                                                                                                                                                                                                                                                                                                                                                                                             |

Table 8 Topology Toolbox

<!-- image -->

<!-- image -->

| Section    | Tool GUI   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select     |            | Includes buttons to: • Select related topology plans • Select related topology edges • Select related topology nodes • Select related topology repeaters • Select connected topologies                                                                                                                                                                                                                                                                                                                                                   |
| Edit       |            | Includes buttons to: • Move or attach topology objects • Merge topology nodes • Remove selected topology nodes • Associate valid overlapped object with selected topology nodes • Remove routes associated with topology plans                                                                                                                                                                                                                                                                                                           |
| Edge       |            | Includes buttons to: • Automatically cycle shapes with different options Cycle: Auto →L-Shape (x) →L-Shape (y)→ S-Shape (x) →S-Shape (y) • Automatically set the shape of the edges • Set edge L-Shape (X-First) that is, horizontal first • Set edge L-Shape (Y-First) that is, vertical first • Set edge S-Shape (X-First) • Set edge S-Shape (Y-First) • Reverse edge direction • Set edge layers from net estimation rule • Estimate topology edges • Reset estimate topology edges that is, reset the width for edge shape to zero. |
| Connection |            | Includes buttons to: • Create fishbone connection • Create chain connection • Create star connection • Connect nodes to the left • Connect nodes to the right • Connect nodes up • Connect nodes down                                                                                                                                                                                                                                                                                                                                    |
| Analyze    |            | Includes buttons to: • Check topology plan • Estimate topology plan                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

Table 8 Topology Toolbox (Continued)

<!-- image -->

Table 8 Topology Toolbox (Continued)

| Section   | Tool GUI   | Description                                                                                                                                                                                     |
|-----------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Implement |            | Includes buttons to: • Create topology trunk • Implement topology repeater • Remove routes associated with topology plans • Remove placed and created repeaters for the selected topology plans |

## Customizing the Topology Toolbox

To add frequently used actions to the Topology Toolbox, you can customize the toolbox and add the actions to a new User section.

In the following example, two buttons are added to the Topology toolbox, Nudge Left and Nudge Right , which pan the view slightly to the left and right.

```
gui_create_menu -menu "My_Menu->&Nudge_Right" \
```

```
-tcl_cmd {gui_scroll \ -window [gui_get_current_window -view] -hrel .05} gui_create_menu -menu "My_Menu->&Nudge_Left" \ -tcl_cmd {gui_scroll \ -window [gui_get_current_window -view] -hrel -.05} gui_set_pref_value -category topologyToolbox \ -key userButtonsList -value "My_Menu->Nudge_Right My_Menu->Nudge_Left"
```

<!-- image -->

## Using the Create Topology Layout Tool

To create topology objects, such as nodes, edges, and repeaters, use the Create Topology Layout tool. You can also create topology edges with mixed values (percentage and distance) for the shape layers.

Use the tool to define connections between bump regions for die-to-die connections. You can also associate topology nodes with bump region as with any other valid object by using the create\_topology\_node command, in Create Topology Layout tool, Move Topology Object tool, or through Properties Editor.

<!-- image -->

<!-- image -->

You can use the topology layout tool as follows:

1. Select a topology plan in the Design Assistant &gt; Topologies tab.
2. Open the Create Topology Layout toolbar, by using one of the following methods:
- In the Design Assistant &gt; Topologies tab, choose Create &gt; Topology Layout .
- In the Design Assistant &gt; Topologies tab, right-click on the topology plan and click Topology Layout .
- In the block window, choose Create &gt; Topology Layout .
3. In the layout view, click on a topology node object that you want to connect or start with a new topology node.
4. Move your cursor to the next target, maybe an existing or new topology node. As you move the pointer, the tool outlines only objects that can be associated with the new node.
5. Click your mouse button to place a node.
6. Click on the end object (topology node) to complete the route or double-click to finish it with the new node.

Figure 78 Create Topology Layout Toolbar

<!-- image -->

To reset the options to their defaults, use the appropriate icon on the Create Topology Layout toolbar (see Figure 78).

To undo the changes you made, choose Edit &gt; Undo .

<!-- image -->

Table 9 Create Topology Layout Tool Options

| Options   | Description                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------|
| Plan      | Specifies the name of the topology plan to which the new nodes, edges, and repeaters are added. |
|           | Creates a topology plan.                                                                        |
| Add       | Specifies the type of objects to add.                                                           |
| Angle     | Sets the starting input direction in orthogonal input mode.                                     |

| Options                                  | Description                                                                                                                                                                                                                             |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Orthogonal                               | Toggles the orthogonal input direction.                                                                                                                                                                                                 |
| Node                                     | Specifies the node constraint type for topology nodes.                                                                                                                                                                                  |
| Edge                                     | When set to Split, inserts the new node in the middle of topology edge, splitting the last one into two; otherwise, creates a tap node.                                                                                                 |
| Horizontal Layer/Width/Length Percentage | Specifies the shape layer and width for horizontal edges. When the horizontal length percentage option is selected, the tool sets the horizontal edge shape length in percentage; otherwise, the edge length is set to absolute length. |
| Vertical Layer/Width/Length Percentage   | Specifies the shape layer and width for vertical edges. When the vertical length percentage option is selected, the tool sets the vertical edge shape length in percentage; otherwise, the edge length is set to absolute length.       |
| Snap                                     | Turns on and off snapping of topology nodes to the visible or selectable objects.                                                                                                                                                       |
| Delta                                    | Specifies offset information relative to the active inference point when entering points for layout editing.                                                                                                                            |
| More > Node > Attach                     | When set to true, preselects and annotates the valid objects the node can be attached to.                                                                                                                                               |
| More > Node > Prefer pins                | When set to true, associates the topology node with pins rather than with blocks.                                                                                                                                                       |
| More > Node > Routing target             | Specifies whether nodes of constraint types edge, side, and bounding box can be routing targets.                                                                                                                                        |
| More > Actions > Auto apply              | When set to true, finishes input when the new node (end node of the edge) is associated with any valid object (block, pin, port, and so on).                                                                                            |
| More > Show > Port Guidance              | Displays guidance for pin connections and locations.                                                                                                                                                                                    |
| More > Show > Flylines                   | Displays flylines for the pins or flyline to the nearest open for the specified nets.                                                                                                                                                   |
| More > Show > Routes                     | Highlights the specified nets or bundles.                                                                                                                                                                                               |

Table 9 Create Topology Layout Tool Options (Continued)

<!-- image -->

<!-- image -->

## Using Custom Symbols to Represent Topology Nodes

By default, the tool uses the following conventions to represent the topology nodes.

<!-- image -->

If needed, you can use custom symbols to represent these nodes. To use custom symbol,

1. In the Layout View, select the node.
2. Open Properties Editor .
3. Switch to Application attribute group.
4. Select one of the symbols from the symbol drop-down list.
5. Click Apply Changes ( ).

<!-- image -->

<!-- image -->

## Using the Move Topology Object Tool

To move and associate or dissociate topology nodes with allowed objects, use the Move Topology Object tool. However, to automatically associate many topology nodes at the same time, see the Attaching Topology Nodes With Valid Overlapped Objects topic.

Figure 79 Move Topology Object Toolbar

<!-- image -->

The flow is as follows:

1. Choose Edit &gt; Topology &gt; Move .
2. Click on the topology node that you want to modify.
3. Move the node to a new location.

To reset the options to their defaults, use the appropriate icon on the Move Topology Object toolbar (see Figure 79).

To undo the changes you made, choose Edit &gt; Undo .

The Node , Edge , More , Snap , and Delta options on the Move Topology Object toolbar have the same behavior as those options on the Create Topology Layout toolbar. For more information, see Table 9.

<!-- image -->

<!-- image -->

To use the layer color for shape layers in topology edges or to use different colors for beginning, intermediate, and ending topology nodes, use the options as shown in Figure 80.

Figure 80 Using Coloring for Topology Edges and Topology Nodes

<!-- image -->

## Attaching Topology Nodes With Valid Overlapped Objects

To automatically attach topology nodes to valid objects that overlap these nodes, while copying or moving topology plans or edges to the target location, use the attach\_topology\_nodes command. However, to attach topology nodes one by one, use the Move Topology Object tool (for more information, see the Using the Move Topology Object Tool topic).

The valid overlapped objects are,

- Annotation shapes
- Bounds
- Bound shapes
- Bump regions
- Cells
- Pins

- Ports
- Shapes
- Placement blockages
- Routing blockages
- Topology edges
- Terminals
- Voltage areas
- Voltage area shapes

In case of many overlapping objects, pins and ports have higher priority over cells and cells have priority over other types of objects.

In the following example, the tool tries to attach all the topology nodes in topology plan tp1 with the valid objects.

```
icc2_shell> attach_topology_nodes [get_topology_nodes \ -of_objects [get_topology_plans tp1]]
```

For more information, see the attach\_topology\_nodes command man page.

## Daisy Chaining Topology Nodes

To quickly connect or daisy chain selected or specified topology nodes in the current block in a given direction:

1. In the layout view, select the topology nodes you want to connect.
2. Create topology edges between the selected nodes in a specified direction, choose Edit &gt; Topology &gt; Connect Nodes Down (Up, Left, Right) .

Alternatively, you can use the corresponding context-sensitive menu commands or the connect\_topology\_nodes command.

## Note:

If some nodes are already connected, they are omitted from operation.

<!-- image -->

Table 10 Connecting Topology Nodes

Connecting Topology Nodes Down

Connecting Topology Nodes Left

<!-- image -->

Connecting Topology Nodes Up

<!-- image -->

Connecting Topology Nodes Right

<!-- image -->

<!-- image -->

## Setting Topology Edge Shape Layers

The tool enables you to set shape layers for selected or specified topology edges, or reverses their direction.

<!-- image -->

<!-- image -->

1. In the layout view, select topology edges for which you need to set the shape layers.
2. Choose Edit &gt; Topology and do one of the following:

Table 11 Setting Shape Layers for Topology Edges

| To do this                                                                                                           | Use this feature                |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------|
| L-shape with first segment in x-direction                                                                            | Set Edge L-Shape (X First)      |
| L-shape with first segment in y-direction                                                                            | Set Edge L-Shape (Y First)      |
| S-shape with first segment in x-direction                                                                            | Set Edge S-Shape (X First)      |
| S-shape with first segment in y-direction                                                                            | Set Edge S-Shape (Y First)      |
| The shape template is chosen automatically with respect to the access direction of the start and end topology nodes. | Set Topology Edge Auto          |
| Reverse edge direction by swapping start and end nodes.                                                              | Reverse Topology Edge Direction |
| Update the shape layers of an edge with respect to the net estimation rule layer definitions                         | Set Edge NER Layers             |

## Working With Topology Groups and Topology Plans

- Setting the Current Topology Group
- Removing Topology Groups
- Viewing and Editing Aggregate Attributes of Topology Groups
- Uniquifying Topology Plans
- Automatically Select Topology Plans
- Merging Stacked Topology Nodes

Topology groups enable you to divide your topology plans into multiple smaller groups. You can then work on the smaller chunks independently, which essentially helps in dividing a large design into manageable chunks. It also enables you to group similar topology plans that allows you to take actions such as modify, remove, and so on on a set of topology plans.

The flow is as follows:

1. Create a net estimation rule

A net estimation rule defines the routing layers, nondefault routing rule, repeater cell name, repeater cell spacing, clock, and other routing- and timing-related constraints. After creating a topology plan, associate a net estimation rule with the topology plan. If needed, you can associate multiple net estimation rules to a topology plan or a topology edge from the Properties Editor panel, Design Assistant , or from the automatically generated command forms (for example, the create\_topology\_plan command dialog box).

- a. Open the Design Assistant by choosing View &gt; Assistants &gt; Design Assistant .
- b. Choose Create &gt; Net Estimation Rule .
- c. Enter information in the set\_net\_estimation\_rule dialog box, if required, and click OK .

You can also create a net estimation rule by using the context-sensitive menus on the TopologyPlans and TopologyGroups tabs of the Design Assistant (Right-click on a topology plan or a topology group and choose Create Net Estimation Rule from the menu).

For more information on creating a net estimation rule, see the Creating Net Estimation Rules for Topology Plans topic in the IC Compiler II Design Planning User Guide .

2. Create topology plans for the nets
- a. Click on the Nets tab and use the get\_nets command to populate the list.
- b. Select the nets from the list, right-click the selection, and select Create Topology Plan .
- c. Enter information in the create\_topology\_plan dialog box, if required, and click OK .
- d. Open the TopologyPlans tab by choosing View &gt; New topology Plans .
- e. On the TopologyPlans tab, use the get\_topology\_plans command to view the newly created topology plans.
- f. Create as many topology plans as needed to serve your purpose.

At the time of creation, all topology plans are assigned to a default topology group, DEFAULT\_TOPOLOGY\_GROUP . The group column shows the topology group to which the topology plan is associated with. You can also right-click on a topology plan and choose Get Topology Group from the context-sensitive menu to view the topology group it belongs to.

Use the following step to reassign the topology plans to a specific topology group.

<!-- image -->

3. Create topology group for specific topology plans
- a. On the TopologyPlans tab, select the topology plans from the list, right-click on the selection, and select Create Topology Group .

One topology plan belongs to only one topology group. You cannot share the topology plans across multiple topology groups.

- b. Enter information in the create\_topology\_group dialog box, if required, and click OK .

If you provide a name to the topology group and if it previously exists within the current block, an error is thrown. However, you can have topology groups with the same name within different blocks of the design. If you do not assign a name to the topology group, the tool automatically assigns a name of format TOPOLOGY\_GROUP&lt;#n&gt; , where n is an integer starting from 1.

## Note:

If a topology group contains multiple plans, and those plans have differing values for an attribute, the tool shows the value of that attribute as &lt;mixed&gt; . For example, if a topology group TG1 has two topology plans, TP1 and TP2 with colors red and blue- in the TopologiesGroup tab, the color column displays &lt;mixed&gt; .

You can update the values that are shown as &lt;mixed&gt; to a value that suits your requirements. However, you cannot set the attribute to &lt;mixed&gt; . If the value that you provided is invalid for that attribute, the tool throws an error.

For more information on creating a topology group, see the Creating Topology Groups topic in the IC Compiler II Design Planning User Guide .

After you associate topology plans with a topology group, you can view this association in the group column in the TopologyPlans tab.

To work with a specific set of topology plans:

1. On the TopologiesGroups tab, select the relevant topology group.

If you have added a comment while creating the topology group, you can use this information on the comment column to pick the relevant topology group.

2. Right-click on the selected topology group and select Get Topology Plans .

The topology plans that are a part of this topology group are displayed on the TopologiesPlans tab. You can perform necessary actions on the topology plans from the options that are available in the GUI.

<!-- image -->

To view the topology plans in a specific topology group,

1. On the TopologiesGroups tab, select the topology groups.
2. Choose View &gt; Toolbars &gt; Constraints Editor .

This step brings up the Constraints Editor view that lists all the topology plans that belong to the selected topology groups along with their topology nodes and edges.

## Setting the Current Topology Group

When you create a topology group, it becomes the current topology group.

To set a topology group as the current topology group,

1. On the TopologiesGroups tab, select the relevant topology group.
2. Choose Edit &gt; Topology &gt; Set Current Group or choose Set Current Topology Group from the context menu in Design Assistant.

For more information on creating a topology group, see the Setting the Current Topology Group topic in the IC Compiler II Design Planning User Guide .

## Removing Topology Groups

When you do not need one or more topology groups, you can remove them from the GUI by selecting the topology groups and choosing the Edit &gt; Topology &gt; Remove Group menu. When you remove a topology group that contains topology plans, the tool automatically moves these topology plans to the default topology group. You cannot remove the default topology group if it has any topology plans; however, you can use the -remove\_plans option with the -remove\_topology\_groups command to remove both the topology plans and the default topology group.

For more information on creating a topology group, see the Removing Topology Groups topic in the IC Compiler II Design Planning User Guide .

## Viewing and Editing Aggregate Attributes of Topology Groups

The IC Compiler II tool supports editing the aggregate attributes of the topology groups.

When different topology plans in a topology group have different values for an attribute, the tool aggregates the values of the attribute and displays them as an aggregated attribute. For example, if the colors of topology plan A and topology plan B in a topology group are red and blue, then the topology group color column shows a value of &lt;mixed&gt; for the color attribute.

To change the value of an aggregate attribute,

1. Choose View &gt; Assistants &gt; Design Assistant .
2. On the TopologyGroups tab, select the topology group.

<!-- image -->

3. To apply or edit the color,
- a. Click the color palette icon ( ) in the color column.
- b. Choose a color from the Select Color dialog box.
- c. Click OK .

<!-- image -->

The color is applied to the selected topology group and all the topology plans associated with this topology group. The color column displays the hexadecimal value of the color chosen using the Select Color dialog box in 24-bit RGB hexadecimal string format - for example, #aa0000.

4. To edit whether the topology group is visible or not,
- a. Click the drop-down list in the is\_visible column.

You can control which topology plans to view in the layout view by setting the is\_visible attribute of a topology plan to either true or false . This feature is useful when there are numerous topology plans and you want to work with only a few of the topology plans at a time.

- b. Set the value to true or false .

You cannot set the attribute value to &lt;mixed&gt; . The tool automatically populates the value to &lt;mixed&gt; when the topology plans in the selected topology group have different values for the is\_visible attribute.

<!-- image -->

- c. Click Apply Changes ( ).
5. To edit the physical status of the selected topology group,
- a. Click the drop-down list in the physical\_status column.
- b. Set the value to locked or unrestricted . By default, the value is set to unrestricted .

You cannot set the attribute value to &lt;mixed&gt; .

A physical status of locked prevents accidental physical editing (move, stretch, and so on) of a topology plan. The various elements of a topology plan (nodes, edges, and repeaters) also have locked and unrestricted statuses. To edit topology nodes, edges, and repeaters, their physical status and the physical status of the parent topology plan must be unrestricted (unlocked).

<!-- image -->

- c. Click Apply Changes ( ).

<!-- image -->

## Uniquifying Topology Plans

You can create new topology plans for each physically connected set of topology nodes of specified topology plans by using the uniquify\_topology\_plans command.

In the following example, the tool breaks down the current topology plan into connected components.

icc2\_shell&gt; uniquify\_topology\_plans [current\_topology\_plan]

In addition to topology plan names, you can specify patterns and collections in the uniquify\_topology\_plans command. For more information, see the command man page.

<!-- image -->

## Automatically Select Topology Plans

For operations that require a topology plan, you can select a topology edge, a node, or, a repeater and then proceed with the operation. Then, the operation or the command window is populated automatically with the topology plan associated with the selected object.

<!-- image -->

<!-- image -->

For the following operations, the associated topology plans are populated in the respective command windows,

- Characterize plan
- Check plan
- Estimate timing
- Implement repeaters
- Implement trunks
- Optimize
- Uniquify
- Write

## Merging Stacked Topology Nodes

You can use the merge\_objects command to merge topology nodes that are stacked on top of each other. The merge operation helps in removing redundant topology nodes. The following command merges all the selected objects.

```
icc2_shell> merge_objects [get_selection]
```

Alternatively, you can use the GUI ( Edit &gt; Merge Shapes ) to merge the selected objects.

## Working With Bundle Objects

From the tool GUI ( Manage Bundle dialog box Create &gt; Bundle ), you can:

- Create a bundle
- Add objects to an existing bundle
- Remove an object from an existing bundle
- Sort bus with respect to bus limiter

In n[1] and n[2], the bus delimiter is [].

## Creating a Bundle

You can create a bundle with specific nets in one of the following ways:

- From the block window, choose Create &gt; Bundle
- From Design Assistant , choose Create &gt; Bundle

## In the Manage Bundle dialog box,

1. In the Bundle name field, enter the name of your bundle or choose a bundle from the drop-down list.

If you are naming a bundle, ensure that the bundle name is unique.

2. Add or modify a list of nets,
- By searching for specific nets Search
- By using the locations of the selected layout shapes (for example, pins, terminals, wires, and vias) Get selection

Use this option to insert nets that are connected to the selected objects.

The tool orders the nets according to the geometry of the corresponding net objects. By default, the order is left to right. To use a different order, choose a command on the menu to the right of the Get selection button.

- By loading a text file that contains a list of net names Load from file

Choose the file from the Read nets from file explorer dialog box.

- You can perform the following actions on the selected nets:

| To do this                                                                                                                                                                                                                                                                                                                                                            | Use this   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Sort the nets Before sorting, ensure that you have set the preference for sorting by using Sort mode , Precedence , Bus delimiter , and Wildcard list . When you choose Left for Precedence , the nets are sorted by first index and when you Right , the nets are sorted by last index. For more information, see the context-sensitive online help in the tool GUI. | Sort       |
| Reverse the order of nets in a bundle                                                                                                                                                                                                                                                                                                                                 | Reverse    |
| Select nets to remove                                                                                                                                                                                                                                                                                                                                                 | Remove     |
| Remove all the nets from a bundle                                                                                                                                                                                                                                                                                                                                     | Remove All |

<!-- image -->

<!-- image -->

- Click OK to apply and close the dialog box, or click Apply to continue working.

<!-- image -->

## Viewing Estimate Topology Timing Results in GUI

You can view the results of the estimate\_topology\_timing command in the tool GUI in the form of a user table.

To view the results,

1. Open the top-level design.
2. Set the constraint mapping file.
3. Source the top-level constraints created by the split\_constraints command.

```
icc2_shell> open_block orca:ORCA
```

```
icc2_shell> set_constraint_mapping_file split/mapfile
```

```
icc2_shell> source ./split/ORCA/top.tcl
```

4. In the Topology toolbox, click Estimate Timing .
5. Set the necessary options in the gui\_estimate\_topology\_timing dialog box and click OK .

The user table view opens with the timing estimate results.

<!-- image -->

<!-- image -->

## Using Flyline Analysis Tools

The IC Compiler II GUI provides tools to view net connections, feedthrough paths, timing paths, and other path information as flylines in the layout.

The following topics describe design planning tasks supported by the GUI:

- Net Connections Flylines
- Path Analyzer Flylines
- Data Flow Flylines
- Register Tracing Flylines
- Clock Trunk Planning Flylines

## Net Connections Flylines

The IC Compiler II tool provides the Net Connections Flylines tool to view net connections between hierarchies, macros, standard cells, and ports in your design. Use the tool to view the number of connections between these objects and to trace individual nets. To open the Net Connections Flylines panel, choose View &gt; Flylines &gt; Net Connections or click the Net Connections Flylines button. The Net Connections Flylines panel is shown in Figure 81.

<!-- image -->

<!-- image -->

Figure 81 Net Connections Flylines Panel

<!-- image -->

## Flyline Display Modes

The Net Connections panel supports the following modes for flyline display:

- Aggregated (default)
- Pin to Pin
- By Levels

These modes are described below. Each mode is accessed by clicking the appropriate tab (Aggregated, Pin to Pin, or By Levels) at the top of the panel, then clicking Apply.

## Pin to Pin Flylines

In Pin to Pin mode, the tool displays flylines for individual pins. The flylines are drawn from each start pin to all traced load pins (if the start pin is a driver pin). If the start pin is a load pin, the tool draws flylines to all traced driver pins.

## By Levels

In By Levels mode, the tool displays flylines based on the tracing depth you specify with the Driver and Load options. Except for buffer cells, the tool counts each standard cell as a level. If the Ignore buffers option is selected, buffers are not counted as levels. This mode also supports different flyline colors for the selected driver and load pins.

You can drill down and view details for individual flylines by clicking an aggregated flyline. The tool opens the Net Connections Explorer dialog box and displays the list of nets represented by the aggregated flyline. For more information about the Net Connections Explorer dialog box, see Net Connections Explorer. To view individual flylines, you can also deselect the Aggregate by block option. When this option is deselected, the tool replaces the aggregated flyline with individual flylines.

## Note:

The tool displays flylines based on which pin you select in the path and the type of object you select. The tool displays different flylines depending on whether the pin you select is on a hierarchy boundary.

## Aggregated Flylines

In Aggregated flylines mode, the tool groups the driver and load pins of the flylines based on their parent hierarchical cell, move bound, edit group, RP group, or voltage area. Aggregated flylines are displayed as a single line together with a count of load and/or driver pins. The count is displayed at the center of each unique connected parent object pair. The types of parent objects to display are determined by the 'Trace through' options you select. If the trace-through object is not selected in the panel, then it is included as a possible parent object type. If the original selected object is an edit group, an RP group, a move bound, or a voltage area, then these object types are also candidate parent object types.

<!-- image -->

<!-- image -->

## Setting Flyline Display Options

Use the Connectivity Display options to change the connections that are displayed based on the objects you selected:

- Selected to All: Display flylines between any selected objects and any other object
- Selected to Selected: Display flylines only between the selected objects
- Selected to Not Selected: If one object is selected, display flylines between the selected object and any other object; if two or more objects are selected, display flylines from each selected objects that does not connect to another selected object

Use the Trace through options to control how a net is traced:

- Buffers: Select this option to continue tracing through buffer cells until a nonbuffer cell is reached. When deselected, the tool stops tracing when a buffer cell or any other cell is reached.
- Hierarchy: Select this option to continue tracing through a hierarchical pin. When deselected, the tool stop tracing when a hierarchical pin is reached.
- Edit groups: Select this option to stop tracing at the edit group boundary. When deselected, the tool ignores edit groups when tracing.
- RP groups: Select this option to stop tracing at the RP group boundary. When deselected, the tool ignores the RP group when tracing.
- Inside nets: Select this option to trace nets within a block. By default, nets outside the block are traced. This option can be combined with the 'Through points' option in the Pin to Pin tab to trace feedthrough connections when one of the block pins is selected.
- Move bounds: When this option is disabled, tracing stops at nets that connect from pins at the move bound boundary. The boundary occurs when cells inside the move bound connect to cells outside the move bound. If you select a cell inside the move bound, the tool does not trace flylines to cells outside the move bound. If you select a cell outside the move bound, the tool does not trace flylines to cells inside the move bound. By default, this option is selected and the tool traces through move bounds.

Use the Net Types option to specify which type of nets to trace:

- Signal
- Clock
- Reset

- Scan
- PG
- Tie High
- Tie Low

## Note:

Flylines of PG nets connects between pseudo bump or bump cell and terminals (pin shapes). This direction follows PG delivery within the single die.

Use the Cell Types options to specify one or more types of cells to trace: macros, I/Os, or standard cells.

Use the Flylines options to further control which flylines are displayed:

- Connected loads: Select this option to display flylines between two loads. When deselected, the tool displays flylines between only drivers and loads.
- Query selected: Select this option to update the Query panel when you click an object. The panel displays information about the source, destination, and number of connections for the currently displayed flylines.
- Pin max fanout: Hide flylines with a fanout greater than the specified number.
- Only show bundles: Select this option to display flylines only for bundle signals.
- Min bundle pins: Hide flylines for bundles with less than the specified number of pins.

Use the Aggregated Connections options to control the display of aggregated flylines based on connection count:

- Number of connections: Select this option to use the Min and Max settings to filter aggregated flylines; aggregated flylines are hidden if the total connection count is outside the specified range
- Min: Hide an aggregated flyline if Number of connections is selected and the total number of connections is less than the specified value
- Max: Hide an aggregated flyline if Number of connections is selected and the total number of connections is greater than the specified value

Use the Include options to control the type of cells that are traced:

- Macros: Select this option to include macro cells in the trace.
- IOs: Select this option to include I/O cells in the trace.
- Standard cells: Select this option to include standard cells in the trace.

<!-- image -->

<!-- image -->

Use the Appearance options to control the width and position of flylines:

- Connect Position: Specifies where to draw the startpoint or endpoint for the flyline (center, inside, lower left, lower right, upper left, or upper right)
- Max pixel width: Limits the drawn width of the flyline to the specified number of pixels
- Nets per pixel: Specifies the width of the flyline based on the number of net connections; for example, a setting of 100 nets/pixel and a net connection containing 300 connections causes the tool to draw a 3 pixel line (300 nets / 100 nets per pixel = 3 pixels)
- Color: Specifies the color of the flyline

## Displaying Connections to Route Corridors

When you select a route corridor, the tool gets the pins of the nets for the route corridor and draws a flyline from the pin center to the nearest edge of the route corridor shape. If the route corridor contains intermediate cells that connect to the route, the tool draws flylines to these cells by using a different color.

## Net Connections Explorer

Use the Net Connections Explorer to query individual nets in an aggregated flyline, or display individual net segments in a single flyline.

Open the dialog box by clicking any flyline. The dialog box shows the source block or cell, the destination block or cell, and a list of nets that are represented by the flyline. You can click the name following the From: or To: text to select the block, cell, or port. Move the pointer over the Info icon at the upper right of the dialog box to view summary information about the net connections displayed in the dialog box.

Figure 82 Net Connections Explorer Aggregated Flyline Mode

<!-- image -->

The dialog box displays two tabs: one tab containing pins and nets for the source object, and one tab for pins and nets of the destination object. Click the appropriate tab to show the nets and pins associated with the object.

To filter the list of nets, enter a filter expression in the box. The expression can be a simple matching expression or a Tcl regular expression. By default, the filter expression is applied to net names. To apply the expression to pin names, use the syntax "Pin Name:string", where "string" is the search expression and "Pin Name" is the header for the column.

Click the Select Pins or Select Nets button to select the pins or nets in the layout for highlighted net. Click Select Bundles to select the net bundles for the highlighted net.

To change the color of either unselected and selected flylines, click the flyline box to the right of Normal or to the right of Selected. To continue displaying a previously selected flyline in the layout, select Highlight. To clear a previously displayed flyline, click Clear.

Use the Follow setting to control how the tool centers the selected flyline in the view. To retain the same zoom factor and pan the layout to center the selected flyline in the view, select Pan in the Follow box. To pan the layout and zoom in to fit the flyline to the view, select Zoom in the Follow box.

<!-- image -->

<!-- image -->

When tracing a single flyline, the display changes as shown in Figure 83.

To display the current list of flyline connections in the Query panel, click Query Flylines. To view help information for the Net Connections Explorer dialog box, click Help.

Figure 83 Net Connections Explorer Single Flyline Mode

<!-- image -->

## Path Analyzer Flylines

The IC Compiler II tool supports the Path Analyzer Flylines tool to view timing path connections between top-level signals, macros, ports, and hierarchies in your design. Use the Path Analyzer Flylines tool to identify potential layout-related timing issues and perform an interactive analysis to examine the effect of placement on timing. The tool provides two analysis modes, connection mode and timing mode, to prioritize the information displayed by the flylines. To open the Path Analyzer Flylines panel, choose View &gt; Flylines &gt;  &gt; Path Analyzer Flylines or click the Path Analyzer Flylines button. The Path Analyzer Flylines panel is shown in Figure 84.

Figure 84 Path Analyzer Flylines Panel

<!-- image -->

The tool provides two analysis modes, connection mode and timing mode, to prioritize the information displayed by the flylines. Click the Reload button at the top of the panel to reload the flylines.

If your layout contains module boundaries, click the Place Boundary button in the Tools section to position any currently displayed module boundaries on the block layout display. The tool centers each module boundary over the standard cells for the module. The tool represents connections to standard cells by drawing a flyline to the module boundary, while macros and hierarchy blocks contained inside of the module are not considered. Connections to macros are represented with flylines directly to the macros, not to the module boundary. If a module contains no standard cells, the module boundary is placed at the coordinate (0,0) and no flylines are drawn to the module boundary Module boundaries provide information about the physical location of cells in a design hierarchy. You can use the Hierarchy Browser to create module boundaries and use the boundaries with the Path Analyzer Flylines tool. When a flyline connects to a cell within a module boundary, the Path Analyzer Flylines tool draws a flyline to the module boundary. If a module boundary is not present, the Path Analyzer Flylines tool draws a flyline to the center of the block. To examine the hierarchy, choose View &gt; Hierarchy Browser to start the Hierarchy Browser tool.

<!-- image -->

<!-- image -->

## Viewing Timing Paths by Number of Connections

After clicking the 'Reload' button, the Connection mode in the 'Connection/Timing' section is selected by default. The Connection mode displays timing path connection flylines between ports, modules and macros in the design. The tool partitions and groups the flylines by number of connections; flylines with the greatest number of connections are shown in red. If you see only light blue flylines, you can adjust the binning by changing the value for Threshold for Top Bin in the Line Appearance section.

If you see red or bright purple flylines that extend over long distances, you might need to change your floorplan to shorten the paths. A large number of long paths can cause routing congestion and contribute to total negative slack problems when timing your block.

Move the mouse pointer over a flyline to view more information. The tool displays an infotip as shown in Figure 85; in this example, all the path for the highlighted flyline have same direction. The infotip shows the path endpoints, the count of the flylines between the two objects, and the relative timing effort required to optimize the timing for those paths. If the effort is greater than 1.0, you might encounter difficulty when closing timing for the path.

Figure 85 Single Direction Flyline With Infotip

<!-- image -->

<!-- image -->

Figure 86 shows a flyline with signals that travel in both directions. The direction arrow on the flyline is not displayed, the infotip displays the signal count as "Total - (endpoint1 to 2 + endpoint2 to 1)" and the Effort as "Total maximum - max of (endpoint1 to 2 max to endpoint2 to 1 max)".

Figure 86 Flyline for Mixed Directions

<!-- image -->

Click the flyline to expand the flyline and view the individual connections between the objects. The tool displays a flyline for each individual timing path as shown in Figure 87. To remove the detail flylines, select another object or click outside the layout.

Figure 87 Detailed Connection Flylines

<!-- image -->

To view only flylines which pass through a specific region of the design, select Region in the Path Display box and click the dotted square button as shown in Figure 88. Use the mouse to draw a rectangle on the layout to specify the region for analysis. The tool removes flylines which do not pass through the region.

Figure 88 Creating an Area Rectangle

<!-- image -->

See Filtering by Design Object and Other Constraints for more information about filtering flylines.

## Viewing Timing Paths by Criticality

Select Timing in the "Connection/Timing" section to display timing path connection flylines for the most timing critical paths between objects in the design. In timing mode, the tool bins the flylines by the criticality of the connection and displays the most critical flylines in red. Move your pointer over the flylines and click the flylines as described in Viewing Timing Paths by Number of Connections to view more information about the flylines.

Use the Distance Sensitivity box to control the weighting applied to flyline length when calculating optimization effort. As you change the Distance Sensitivity, the tool recalculates the optimization effort for the flyline. For larger values of Distance Sensitivity, the tool puts more weight on longer flylines. You can view the updated effort value in the infotip.

In general, technologies with higher wire resistance might require a higher Distance Sensitivity setting. If you see red flylines only if the sensitivity is very high (7 or more), then your design probably does not have a timing problem.

## Changing the Flyline Display

Click the Display tab to view and modify the settings for line thickness and binning for the Path Analyzer Flylines display. Select Apply line widths to change the line widths of the flylines based on count of connections between objects. Select Log Scale to change the binning to use a logarithmic scale rather than a linear scale. Enter a new value in the Threshold for Top Bin box to set the maximum value the highest bin.

In connection mode, the Display tab uses color to represent the relative number of connections for each flyline. If the Apply line widths option is selected, the tool displays flylines by using different widths, with the highest bin shown by using the widest line.

In timing mode, color represents the criticality of the timing flyline. If the Apply line widths option is selected, the tool displays the relative number of connections by using different widths, where the widest line represents the highest number of connections.

<!-- image -->

## Filtering by Design Object and Other Constraints

Select object types for analysis by selecting them in the "From" and "To" settings section. Select an entry in the Path Display box to specify the source and destination objects that are used when creating flylines:

- All: Display flylines without any selection criteria. The From and To settings are enabled.
- Region: Display flylines through a user-specified rectangle. The From and To settings are enabled.
- Selected From/To All: Display flylines that either begin or end with the selected objects and any other object. The From and To settings are disabled.
- Selected to Selected: Display flylines that begin or end with the selected objects. The From and To settings are disabled.
- All to Selected: Display flylines that begin at any object and end at the selected objects. The From and To settings are disabled.
- Selected to All: Display flylines that begin at the selected objects and end at any other object. The From and To settings are disabled.

## Checking Timing Paths Info in Table

Click the Table button at the top of the palette to display the flyline endpoints, connection count, and timing effort in a table. Figure 89 shows an example table.

<!-- image -->

Figure 89 Path Analyzer Flyline Table

<!-- image -->

## Path Analyzer Flylines Best Practices

Consider the following suggestions when using the Path Analyzer Flylines tool:

- For most applications, you should deselect the Top option in the From and To sections to remove flylines that do not connect to any particular macro or module boundary. This selection makes the remaining flylines and other information easier to see.
- In connection mode, enter a Minimum count value greater than zero to specify a lower limit on the number of connections required between objects before displaying a flyline.
- In timing mode, toggle the "Unconstrained" option in the Path Display section to include flylines for timing paths without timing constraints, that is, the effort is 0. Toggle "Unachievable" to include flylines for paths which cannot meet the current timing constraints, that is, the effort is 10 or greater. Enter a minimum effort level in the "Minimum Effort" to hide paths with an effort level less than or equal to the specified value.

## Data Flow Flylines

<!-- image -->

Use the Data Flow Flylines tool to view connections between macros, blocks, module boundaries, and I/O ports. The tool helps you understand macro placement quality and view macro-to-macro paths in your design. To open the Data Flow Flylines panel, choose View &gt; Flylines &gt; Data Flow Flylines or click the Data Flow Flylines button ( ).

<!-- image -->

Figure 90 Data Flow Flylines Panel

<!-- image -->

- Computing Data Flow Flylines
- Tracing Flylines
- Setting Tracing Options
- Viewing Flyline Details and Filtering Flylines
- Data Flow Flylines Pin and Net Filters

<!-- image -->

- Using Tcl Commands to Analyze Data Flow Flylines
- Saving and Restoring Data Flow Flylines Connection Data

## Computing Data Flow Flylines

Before tracing flylines, you must compute the flylines to load them into tool as follows:

1. Click the Reload button on the Data Flow Flylines panel.
2. In the Compute Data Flow Flylines dialog box, select the number of register levels, gate levels, and maximum fanout to trace.
3. Click the Filters button to specify nets and pins to ignore during tracing. For more information, see Data Flow Flylines Pin and Net Filters for more information.
4. Click OK to compute the data flow flylines

## Tracing Flylines

After initializing the data flow flylines, you can trace flylines interactively in the layout window. A typical workflow includes the following steps:

1. Click a macro, block, module boundary, or I/O port to select it; the tool displays flyline connections to the objects selected in the Include section.
2. Move the pointer over the flyline and view the number of connections in the infotip.
3. Click the flyline to open the Data Flow Connections and Filters dialog. The dialog box shows the list of connections represented by the flyline, see Viewing Flyline Details and Filtering Flylines for more information.
4. Click a path in the list to show the flyline for that path.
5. Expand the path by clicking the ([+]) button and click a line that represents a segment of the path; the tool shows the detailed path flyline in red for the segment.
6. Continue to trace other segments in the path by clicking on them, or by pressing the Up Arrow or Down Arrows key to scroll through the list of segments.

## Setting Tracing Options

The Data Flow Flylines tool supports options to control flyline tracing. Use the Connectivity Display setting to control which connections are displayed:

- All : Display all paths
- Selected To All : Display paths from selected objects to all connected objects

<!-- image -->

<!-- image -->

- Selected To Selected : Display paths from selected objects to other selected objects that are connected
- Selected To Not Selected : Display paths from selected objects to connected objects that are not selected

Use the Include section to select the type of objects to include when tracing.

Use the Limit Tracing section to adjust the number of registers and number of gates to include in the flyline. You can only reduce the number of levels based on the numbers you specified in the Compute Data Flow Flylines dialog; to increase the available levels, click Reload and compute the flylines again. Note that by default, buffers and inverters are not included in the gate count for minimum and maximum number of gates between the source and destination pins. As a result, the detailed path connectivity can show more gates than expected.

Aggregated connections are flylines which combine flylines with the same source and destination object into a single flyline. To change the behavior of aggregated flylines,

- Select or deselect the Aggregate option to show aggregated flylines or show individual flylines
- Select the Number of connections option and choose values for the minimum and maximum number of connections for an aggregated flyline; the tool hides aggregated flylines with a number of connections outside this range

Use the Appearance section to change the connection point, line width, and color of the flylines:

- Select a Connect Position option in the list to change where the flylines are drawn in the layout; the tool draws the flyline to the specified location on the object
- Use the Max pixel width setting to limit the drawn width of the flyline to the specified number of pixels
- Use the Nets per pixel setting to specify the width of the flyline based on the number of net connections; for example, a setting of 100 nets/pixel and a net connection containing 300 connections results in a 3 pixel line (300 / 100 = 3)
- Use the Color setting to change the color used when displaying a flyline between macros, blocks, and module boundaries
- Use the To port color setting to change the color of flylines to ports
- Use the Port-to-port color setting to change the color of port-to-port flylines
- Wire length is the total flyline length for the selected objects, which is auto calculated.

## Viewing Flyline Details and Filtering Flylines

Use the Data Flow Connections and Filters dialog box to view individual connections within an aggregated flyline, view single flylines, or set pin and net filters to use when tracing flylines. To open this dialog box, click an aggregated flyline generated by the Data Flow Flylines tool.

Note that after you create a filter, you must click Reload in the Data Flow Flylines panel to recompute the flylines and apply the filter.

Figure 91 Data Flow Connections and Filters

<!-- image -->

The Connections tab displays a list of connections within the selected flyline. At the top of the tab, the tool shows the names of the two objects connected by the flyline and the number of connections that originate from either object. If there are connections in both directions between the objects, click the Show button to the right of the object name to add to list or remove from the list the connections which originate from that object.

<!-- image -->

To trace flylines by using the Connections tab,

1. Click a path in the list; the tool shows the flyline for that path
2. Select the Detailed path option to display all intermediate connections in the path; the tool shows a red flyline for each pin-to-pin connection
3. Click the Source Pins , Source Nets , Destination Pins , or Destination Nets buttons to copy the selected path to the respective filter; to apply the filters, you must click Reload to recompute the flylines
4. Expand the path by clicking the ([+]) button to show the source and destination pins for the intermediate connections
5. Click an entry in the list that represents a segment of the path; the tool shows the detailed path flyline in red for the segment
6. Press the Up Arrow or Down Arrow key to scroll through the path and highlight different segments in the layout
7. Press and hold the mouse button and drag the pointer down the list to add additional segments in the path

<!-- image -->

Figure 92 Flyline and Detailed Path

<!-- image -->

To improve performance, the tool might not load all path details. In this case, the tool displays the message " Path is not loaded. Double-click to load. " in the Detailed Path column. You can load the path by double-clicking it, or load all remaining unloaded paths by clicking the Load All Paths button.

To save a comma-separated list of source pins, destination pins, number of registers, and number of gates for paths in the list, click the Export button.

## Data Flow Flylines Pin and Net Filters

To open the Data Flow Connections and Filters dialog box, click the Filters button in the Data Flow Flylines panel. The Pin Filters and Net Filters tabs contain the list of pins and nets to ignore during flyline tracing. To add an entry to the list, enter the name in the Patterns box and click Add . Alternatively, enter an expression compatible with the get\_pins or get\_nets command to specify one or more pins or nets.

<!-- image -->

<!-- image -->

In the Pin Filters or Net Filters tabs, use the buttons on the right modify the list:

- Use the Add Selected Pins button or Add Selected Nets button to add to the list the pins or nets that are selected in the layout
- Use the Add Pins of Selected button or Add Nets of Selected button to add all pins or nets of the selected object
- Use the Remove button to remove the selected item from the list
- Use the Remove All button to clear the list
- Use the Write to File button to write the list of pins or nets, one item per line, to a file
- Use the Read from File button to load a list of pins or nets from a file

## Using Tcl Commands to Analyze Data Flow Flylines

When you click the Reload button in the Data Flow Flylines panel, the tool opens the Compute Data Flow Flylines dialog box and prompts you for information about the number of levels and maximum fanout to trace. You can also use the compute\_dff\_connections Tcl command directly and specify options to the command to generate the register tracing information. For example, the following compute\_dff\_connections command generates path information and specifies tracing for two register levels, 15 levels of gates, and a maximum fanout count of 50.

```
icc2_shell> compute_dff_connections -max_reg 2 -max_gate 15 \ -max_fanout 50
```

After tracing the flylines with the compute\_dff\_connections command, use the get\_dff\_connections command to return all paths or return only paths that meet a specified criteria. By default, the command returns a collection of all paths generated by the compute\_dff\_connections command. Note that the values specified using the -max\_reg and -max\_gate options must be less than or equal to the values specified to the corresponding options in the compute\_dff\_connections command.

The following examples return specific paths extracted by the compute\_dff\_connections command and return attributes for individual paths.

- Return all paths.
- Return paths with no registers and no gates.

```
icc2_shell> get_dff_connections
```

```
icc2_shell> get_dff_connections -max_reg 0 -max_gate 0
```

<!-- image -->

- Return all paths to the pad[0] port, from the pad[0] port, and through the pad[0] port.
- Return all paths through the pad[0] and u1/u2/o1 ports.
- Examine the start.full\_name , end.full\_name , and other attributes returned for an individual path in the collection.

```
icc2_shell> get_dff_connections -to pad[0] icc2_shell> get_dff_connections -from pad[0] icc2_shell> get_dff_connections -through pad[0]
```

```
icc2_shell> get_dff_connections -through pad[0] -through u1/u2/o1
```

```
icc2_shell> set paths [get_dff_connections -from {pad[6]}] {{pad[6]::I_ORCA_TOP/I_CONTEXT_MEM ... icc2_shell> set path [index_collection $paths 0] {{pad[6]::I_ORCA_TOP/I_CONTEXT_MEM/I_CONTEXT_RAM_0_1/A1[0]}} icc2_shell> get_attribute $path start.full_name pad[6] icc2_shell> get_attribute $path end.full_name I_ORCA_TOP/I_CONTEXT_MEM/I_CONTEXT_RAM_0_1/A1[0] icc2_shell> get_attribute $path name pad[6]::I_ORCA_TOP/I_CONTEXT_MEM/I_CONTEXT_RAM_0_1/A1[0] icc2_shell> get_attribute $path registers 0 icc2_shell> get_attribute $path gates 10
```

## Saving and Restoring Data Flow Flylines Connection Data

The tool does not save data flow flylines connection information when you exit the session. However, if you want to use the same data in a future session, you can save this information to a file. You can also restore previously saved data flow flylines connection information by loading it from the saved file.

To save the current data flow flylines connection information for the active view,

1. Ensure that you have computed the flylines and loaded them into tool. See Computing Data Flow Flylines for more information.
2. After computing the flylines, write out the data flow flylines connection information to a file by using the write\_dff\_connections command.

In the following example, the tool writes out the data to file named dfffile. The -force option overwrites any existing file with the same file name.

```
icc2_shell> write_dff_connections -force -filename dfffile
```

To restore the previously saved data flow flylines connection information, use the read\_dff\_connections command.

<!-- image -->

In the following example, the tool reads the data flow flylines connection information from a file named dfffile.

icc2\_shell&gt; read\_dff\_connections -filename dfffile

- Use the -threshold option with the read\_dff\_connections command to avoid any issues that might arise when there is a mismatch between the current netlist and the data flow flylines connections that you are trying to read. For more information about this option, see the command man page.
- If the specified file is not in the current working directory, the tool displays an error message.

```
File-013 error will be issued in case no such attachment exists. Error: Cannot open file 'filename' for read. (FILE-013)
```

To remove the data flow flylines connection information file from the system, use the remove\_dff\_connection\_files command.

In the following example, the tool removes data flow flylines connection file named dfffile. To skip any messages and to run in a quiet mode, use the -quiet option with this command.

```
icc2_shell> remove_dff_connection_files -filename dfffile
```

## Register Tracing Flylines

The IC Compiler II tool provides the Register Tracing Flylines tool to display register connections between hierarchies, macros, and ports in your design. Use the tool to view flylines for register connections between objects, limit tracing based on number of levels of registers or fanout, display connected pins and ports, and list the registers in the path. To open the Register Tracing Flylines panel, choose View &gt; Flylines &gt; Register Tracing or click the Register Tracing Flylines button ( ). The Register Tracing Flylines panel is

shown in Figure 93.

Figure 93 Register Tracing Flylines Panel

<!-- image -->

## Displaying Flylines

The Register Tracing Flylines tool displays flylines between the driving register pin and receiving register pin for the nets that meet the specified criteria. You can change the flylines that are displayed by changing the settings in the panel as follows and clicking the Apply button to commit the changes.

- Trace Selected to All: Trace the output ports by the specified number of levels and display the flylines
- Trace Selected to Selected: Trace connections between the selected objects and display connections with an endpoint in one of the selected objects
- Trace All to Selected: Trace all possible ports and macro pins to the select objects and display only those connections with an endpoint in the selected object
- Limit Tracing Max levels: Set the maximum number of register levels to trace

<!-- image -->

<!-- image -->

- Limit Tracing Max fanout: Specifies the fanout level at which to stop tracing
- Highlight registers: Display and highlight cells that are registers
- Highlight End points: Display and highlight registers and ports in the specified highlight color
- Highlight Direct End points: Display and highlight endpoints that are driven directly by the source pin
- End point type Pins: Consider only pins as endpoints
- End point type Ports: Consider only ports as endpoints
- End point type Both: Consider both pins and ports as endpoints
- Show flylines: Toggle flyline visibility
- All Levels: Toggle visibility for all tracing levels up to the maximum level set in the Limit Tracing section
- Level 1, etc: Toggle visibility for the specified level
- Show Table: Display a dialog box that contains a list of startpoints, endpoints, and intermediate registers that meet the tracing criteria. Click on a line in the list to display the flyline in the layout. Click Export to write out the list.

## Clock Trunk Planning Flylines

The IC Compiler II tool provides the Clock Trunk Planning Flylines tool to view and modify the clock trunk for clock signals in the design. You can use the tool to view individual clock trunks, add buffers, remove buffers, check and repair clock trunk violations, and push down cells for the displayed clock trunk. Timing information, such as WNS, TNS, and other parameters, can be viewed by displaying an infotip for different clock trunk planning flylines in the design. To open the Clock Trunk Planning Flylines panel, choose View &gt; Flylines &gt; Clock Trunk Planning from the menu or click the Clock Trunk Planning button ( ). The Clock Trunk Planning Flylines panel is shown in Figure 94.

Figure 94 Clock Trunk Planning Palette

<!-- image -->

## Loading Clock Data

To load clock information into the Clock Trunk Planning tool,

1. Click the reload button
2. In the Reload clock trunk planning dialog shown in Figure 95, choose the clocks to load

<!-- image -->

- Choose Automatic to load all clock trunks
- Choose Specified to choose one or more individual clock trunks from the list. Hold the Ctrl key and click to add clocks to the list, or hold the Shift key and click to add multiple clocks.
3. Click OK

Figure 95 Reload Dialog Box

<!-- image -->

The tool loads the specified clock trunks. If you chose Automatic or selected multiple clock signals, the tool selects one of the signals and displays it. To change the clock trunk that is displayed, choose another clock signal from the Clock drop-down list.

## Changing Clock Trunk Highlighting

Use controls in the Clock trunk section to change the color of the clock trunk elements displayed in the layout. Select the box next to the element name to display it in the layout.

<!-- image -->

<!-- image -->

Change the color of a clock trunk element by clicking the color bar next to the element name and selecting a color from the list.

- End Points: Defines the color of the clock end points
- Arcs: Defines the color of the flylines between the clock origin and a clock buffer or block
- Repeaters: Defines the color of repeater cells
- Logic: Defines the color of logic cells
- High Fanouts: Defines the color of high-fanout nets

## Adding and Removing Clock Trunk Cells

To insert a clock buffer cell on a clock trunk,

1. In the palette, select the clock signal clock trunk for which to insert the buffer in the Clock box.
2. In the layout, select the port, cell, or pins to buffer. The object must be on the currently selected clock trunk.
3. Click the Add button.
4. In the dialog box shown in Figure 96, select the pins to buffer: source pin, sink pin, or both pins.
5. Select the 'Allow on top of blocks' button to allow the tool to insert a buffer if the buffer overlaps the block.
6. Click Add buffer

The tool applies the create\_clock\_buffer command to insert a clock buffer cell for each pin selected in step 4.

Figure 96 Add Clock Trunk Buffer

<!-- image -->

To remove one or more clock buffer cells,

1. Select the cells in the layout
2. Click the Remove button

## Displaying Timing Flylines Between Blocks

The Clock Trunk Planning tool can display timing flylines between blocks in the design. Select a timing metric (WNS, WNS(OCV), TNS, Slack, Slack(OCV), Paths, or VioPaths&amp;TNS) from the 'Color flylines by' box in the Timing flylines section near the bottom of the palette. The tool bins the paths, adds flylines to the layout according to bin, and displays a histogram of values at the bottom of the palette. To change the number of bins displayed, set a new value in the 'Num of bins' box.

To remove timing flylines from the layout, select None on the 'Color flylines by' box.

<!-- image -->

## 7

## Using Map and Visual Modes

The IC Compiler II GUI provides tools to view data about the design as an overlay on the layout. Using map modes and visual modes, you can quickly identify problem areas in your design, make corrections, and evaluate the fix.

The following topics describe map modes supported by the GUI:

- Map Mode Overview
- Global Route Congestion Map
- Channel Congestion Map
- Cell, Pin, Block Pin, and Power Density Maps
- Effective Voltage Areas Map
- Effective Site Arrays Map
- Wire Utilization Map
- Exporting and Importing Map Data
- Visual Mode Overview
- Snapshot Visual Mode
- Highlight Visual Mode
- Clock Tree Visual Mode
- Scan Chain Visual Mode
- Net Connections in Area Visual Mode
- Relative Placement (RP) Groups Visual Mode
- Relative Placement (RP) Net Connection Visual Mode
- Hierarchy Visual Mode
- Cell Slack Visual Mode

<!-- image -->

- Imported Path Pins Visual Mode
- Voltage Areas Visual Mode

## Map Mode Overview

Map modes are analysis tools you can use to highlight specific floorplan, placement, or routing results in the active layout view. When you enable a map mode, the GUI dims the visible objects in the layout view and opens the Map Mode panel. To view or hide a map mode in the active layout view, you can choose View &gt; Map and select a map mode. Alternatively, click the map mode button on the toolbar. The name of the active map mode appears in the list at the top of the Map Mode panel as shown in Figure 97. The Global Route Congestion Map is shown in Figure 98.

<!-- image -->

## Figure 97 Map Modes

<!-- image -->

<!-- image -->

<!-- image -->

Figure 98 Global Route Congestion Map

<!-- image -->

## Configuring the Histogram

At the bottom of the map mode panel, the tool displays a histogram of values for the current map mode. You must click Reload to generate the histogram for the first time. To modify the histogram,

- Display or hide histogram bars and their corresponding data in the layout by selecting or deselecting the box at the left of the bar; alternatively, right click anywhere in the row and choose Show or Hide . You can also choose Show all or Hide all to display or hide all the histogram bars.
- Change the color of the histogram bar, corresponding grid, and line style in the layout by right clicking anywhere in the row and choosing Set Style .
- Change other display options by right clicking anywhere in the row and selecting Configure ; see Configuring Map Options for more information

Click Apply to update the map based on the new settings

- Change the color palette of the current map to Standard, Neon, or RGB by right clicking anywhere in the row and choose Set Color Palette .
- Navigate to a specific grid in the design layout by choosing Show in List and clicking one of the rows in the Map Data dialog box.

<!-- image -->

Figure 99 Map Mode Histogram

<!-- image -->

## Map Mode Preset

You can configure the map mode by applying a predefined set of map configurations called a preset. You can apply a system preset provided by the tool, or you can create your own custom presets.

You can preset and save the map configurations in the map infrastructure by using the Preset option available at the bottom of the Map Mode panel. Alternatively, you can use the -category category option with the gui\_set\_preset command to preset the specific map configurations for the specific map.

Figure 100 Map Mode Preset

<!-- image -->

Select, reload, or change view seting presets

To create a custom preset,

1. Click the button and choose Save preset .
2. The Select Preset Name dialog box appears.

<!-- image -->

<!-- image -->

3. Select an existing preset, or type a new preset name in the Select or type a preset name box.
4. Click OK .

The tool saves the preset and adds the preset name to the Preset list on the Map Mode panel. When you save the preset for the specific map, include the prefix 'map:' , appended with the map name such as map:thermal\_profile or map:cellDensity to avoid naming issues.

You can specify a preset as the default configuration when you open a Map Mode view. You can remove a custom preset but not a system preset.

<!-- image -->

If you need to reload the settings from the preset, click the button. To reconfigure the map view with the default view settings, select Default in the Preset list.

Here is an example of presetting the map configurations by using the gui\_set\_preset command.

icc2\_shell&gt; gui\_set\_preset -category map:thermal\_profile -default

## Changing the Transparency

You can adjust the transparency of a map by using the Alpha control that is available in the tool GUI. Alternatively, you can use the -option alpha option with the gui\_get\_map\_option , gui\_get\_map\_option\_list , and gui\_set\_map\_option commands.

The following table shows how some of the settings affect the transparency of a map.

<!-- image -->

Table 12 Transparency Control Settings

<!-- image -->

Table 12 Transparency Control Settings (Continued)

<!-- image -->

Here is an example of setting the transparency by using the gui\_set\_map\_option command.

icc2\_shell&gt; gui\_set\_map\_option -map cellDensityMap -option alpha -value 10%

To retrieve the settings, you can use the gui\_get\_map\_option command. For example,

icc2\_shell&gt; gui\_get\_map\_option -map cellDensityMap -option alpha

## Configuring Map Options

You can perform additional configuration of each map mode by clicking the Show Options button ( ) and selecting configure:

- Exaggeration scheme : Set the Top , Middle , and Bottom values to specify the color exaggeration scheme in map modes and visual modes; these values set the minimum, median, and maximum number of pixels to use when displaying congestion bars in the layout
- Show styles : Displays or hides the color key square in the histogram
- Show exaggeration : Displays or hides the calculated exaggeration value next to each histogram bar
- Show counts : Displays or hides the count of edges for each histogram bin

<!-- image -->

- Show histogram : Displays or hides the histogram bars
- Show only visible bins in histogram : When selected, displays a histogram bar only if the check box for the bin is selected

## Global Route Congestion Map

The IC Compiler II tool supports the Global Route Congestion map to highlight areas of the design which contain a high demand for global routes. Congested areas might lead to problems during detail route. To display the Global Route Congestion Map, choose View &gt; Map &gt; Global Route Congestion or click the Global Route Congestion button ( ).

To generate the global route congestion map, click the Reload button. The tool displays a dialog box with the route\_global command and options to use to generate the map data. Click OK to run the command. After completion, the tool displays the congestion map.

After the tool displays the congestion map, move the pointer to the layout window and zoom in to view the map in more detail. You can move the pointer over a congestion bar to view more information in the infotip.

## Refining the Global Route Congestion Map

You can modify settings in the Global Route Congestion Map panel to change how the congestion map is displayed. Use the following settings to change the congestion map:

- Rule level: Select the rule level to apply to the congestion calculation
- Congestion calculation: Select Sum of overflow for each layer or Total demand minus total supply to select the method used to calculate congestion; see Congestion Map Calculations for information about how this setting affects the display
- Bins: Change the number of unique bins used to display the map by changing the Bins value; a larger number of bins partitions the map into a greater number of value ranges
- From: and To: Change the range of overflow values displayed in the map and the histogram by changing these values; these values represent the overflow in routing capacity for the route cell, where higher numbers represent more severe congestion
- Edges: Select the edges, Horizontal and Vertical, of the global route cell for which to display congestion values
- Text: Select this option to display in the layout a number that represents the calculated congestion values; if the values are not visible, you must zoom in to view them and make sure that range is selected in the histogram
- Banded: Use this option to enable or disable the smooth rendering of the map. When you deselect the Banded check box, the display of colors in the map palette changes

<!-- image -->

<!-- image -->

from buckets into a continuous color gradient for the smooth color distribution of the map.

- Hierarchical: Select this option to display a congestion map within a hierarchical block
- Layers: Select the routing layers to consider when calculating congestion

At the bottom of the panel, the tool displays a histogram of the congestion values. To modify the histogram after generating the map,

- Select or deselect layers to include or exclude them from the congestion calculation
- Display or hide histogram bars and their corresponding grids in the layout by selecting or deselecting the box at the left of the bar; alternatively, right click anywhere in the row and choose Show chosen rows or Hide chosen rows
- Change the color of the histogram bar and corresponding grid in the layout by right clicking anywhere in the row and choosing Set Style
- Click Apply to update the map based on the new settings

## Congestion Map Calculations

The Global Route Congestion map supports two calculation modes: 'Sum of overflow for each layer' and 'Total demand minus total supply'. The mode determines the congestion value that the tool displays when a global route cell has congestion; the sum-of-overflow mode is the default.

The following shows an example calculation for both modes. The example explains one direction through a global route cell in a design with congestion.

Figure 101 Congestion Example

<!-- image -->

<!-- image -->

In this example, Layer METAL2 is heavily congested, with a demand of 13 routing tracks and a supply of only 7 tracks, for an overflow of 6. Layer METAL 4 is moderately congested with an overflow of 4, and layer METAL6 is not congested and contains underflow of 3. Other layers are not used in the congestion calculation is this example.

The sum-of-overflow calculation is the default calculation mode and considers only the overflow for each layer. In this example, the overflow on METAL2 is 6, the overflow on METAL4 is 4, for a total sum of overflow of 6+4=10. No overflow exists on METAL6 and this layer is not used in the calculation, even though it is selected. In a region that contains only underflow, the tool sums the underflow for each selected layer.

The Total Demand Minus Total Supply calculation sums the total demand and subtracts the total supply. In this example, the total demand is 24, the total supply is 17, and the result is 24-17=7. Note that the Total Demand Minus Total Supply calculation produces a more optimistic congestion result in regions which contain both overflow and underflow.

## Examining Cells in Congested Areas

When the congestion map is visible, you can view and select cells in congested areas across multiple layers of the design by using the congested region dialog box to define a rectangular region in the layout view. The dialog box lists the cells in congested areas within the region.

<!-- image -->

You can select cells in the cell list to view or highlight them in the layout view, and you can filter the cell list by setting a minimum global routing congestion (GRC) violation threshold. In addition, you can cross-probe the RTL for cells in congested areas to identify the RTL code that could be causing the congestion.

To select and view cells in a congested region,

1. (Optional) To view the congested region on the top hierarchy alone, select the 'Current design only' check box.

If this check box is unselected, which is the default, the congested regions across physical hierarchies are displayed.

2. Click the 'Cells in congested region' button on the Global Route Congestion panel.

The congested region dialog box appears. You can move this dialog box to a location on the screen where you can work with both it and the layout view at the same time.

<!-- image -->

3. Define the shape and location for the region by doing one of the following:
- Drag the pointer in the layout view to form the rectangle where you need it
- Enter the x- and y-coordinates for the upper-left and lower-right corners of the rectangle in the 'GR Congestion region' box.
4. Click Apply.

The names of the cells in the region appear in the Cell Name list. Only cells in highly congested areas are listed.

5. (Optional) To filter the cells by their global route congestion thresholds, enter a value in the 'GRC violation threshold' box.

Only cells that have a global route threshold value equal to or greater than this value appear in the dialog box.

<!-- image -->

6. Repeat steps 2 through 4 if you need to list cells in a different area of the design.

The cell list tree has two modes - File/Line/Object and File/Object. File/Line/Object mode shows the objects on each line of each file. The File/Object mode shows the objects of each file.

To select and view congested cells in the layout view, select the cell names in the cell list. The layout view displays the selected cells in the selection color, which is white by default.

## Cross-Probing Cells in Congested Areas

During congestion analysis, cross-probing cells in highly congested areas can help you to identify the RTL code that is causing the congestion.

To quickly view the RTL for a cell, click on a cell in the Cells in Congested Region panel. The RTL code is highlighted in the RTL browser.

## Channel Congestion Map

<!-- image -->

The Channel Congestion map displays areas of the design in channels between objects which contain a high demand for global routes. You can generate the Channel Congestion map for a small area of the design, modify the design, and regenerate the map to perform quick iterations to repair congested areas of the design. To display the Global Route Congestion Map, choose View &gt; Map &gt; Global Route Congestion or click the Global Route Congestion button ( ).

To generate the channel congestion map, click the Reload button. The tool displays a dialog box; select Whole design area or Specified area to define the area to analyze for channel congestion. Click OK to run the command. After completion, the tool displays the channel congestion map.

After the tool displays the channel congestion map, move the pointer to the layout window and zoom in to view the map in more detail. You can move the pointer over a congestion bar to view more information in the infotip.

You can modify settings in the Channel Congestion Map panel to change how the congestion map is displayed. Do the following to change the congestion map:

- Congestion calculation: Select Sum of overflow for each layer or Total demand minus total supply to select the method used to calculate congestion; see Congestion Map Calculations for information about how this setting affects the display
- Bins: Change the number of unique bins used to display the map by changing the Bins value; a larger number of bins partitions the map into a greater number of value ranges

<!-- image -->

- From: and To: Change the range of overflow values displayed in the map and the histogram by changing these values; these values represent the overflow in routing capacity for the route cell, where higher numbers represent more severe congestion
- Edges: Select the edges, Horizontal and Vertical, of the global route cell for which to display congestion values
- Text: Select this option to display in the layout a number that represents the calculated density values; if the values are not visible, you must zoom in to view them
- Banded: Use this option to enable or disable the smooth rendering of the map. When you deselect the Banded check box, the display of colors in the map palette changes from buckets into a continuous color gradient for the smooth color distribution of the map.
- Hierarchical: Select this option to display a congestion map within a hierarchical block
- Layers: Select the routing layers to consider when calculating congestion

For more information about modifying the histogram, see Configuring the Histogram.

## Cell, Pin, Block Pin, and Power Density Maps

Density maps display areas of high density of an object type or calculated value in the core area or rectangular area within the core. The IC Compiler II tool provides the Cell Density Map to analyze the density of standard cells, the Pin Density Map to analyze the density of pins in a given region, and the Power Density map to analyze power density in the layout. The Block Pin Density map displays the density of pins on block pin edges. To display the appropriate density map:

- Choose View &gt; Map &gt; Cell Density or click the Cell Density button ( ) in the Analysis toolbar to display the Cell map.
- Choose View &gt; Map &gt; Pin Density or click the Pin Density button ( ) in the Analysis toolbar to display the density map.
- Choose View &gt; Map &gt; Block Pin Density or click the Block Pin Density button ( ) in the Analysis toolbar to display the density map.
- Choose View &gt; Map &gt; Power Density or click the Power Density button ( ) in the Analysis toolbar to display the density map.

To generate the density map, click the Reload button. Select Whole design area or Specified area to define the area to analyze. Click OK to run the command. After completion, the tool displays the cell density map.

<!-- image -->

After the tool displays the map, move the pointer to the layout window and zoom in to view the map in more detail. You can move the pointer over a grid point to view more information in the infotip. For the cell density, pin density, and power density maps, the Grid size label displays the number of horizontal and vertical grid points in the current map. The Grid size value is determined by the number of standard cell heights per grid point and the size of the rectangle you specified in which to calculate the map.

You can modify the following settings in the map panel to change the display:

- Grid dimension: Select the number of standard cell heights used to define the grid for the cell density, pin density, or power density maps
- Solid filled grids: Fills each grid cell with the histogram color that represents the density for that section of the layout for the cell density, pin density, or power density maps
- Bins: Changes the number of unique bins used to display the map by changing the Bins value; a larger number of bins partitions the map into a greater number of value ranges
- From: and To: Sets the range of density values displayed in the cell density, pin density, or power density map
- Text: Displays in the layout a number that represents the calculated density value at each grid point; if the values are not visible, you must zoom in to view them
- Banded: Use this option to enable or disable the smooth rendering of the map. When you deselect the Banded check box, the display of colors in the map palette changes from buckets into a continuous color gradient for the smooth color distribution of the map.
- Current design only: Displays a density map only for the current hierarchy level

For more information about modifying the histogram, see Configuring the Histogram.

## Effective Voltage Areas Map

The Effective Voltage Areas map displays the default voltage area and other user-created voltage areas for the design. To display the Effective Voltage Areas map, choose View &gt; Map &gt; Effective Voltage Areas or click the Effective Voltage Areas button ( ).

<!-- image -->

After the tool displays the map, move the pointer over a voltage area to view more information in the infotip. Click the voltage area to display information about the voltage area in the Query panel.

<!-- image -->

<!-- image -->

You can modify settings in the Effective Voltage Areas map panel to change how the map is displayed. Do the following to change the map display:

- Show as fractured rectangles: Select this item to display the voltage areas as fractured rectangles
- Hierarchical: Select this option to display a pin density map within a hierarchical block

For more information about modifying the histogram, see Configuring the Histogram.

## Effective Site Arrays Map

The Effective Site Arrays map displays the currently defined site arrays for the design. To display the Effective Site Arrays map, choose View &gt; Map &gt; Effective Site Arrays or click

the Effective Site Arrays button ( ).

After the tool displays the map, move the pointer over the site array to view more information in the infotip. Click the site array to display information about the site array in the Query panel.

Select the Current design only option to display site arrays only for the current level of hierarchy.

For more information about modifying the histogram, see Configuring the Histogram.

## Wire Utilization Map

The Wire Utilization map displays utilization values on the layout. Utilization is the demand for routing tracks divided by the capacity, where demand is the number of tracks occupied by preroutes and detail route shapes.

To display the wire utilization map, choose View &gt; Map &gt; Wire Utilization from the menu. The Wire Utilization map is shown in the following figure.

## Figure 102 Wire Utilization Map

<!-- image -->

<!-- image -->

<!-- image -->

Modify the settings in the Wire Utilization map to change how the map is displayed:

- Wire utilization contributed by: Select Preroutes, Preroutes + clock, or Preroutes + clock + signal nets: Includes only the selected route types in the calculation of the demand number
- Bins: Changes the number of unique bins used to display the map by changing the Bins value; a larger number of bins partitions the map into a greater number of value ranges
- From: and To: Changes the range of overflow values displayed in the map and the histogram by changing these values; these values represent the utilization for the route cell
- Edges: Selects the edges, Horizontal, Vertical, or both, for which to display utilization values
- Text: Displays in the layout a number that represents the calculated utilization values; if the values are not visible, you must zoom in to view them
- Banded: Use this option to enable or disable the smooth rendering of the map. When you deselect the Banded check box, the display of colors in the map palette changes from buckets into a continuous color gradient for the smooth color distribution of the map.
- Current design only: Limits the utilization calculation to only the current level of hierarchy
- Layers: Selects the routing layers to consider when calculating the utilization

For more information about modifying the histogram, see Configuring the Histogram.

## Exporting and Importing Map Data

The tool supports reading and writing map data.

This feature enables you to,

- Export the map data in a simple ASCII format, which you can post process (the ASCII file) or use it as input for other tools
- Import (or read) map data into the tool to generate a plot or histogram by using the User Map map mode

The tool reads or writes the map data in simple ASCII format that consists of the following sections-metadata (optional), header (optional), and data. For the optional sections, if nothing is specified, defaults are applied automatically. Here is an example of what a map data file might look like:

<!-- image -->

<!-- image -->

## To export the map data for a specific map:

1. In the GUI, enable a map mode in the layout view; for example, the Global Route Congestion map.
2. Click on the Settings icon.
3. Choose Export as User Map file.

<!-- image -->

4. In the gui\_write\_user\_map dialog box, enter a file name.
5. Click OK .

The output file contains the map data in CSV format.

## Note:

The output file contains data for whole design area and not for a selected region.

The tool ignores the layers that are not selected.

For values that are empty for the metadata and header sections, the values are populated automatically with the defaults.

<!-- image -->

| Metadata Information   | Metadata Information   | Metadata Information   | Metadata Information                             | Metadata Information   | Metadata Information                                                                   |
|------------------------|------------------------|------------------------|--------------------------------------------------|------------------------|----------------------------------------------------------------------------------------|
| Type                   | Name                   | Property               | Value                                            | Default                | Comments Examples                                                                      |
| table                  | ""                     | app_name               | string                                           | ""                     | Tool used for writing the map data fc                                                  |
| table                  | ""                     | report_date            | string                                           | ""                     | Date and time when the map data is generated 2020-Sep-30 09:49:58                      |
| table                  | ""                     | title                  | string                                           | "map_filename"         | Map title Cell Density                                                                 |
| table                  | ""                     | version                | string                                           | ""                     | User map version V 1.0                                                                 |
| table                  | ""                     | bins                   | int                                              | 10                     | Map bucket count 9                                                                     |
| table                  | ""                     | max_threshold          | int or float                                     | ""                     | Maximum map data 1.0                                                                   |
| table                  | ""                     | min_threshold          | int or float                                     |                        | Minimum map data 1.0                                                                   |
| table                  | ""                     | color_scale            | TemperatureScale/ RainbowScale/ QualitativeScale | TemperatureScale       | Three sets of color schemes, which the tool sets based on bin counts. TemperatureScale |

Table 13 Map Data ASCII File - Metadata Defaults

<!-- image -->

Table 14 Map Data ASCII File - Header Defaults

| Header Information   | Header Information   |          |              |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------|----------------------|----------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type                 | Name                 | Property | Value        | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| column               | Coordinates          | type     | poly_rect    | Region for the map data - it can be a polygon or rectangle For a rectangle, the coordinate format is: {llx lly} {urx ury} (default) or llx lly urx ury . For example, {10 10} {50 50} or 10 10 10 50 . For a polygon, the coordinate format is: {x1 y1} {x2 y2} … {xn yn} or x1 y1 x2 y2 ... xn yn , where x1==xn and y1==yn . For example, {20 20} {20 40} {30 40} {30 30} {40 30} {40 20} {20 20} or 20 20 20 40 30 40 30 30 40 30 40 20 20 20 . |
| column               | Value                | type     | int or float | Data 0.835556                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| column               | Comment              | type     | string       | Data text information For maps that show objects in the layout view, the comment is the object name. For example, "map_data: 0.83556 " .                                                                                                                                                                                                                                                                                                           |
| column               | Comment_1            | type     | string       | Optional comment To indicate the data is in a special bucket. For example, the blocked regions in a route congestion map.                                                                                                                                                                                                                                                                                                                          |
| …                    | …                    | type     | string       | Optional comment that you would like to add Other additional columns                                                                                                                                                                                                                                                                                                                                                                               |

## To preview map data before importing it into the tool:

You might want to ensure that the map data is accurate before you load it into the tool. The GUI supports a preview dialog window that enables you to preview the map data.

To preview map data:

1. Ensure that you have the map data as a CSV file.

For more information on generating the CSV file, see the 'To export the map data for a specific map' section.

<!-- image -->

2. Run the following command using the -preview option:

```
icc2_shell> gui_read_user_map -preview -file global_congestion.csv
```

In this example, the global\_congestion.csv file is in the same directory as your design. If the file is in another location, provide the path to the file.

The (Re)Load User Map Data dialog box appears with the Column , Base Type , Data Type , First Row Values populated from the CSV file. If there are any errors, the dialog box displays the errors.

<!-- image -->

3. (Optional) Correct any errors them in the CSV file and preview the data before importing it into the CSV file.

Alternatively, you can use the Reload button in the User Map palette to load the preview dialog box.

## To import map data:

1. In the GUI, enable the User Map map mode in the layout viewView &gt; Map &gt; User Map
2. Click Reload
3. In the (Re)Load User Map Data dialog box, enter the name of the CSV file (along with the full path)

It may take a few minutes to load the data.

<!-- image -->

<!-- image -->

<!-- image -->

After the data is loaded, the layout view displays the map data. For example:

<!-- image -->

## To remove the map data that was read from the layout view:

1. In the GUI, enable the User Map map mode in the layout viewView &gt; Map &gt; User Map
2. Click Remove Current Map

<!-- image -->

## Visual Mode Overview

Visual modes highlight design information in colored overlays in the layout view. Use visual modes to highlight different elements of your design and organize the elements into bins. Visual mode support is provided for clock trees, scan chains, relative placement groups, and so on as shown in Figure 103. To view or hide a map mode in the layout view, choose Highlight &gt; Color By and select a visual mode, or click the Visual Modes button ( ).

<!-- image -->

<!-- image -->

Visual modes support style, histogram, and other configuration as described in Configuring Map Options.

Figure 103 Visual Modes

<!-- image -->

## Snapshot Visual Mode

Use the Snapshot Visual Mode to collect a group of selected objects into a bin and apply a highlight color. Enable the Snapshot Visual Mode by choosing Highlight &gt; Color By &gt; Snapshot from the menu.

Figure 104 Snapshot Visual Mode

<!-- image -->

<!-- image -->

You can perform the following operations with the Snapshot Visual Mode:

- Color the currently selected objects, create a new bin, and add the selection to the bin by clicking the Copy selection to new bin button ( ).
- Create a new empty bin by clicking the Create a new bin button ( ).
- Add selected objects to a bin by clicking the histogram bar to select the bin, clicking the down arrow at the left of the panel, and choosing Add selection to chosen bins.

<!-- image -->

Use the same context menu to remove selected objects from a bin or replace objects in a bin with the current selection.

- Delete a bin by clicking the row to select it and clicking the Delete chosen row button ( ).
- Remove all rows from the histogram by clicking the Delete all bins button ( ).
- Change the highlight color by right-clicking the histogram row, choosing Set Style, choosing a new color, and clicking OK.
- Change the ordering of the histogram bars or hide histogram bars by right-clicking a histogram bar and selecting the appropriate item in the context menu (Move to top, Move up, Move down, or Move to bottom).

<!-- image -->

## Highlight Visual Mode

Use the Highlight Visual Mode to create a histogram that represents the count of highlighted objects grouped by highlight color. Before using the Highlight Visual Mode, you can highlight objects in the layout by selecting them and choosing Highlight &gt; Selected . Enable the Highlight Visual Mode by choosing Highlight &gt; Color By &gt; Highlight from the menu.

Figure 105 Highlight Visual Mode

<!-- image -->

You can perform the following operations by right-clicking a histogram bar in the Highlight Visual Mode panel:

- Show or hide a histogram row and corresponding highlight color in the layout by choosing Show chosen rows or Hide chosen rows from the context menu.
- Configure exaggeration scheme and other display options by choosing Configure from the context menu.
- Change the color of the highlight by choosing Set Style from the context menu.
- Rearrange the order of the histogram bars by choosing Move to top, Move up, Move down, or Move to bottom from the context menu.
- Select or unselect highlighted objects in the layout by choosing Modify Global Selection and choosing an option to set the selection, append the selection, or remove from selection.

<!-- image -->

## Clock Tree Visual Mode

Use the Clock Tree Visual Mode to view and overlay information about the clock trees in your design.

Figure 106 Clock Tree Visual Mode

<!-- image -->

The panel displays a table containing a list of clock sources in the design. The table displays the type of clock using the following notation:

- M: Master clock
- G: Generated clock
- V: Virtual clock

<!-- image -->

<!-- image -->

The panel also displays a histogram that shows the number of clock sources, nets, and pins per level and number of clock elements of each type. You can perform the following operations with the Clock Tree Visual Mode:

- Sort the clock sources by name, port/pin, or is\_generated attribute by clicking the column heading in the clock table.
- Set the range hierarchy levels that are displayed by setting the values in the Levels: section of the panel.
- Show cells by level by selecting the Show cells by level option.
- Add information regarding the type of cell for clock buffers, inverters, and other cells in the layout by selecting Show cells by type .
- Display clock net flylines in the layout and add the count of clock nets to the histogram by selecting the Show nets option.

When selected, move the pointer over the clock net flyline to display additional information. If you perform global routing, the tool displays global routes instead of flylines.

- Display pins of cells in the clock tree and add the count of pins to the histogram by selecting the Show pins option.
- Change the highlight color by right-clicking the histogram row, choosing Set Style , choosing a new color, and clicking OK .
- Change the ordering of the histogram bars or hide histogram bars by choosing the appropriate item in the context menu.

## Tracing Clock Tree

The clock tracer view provides an easy-to-use interface to trace clocks and their associated clock pins, up to the clock tree sink pins.

You can use the clock tracer view to:

- Optimize and debug clock tree synthesis results
- View clock tree sinks that you might be interested in

To open the clock tracer view,

1. Choose Window &gt; Clock Tree Analysis Window .

Depending on how complex or simple your design is, the time taken to load the clock information in the CTS window varies. Complex designs take longer than simple designs.

<!-- image -->

You can filter the clocks and mode to narrow down the information that is displayed.

<!-- image -->

2. After the clock information is loaded, choose View &gt; Clock Tracer .

The CTS window displays a list of clocks organized by mode.

<!-- image -->

<!-- image -->

To expand the tracing of the clock tree, double-click on a clock or a clock pin from the CTS window. A new column appears displaying the clock pins for the respective clock or the clock pin. For example, Click the Schematic button for a pictorial representation of the clock hierarchy. For example, Use the Forward and Back buttons to navigate the clock hierarchy.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Examining Clock Tree Overlaps

The clock tree overlap analyzer view displays a hierarchical or flat list of clocks and a matrix of overlapping clock pairs. The overlap matrix consists of a grid with a row and column for each clock in the clock list.

To open the clock tree overlap analyzer,

1. Choose Window &gt; Clock Tree Analysis Window .

Depending on how complex or simple your design is, the time taken to load the clock information in the CTS window varies. Complex designs take longer than simple designs.

You can filter the clocks and mode to narrow down the information that is displayed.

<!-- image -->

2. After the clock information is loaded, choose View &gt; Clock Overlap Analyzer .

You can filter the clocks and mode to narrow down the information that is displayed.

<!-- image -->

<!-- image -->

<!-- image -->

In the clock list, expandable hierarchy trees represent the clock hierarchy among primary and generated clocks. You can click the expansion button (plus sign) next to a clock name to expand the tree, showing the names of the clocks at the next level in the hierarchy.

The overlap matrix consists of a grid with a row and column for each clock in the clock list. The Clock column on the left side of the matrix correlates the clock names (both primary and generated clocks) in the list with the rows and columns in the matrix. A light gray color in the grid indicates that clocks belong to the same clock domain. When you select a clock name in the clock list, a light blue color highlights the row for the corresponding clock in the matrix. Background pattern shows which clocks are in the same clock domain.

The matrix displays a number in the grid that indicates the number of overlapping points for the pair of clocks. If you click a box in the grid that represents an overlap, the tool displays the overlap point in the selection color, which is white by default, in other views such as a clock tree schematic or clock graph view.

Right-click anywhere on the grid to load the context-sensitive menu. The actions in the menu provide additional details, including clock graphs and clock attributes. From these details, you can view the overlapping points, which are highlighted.

## Viewing User-Defined Skew Groups

Skew groups allow you to balance more than one group of clock pins within a clock domain. In addition, you can include clock pins of integrated clock-gating cells and clock pins of clock-generating flip-flops in a skew group definition such that these pins are balanced with other pins and with the regular sinks in the same skew group definition.

Some of the benefits of using skew groups:

- You can group clock sinks that are not related to timing critical paths in a skew group and relax the target skew goals of the skew group.
- You can also give separate goals of target early delay to different skew groups and achieve the similar effect of useful skew to improve the slack of critical timing paths.

There are two types of skew groups:

- Default:
- Created by the tool
- A skew group is defined for each master clock and is named as default\_&lt;master\_clock&gt; .
- There are no specific sink pins associated with these skew groups.
- The sink pins are those for the associated master clock.

- User-defined:
- Created by the user by using the create\_clock\_skew\_group command.
- Each skew group is associated with a given mode.
- Each skew group is associated with a list of pins or ports.

To view the user-defined clock skew groups,

1. Choose Window &gt; Clock Tree Analysis Window .
2. Choose View &gt; Skew Group Analyzer .

The clock tree synthesis window displays both the user-defined ( ) and default ( ) clock skew groups. D

The skew groups are organized by mode. For user-defined skew groups, all paths to associated sinks are highlighted.

You can toggle between the Skew Groups mode and the Clocks mode by right-clicking any clock in the clock tree synthesis window. As shown in the following screenshots, the Skew Groups and Clocks modes display data that is relevant to skew groups and clocks, respectively. Clocks mode displays the skew groups by clock and the Skew Groups displays the related clocks by skew group. This categorization is helpful when the design has complex skew group definition.

<!-- image -->

Figure 107 Skew Groups Mode

<!-- image -->

## Figure 108 Clocks Mode

<!-- image -->

Using the Highlight Selected menu, you can highlight the selected clock or a skew group in the clock graph. For example,

<!-- image -->

## Viewing Full or Partial Clock Tree Graph

You can use the Abstract Clock Tree Graph to view,

- All clock trees associated with the master clocks for the skew group
- Only part of the clock tree associated with the selected user-defined skew groups

To build the clock tree graph,

1. Choose Window &gt; Clock Tree Analysis Window .
2. Choose View &gt; Skew Group Analyzer .

<!-- image -->

<!-- image -->

3. On the CTS window, right-click on a skew group and choose Clock Graph . The Abstract Clock Graph - Levelized window opens and displays the clock trees. In this window, you can also view the integrated clock gates.

Figure 109 Full Clock Tree Graph

<!-- image -->

Figure 110 Partial Clock Tree Graph

<!-- image -->

## Scan Chain Visual Mode

Use the Scan Chain Visual Mode to display connections between scan input, scan registers, and scan output for one or more scan chains. Enable the Scan Chain Visual Mode by choosing Highlight &gt; Color By &gt; Scan Chain from the menu.

<!-- image -->

Figure 111 Scan Chain Visual Mode

<!-- image -->

After clicking Reload in the panel, you can perform the following operations in the Update Scan Chain Visual Mode dialog box:

- Select the box next to the scan chain name and click the OK button to display the selected scan chains in the layout window.
- Click Select All button or the Clear All button to perform the action on the scan chains in the list.
- Click the Wire Length button to add a wire length column to the list.
- Click a column and drag it to a new position to reorder the columns.
- Move the mouse over a column header, click the right mouse key, and select an item from the context menu to configure or sort the columns in the list.

You can perform the following operations with the Scan Chain Visual Mode:

- Click the Query button to start the Query tool. Use the Query tool to display additional information about scan chain cells and pins.

<!-- image -->

<!-- image -->

- Select the Only reorderable nets option to display only nets that can be reordered.
- Select the Show boundary option to display an overlay boundary for the scan chain.
- Select the Show start/stop point option to show the port or pin connections to the first and last scan chain registers.
- Change the highlight color by right-clicking the histogram row, choosing Set Style, choosing a new color, and clicking OK.
- Change the ordering of the histogram bars or hide histogram bars by choosing the appropriate item in the context menu.

## Net Connections in Area Visual Mode

<!-- image -->

Use the Net Connections in Area Visual Mode to view nets that intersect a specified area of the layout and help identify the causes of congestion and placement issues during the initial placement stage. Enable the Net Connections Visual Mode by choosing Highlight &gt; Color By &gt; Net Connections in Area , or by clicking the Net Connections in Area button ( ).

Figure 112 Net Connections in Area

<!-- image -->

The tool highlights nets in the area you specify and classifies them into three types of nets:

- Local connections: Nets that have all pins and terminals within the specified area
- Global connections: Nets with at least one pin or terminal inside the specified area and at least one pin or terminal outside the specified area
- Pass-through connections: Nets that intersect the specified area but have no pins or terminals inside

<!-- image -->

To display net connections within a specified area,

1. Click the Reload button and specify the coordinates for the bounding box in which to display the nets.

To define a rectangular bound, click the area selection button ( ) and either type the x- and y-coordinates for the upper-left and lower-right corners of the rectangle in the Coordinates box or drag the pointer in the layout view to form the rectangle.

2. Select the types of nets to display (Signal, Clock, Power, Ground, Tie High, or Tie Low).
3. Click OK.

The tool displays the number of nets for each category and colors the nets in the layout window as shown in Figure 112.

Note that Figure 112 shows the layout after performing global routing. If you use the Net Connections in Area Visual Mode before performing global routing, the tool displays flylines instead of global routes.

Select Show only pins to hide the nets highlighted by the tool and highlight only the pins. For more information about modifying the histogram, see Configuring the Histogram. Click the List button to display a dialog box containing a list of nets as shown in Figure 113.

<!-- image -->

Figure 113 List of Net Connections in Area

<!-- image -->

<!-- image -->

You can perform the following actions by using the Net list dialog box:

- Click the Local connection nets, Global connection nets, or Pass-through connection nets options to toggle the visibility for that net type.
- Select a net name in the list of nets to highlight the net in the layout.
- Click the Select all button to select all nets in the list.
- Click the Histogram button to configure a simple histogram that displays the count of the number of pins or number of wires in the area; click OK in the dialog box to generate the histogram and display it in the histogram panel in the layout window.
- Click the Export button to write out the contents of the table into a file in commaseparated value format.
- Click the Columns button to configure which columns of data are shown.

## Relative Placement (RP) Groups Visual Mode

Use the RP Groups Visual Mode to highlight relative placement groups. Enable the RP Groups Visual Mode by choosing Highlight &gt; Color By &gt; RP Groups from the menu.

Figure 114 RP Groups Visual Mode

<!-- image -->

You can perform the following operations with the RP Groups Visual Mode:

- Highlight the relative placement groups in the design by clicking Reload and clicking OK.
- Highlight the relative placement groups based on group names by selecting Color by RP group.
- Highlight the relative placement groups based on their location in the hierarchy by selecting Color by RP hierarchical level.

<!-- image -->

- Highlight only the cells in the relative placement groups by selecting the Color cell only option.
- Increase or decrease the number of groups that are highlighted by entering a new value in the Maximum number of colors box; you can enter an integer value between 5 and 20.
- Select or unselect relative placement groups in the layout by right-clicking a histogram bar, choosing Modify Global Selection, and choosing an option to set the selection, append the selection, or remove from selection.
- Change the ordering of the histogram bars or hide histogram bars by choosing the appropriate item in the context menu.

## Relative Placement (RP) Net Connection Visual Mode

Use the RP Net Connections Visual Mode to highlight nets that connect relative placement groups. Enable the RP Visual Mode by choosing Highlight &gt; Color By &gt; RP Net Connections from the menu.

Figure 115 RP Net Connections Visual Mode

<!-- image -->

To display RP net connections,

1. Specify one or more RP group names in the RP Group box or click the Browse for RP group button ( ) and select one or more groups.
2. Select the Signal option to display signal nets, the Clock option to display clock nets, or both options to display both types of nets.
3. Click the Reload button to display Net Connections for the specified RP group in the layout.
4. (Optional) Click the List nets button to open a dialog box and display the local and global connections for the specified RP group as shown in Figure 116.

Use the dialog box to select, highlight, or export nets as described in Net Connections in Area Visual Mode.

Figure 116 RP Net Connections List

Total Nets: 116

<!-- image -->

<!-- image -->

<!-- image -->

You can perform the following operations with the RP Net Connections Visual Mode:

- Highlight only the pins connected to the RP net connections by selecting the Show only pins option.
- Show or hide RP net connection flylines by selecting or deselecting the check box next to Local Connection or Global Connection.

Local connections are nets that connect only to cells in the same relative placement group. Global connections connect at least one cell in the relative placement group to at least one cell outside the relative placement group.

- Select or deselect relative placement net connections in the layout by right-clicking a histogram bar, choosing Modify Global Selection, and choosing an option to set the selection, append the selection, or remove from selection.
- Change the ordering of the histogram bars or hide histogram bars by choosing the appropriate item in the context menu.

## Hierarchy Visual Mode

Use the Hierarchy Visual Mode to highlight and select different levels of hierarchy or specific hierarchical cells in your design. Enable the Hierarchy Visual Mode by choosing Highlight &gt; Color By &gt; Hierarchy from the menu.

Figure 117 Hierarchy Visual Mode

<!-- image -->

## Cell Slack Visual Mode

Use the Cell Slack Visual Mode to view and overlay information about setup and hold timing slack in your design. Open the panel by choosing Highlight &gt; Color By &gt; Cell Slack from the menu.

<!-- image -->

Figure 118 Cell Slack Visual Mode

<!-- image -->

Begin cell slack analysis by clicking the Reload button and selecting options in the dialog box. After setting the options, click OK to generate the data, The Cell Slack dialog box supports the following operations:

- Specify a scenario for analysis by selecting the scenario name from the box.
- Display setup time slack or hold time slack information by selecting the Setup or Hold option.
- Specify the number of bins into which to partition slack results by choosing Number of bins and selecting an integer value greater than zero.

Alternatively, specify a range of bin values by choosing Value range per bin and specifying the minimum and maximum cell slack values. Click the Lower bound strict or Upper bound strict options to remove slack values outside the specified range from the histogram.

## Note:

To generate the required list of slack results by specifying the number of bins, you can use this Tcl procedure:

```
proc_qor proc_histogram -num_bins
```

<!-- image -->

<!-- image -->

- Analyze specific cells by entering a list of cell names in the Cells box, or by selecting the cells and clicking the populate from selection button ( ).
- Change the color palette used in the histogram by choosing the Temperature or Gradient option.

## Imported Path Pins Visual Mode

Use the Imported Path Pins Visual Mode to highlight timing paths in the layout. Enable the Imported Path Pins Visual Mode by choosing Highlight &gt; Color By &gt; Imported Path Pins from the menu.

Figure 119 Imported Path Pins Visual Mode

<!-- image -->

To import a timing path and highlight the path in the layout,

1. Choose Highlight &gt; Color By &gt; Imported Path Pins to open the Imported Path Pins Visual Mode.
2. Update the timing for your design with the update\_timing command.

```
icc2_shell> update_timing -full
```

<!-- image -->

3. Report the timing for a path with the report\_timing command and save the result to a file.
4. Click the Reload button.
5. Select Import Path Pins from Timing Report and click the file chooser button.
6. Select the timing.rpt file you wrote out in step 3 and click OK.

```
icc2_shell> report_timing \ -from I_RESET_BLOCK/sdram_rst_n_buf_reg \ -to I_ORCA_TOP/I_SDRAM_TOP/I_SDRAM_IF/DQ_out_1_reg_6_ -nosplit \ -physical > timing.rpt
```

The Imported Path Pins Visual Mode panel displays a histogram bar for the path with the number of pins in the path. The tool also displays the flylines for the path in the layout view.

7. Repeat steps 3 through 6 to import and display additional paths. Choose the Clear all buckets before importing new path pins option to delete the histogram before importing the new path.

Instead of selecting the Import Path Pins option and importing the file as shown in steps 5 and 6, you can select Import from timing report text and paste the contents of the timing report into the text box as shown in Figure 120.

Figure 120 Import From Timing Report Text

<!-- image -->

## Voltage Areas Visual Mode

Use the Voltage Areas Visual Mode to highlight and select power domains, level shifters, isolation cells, and other cells related to the power domains in your design. Enable the Voltage Areas Visual Mode by choosing Highlight &gt; Color By &gt; Voltage Areas from the menu.

<!-- image -->

Figure 121 Voltage Areas Visual Mode

<!-- image -->

Click the Reload button to populate the Voltage Areas Visual Mode panel. Right-click a histogram bar and choose an item from the context menu to change the color, move the bar up or down in the list, select related objects in the layout, show or hide the histogram bar, and perform other operations.

## Viewing Schematics

The IC Compiler II tool supports design schematics to examine logic elements (blocks and gates) in a design. A design schematic displays a graphic representation of a hierarchical cell in a schematic view. You can move up or down in the design hierarchy to view the schematic for each design in the hierarchy.

The following topics describe the schematic view:

- Schematic View
- WordView in the Schematic View
- Annotating Attributes on the Schematic View
- Adding Pin Markers to the Schematic View

## Schematic View

To view a schematic, use one of the following methods:

- Choose View &gt; Schematic View in the main menu bar or in the Hierarchy Browser
- Click the button on the toolbar

<!-- image -->

Use schematic views to visually analyze timing and logic for use in further optimization operations. For example, you can

- View graphic representations of the logic elements (blocks and gates) in a design or subdesign
- Examine timing problems by focusing on critical paths in your logic design

To customize a schematic view, use the View Settings panel located in the tab on the right side of the tool.

## See Also

- Setting and Saving View Properties

<!-- image -->

## WordView in the Schematic View

WordView models wide combination logic gates that can be easily represented in schematic views. In the GUI, WordView allows for a cleaner schematic view of unmapped logic. The tool uses a wide logic gate instead of cascaded gates, and it shows bused instances in a collapsed representation. For purposes of area estimation, WordView more accurately models the original logic represented in the RTL.

WordView uses a WVGTECH library as opposed to a GTECH library. In order for the tool to infer these gates, you must have a WVGTECH library available.

When you are in the Schematic View, the GUI uses WordView gates to display:

- Bused instances
- Wide gates
- Operators
- Bused registers to multibit cells

The example in Figure 122 shows a collapsed bused instance. In this case, it is a WVGTECH\_AND gate with four inputs pins.

Figure 122 Collapsed View of a Bused Instance

<!-- image -->

You can expand the WVGTECH gate by selecting it and opening the context menu and selecting the Expand &gt; Selected Objects option. By default, bused instances are displayed in the GUI with a dashed border (see Figure 123). Bused nets are shown with one thick, blue line and bus inverters have the same logic symbol with a thick, green line. You can change the view from scalar to bus representation for a bused object using the Schematic View's context menu and select the Expand or Collapse menu options.

<!-- image -->

Figure 123 Expanded View of a Bused Instance

<!-- image -->

An example of the GUI representation of a WordView wide gate is shown in Figure 124. The XOR gate has 16 input pins and is named WVGTECH\_XOR16.

<!-- image -->

Figure 124 Example of Wide Gates

<!-- image -->

The GUI represents operators as basic symbols as shown in Figure 125. In this example, the tool is representing the addition operator.

<!-- image -->

Figure 125 Example of Operators

<!-- image -->

## Annotating Attributes on the Schematic View

To aid in debugging, you can annotate attributes on cells, pins, and ports in the schematic view. To do this, select the attribute to annotate in the Annotation Attributes section of the Settings tab on the View Settings panel, as shown in Figure 126. You can annotate only a single attribute on an object.

<!-- image -->

Figure 126 Annotation Attributes Section of the Settings Tab

<!-- image -->

In the following figure, the attribute annotations are shown in white. The area attribute is annotated on the cell and the port\_type attribute is annotated on the pins.

<!-- image -->

Figure 127 Attribute Annotations on Cell and Pins

<!-- image -->

You could use this capability to debug a timing violation by annotating an attribute such as late\_rise\_transtion on the pins on the path or to analyze the power by annotating an attribute such as switching\_activity or toggle\_rate on the pins on the path.

## Adding Pin Markers to the Schematic View

To highlight content in the schematic view, you can add markers on pins in the schematic view. When you add a marker, you can select the following characteristics of the marker:

- Shape: diamond or dot
- Color: yellow, orange, or red

To add a marker to a pin, right-click the pin, and choose Pin Markers &gt; Set &gt; marker\_type , where marker\_type is one of Yellow Diamond, Orange Diamond, Red Diamond, Yellow Dot, Orange Dot, or Red Dot. Figure 128 shows the interface for adding pin markers.

<!-- image -->

<!-- image -->

Figure 128 Adding Pin Markers

<!-- image -->

## Timing Analysis Using the GUI

Use the GUI to view timing analysis results and perform interactive queries on problematic timing paths.

The following topics describe timing analysis in the IC Compiler II tool.

- Opening the Timing Analysis Window
- Displaying the Timing Analysis Endpoint Summary
- Creating Path Collections
- Analyzing Timing Path Collections
- Analyzing Logic Levels

## Opening the Timing Analysis Window

After you have compiled your design, you can review timing analysis results by using the GUI.

To gather timing analysis results using the GUI,

1. Use the Timing Analysis window to get the endpoint summary information.

In the main menu bar, select Window &gt; Timing Analysis Window .

<!-- image -->

<!-- image -->

<!-- image -->

2. Create a collection of paths per endpoint summary
3. Analyze the timing slack for the selected collection of the paths

## See Also

- Displaying the Timing Analysis Endpoint Summary
- Creating Path Collections
- Analyzing Logic Levels

## Displaying the Timing Analysis Endpoint Summary

The Timing Analysis Window shows the timing summary of the current design. This should match the results of running the report\_qor -summary command.

Before using this information for analysis, make sure that the timing is up-to-date. The green check mark indicates that the timing is up-to-date. If it is not, a red mark is displayed. To update the timing, click the Update button (see Figure 129).

Figure 129 Timing Analysis Summary Window

<!-- image -->

## Creating Path Collections

When you are in the Timing Analysis window and select the Endpoints Summary tab, you can select which paths to analyze by creating a path collection. Do this by selecting the endpoints in the Endpoint Slack Table at the bottom of the window. Then, select Create Paths as shown in Figure 130.

<!-- image -->

Figure 130 Creating Path Collections

<!-- image -->

<!-- image -->

## Getting Timing Paths

After you select the Create Paths button, the Get Timing Paths dialog box appears as shown.

Figure 131 Get Timing Paths Dialog Box

<!-- image -->

Use this dialog box to fill out the options to report paths by design, group, scenario, mode, or corner. Clicking the OK button populates the summary of endpoints in histogram format. To perform logic-level analysis on the displayed summary of endpoints, select logic\_levels from the pulldown menu as shown in Figure 132.

<!-- image -->

Figure 132 Selecting Logic-Level Analysis

<!-- image -->

## Saving and Loading Timing Path Data

To save the selected timing path collections to disk, click the Write button at the bottom of the Timing Analysis window ( Path Collections tab). If parametric on-chip variation (POCV) is enabled when you save the timing path collection, the POCV data is saved with the timing paths. To load previously saved timing path data, click the Read button at the bottom of the Timing Analysis window ( Path Collections tab). If the POCV is enabled and the file contains POCV data, the POCV data is restored with the timing paths.

## Analyzing Timing Path Collections

You can use the path analyzer to analyze a collection of timing paths and determine where timing failures occur in the design. The path analyzer analyzes the paths using a rule that you specify, categorizes them based on available attribute values, and displays the categories in a color-coded treemap view. You can select a predefined category rule or define a custom category rule. You can also add subcategories.

<!-- image -->

<!-- image -->

To open the path analyzer, choose View &gt; New Path Analyzer in the timing analysis window.

You must load and categorize the timing paths before you can view them in the treemap.

To load a collection of timing paths,

1. Specify the collection in the Collections box. You can enter the collection name or a Tcl command that creates the collection.
2. Click Apply .

To categorize the timing paths,

1. Select All in the categories tree.
2. Click the Create button.

The Create Category dialog box appears.

3. Select a rule.
4. Click OK .

You can load one or more collections of timing paths from the same design.

After categorizing the paths, select All at the top of the category tree and reposition the slider on the right to view the categories in the treemap view. The All category contains all the paths that you have loaded into the path analyzer.

<!-- image -->

## Analyzing Logic Levels

When you perform logic level analysis in the GUI, the path collection window shows an updated histogram of timing paths.

Figure 133 Path Collection Window With Logic Levels

<!-- image -->

If you select a path in the endpoint slack table and then open the context menu, you can select options for further investigation such as viewing the schematic of the selected path or displaying the associated RTL using the Cross Probe option.

<!-- image -->

## Figure 134 Topics for Further Analysis

<!-- image -->

<!-- image -->

## 10

## Using the Error Browser

The IC Compiler II GUI provides the error browser tool to view error and informational messages, highlight related objects in the layout view, and disposition errors. Using the error browser tool, you can quickly select a group of errors to review, locate a particular error, and investigate the problem in the layout.

The following topics describe the error browser tool:

- Error Browser Overview
- Loading and Saving Error Data
- Managing the Error Hierarchy
- Managing the Error List and Viewing Error Details
- Using Error Filters
- Highlighting Errors
- Marking Errors as Fixed and Changing Error Status
- Writing Out DRC Error Data
- DRC Error Waiver and Container

## Error Browser Overview

The error browser provides functions to help you review errors, disposition errors, and save the updated error file to disk. As you select errors in the error browser, the layout viewer pans to the error location and zooms in to isolate the error in the view. Note that only the active layout view changes when the error browser zooms or pans to display the selected errors.

The error browser groups together errors based on error types, where error types are assigned by the GUI task or Tcl command that generated the error. Each error contains a brief description, bounding box coordinates for the error, and other information about the error.

To start the error browser, chose View &gt; Error Browser . When you open the error browser for the first time, the tool displays a dialog box containing the list of available error Options and controls message files, the checking task that generated the file, and the time the file was last modified. Select an entry in the list and click Open Selected to continue. The error browser is shown in Figure 135.

<!-- image -->

<!-- image -->

## Figure 135 Error Browser

<!-- image -->

A typical flow for debugging errors with the error browser includes the following steps:

1. Verify the design and save the results.
2. Open the saved error file in the error browser.
3. Select a group of errors to review.

You can group errors by either error type or the layer associated with the errors. Alternatively, choose a group of errors by their physical location in the design.

4. Analyze and debug each error by selecting the error in the list and viewing the error context in the layout view.

<!-- image -->

5. Correct the error in the layout view and mark the error as fixed or ignored in the error browser.
6. (Optional) Hide the fixed errors.

## Loading and Saving Error Data

By default, the error browser reads and writes error data files associated with the current block. The files are stored with a .err extension and are saved in the library directory for the block. You can also save and load an XML-format error data file not associated with the block.

To open an existing error data file that is associated with the current block,

1. Choose File &gt; Open to open the Open Error Data Dialog Box.
2. Select the error data file to open.
3. Click the Open Selected button.

To open an error data file with a .err extension or an unmanaged XML-format error data file,

1. Choose File &gt; Read Error File to open the file browser.
2. Select the file that you want to open.

If your file has a .xml extension, choose Any files in the Files of type box in the Open Error Data File dialog box.

3. Click OK .

To save changes to the error data after updating the fixed status or making other changes,

1. Choose File &gt; Save .
2. Click the Save button.

The tool writes the current state of the Error Browser to the output file. This menu operation is disabled if there are no open error data files or if there are no changes to the error data.

To save the error data in other formats,

- Choose File &gt; Export as CSV to write out the error data as a comma-separated values.
- Choose File &gt; Export to Error File to write out the information as error data.

## Managing the Error Hierarchy

The error browser displays two tabs below the menu bar: DRC and Editor DRC. The list in the DRC tab shows the hierarchy of errors in the current error data file. You can perform the following operations with the error hierarchy list:

- Click the [+] button to the left of the ErrorSet column to expand the list, or click the [-] button to collapse the list.
- Click a column header to sort the column or change the sort order for the column.
- Move the pointer over a row in the list to display information in the infotip.
- Click a row in the list to pan and zoom to the error in the layout view, and display additional information in the error list section of the browser.
- Click a row, hold down the Shift key, and click another row further down the list to select the range of rows.
- Click a row, hold down the Ctrl key, and click a second row to select multiple rows. Continue holding the Ctrl key and click additional rows to add them to the selection.
- Right click the mouse to display a context menu; select an item from the menu to open new error data, save the current error data, mark the current error as fixed, and so on.
- Choose Errors &gt; Next Error Group or Errors &gt; Previous Error Group from the Error Browser menu to navigate to another error group in the error hierarchy.

## Managing the Error List and Viewing Error Details

Below the error hierarchy list, the tool displays the error list. The error list contains a list of individual errors for the error type you selected in the error hierarchy section of the tool. You can perform the following operations with the error list:

- Click a column header to sort the column or change the sort order for the column.
- Click and drag a column header to reorder the columns.
- Move the pointer over a row in the list to display information in the infotip.
- Click a row in the list to pan and zoom to the error in the layout view, and display additional information in the error list section of the browser.
- Right click the mouse to display a context menu; select an item from the menu to toggle the fixed state of the error, highlight errors, and so on.
- Hold the Ctrl or Shift key and click additional rows in the list, or click and drag the mouse down the list to select more than one error.

<!-- image -->

<!-- image -->

- Clear the list by selecting the context menu item or by choosing Errors &gt; Clear Error List
- Choose Errors &gt; Next Error Group or Errors &gt; Previous Error Group from the Error Browser menu to navigate to another group in the error list.

The error browser displays details about the selected errors in the error detail section below the error list. Hold the pointer over the error detail pane to display an infotip that contains the error detail information.

## Using Error Filters

Use error filtering to temporarily remove the errors from the error browser and the layout view. Apply filters by using the Set Error Data Filter dialog box.

To create an error filter,

1. Choose Errors &gt; Set Filter .
2. Choose Show only matching errors or Hide matching errors to set the filter type.
3. Create the filter criteria by selecting the error type, layer setting, nets, and other settings.
4. Click Apply or OK to apply the filter, or Clear Filter to remove the filter.

When you create a filter, the filter is applied to the currently open error data and any other error data opened in the current session. Filters do not accumulate; applying a new filter overrides any previously set filter. To clear a filter, choose Errors &gt; Clear Filter or click Clear Filter in the Set Error Data Filter dialog box.

Figure 136 Set Error Data Filter Dialog

<!-- image -->

## Highlighting Errors

You can annotate errors in the layout view by applying different highlight colors. Use the Highlight menu to highlight errors and to remove highlighting. Alternatively, use the highlight buttons at the bottom of the GUI to perform these tasks. The Highlight menu provides the following menu commands:

- By Type, Layer, Net: Opens the Highlight Errors dialog box to highlight errors based on error type, layer string, or associated nets.
- Selected: Highlights selected errors with the current highlight color.
- All Errors in List: Highlights all visible errors in the error list with the current highlight color.
- Clear Selected: Clears highlight coloring from selected errors.
- Clear Current Color: Clears all highlighting of the current highlight color.

<!-- image -->

- Clear All: Clears all error highlighting.
- Set Current Color: Provides a menu of colors to select as the current highlight color.
- Next Color: Advances the current highlight color to the next color in the Set Current Color menu.
- Auto Cycle Colors: Toggles the option for changing the current highlight color to the next color after each Highlight &gt; Selected operation.
- Error Highlight Counts: Opens a dialog box that displays the number of errors in each highlight set and a simple histogram chart.

## Marking Errors as Fixed and Changing Error Status

To change the status of an error, select one or more errors in the error list and do one of the following:

- Click the Fixed button to toggle the fixed status value in the Status column.
- Click the right mouse key and choose Set Status, then select Error, Fixed, or Ignored as needed. Alternatively, choose Errors &gt; Set Status from the Error Browser menu and make the same selection.

These actions change the status of the selected errors. The value in the 'Status' column changes to a check mark to indicate that the error is fixed, clears to indicate an unfixed error, or changes to an (X) to indicate an ignored status.

## Writing Out DRC Error Data

The error browser provides a graphical tool for reviewing errors reported by various checking commands in the tool. To write a text report of the errors in a specific error data file, use the report\_drc\_errors command and use options to report specific error types or errors on specific layers.

The command writes out the following types of reports: error\_type, error\_layer, detailed, and matrix. Use the -report\_type option to specify the report type. The error\_type report, generated by default or by specifying the -report\_type error\_type option, is the default report type and lists the types and counts for each error type as shown in the following example. The error\_layer report type, generated by the -report\_type error\_layer option, is similar to the error\_type report, but groups errors first by layer, then by error type.

| ErrorSet -----------------------------------------------------------------------   |   Total |   Visible |   Fixed |   Ignored |
|------------------------------------------------------------------------------------|---------|-----------|---------|-----------|
| Design : test                                                                      |      54 |         3 |       0 |         0 |

Data : zroute.err                  54     3        0      0

<!-- image -->

<!-- image -->

| Net                | 3    |   1 |   0 |    |
|--------------------|------|-----|-----|----|
| METAL3 (28)        | 1    |   1 |   0 |  0 |
| Route Spacing      | 6    |   2 |   0 |  0 |
| METAL2 (18)-METAL3 | 1    |   1 |   0 |  0 |
|                    | (28) |     |     |    |

```
Net                          3      1        0      0 METAL3 (28)              1      1        0      0 Route Spacing                6      2        0      0 METAL2 (18)-METAL3 (28)  1      1        0      0 METAL3 (28)-METAL4 (31)  1      1        0      0
```

The detailed report type, generated by the -report\_type detailed option, reports error id, error type, and other information for each error similar to the comprehensive error information displayed in the error browser. The detailed report is shown in the following example.

```
Error ID          : 1 Error Type        : Route Spacing Error Layer       : METAL3 (28)-METAL4 (31) Number of errors  : 6 Description       : Spacing violation between hmg_out44_10_ and RES_I109_X9 on layers {METAL3 (28) METAL4 (31)} -direction: vertical, required: 1.2 um, actual: 0.6 um Status            : error Bbox              : {293.8000 364.4000} {294.2000 366.8000} Error ID          : 3 Error Type        : Route Spacing Error Layer       : METAL2 (18)-METAL3 (28) Number of errors  : 6 Description       : Spacing violation between A0_9_ and B0_9_ on layers {METAL2 (18) METAL3 (28)} -direction: upper left to lower right, required: 1.2000 um, actual: 0.6000 um Status            : error Bbox              : {261.0000 301.8000} {261.4000 303.0000}
```

The following examples write out different error reports based on the command options used:

- Write out the default error\_data error report for all errors in the error data file.
- Write out a detailed report only for the METAL3 layer for errors of type Route Spacing and Net.

```
icc2_shell> report_drc_errors -error_data zroute.err
```

```
icc2_shell> set type [get_drc_error_types \ -error_data zroute.err {{Route Spacing} {Net}}] icc2_shell> report_drc_errors -error_data zroute.err \ -report_type detailed -error_type $type -layers {METAL3}
```

## DRC Error Waiver and Container

To set the error waiver and container, choose Errors &gt; Set Error Waiver and Container .

Figure 137 Error Browser Dialog

<!-- image -->

Alternatively, you can use the following Tcl commands, see the man pages for detailed information:

- create\_drc\_error\_waiver
- remove\_drc\_error\_waivers
- write\_drc\_error\_waivers
- get\_drc\_error\_waivers
- set\_drc\_error\_status\_from\_waivers
- create\_waiver\_container
- remove\_waiver\_containers
- write\_waiver\_containers

<!-- image -->

- get\_waiver\_containers
- set\_drc\_error\_status\_from\_containers

You can find all the created waivers and containers by 'Select by Name Toolbar' as shown.

<!-- image -->

<!-- image -->

## 11

## Using the Message Browser

The IC Compiler II GUI provides the enhanced message system (EMS) database and message browser tool to manage and view error and informational messages related to rule violations in the layout. The EMS database is generated by the check\_design command and other checking commands. Using the message browser, you can select individual messages, select messages by message type, highlight the affected objects in the layout view, and create waivers for violations. The message browser also displays an HTML-format man page for the currently selected message. If you have multiple EMS databases, the message browser can merge the databases into a single consolidated database.

The following topics describe the message browser:

- Preparing the EMS Database
- Message Browser Layout
- Reclassifying a Message
- Creating a Waiver
- Merging EMS Databases

## Preparing the EMS Database

Before using the message browser, you must create an EMS database.

The database is created by design checking tools such as check\_design , check\_hier\_design , check\_netlist , check\_routability , and check\_timing . Run the create\_ems\_database command before the checking command and the save\_ems\_database command afterward. For example, icc2\_shell&gt; create\_ems\_database check\_hier.ems icc2\_shell&gt; check\_hier\_design -stage timing icc2\_shell&gt; save\_ems\_database Choose Window &gt; Message Browser Window from the layout window to open the message browser. Alternatively, use the check\_design command with the -open\_message\_browser option to automatically open the message browser after the analysis.

<!-- image -->

## Message Browser Layout

Figure 138 shows the different areas displayed in the message browser.

Figure 138 Message Browser

<!-- image -->

The following sections describe the panes in the message browser.

## Message Tree

The message tree lists errors in a tree view at the left of the browser as shown in Figure 139. The tree view displays the name of the current EMS database and the hierarchy of errors and warnings in the database.

<!-- image -->

Figure 139 Message Browser Tree

<!-- image -->

## Message List

The message list displays a complete list of messages for the currently selected error message type as shown in Figure 140. Each entry includes the Violation ID, internal error message index, current status (active, waived, or fixed), message text, and additional information if available. Move your mouse pointer over a message row to view additional information about the message. Click a row in the list to select it. After selecting the message row, the tool updates the detailed error message display. Click and drag the pointer to select more than one row, or press the Shift or Control key while clicking the row to add the row to the selection. Press Control-A to select all rows.

<!-- image -->

Figure 140 Message List

<!-- image -->

In the messages area, right click the mouse to display the context menu; select an entry from the menu to perform an action as follows:

- Waive: Reclassify the selected messages as waived; this action persists only for the current session
- Mark Fixed: Reclassify the selected messages as fixed; this action persists only for the current session
- Mark Active: Reclassify the selected messages as active; this action persists only for the current session
- Select: Select the related object in the layout view
- Highlight: Highlight the related object in the layout view
- Properties: Display the properties for the object
- Show Column Groups: Opens the Column Groups and Column Status Values panes
- Create Waiver: Opens the Create Waiver dialog; use this dialog to create a waiver as described in Creating a Waiver
- List Waivers: Opens the Message Waivers dialog; use this dialog to display the current list of waivers
- Copy: Copy the text for the currently selected rows

You can filter the list of messages by entering a filter pattern or by using column groups. As you enter characters in the search box, the tool updates the display to show only the messages containing the search string.

<!-- image -->

<!-- image -->

Column groups combine information counts from the columns in the message list area into a histogram view. The values column displays the number of unique results for each column. Click in a row in the Column Groups box to display additional information in the column values area on the right. As you click a row in the column values area, the list of messages is filtered to display only messages that match the currently selected value group. Click the Close button to close the column groups panel.

Figure 141 Column Groups

<!-- image -->

## Detailed Error Message

The message browser displays a detailed message summary and a description of the currently selected error. As you click different error messages in the message list, the detailed error message shows the message summary and detailed description for the error.

To change the position of the detailed error message, choose View &gt; Html Pane from the menu and select On Right or On Bottom.

## Reclassifying a Message

Use the message browser to reclassify individual messages as active, fixed, or waived. To reclassify a message only for the current session,

1. Select the message in the Tree View.
2. Choose Waive, Mark Fixed, or Mark Active from the Message Menu as shown in Figure 142. Alternatively, click the message and select the action from the context menu.

The tool updates the count in the list view.

Figure 142 Reclassify a Message

<!-- image -->

Note that these changes are active only for the current session and are not saved when you exit the message browser.

## Creating a Waiver

Create a waiver for a message to attach additional information to the message. This information is not saved to the EMS database. However, you can write out the waivers as Tcl commands and apply them in a later session. To create a waiver,

1. Select a message row to be waived.
2. Right-click and select Create Waiver from the context menu.

The tool displays the error waiver form above the message list as shown in Figure 143.

<!-- image -->

<!-- image -->

3. Complete the error waiver form by entering information in the Name and other boxes. Box labels preceded by an asterisk (*) are required entries.
4. Modify the criteria as needed.

Click the plus sign button (+) to add criteria, click the minus sign button (-) to remove a criterion, or click Remove All to remove all criteria.

Note that the criteria are applied to all messages in the list.

5. Click Apply to create the waiver.

The tool applies the criteria to all messages in the list and updates the status to Waived for the matching messages.

To display a list of waivers for the current session, choose View &gt; List Message Waivers from the menu. The tool displays a list of current waivers as shown in Figure 144.

Figure 143 Create Waiver

<!-- image -->

Figure 144 List Message Waivers

<!-- image -->

Click on the waiver to view the criteria used to create the waiver. To edit the waiver, select Edit criteria, modify the criteria settings, and click Commit. You can also use this dialog to write out the current waivers as a Tcl file, read in waivers stored in a Tcl file, or delete current waivers.

To use the waivers in another session, you must save them to disk. To save the waivers to disk, click Write from the Message Waivers dialog or choose File &gt; Write Waiver to Script from the message browser menu. The tool writes out gui\_create\_message\_waiver commands to the file. To read in waivers saved in a Tcl file, click Read from the Message Waivers dialog or choose File &gt; Read Waiver from Script from the message browser menu, then select the Tcl file that contains the waivers.

<!-- image -->

## Merging EMS Databases

The message browser can load multiple EMS databases in the same session. Only one database can be active at a time. To load more than one database,

1. Choose File &gt; Open Message Database from the menu.

Alternatively, open the database with the open\_ems\_database Tcl command as in the following example:

```
icc2_shell> open_ems_database MV.ems
```

2. (Optional) If you have opened multiple EMS databases, click the database to be merged to select it and choose File &gt; Set Current Message Database from the menu.
3. Choose File &gt; Merge Message Database from the menu, select a file, and click OK .

The tool loads the database file you selected and sets it as the current database as shown in Figure 145. The newly loaded database file contains its original messages and the messages from the current database before the merge.

Figure 145 Merging Databases

<!-- image -->

For more information about managing EMS databases with Tcl commands, see the man pages for the following commands:

- close\_ems\_databases
- create\_ems\_database
- get\_current\_ems\_database
- get\_ems\_databases
- open\_ems\_database
- save\_ems\_database
- set\_current\_ems\_database

<!-- image -->

## 12

## Creating Charts

The IC Compiler II tool contains a comprehensive plot generation utility you can use to generate interactive plots based on design, layout, and other data. See the following topics for more information:

- Creating a Model
- Creating a Plot

## Creating a Model

To create a chart, begin by importing the chart data from a comma-separated values (CSV) file to create a model. Use the gui\_create\_charts\_model command to read the CSV and save the information as a Tcl variable.

The following example writes out a simple CSV file containing the instance name, number of pins, and area for each macro in the design. The gui\_create\_charts\_model command loads the CSV file and creates a chart model.

```
set macros [get_cells -hier -filter "design_type==macro"] set csv_file /tmp/count_area.csv echo "macro_inst,count,area" > $csv_file foreach_in_collection c $macros { echo [get_object_name $c],[get_attribute $c number_of_pins],[get_attribute $c area] >> $csv_file } set model [gui_create_charts_model -csv $csv_file -first_line_header ]
```

Note that the gui\_create\_charts\_model command automatically derives the data type for each column of data.

Alternatively, you can import the CSV file by using the GUI. Click the Charts tab in the View Settings panel, then click the Models tab. Click the Create button to open the Load Model dialog box. Enter the file name, select options to specify the header. The tool displays a preview of the data as shown in the following figure. Click OK to create the model.

<!-- image -->

Figure 146 Load Model Dialog Box

<!-- image -->

In addition to using CSV, you can create a model directly from a collection or a Tcl array. For example:

```
set selection [get_nets] set model1 [gui_create_charts_model -clct $selection -columns {name dr_x_length dr_y_length}] set data [list \ [list State {Under 5 Years} {5 to 13 Years} {14 to 17 Years} {18 to 24 Years} {25 to 44 Years} {45 to 64 Years} {65 Years and Over}] \ [list CA 2704659 4499890 2159981 3853788 10604510 8819342 4114496] \ [list TX 2027307 3277946 1420518 2454721 7017731 5656528 2472223] \ [list NY 1208495 2141490 1058031 1999120 5355235 5120254 2607672] \ [list FL 1140516 1938695 925060 1607297 4782119 4746856 3187797] \ [list IL 894368 1558919 725973 1311479 3596343 3239173 1575308] \ [list PA 737462 1345341 679201 1203944 3157759 3414001 1910571] \ ] set model2 [gui_create_charts_model -tcl $data -first_line_header]
```

<!-- image -->

## Checking the Model

After creating the model, check the model in the GUI by clicking the Charts tab in the View Settings panel. Click the Models tab to show the list of models created with the gui\_create\_charts\_model command.

To view details for a model, including column names, data types, and other properties, click the model in the table and click the Edit button to show the table of data. Click each column to show the column name, data type, and other attributes for the data column. To change the properties for the column, select an entry in the Column Data section and click Apply .

<!-- image -->

Figure 147 View/Edit Model Dialog Box

<!-- image -->

## Adding or Deleting Data From the Model

After importing the CSV file, you can modify the data type by adding columns, deleting columns, and performing other operations with the gui\_change\_charts\_model command. The following example adds a new column called 'double\_count' which is twice the value of the data in column(1).

```
gui_change_charts_model -model $model -add \ -expr {column(1) + column(1)} -header double_count
```

<!-- image -->

<!-- image -->

Remove all model from all charts using the gui\_remove\_charts\_model command.

## Creating a Plot

After importing the CSV file to create a model, you can create a plot to view the data. Use the gui\_create\_charts\_plot command to create a bar chart, distribution plot, XY chart, and so on.

The following example writes out a CSV file that contains the pin count and area for four macros in the design. The gui\_create\_charts\_plot command creates the initial plot based on the CSV file contents. Next, the plot is converted to a horizontal bar chart by choosing Horizontal from the context menu. The data table is displayed by choosing Show Table from the context menu.

```
# Create the Charts window set view [gui_create_window -type Charts] # Specify the macros and output CSV file set macros [get_cells { cmem0/idata0_2/x0_t0 cmem0/dtags1_1/x0_t0 rf0/x0/t_bl cmem0/itags0_3/x0_t0 }] set csv_file count_area.csv # Write out the CSV file echo "macro_inst,count,area" > $csv_file foreach_in_collection c $macros { echo [get_object_name $c],\ [get_attribute $c number_of_pins],\ [get_attribute $c area] >> $csv_file } # Create the model set model [gui_create_charts_model -csv $csv_file -first_line_header] # Create the bar chart from the model set plot [gui_create_charts_plot -view $view -type barchart \ -model $model -columns {{name 0} {value {1}}}]
```

Figure 148 Bar Plot

<!-- image -->

After creating the chart, click the column headers to sort the data. To filter the table data, enter a filter expression in the filter expression box. For example, to show only macros with a count greater than 100, enter 'count &gt; 100' in the filter expression box as shown in the following figure.

<!-- image -->

Figure 149 Filtering Plot Data

<!-- image -->

## Customizing a Plot

You can modify the plot to:

- Customize the appearance using the View Settings &gt; Properties or the gui\_set\_charts\_property command and set the data using the gui\_set\_charts\_data command.
- Add annotations using View Settings &gt; Annotations or the gui\_create\_charts\_*\_annotation commands.
- Lay out multiple plots in view using View Settings &gt; Plots , or the gui\_place\_charts\_plots and gui\_group\_charts\_plots commands.
- Run custom Tcl procedures on user interaction using the gui\_connect\_charts\_signal command.

<!-- image -->

## 13

## Using the PG Pattern Viewer

The IC Compiler II GUI provides the PG Pattern window for creating and previewing PG patterns. Use the PG Pattern window to view a collection of prepackaged PG pattern templates. After selecting a template for a PG pattern, copy the pattern template to the PG Pattern Editor and edit the pattern to conform to your design requirements. If the pattern uses parameters, you can set parameters in the PG Pattern window. Preview the pattern and make any necessary changes to the Tcl command. Only after the pattern is finalized, return to the layout window and instantiate the pattern in your design.

See the following topics for more information about the PG Pattern window:

- Selecting a PG Pattern Template
- Previewing a Template PG Pattern
- Previewing Existing Pattern and Strategy Definitions
- Highlighting Individual Patterns

The PG Pattern window is shown in the following figure.

<!-- image -->

## Figure 150 PG Pattern Window

<!-- image -->

## Selecting a PG Pattern Template

The PG Pattern window contains a set of prepackaged templates that you can use as a starting point for creating your own pattern. Open the PG Pattern window by choosing Window &gt; PG Pattern Window from them menu. To view and select a template in the PG Pattern Window,

<!-- image -->

<!-- image -->

1. Open the PG templates dialog box by clicking the View Templates button in the PG Pattern window.
2. (Optional) In the PG Pattern Templates dialog box, enter a string in the filter pattern box to filter the list of templates. The matching is case-insensitive.

For example, enter 'Mesh' or 'mesh' to display only templates that contain the word Mesh.

3. Select a template by clicking a template name in the list.

The tool displays the template in the PG Pattern Template window. A typical template includes a brief description, an image of the pattern, and the Tcl command used to create the pattern.

4. Click the Send to Editor button to copy the template to the PG Pattern Editor in the PG Pattern window.

<!-- image -->

Figure 151 PG Pattern Templates

<!-- image -->

## Previewing a Template PG Pattern

The pattern preview function displays a template pattern in the preview window. To use the pattern preview function,

1. Copy a pattern template to the PG Pattern Editor as described in Selecting a PG Pattern Template.
2. (Optional) Modify the layer, spacing, width, and other parameters of the pattern to match the current design.
3. Click the Apply button to display the pattern in the preview window.

The tool runs the create\_*\_pattern command specified in the PG Pattern Editor panel and adds the pattern name to the list of patterns in the PG Pattern Browser. Use the report\_pg\_patterns command in the layout window to write out a detailed report for the current patterns defined for the design. If any errors occur while creating the pattern, the tool writes error messages to the console.

<!-- image -->

<!-- image -->

## Previewing Existing Pattern and Strategy Definitions

You can use the PG Pattern window to preview previously defined patterns and strategies as follows:

1. Create the PG pattern by running the create\_pg\_ring\_pattern , create\_pg\_ring\_pattern , or other pattern creation command in the layout window.

You can create the patterns before or after opening the PG Pattern window. Any PG patterns that you define in the layout window are listed in the Patterns list under PG Pattern Browser. In this example, four ring patterns are defined.

Figure 152 Predefined Patterns

<!-- image -->

2. (Optional) Click the right mouse button and choose Delete from the context menu to remove a pattern from the list.
3. Click a pattern in the list to select it and display the corresponding create\_*\_pattern command in the Pattern Creation Script editor.
4. (Optional) Modify the pattern in the editor.

Figure 153 Pattern List Context Menu

<!-- image -->

<!-- image -->

5. (Optional) Create one or more PG strategies with the set\_pg\_strategy command.
6. (Optional) Select the strategy to create the pattern in the Strategy box under Strategy Setting.

Only the strategies available for the selected pattern are displayed in the Strategy box. The tool also creates a default strategy for the pattern you selected.

7. Click Apply to create the pattern in the preview window based on the selected strategy and pattern.

Note that the pattern is created only in the preview window, not the layout window for the current design.

8. (Optional) Select a new pattern from the pattern list or a new strategy from the strategy box and repeat the previous step to generate a new pattern.

## Highlighting Individual Patterns

The PG Pattern viewer supports the highlighting of individual child patterns within a pattern. Use this feature to highlight the power straps and vias for a child pattern within a pattern definition and make adjustments to the metal layer, layer width, spacing, and so on. To view an individual child pattern within a pattern,

1. Select the pattern for the list of pattern templates, such as the via bridging pattern.
2. Click the right mouse button and select the child pattern number from the list.

The tool highlights the metal shapes that compose the pattern number.

The following figure shows the sample via bridging composite pattern with second pattern highlighted.

<!-- image -->

Figure 154 Highlight Child Patterns

<!-- image -->

## 14

## Creating Routes

The IC Compiler II GUI provides interactive and programmatic interfaces to quickly and easily create routes. Use the Create Route tool to route one or more nets or bundles between pins, ports, and other route shapes in the design. Similar to the Create Route tool, use the Create RDL tool to route single nets to create orthogonal and 45degree routes on the redistribution layer or other metal layers. The create\_trunk , create\_trunk\_pin\_to\_pin , and create\_trunk\_pin\_to\_trunk commands create route segments on specified nets based on command line options.

The following topics describe how to create routes by using the GUI:

- Creating Routes Interactively
- Performing Interactive Design Rule Checking on Routes
- Creating Route Trunks With Tcl Commands or GUI
- Adding Buffers on Routes
- Estimating Point-to-Point Resistance

## Creating Routes Interactively

The Create Route tool enables you to interactively route one or more nets or bundles. Options to the tool specify how the routes are created. The tool supports blockage avoidance and DRC feedback to help create high quality, violation-free routes and connection. Snapping, auto-alignment, and auto-welding are provided to quickly and easily connect new routes to pins or preexisting routes. Bundle routing is supported for the simultaneous routing of several signals at one time.

## Starting the Create Route Tool

To start the Create Route tool, do one of the following:

<!-- image -->

- Click the Create Route button ( )
- Choose Create &gt; Route from the menu
- Press Shift+R

<!-- image -->

The tool starts and displays the Create Route toolbar.

## Specifying Layer, Width, Pitch, and End-Cap Style

The Create Route tool provides settings and options on the toolbar to specify the layer, width, pitch, and end-cap style for routes as shown in the following figure. Other settings are available by clicking the More , DRC , or Snap buttons on the toolbar.

Figure 155 Layer Name, Width, Pitch, and End-Cap Settings

<!-- image -->

Use any of the following methods to specify the layer name, width, and pitch for a net or bundle:

- Enter net names or a bundle names in the box; the tool sets the horizontal and vertical layers to match the lowest metal layers for routing.
- Select a pin before starting the Create Route tool to infer the net name. The tool sets the layer, width, and so on based on the selected pin.
- Select the Net option in the Auto section of the toolbar, then click an existing route to infer the net name from that route. To infer the layer, width, or end-cap style from the existing route, select the corresponding option in the Auto section.
- In the More settings panel in the toolbar, enable the Connect to pin by layer option and specify a layer name. The tool uses the specified layer when automatically connecting to pins, unless the pins are the starting or ending point for the route.

## Creating Routes Between Pins

To create routes for a collection of pins,

1. Select the source or destination pins for the nets to be routed.
2. Start the Create Route tool by pressing Shift+R or by clicking the Create Route tool button ( ).
3. Click the More button in the toolbar and select the Extend first option and the Extend last options in the Advanced options section.

<!-- image -->

Figure 156 Settings for Connecting Routes Pin-to-Pin

<!-- image -->

4. Begin drawing the route by placing the pointer in the route path near the selected pins and clicking the mouse as shown in image (A) in the following figure.
5. Click to create a corner, then move the mouse pointer in the orthogonal direction as shown in image (B).

Figure 157 Routing From Selected Pins

<!-- image -->

Repeat this step as needed to create additional route segments.

6. Move the mouse pointer near the destination pins until the tool shows the completed route as shown in image (C) in the following figure.

<!-- image -->

Figure 158 Completing the Route

<!-- image -->

<!-- image -->

7. Press the Enter key or click the right mouse key and choose Apply from the context menu to complete the route.

The tool completes the route as shown in image (D).

## Applying Route Segment Width and Spacing Based on the First Segment

To create all route segments with the same width and spacing as the first route segment, click the More button on the toolbar and enable the Pitch and Width options in the Follow first segment section. When enabled, the tool creates all subsequent route segments to match the first segment as shown in the following figure.

Figure 159 Follow First Segment

<!-- image -->

## Creating Off-Track Routes

To create off-track routing segments, click the More button on the toolbar and disable the First net and Every net options in the Snap to track section. By default, the First net option is enabled and the first routing segment is created on the routing track. The following figure shows these options.

<!-- image -->

<!-- image -->

<!-- image -->

Figure 160 Snap to Track

<!-- image -->

## Creating Successive Routes Above or Below the Drawn Path

The Create Route tool starts with the first net in the bundle or the net name box and creates the route along the path you draw with the mouse. Subsequent nets are created in parallel to the first net; the direction is determined by the Low end and High end options in the When starting use section of the More settings panel.

In the following example, the bundle named bundle4 is created with the create\_bundle command and is used to route the four nets as follows:

```
icc2_shell> create_bundle -name {bundle4} \ {net2[127] net2[126] net2[125] net2[124]}
```

The first net in the list is net2[127] and is created along the path you draw with the mouse. By default, subsequent nets are created above or to the right of net2[127] as shown in the left image in the following figure. The yellow highlight represents the path of the mouse used to draw the route.

Figure 161 Low End and High End Routing Options

<!-- image -->

To create subsequent routes to the bottom or to the left of the mouse path, click the More button in the toolbar and choose the High end option. The tool creates routes as shown in the right image in the previous figure.

## Changing the Route Ordering for Orthogonal Routes

The Create Route tool supports different methods for ordering nets when creating an orthogonal route. By default, the tool maintains the ordering of the nets and does not overlap the routes when creating new route segments. To reverse the ordering of the routes when creating an orthogonal route, click the More button and enable the Switch ends option in the When turning section. To stagger the routes at the turn, enable the Switch ends option and set the Skip count to a value greater than 1. The following figure shows the routing result after setting these options.

<!-- image -->

Figure 162 Route Turn Styles

<!-- image -->

<!-- image -->

## Displaying Route Guidance Flylines and Annotations

The Create Route tool displays flylines and other guidance to help you create the route. When you start the Create Route tool and enter a net name, the tool displays a static flyline between the pins and ports on the route. After you begin the route, the tool adds a dynamic flyline to show the shortest path to the closest pin connection; the dynamic flyline updates as you move the mouse to create the route segments. After you complete the route, the dynamic flyline is removed. By default, to tool displays flylines between the pins and ports on the route, and port guidance markers on the ports in the route.

To hide flylines and port guidance markers, click the More button and deselect the Port Guidance and Flylines options in the Show section of the panel. To display existing routes and a resistance value for the current route that dynamically updates as you create route segments, select the Routes and Resistance options in the panel. The following figure shows the options in the panel and the layout annotations associated with the options.

<!-- image -->

<!-- image -->

Figure 163 Show Flylines and Other Annotations

<!-- image -->

Route markers

## Preventing Connections to Existing Routes

To prevent the tool from automatically creating vias when crossing a route of the same net, click the More button and deselect the Auto welding option in the Advanced options section of the panel. The following figure shows the routing result created by changing this option.

<!-- image -->

Figure 164 Auto Welding

<!-- image -->

## Setting a Search Distance and Specifying Layers to Search

The Create Route tool automatically connects routes to the pins that are within the search distance of the current mouse position. To prevent the tool from connecting to pins when the Auto welding option is enabled, click the More button and set the value in the Search distance box in the Welding and extend options section to 0. To allow the tool to connect to pins at a greater distance, increase the distance to allow the tool to search for pins farther from the route. The following figure shows the layout result for the same pins and drawn route (along the yellow highlight) at different search distances.

Figure 165 Search Distance

<!-- image -->

The tool searches all routing layers for connections. To limit the search to only adjacent layers, click the More button and select the Search Layers: Adjacent option in the Welding and extend options section of the panel. When selected, the tool only connects to pins that are on a layer adjacent to the current routing layer. To specify a range of layers to search, select the Specified option in the same section and select one or more layers in the layer box.

<!-- image -->

## Specifying Other Welding and Connection Options

The Create Route tool supports additional options for specifying the connection to existing routes or pins.

- Ignore pin access direction : When selected, the tool automatically connects routes to pins regardless of pin access direction. By default, pin access direction is considered.
- Skip PG nets : When selected, avoid creating a connection to a PG net. This option is used to skip connections to ground nets when the nets are used for net shielding.
- Honor via to via spacing : When selected, the tool honors same-net via-to-via spacing rules.
- No via on pin : Avoids inserting a via when making a connection to a pin.
- Adjust to pin width : When selected, the tool sets the width of the route to the width of the pin, if the wire width is less than the pin width. By default, this option is deselected and the width of the wire is specified in the toolbar. Note that if the wire width is greater than the pin width, the pin width is used for the wire width.
- Align with pin center : When deselected, the tool aligns the connecting wire with the nearest parallel pin edge or extends the wire within the parallel pin edge boundaries. Track snapping and spacing requirements might affect the final wire position. By default, this option is selected and the tool aligns the route with the center of the bounding box for the pin if possible. When the pin is wider than the connecting wire, the tool might shift the wire off-center to honor track snapping and spacing settings.

## Creating 45-Degree and RDL Routes

The Create RDL tool supports many of the same features of the Create Route tool. In addition, the Create RDL tool can be used to create redistribution layer (RDL) routes and general 45-degree routes on one metal layer.

<!-- image -->

Figure 166 Create RDL Tool

<!-- image -->

To create a 45-degree route with the Create RDL tool,

1. Start the Create RDL tool by choosing Create &gt; RDL from the menu or by clicking the Create RDL button ( ).
2. Enter the net or bundle name to route in the net name box.
3. (Optional) Click the More button and modify settings in the More options panel.

The Create RDL tool supports many of the same settings as the Create Route tool, such as extend first, extend last, high end, low end, and so on as described in the previous sections.

4. Click the Route button at the left of the toolbar and choose the angle to use to route the net.

This setting determines how the route is created as shown in the following figure.

<!-- image -->

Figure 167 Create RDL Drawing Modes

<!-- image -->

5. Click the pin, port, or net connection to begin the route.
6. Click to complete a route segment and begin a new segment.
7. Press Enter to complete the route.

<!-- image -->

## Recording and Replaying Create Route Actions

The Create Route and Create RDL tools support a record feature that captures the mouse actions used to create a route and saves them to the Script Editor. The script can be saved to disk and run at a later time. Alternatively, the script can be run directly from the Script Editor. The record feature can be configured with options to tolerate small changes in the position of the pins; this allows you to re-create a route after minor design changes.

To create a route and enable recording,

1. Start the Create Route tool by choosing Create &gt; Route , clicking the Create Route button ( ), or pressing Shift+R.
2. Start the Create RDL tool by choosing Create &gt; RDL or by clicking the Create RDL button ( ).
2. (Optional) Set any necessary routing options in the toolbar.
3. (Optional) If the pin or segment coordinates in the route are expected to change when the route is re-created, click the More button and enable the Relative to nets option in the Log/replay coordinates section.

When this option is enabled, the tool captures coordinates relative to the bounding box for the entire route, rather than capturing absolute coordinates. This option is useful if the script is applied to create routes in a different area of the design.

4. Click the Record button ( ) on the Create Route tool toolbar.
5. Create the route by clicking the startpoint, creating net segments, and terminating the route.
6. When the route is complete, open the Script Editor and click the Save As button ( to save the script to a file.

<!-- image -->

)

As you create the net segments, the Create Route tool captures the actions in the Script Editor. A sample script captured by the record function is as follows:

```
... # Info : recording session started ... gui_mouse_tool -window [gui_get_current_window -types Layout -mru] \ -start CreateRouteTool set_edit_setting -default set_snap_setting -default ... gui_set_mouse_tool_option -tool CreateRouteTool -all -default gui_set_mouse_tool_option -tool CreateRouteTool \ -option {BundleOrNetNames} \ -value {net2[127] net2[126] net2[125] net2[124]}
```

<!-- image -->

<!-- image -->

```
... gui_mouse_tool -window [gui_get_current_window -types Layout -mru] \ -add_point {455.756 907.825} -scale 0.02 gui_mouse_tool -window [gui_get_current_window -types Layout -mru] \ -add_point {568.946 1194.223} -scale 5.6331 ... gui_mouse_tool -window [gui_get_current_window -types Layout -mru] -apply gui_mouse_tool -window [gui_get_current_window -types Layout -mru] -abort ... # Info : recording session ended
```

To re-create the route, run the script by clicking the Run Script button in the Script Editor. Alternatively, save the script to a file and execute the script with the source command.

## Performing Interactive Design Rule Checking on Routes

The GUI offers two types of interactive design rule checking:

- Editor DRC

For more information about the Editor DRC tool, see Diagnosing Design Rule Violations Using the Editor DRC tool in this guide.

- ICV Live

For more information about the ICV Live feature, see Checking Signoff Design Rules Interactively in the GUI in the IC Compiler II Implementation User Guide .

## Diagnosing Design Rule Violations Using the Editor DRC tool

The layout view provides the Editor DRC tool to identify and diagnose DRC violations caused by interactive editing operations. The Editor DRC tool detects design rule violations, displays error shapes in the active layout view, and records the violations in an Editor DRC error data file. Note that the Editor DRC tool runs only a quick check and displays errors using a set of the DRC rules defined in the technology file; the Editor DRC tool does not replace a comprehensive DRC tool such as IC Validator.

In addition to the Create Route tool, the following layout editing tools work with the Editor DRC tool:

- Copy Objects tool
- Create Fill tool
- Create RDL tool
- Create Shape tool
- Create Terminal tool

- Create Via tool
- Quick Connect tool
- Stretch Connected tool
- Stretch tool

## Verifying Route Edits Interactively

<!-- image -->

To enable or disable the Editor DRC tool for interactive editing operations, click the DRC button ( ) on the toolbar and select the DRC enabled option.

When you enable the Editor DRC tool for an interactive editing operation, the tool provides immediate visual feedback if it detects a violation. The layout view displays a different visual cue for each type of violation.

The Editor DRC tool supports rule checking on the following types of objects:

- Horizontal and vertical net shapes and user shapes, including wires, vias, via arrays, paths, polygons, and rectangles
- Port shapes and terminals
- Standard cells, hard and soft macros, and black boxes
- Routing blockages

## Verifying Edited Nets

To check selected nets for Editor DRC tool violations,

1. Select one or more nets you need to check.
2. Choose Edit &gt; DRC &gt; Run DRC on Selected Shapes.

Alternatively, you can use the gui\_check\_drc\_errors command.

If an error is found, the tool creates the error data and opens the Error Browser with the error data displayed.

## Setting Editor DRC Options

The Editor DRC tool provides rule checking for a set of DRC rules defined in the technology file. The interactive editing tools use the Editor DRC tool to detect routing design rule violations that occur during interactive editing operations. You can set the maximum number of violations that the tool can detect and control whether the tool opens the error browser and loads the errors automatically when violations are detected.

<!-- image -->

<!-- image -->

To set Editor DRC tool options, click the DRC button ( ) on the toolbar when a tool that supports the Editor DRC is active.

When you change an option setting in the Editor DRC options dialog box, the change occurs immediately for all applicable tools in all open layout views. If GUI command output logging is enabled in the Application Preferences dialog box, the tool also records the change by displaying a set\_edrc\_setting command in the console log view and history view.

## Examining Errors Reported by Editor DRC

When the Editor DRC tool detects design rule violations, it displays error shapes in the active layout view, records the errors in an Editor DRC error view, and automatically loads information about the error into the error browser as shown in the following figure.

Figure 168 Editor DRC

<!-- image -->

The error view contains error records for violations detected during interactive editing operations and violations detected when you run checks on selected shapes. The Editor DRC tool updates the error data when you fix a violation, reverse an editing operation that caused a violation, disable the design rule check used to detect a violation, or remove errors in the error browser.

<!-- image -->

The Editor DRC error view is associated with the current design. It remains open and loaded in the error browser until you close the design or change the current design. However, the tool does not save the error view when you save or close the design. If you close the current design, the Editor DRC tool closes the error view and removes the errors from the error browser.

## Creating Route Trunks With Tcl Commands or GUI

The IC Compiler II GUI supports Tcl commands to create route trunks for specified nets and bundles. Use the create\_trunk , create\_trunk\_shared\_track , create\_trunk\_pin\_to\_trunk , create\_trunk\_pin\_to\_pin , and create\_trunk\_topology commands to create route trunk segments and connections as described in this topic.

## Creating Route Segments in One Direction

To create route trunks in one direction on a single metal layer, use the create\_trunk command as follows:

```
icc2_shell> set nets [get_nets {net1 net2 net3 net4}] icc2_shell> create_trunk -nets $nets -layer M3 \ -gravity percentage -percentage 25
```

The command creates a route segment for each net or bundle specified by the -nets option. In this example, the -gravity percentage option specifies how the route segments are aligned with the bounding box for the nets. The -percentage 25 option specifies that the first route segment is placed at the bottom edge of the bounding box plus 25 percent of the height of the bounding box. The following figure shows different routing results for percentage values of 25, 50, and 75.

## Figure 169 Create Trunk

<!-- image -->

Specify the following options to the create\_trunk command control how the routes are created.

- Specify the routing direction for the layer with the -direction horizontal | vertical option. By default, the command creates routes in the preferred direction.
- Align routes with the driver for the net by specifying -gravity driver . Align routes with the load for the net by specifying -gravity load .
- Create the routes on specific tracks within the bounding box for the net by using the -track\_numbers , -track\_coords , -track\_step , and -track\_ref\_bbox options. For example, to create routes within the bounding box from (50,50) to (100,100), starting from the second track within the box, specify the following command:
- Place routes on the next available unobstructed track by using the -avoid\_obstructions option. By default, the command issues a warning message and skips the net if an obstruction is found.
- Disable checks for shorts and obstructions and preview the route with the -do\_not\_check\_shorts option.

```
icc2_shell> create_trunk -nets $nets -layer M3 \ -track_ref_bbox {{50 50} {100 100}} -track_numbers 2
```

<!-- image -->

The following figure shows the layout result created by using the -do\_not\_check\_shorts and -avoid\_obstructions options.

Figure 170 Ignoring Obstructions and Shorts, and Avoiding Obstructions

-do\_not\_check\_shorts

<!-- image -->

-avoid\_obstructions

<!-- image -->

- Avoid snapping routes to tracks by using the -do\_not\_snap\_to\_track option.
- Create more than one route per net by using the -num\_wires option.
- Restrict the routes only certain track widths by using the -width option. By default, routes are created on the tracks with the default width.

To create route trunks in one direction on a single metal layer in the GUI,

1. Choose Task &gt; Trunk Routing .
2. In the Trunk Routing panel, click Setup .
3. In the Trunk Routing Setup window, click on the create\_trunk link.
4. Specify the nets or bundles for which to create route trunks.
5. Specify the layer on which to create route trunks.
6. (Optional) Specify the information for the rest of the fields as necessary.
7. Click OK .

<!-- image -->

## Figure 171 create\_trunk Command - GUI

<!-- image -->

<!-- image -->

Figure 172 create\_trunk Command Results

<!-- image -->

## Creating Route Segments on the Same Track in One Direction

To create route trunks in one direction on the same track, use the create\_trunk\_shared\_track command as follows:

```
icc2_shell> create_trunk_shared_track -nets {sfr_small_bundle} -layer m3 \ -track_coord 175 -width {0.4 0.6}
```

The command creates a route segment for each net specified by the -nets option. In this example, the -track\_coord option specifies the x- or y-coordinate that determines the starting point of the route and is snapped to the closest track. The -width option specifies the list of track widths to put the routes on.

<!-- image -->

<!-- image -->

Figure 173 Creating Route Segments on the Same Track in One Direction

<!-- image -->

Specify the following options to the create\_trunk\_shared\_track command control how the routes are created.

- Specify the layer to use to connect the pins to the routes with the -layer option. The command creates routes in the preferred direction for the specified layer and skips connections in the nonpreferred direction.
- Specify the routing direction for the layer with the -direction horizontal | vertical option. By default, the command creates routes in the preferred direction.
- Create the routes on specific tracks within the bounding box for the net by using the -track\_numbers , -track\_coords , and -track\_ref\_bbox options.
- Place routes on the next available, unobstructed track by using the -avoid\_obstructions option. By default, the command issues a warning message and skips the net if an obstruction is found.
- Disable checks for shorts and obstructions and preview the route with the -do\_not\_check\_shorts option.
- Avoid snapping routes to tracks by using the -do\_not\_snap\_to\_track option.
- Allow routes to be created outside the boundary specified by the -track\_ref\_bbox option or the bounding box defined by the pin connections for the specified nets by using the -track\_freedom option.

Use this option with the -avoid\_obstructions option.

- Shorten the route segment from the starting pin with the -start\_pullback option, or shorten the route segment at the ending pin with the -stop\_pullback option. Specify a negative value for the distance to extend the route segment rather than shorten it.

<!-- image -->

The -start\_pullback and -stop\_pullback options apply to shielding as well as to signals. Use the -shield\_pullback option to specify additional pullback for shielding only.

- Add a gap between trunks on a track by using the -gap option.
- Specify a bounding box in which to create the route segments with the -net\_bbox\_override option. The actual bounding box for the specified nets is ignored and the command does not try to connect the pins.
- Include or exclude cells to calculate the net bounding box by using the -of\_cells option or -exclude\_cells option. Use these options in multi-fanout scenarios to avoid unnecessary branches.
- Create a routing blockage instead of routing shapes by using the -create\_obstruction option.
- Avoid searching for obstructions in library cells by using the -skip\_lib\_cells option. Use this option with the -avoid\_obstructions option.
- Specify the hierarchy depth to search for obstructions by using the -depth option. By default, all levels of hierarchy are searched.

Use this option with the -avoid\_obstructions option.

To create route trunks in one direction on the same track in the GUI,

1. Choose Task &gt; Trunk Routing .
2. In the Trunk Routing panel, click Setup .
3. In the Trunk Routing Setup window, click on the create\_trunk\_shared\_track link.
4. Specify the nets or bundles for which to create route trunks.
5. Specify the layer on which to create route trunks.
6. (Optional) Specify the information for the rest of the fields as necessary.
7. Click OK .

Figure 174 create\_trunk\_shared\_track Command - GUI

<!-- image -->

<!-- image -->

Figure 175 create\_trunk\_shared\_track Command Results

<!-- image -->

## Creating Routes From Pins to Existing Route Segments

To create routes between pins and existing route segments, use the create\_trunk\_pin\_to\_trunk command as follows:

```
icc2_shell> create_bundle b1 [get_nets {net1 net2 net3 net4}] icc2_shell> create_trunk_pin_to_trunk -nets b1
```

The command creates a route segment between an existing route trunk and the closest pin associated with the nets in the route trunk as shown in the following figure. In this example, the route is created on the same layer as the pin.

Figure 176 Connect Pins to Existing Routes

<!-- image -->

Specify the following options to the create\_trunk\_pin\_to\_trunk command to control how the routes are created.

- Specify the layer to use to connect the pins to the routes with the -layer option. The command creates routes in the preferred direction for the specified layer and skips connections in the nonpreferred direction.
- Create route segments in a specific direction with the -direction horizontal | vertical option. Connections in the other direction are skipped.
- Avoid snapping routes to tracks by using the -do\_not\_snap\_to\_track option.
- Place routes on the next available, unobstructed track by using the -avoid\_obstructions option. By default, the command issues a warning message and skips the net if an obstruction is found.

<!-- image -->

<!-- image -->

- Disable checks for shorts and obstructions and preview the route with the -do\_not\_check\_shorts option.
- Avoid snapping routes to tracks by using the -do\_not\_snap\_to\_track option.
- Reduce the number of route shapes created from the trunk by specifying the -cluster\_proximity option. Use this option to specify the range in microns within which to group individual pin-to-trunk shapes to a single shape. The command creates the route segment from the trunk, but might not complete the connection to the pin.

The following figure shows the layout result after specifying three different values for the cluster proximity.

Figure 177 Cluster Proximity

<!-- image -->

<!-- image -->

To complete the missing connections, run the create\_trunk\_pin\_to\_trunk command again and specify the layer for the orthogonal direction. The following example first creates the vertical routes, then calls the create\_trunk\_pin\_to\_trunk command again to complete the connection to the pins.

```
icc2_shell> create_trunk_pin_to_trunk -nets $nets -layer METAL2 \ -cluster_proximity 40 icc2_shell> create_trunk_pin_to_trunk -nets $nets -layer METAL3
```

To create routes between pins and existing route segments in the GUI,

1. Choose Task &gt; Trunk Routing .
2. In the Trunk Routing panel, click Setup .
3. In the Trunk Routing Setup window, click on the create\_trunk\_pin\_to\_trunk link.
4. Specify the nets for which to create route trunks.
5. (Optional) Specify the information for the rest of the fields as necessary.
6. Click OK .

Figure 178 create\_trunk\_pin\_to\_trunk Command - GUI

<!-- image -->

Figure 179 create\_trunk\_pin\_to\_trunk Command Results

<!-- image -->

## Creating Routes From Pin to Pin

To create route segments between pins, use the create\_trunk\_pin\_to\_pin command as follows:

```
icc2_shell> create_bundle b1 [get_nets {net1 net2 net3 net4}] icc2_shell> create_trunk_pin_to_pin -nets b1 \ -extensions {0.67 1.0 0.33} -layer_legs {M4 M3 M4}
```

<!-- image -->

This command produces the following layout result:

Figure 180 Route Trunk Pin to Pin

<!-- image -->

In this example, the -extensions option specifies the relative length of the route segments, starting at the driving pins and ending at the load pins. To reverse the direction of a route segment, specify a negative extension value. To route from the destination pins, see the description of the -start\_from option in the following list. The corresponding layers for the segments are specified with the -layer\_legs option.

Specify the following options to the create\_trunk\_pin\_to\_pin command to control how the routes are created.

- Specify the specific track widths to use for a given layer with the -layer\_legs option. For example, the following command places routes on layers M2 and M3 only on tracks with a width of 0.4 or 0.8. To use any available track width, replace {0.4 0.8} with the all argument. By default, the command places routes only on tracks with the default width.
- Specify the length of each segment with the -extensions option. The option takes a list of extensions, each element in the list specifies the length of one segment in the route. Extensions can be specified as a fraction of the net bounding box, a percentage of the net bounding box, a distance in microns, or as user-defined units.
- Specify the layer to use for each segment with the -layer\_legs option together with a list of layers. Each layer corresponds to the segment specified by the -extensions option.

```
icc2_shell> create_trunk_pin_to_pin -nets $nets \ -layer_legs {{METAL2 {0.4 0.8}} {METAL3 {0.4 0.8}}} \ -extensions {1 1}
```

<!-- image -->

<!-- image -->

-start\_from   high\_y

<!-- image -->

- Specify a bounding box in which to create the route segments with the -net\_bbox\_override option. The actual bounding box for the specified nets is ignored and the command does not try to connect the pins.
- Specify the relative location of the pins which to begin the route with the -start\_from option.

In the following example, the first command begins the routes from the source pins at the bottom of the figure and produces the layout result shown on the left; the second command begins the routes from the destination pins at the top of the figure and produces the layout result shown on the right.

```
icc2_shell> create_trunk_pin_to_pin -nets b4 \ -extensions {0.25 1.0 0.75} -layer_legs {M4 M3 M4} icc2_shell> create_trunk_pin_to_pin -nets b4 \ -extensions {0.25 1.0 0.75} -layer_legs {M4 M3 M4} \ -start_from high_y
```

Figure 181 Start From Location

(default)

<!-- image -->

- Avoid snapping routes to tracks by using the -do\_not\_snap\_to\_track option.
- Disable checks for shorts and obstructions and preview the route with the -do\_not\_check\_shorts option.

<!-- image -->

- Shorten the route segment from the starting pin with the -start\_pullback option, or shorten the route segment at the ending pin with the -stop\_pullback option. Specify a negative value for the distance to extend the route segment rather than shorten it.

The -start\_pullback and -stop\_pullback options apply to shielding as well as to signals. Use the -shield\_pullback option to specify additional pullback for shielding only.

To create route segments between pins in the GUI,

1. Choose Task &gt; Trunk Routing .
2. In the Trunk Routing panel, click Setup .
3. In the Trunk Routing Setup window, click on the create\_trunk\_pin\_to\_pin link.
4. Specify the nets or bundles for which to create route trunks.
5. Specify the layer on which to create route trunks.
6. Specify the relative length of the route in the extensions text box.
7. (Optional) Specify the information for the rest of the fields as necessary.
8. Click OK .

<!-- image -->

Figure 182 create\_trunk\_pin\_to\_pin Command - GUI

<!-- image -->

Figure 183 create\_trunk\_pin\_to\_pin Command Results

<!-- image -->

## Creating Routes From Topology Edges

To create routes from topology edges, use the create\_trunk\_topology command as follows:

```
icc2_shell> set shape_layers {{m2 50% 0} {m3 100% 0} {m4 50% 0}} icc2_shell> create_topology_plan -name TP1 -objects \ [get_bundles  sfr_bot_bundle] icc2_shell> create_topology_node -plan TP1 -name N1 -constraint_type bbox \ -objects [get_ports sfr_data_out* ] icc2_shell> create_topology_node -plan TP1 -name N2 \ -constraint_type bbox -objects [get_pins cpu/interrupt/sfr_data_out* ] icc2_shell> create_topology_edge -name E12 -plan TP1 \ -nodes {TP1/N1 TP1/N2} -shape_layers $shape_layers -objects [get_nets sfr_data_out*] icc2_shell> create_trunk_topology -edge TP1/E12
```

The previous set of commands creates the following layout result.

<!-- image -->

Figure 184 Route From Topology Edges

<!-- image -->

In the example, the -edge option specifies the topology edge name for which to create routes.

Specify the following options to the create\_trunk\_topology command to control how the routes are created.

- Specify the topology plan name or collection for which to create routes by using the -plan option.
- Place routes on the next available, unobstructed track by using the -avoid\_obstructions option. By default, the command issues a warning message and skips the net if an obstruction is found.
- Disable checks for shorts and obstructions and preview the route with the -do\_not\_check\_shorts option.
- Avoid snapping routes to tracks by using the -do\_not\_snap\_to\_track option.
- Avoid adding vias on pins by using the -do\_not\_add\_vias\_on\_pins option.
- Expand the region horizontally or vertically where the routes can be shifted by using the -horizontal\_freedom or -vertical\_freedom options.
- Shorten the route segment from the starting pin with the -start\_pullback option, or shorten the route segment at the ending pin with the -stop\_pullback option. Specify a negative value for the distance to extend the route segment rather than shorten it.

The -start\_pullback and -stop\_pullback options apply to shielding as well as to signals. Use the -shield\_pullback option to specify additional pullback for shielding only.

- Avoid searching for obstructions in library cells by using the -skip\_lib\_cells option. Use this option with the -avoid\_obstructions option.

<!-- image -->

To create route segments from topology edges in the GUI,

1. Choose Task &gt; Trunk Routing .
2. In the Trunk Routing panel, click Setup .
3. In the Trunk Routing Setup window, click on the create\_trunk\_topology link.
4. Specify the topology plan name or edge for which to creates routes.
5. (Optional) Specify the information for the rest of the fields as necessary.
6. Click OK .

<!-- image -->

Figure 185 create\_trunk\_topology Command - GUI

<!-- image -->

<!-- image -->

Figure 186 create\_trunk\_topology Command Results

<!-- image -->

## Routing Area Bounding Box

By default, the create\_trunk and create\_trunk\_pin\_to\_pin commands create routes within a bounding box formed by the source and destination pins as shown in the following figure.

Figure 187 Route Trunk Default Bounding Box

<!-- image -->

To create the route trunks within a specific bounding box, specify the -net\_bbox\_override option with the create\_trunk and create\_trunk\_pin\_to\_pin commands. The following example creates route trunks for the net1 and net2 nets within the box bounded by (100,100) and (200,200).

icc2\_shell&gt; create\_trunk -nets {net1 net2} -layer METAL3 \ -net\_bbox\_override {{100 100} {200 200}}

## Shielding Nets

You can create shielding nets using the -shield\_nets and -shield\_type options with the create\_trunk , create\_trunk\_pin\_to\_trunk , or create\_trunk\_pin\_to\_pin commands. The -shield\_type option supports full, partial, or cap shields on the routes.

The shielding nets are shared among nets. The order and positioning of shielding nets is relative to the x-axis and y-axis. Therefore, the low shielding net always starts at the low x- or y- position, while the high shielding net starts with the high x- or y- position. The tool supports full and half interleaved shielding.

<!-- image -->

<!-- image -->

The -start\_pullback and -stop\_pullback options apply to shielding as well as to signals. Use the -shield\_pullback option to specify additional pullback for shielding only.

Figure 188 shows the default layout result without shield nets and the layout result after running the following command to create shielding nets. The nonshield nets specified by $nets are highlighted for reference.

```
icc2_shell> create_trunk -nets $nets -layer M3 \ -shield_nets VDD -shield_type full
```

Figure 188 Shield Nets

(no  shielding)

<!-- image -->

-shield\_nets VDD   -shield\_type full

<!-- image -->

Figure 189 and Figure 190 show examples of shared nets for full shielding {VCC VSS} with river and cross corners after running the following command to create shielding nets.

```
icc2_shell> create_trunk_pin_to_pin -nets $nets \ -extensions {0.5 1.0 0.5} -layer_legs {M3 M2 M3} \ -shield_type full -shield_nets VCC VSS
```

<!-- image -->

Figure 189 Full Interleaved Shielding With River Corners - VCC in Green and VSS in Blue

<!-- image -->

Figure 190 Full Interleaved Shielding With Cross Corners - VCC in Green and VSS in Blue

<!-- image -->

<!-- image -->

Figure 191 and Figure 192 show examples of shared nets for half shielding {VCC VSS} with river and cross corners after running the following command to create shielding nets.

```
icc2_shell> create_trunk_pin_to_pin -nets $nets \ -extensions {0.5 1.0 0.5} -layer_legs {M3 M2 M3} \ -shield_type half -shield_nets VCC VSS
```

Figure 191 Half Interleaved Shielding With River Corners - VCC in Green and VSS in Blue

<!-- image -->

<!-- image -->

Figure 192 Half Interleaved Shielding With Cross Corners - VCC in Green and VSS in Blue

<!-- image -->

For the create\_trunk\_pin\_to\_pin command to use the existing PG mesh for shielding, ensure that the PG mesh wire width matches the width of the underlying track - see Figure 193.

Figure 193 Full Shielding {VSS} Shared With Ground Mesh

<!-- image -->

## Adding Buffers on Routes

The Add Buffer on Route tool enables you to add buffers along the route of the specified nets.

To start the Add Buffer on Route tool, click on the Command search button and type add\_buffer\_on\_route in the search box.

In the following figure, 1 is the command search icon, 2 is the text field to type the command, 3 displays the command that match the search text.

<!-- image -->

The Add Buffer on Route dialog box opens up. It is divided into following sections:

- Top region
- Basic tab
- Advanced tab

In the dialog box, fields shown in red or preceded by an asterisk are required.

Any required information that you have not provided is indicated toward the bottom of this dialog box.

<!-- image -->

<!-- image -->

<!-- image -->

| Fields    |                                | Description                                                                                                                                                                                                                             |
|-----------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nets      |                                | Specify the nets to be buffered.                                                                                                                                                                                                        |
| Mode      | Location                       | Specify the center point coordinates for the locations of the buffer or inverter pair cells.                                                                                                                                            |
|           | Specified buffers              | Specify the center point coordinates for the locations of the buffer or inverter pair cells, as well as their names and library cells.                                                                                                  |
|           | Specified bus buffers          | Specify the center point coordinates for the locations of bus buffer or inverter pair cells, as well as their names and library cells, using the format {bus_buffer_pattern1 lib_cell1 x1 y1 bus_buffer_pattern2 lib_cell2 x2 y2 ...} . |
|           | Repeater distance              | Specify the distance in user units between each buffer to be inserted along the route.                                                                                                                                                  |
|           | Repeater distance length ratio | Specify the distance between each buffer that is inserted along the route as a ratio of the total route length.                                                                                                                         |
|           | Point                          | Specify the point coordinates on the layout view.                                                                                                                                                                                       |
|           | Layer                          | Choose a layer from the drop-down list.                                                                                                                                                                                                 |
|           | Detect layer                   | Specify that the tool detects the layer of location coordinates automatically.                                                                                                                                                          |
|           | Name                           | Specify the name of the buffer that is added.                                                                                                                                                                                           |
|           | Lib Cell                       | Specify the library cell object to use as a repeater.                                                                                                                                                                                   |
|           | Distance                       | Specify the repeater distance, which is the distance between each buffer.                                                                                                                                                               |
|           | Scale                          | Scale the distance between buffers by the scaling factor specified for the layer.                                                                                                                                                       |
|           | Ratio                          | Ratio of the distance between each buffer to the total route length.                                                                                                                                                                    |
| Basic tab | Scaled by width                | Scale the distance between buffers by the ratio of the default width for the layer and the actual route width.                                                                                                                          |
|           | Only global routed nets Enable | buffer insertion on global routed nets.                                                                                                                                                                                                 |

Table 15 Add Buffer on Route Dialog Box Options

<!-- image -->

Table 15 Add Buffer on Route Dialog Box Options (Continued)

| Fields       |                                                          | Description                                                                                                                                                            |
|--------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              | Punch port                                               | Enable buffer insertion on a route segment, even when the topology is different than the netlist connection in the logical hierarchy.                                  |
|              | Respect voltage area                                     | Insert buffers within the hierarchy of the voltage area such that the buffer is physically inside hierarchy in the layout.                                             |
|              | Reference Cells > Voltage Area, Lib Cell                 | Specify library cell objects to be used in the specified voltage areas.                                                                                                |
|              | Respect gas station                                      | Add buffers only within gas stations (whose is_primary attribute is false ) for the specified supply net and along the routes.                                         |
|              | Physical feedthrough                                     | Specify the voltage areas in which buffers can be added, even if they are physical-only feedthroughs.                                                                  |
|              | Select MV buffers > Voltage Area, Single Rail, Dual Rail | Specify single-rail and dual-rail library cell objects to be used in the specified voltage areas.                                                                      |
|              | Prefix > Bus cell                                        | Specify the prefix to be used for new buffers that are added by the -user_specified_bus_buffers option.                                                                |
|              | Prefix > Cell                                            | Specify the prefix to be used for new buffers that are inserted in the netlist. By default, the command uses "eco_cell" as the prefix.                                 |
|              | Prefix > Net                                             | Specify the prefix to be used for new nets that are created when buffers are inserted in the netlist. By default, the command uses "eco_net" as the prefix.            |
| Advanced tab | Snap to sites                                            | Snap the newly added buffers to the nearest sites.                                                                                                                     |
|              | On top hierarchy                                         | Add buffers to the net at the highest level of hierarchy. By default, the buffers are added in the lowest common ancestor hierarchy of the pins driven by the buffers. |
|              | Verbose                                                  | Show verbose messages.                                                                                                                                                 |
|              | Respect blockages                                        | Specify that no buffer should be added within a placement blockage, soft macro, or hard macro.                                                                         |
|              | Spare cell aware                                         | Enable the spare-cell-aware feature in                                                                                                                                 |

freeze-silicon mode.

<!-- image -->

Table 15 Add Buffer on Route Dialog Box Options (Continued)

| Fields   | Description                         |                                                                                                                                                                                                                                                        |
|----------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          | Insertion over cell > Allowed       | Specify the soft macro or hard macro instances in which the repeaters can be added. Use this option with the 'Respect blockages' option.                                                                                                               |
|          | Insertion over cell > Not allowed   | Specify the soft macro or hard macro instances in which the repeaters are not allowed.                                                                                                                                                                 |
|          | Max distance > Location to route    | Specify the maximum horizontal or vertical distance in user units between the specified location and route. Use this option with the 'Respect gas station' option. When respect gas station is enabled, the buffers must be added inside gas stations. |
|          | Max distance > Incomplete route     | Define the maximum search distance for incomplete routes.                                                                                                                                                                                              |
|          | Max distance > Route to gas station | Specify the distance between the gas station in which the buffer is added to the route. If this option is not specified, gas stations must be on the route.                                                                                            |
|          | Max distance > Spare cell           | Specify the maximum distance between newly added buffers and spare cells in freeze-silicon mode.                                                                                                                                                       |
|          | First distance - Length             | Specify the distance in user units between the driver pin and the first buffer introduced along the route. Use this option with the 'Repeater distance' or 'Repeater distance length ratio' option.                                                    |
|          | First distance - Ratio              | Specify the distance between the driver pin and the first buffer introduced along the route as a ratio of the total route length. Use this option with the 'Repeater distance length ratio' option.                                                    |

Table 16 Gas Station Examples

When respect gas station is enabled, the buffers must be added inside gas stations.

<!-- image -->

Max distance &gt; Route to gas station allows upsizing the gas stations, so that even the gas stations are not on route, you still can add buffers.

Table 16 Gas Station Examples (Continued)

<!-- image -->

## Example Flow:

1. Select net p0.
2. Add user specified buffers.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

The following figure shows the result.

<!-- image -->

<!-- image -->

## Estimating Point-to-Point Resistance

To calculate the resistance between two points (pins or ports) in the current design, use the estimate\_resistance command.

In the command, you can specify a starting point and an endpoint in various ways:

- By using the -net option - This option works only for a net with only two pins or ports, where each pin or port has a single terminal.
- By using the -pins option - This option works for a net with more than two pins or ports. Ensure that you specify the exact pins and ports in the command so that it can measure the resistance between the specified points.
- By using the -shapes option - This option works for measuring the resistance for arbitrary segments that are set in a complex structure. For example, the connection of a PG pin with a mesh. However, ensure that you avoid passing the whole mesh as a set of shapes for performance reasons.

When you use the -shapes option, specify the starting point, its layer, the ending point, and its layer.

Use the -quiet and -verbose options to either suppress the messages or print them in detail on the console, respectively.

The following command estimates resistance between the VDD pins on the specified cells:

```
icc2_shell> estimate_resistance -pins "INV_279/VDD U27/VDD"
```

<!-- image -->

## 15

## Creating Anchors

Anchors help you to anchor one design object to another. When you anchor an object, that object is the dependent object and the object that the dependent object is anchored to is the anchor object. When you move an anchor object, any dependent object anchored to it also moves with the anchor object. When you move a dependent object, it snaps back to its anchored location.

To create an anchor, in the IC Compiler II GUI, choose Create &gt; Anchor . The anchor creation tool displays. The following image shows the anchor creation tool:

<!-- image -->

The anchor creation tool provides the following options:

- Anchor type - To specify how the object is anchored. You can choose to anchor in X or Y co-ordinates or both X and Y coordinates.
- Dependent - To specify the dependent object
- Anchor - To specify the anchor object
- Position Reference - To specify the position reference for dependent and anchor objects
- Offset - To specify X and Y offset values from the dependent object to the anchor object. Default is {0,0}

You can also create anchors down the hierarchy. To create an anchor in hierarchy, go to the Layout settings panel and enable deep selection and increase the view level. After setting these requirements, you can pick dependent and anchor objects within the hierarchy.

<!-- image -->

## Note:

Dependent object hierarchy level must be equal to or less than the anchor object hierarchy level.

The following table shows the conventions of interactive editing in the CreateAnchor tool.

| Event                 | Action                                                                      |
|-----------------------|-----------------------------------------------------------------------------|
| Click or Drag         | Set corner of rectangle or creates Anchor                                   |
| Double-click or Enter | Create Anchor at current location                                           |
| Middle-Click          | Activate stroke menu                                                        |
| Right-click           | Display context menu                                                        |
| F1                    | Cycle forward through overlapping objects                                   |
| Shift + F1            | Cycle backward through overlapping objects                                  |
| Escape                | Cancel pending changes if any changes are pending; otherwise, exit the tool |

Table 17 Interactions

<!-- image -->

## 16

## Creating Cell

You can create cells (prototype blocks or complete dies) from the IC Compiler II GUI. Using the GUI, you can also create hierarchical blocks without using the edit-in-place feature.

To create a cell, in the IC Compiler II GUI, choose Create &gt; Cell . Alternatively, use the create cell mouse tool. The Create cell tool appears.

The following image shows the Create cell tool.

<!-- image -->

## Creating a Hierarchical Block

To create a hierarchical instance or block:

1. Enable deep selection and increase the Level in the Layout settings panel.
2. Choose Create &gt; Cell . The Create Cell tool appears.
3. Click New Block Cell icon to create a new block or select Add Block Cell icon to create an instance of an existing block.
4. Specify the library in the Library field.

<!-- image -->

5. Specify the Reference Block and Cell instance names.
6. Specify the design type in the Design type field. For example, die, diode, module and so on.
7. Specify the Z offset. You can also set it to Auto .
8. Draw a rectangle to create a new block. If you want to create an instance of an existing cell, drag the shape onto the required location.

<!-- image -->

## 17

## Creating Persistent Annotations

To create persistent annotations (shapes, text, and symbols) that are saved in the database, use the create\_annotation\_shape , create\_annotation\_text , and create\_annotation\_symbol commands. Alternatively, use the Create Annotation tool ( Create &gt; Annotation ) to create them.

When you select the Attach check box in the Create Annotation tool, the objects under the mouse pointer are preselected. When you click over such an object, the annotation is attached or anchored to that object. When you move the object, the annotation follows it.

<!-- image -->

## Creating Annotation Shapes

Use the create\_annotation\_shape command to create annotation shapes of types circle, line, rectangle, and polygon with optional text labels. For more information about this command, see the man page.

Alternatively, use the Create Annotation tool to create an annotation shape. You can specify the type (circle, rectangle, and others), style (fill pattern, line width, color, and others), label, the orientation of the label (R0, MY, and others), and others by using this tool.

<!-- image -->

The following examples create different types of annotation shapes by using the create\_annotation\_shape command.

<!-- image -->

- Add a green rectangle annotation.

icc2\_shell&gt; create\_annotation\_shape -type rect -color green \ -annotation\_points {{200 200} {777 777}}

<!-- image -->

- Add a red line annotation of width 2

```
icc2_shell> create_annotation_shape -type line \ -color red -line_width 2 \ -annotation_points {{123 456} {789 12} {200 200}}
```

<!-- image -->

<!-- image -->

- Add a polygon.

icc2\_shell&gt; create\_annotation\_shape -type polygon \ -annotation\_points {{800 700} {850 700} {900 650} \ {900 600} {800 600}} -color orange

<!-- image -->

- Add a circle with center in the middle of cell 'I\_CLOCK\_GEN/I\_PLL\_PC' and radius 50.

<!-- image -->

<!-- image -->

<!-- image -->

## Creating Annotation Symbols

Use the create\_annotation\_symbol command to create annotation symbols of types cross, diamond, square, triangle, custom symbols, and symbols that are zoom-dependent ( fit\_symbol ). For a custom symbol, you must specify the input file in SVG format by using the -file option. For more information about this command, see the man page.

Alternatively, use the Create Annotation tool to create an annotation symbol. You can specify the type (symbol), its type, size, style (fill pattern, line width, color, and others), orientation of the symbol, and others by using this tool.

The fit\_symbol type of annotation is built out of predefined shapes (such as, cross, diamond, square, triangle, or custom). It renders bigger, when you zoom in and smaller, when you zoom out. In contrast, the symbol and text annotations are zoomindependent, and their sizes are defined by the symbol size in pixels and the font size in points, correspondingly. Use the fit\_symbol annotations for symbols that need to be comparative in size with the annotated physical design objects.

<!-- image -->

The following examples create different types of annotation symbols by using the create\_annotation\_symbol command.

- Add a red diamond annotation with cross-pattern fill.

icc2\_shell&gt; create\_annotation\_symbol -type diamond \ -origin {430.490 629.800} -name annoDiamond \ -size 15 -color red -fill CrossPattern \ -pen\_style SolidLine -pen\_width 2

<!-- image -->

- Add a green square annotation with solid-pattern fill.

icc2\_shell&gt; create\_annotation\_symbol -type square \ -origin {534.440 629.800} -name annoSquare \ -size 15 -color green -fill SolidPattern \ -pen\_style DotLine -pen\_width 1

<!-- image -->

<!-- image -->

- Add a blue triangle with its center in the middle of the I\_CLOCK\_GEN/I\_PLL\_PC cell with a pattern fill.
- Add a fit\_symbol type of annotation, which is zoom-dependent

```
icc2_shell> create_annotation_symbol -type triangle \ -origin [list [get_cells I_CLOCK_GEN/I_PLL_PCI]] \ -name annoTriangle -size 75 -color blue -fill Dense7Pattern \ -pen_style SolidLine -pen_width 1
```

<!-- image -->

<!-- image -->

<!-- image -->

The mandatory options that you should use with the -fit\_symbol option are: -origin , -width , and -height .

```
icc2_shell> create_annotation_symbol -type triangle \ -origin {430.490 629.800} -fit_symbol -width 200 -height 200
```

- Add an annotation symbol from an SVG file by using the -file and -type options.

```
icc2_shell> create_annotation_symbol -type custom \ -origin {534.440 629.800} -name annoCustom \ -file star.svg
```

<!-- image -->

To add a custom symbol (for example, buffer, inverter, OR gate, or a star) from the examples directory:

1. (Optional) Use the gui.annotation\_symbol\_dir application option to define the location of the annotation symbol files. By default, it points to the examples directory. If needed, change this option to reference any specific directory that contains your SVG files.
2. Choose Create &gt; Annotation .
3. From the Symbol drop-down list, choose custom .
4. From the User symbol drop-down list, choose a symbol.

```
icc2_shell> set_app_options -name gui.annotation_symbol_dir \ -value $synopsys_root/auxx/gui/nwtn/svg_examples
```

For a symbol added from an SVG file,

- The path data for the symbol is taken from the SVG file. The following attributes in the SVG file are recognized by the tool:
- M = moveto
- L = lineto
- Q = quadratic Bézier curve
- A = elliptical arc
- Z = closepath
- To set the color, fill pattern, and so on for a symbol, use the options in the create\_annotation\_symbol command.

## Creating Annotation Text

Use the create\_annotation\_text command to create annotation text.

Alternatively, use the Create Annotation tool to create an annotation text. You can specify the type (text), style (fill pattern, line width, color, and others), label, the orientation of the label (R0, MY, and others), and others by using this tool. The Text field supports multi-line text.

<!-- image -->

The following examples create different annotation text by using the create\_annotation\_text command.

- Add a text annotation that is oriented horizontally.

```
icc2_shell> create_annotation_text -text Text1 \ -origin {969.370 1204.625} -name annoText1 \ -font_size 12 -color red -horizontal_alignment center \ -vertical_alignment middle
```

<!-- image -->

<!-- image -->

- Add a text annotation that is oriented vertically.

```
icc2_shell> create_annotation_text -text Text2 \ -origin {969.370 1204.625} -name annoText2 \ -font_size 12 -color green -horizontal_alignment center \ -vertical_alignment middle -orientation vertical
```

<!-- image -->

<!-- image -->

- Add multiple lines of annotation text.

icc2\_shell&gt; create\_annotation\_text -text "Text3\nText4" \ -origin {1000.370 1204.625} -name annoText3 \ -font\_size 14 -color red

<!-- image -->

<!-- image -->

- Add annotation text that is offset from the center of an anchor object.

Select an object in the GUI and use the following commands:

```
icc2_shell> set object [get_selection]
```

```
icc2_shell> create_annotation_text -text "Text5" \ -origin [list $object bbox_center 25% 25%] -color yellow
```

<!-- image -->

## Editing Persistent Annotations

You can move, rotate, copy, and stretch the persistent annotations that you have added to your design.

| Operation          | Circle   | Line   | Polygon   | Rectangle   | Symbol fit_symbol   | Text                |
|--------------------|----------|--------|-----------|-------------|---------------------|---------------------|
| Move Edit > Move   | Yes      | Yes    | Yes       | Yes         | Yes                 | Yes                 |
| Rotate Edit > Move | No       | Yes    | Yes       | Yes         | Yes and Orientation | Yes and Orientation |
| Copy Edit > Copy   | Yes      | Yes    | Yes       | Yes         | Yes                 | Yes                 |

Table 18 Operations Allowed for Persistent Annotations

<!-- image -->

Table 18 Operations Allowed for Persistent Annotations (Continued)

| Operation              | Circle   | Line   | Polygon   | Rectangle   | Symbol fit_symbol   | Text   |
|------------------------|----------|--------|-----------|-------------|---------------------|--------|
| Stretch Edit > Stretch | Yes      | Yes    | Yes       | Yes         | Yes                 | No     |

You can adjust the font size, apply color, and perform other operations by selecting the annotation and editing its properties from the Properties Editor panel.

## Example of Resizing Symbols

From the tool, you can stretch or resize ( Edit &gt; Stretch ) some of the symbol annotations, such as a star, circle, or line. For example,

Figure 194 Resizing a Circle - Drag the Hotspots to Resize

<!-- image -->

Figure 195 Resizing a Line - Click and Drag the Line Boundary to Adjust the Width of the Line

<!-- image -->

## Removing Persistent Annotations

To remove a specific annotation shape,

1. Select the annotation shape
2. Click on the Delete tool button

<!-- image -->

```
(or) Use remove_annotation_shapes [get_selection] command. icc2_shell> remove_annotation_shapes [get_selection]
```

<!-- image -->

## 18

## Working With Manufacturing Objects

The IC Compiler II GUI enables you to view, select, and edit the following manufacturing objects that are in your design. These objects are called manufacturing objects because they play a role in the manufacturing of a semiconductor chip.

- Assembly die - the physical die after being cut from a wafer.
- Sealring - the rectangular portion of the wafer, which is larger than the die boundary. It protects the die from mechanical damage.
- Stitching zone (Kerf) - the width of material removed during the cutting of a wafer to form a die.

<!-- image -->

<!-- image -->

See the following topics for more information:

- Selecting a Manufacturing Object
- Querying Manufacturing Objects
- Viewing the Properties of a Manufacturing Object
- Editing a Manufacturing Object

## Selecting a Manufacturing Object

The IC Compiler II tool enables you to select a manufacturing object

- From the Layout view by clicking on the object
- From the context-sensitive menu by choosing the Related Manufacturing Shapes menu
- From the Select by Name toolbar

When you hover over a manufacturing object, the tooltip displays information about that object. For example,

<!-- image -->

In the Layout view, you control the visibility and selection of a manufacturing object by using the View Settings panel.

<!-- image -->

<!-- image -->

## Querying Manufacturing Objects

Use the Query panel to search for a manufacturing object.

## Viewing the Properties of a Manufacturing Object

Use the Properties panel to view the properties of a manufacturing object.

## Editing a Manufacturing Object

You can stretch, add, or cut a manufacturing object from the IC Compiler II GUI. To perform any of these operations,

1. In the Layout view, select the object.
2. Use the editing tools from the Edit menu.

For more information about how to edit objects in the Layout view, see the Editing the Physical Layout topic.

<!-- image -->

<!-- image -->

## 19

## Extending the Graphical User Interface

The IC Compiler II GUI provides an extensive application programming interface (API) to support customization of menus, buttons, and other elements of the GUI. Use the API to create custom buttons, menu items, map modes, and link them to custom or built-in functions in the tool. Customizations can be loaded automatically when the tool starts, or added later by sourcing the commands from a script file.

In addition, the tool supports annotations. Use annotations to draw lines, rectangles, polygons, symbols, and text on the layout view.

The following topics describe different types of GUI customization:

- Creating Menu Items
- Creating Toolbars and Toolbar Items
- Creating Mouse Palette
- Adding Buttons to the Favorites Palette
- Highlighting Objects With Tcl Commands
- Creating Annotations
- Saving Annotations
- Creating New Visual Modes

## Creating Menu Items

The IC Compiler II tool supports menu customization with the gui\_create\_menu and other commands. Use the gui\_create\_menu commands to modify the menu bar and add new commands; use the gui\_set\_hotkey command to define or redefine hotkeys.

<!-- image -->

<!-- image -->

The following independent examples create increasingly complex menu customizations for new menu entries called 'Nudge Left' and 'Nudge Right', which pan the view slightly to the left and right.

- Define two basic menu items.
- Extend the previous customization to create a header for the menu items and insert a separator.

Figure 196 Simple Menu Item

<!-- image -->

Figure 197 Menu With Header and Separator

<!-- image -->

<!-- image -->

- Extend the previous customization to place the new menu items one position to the left of the Help menu and define a custom icon for each menu item.
- Extend the previous customization to redefine a hotkey definition with the gui\_set\_hotkey command after defining the menu items with the gui\_create\_menu command. The hotkey definition appears in the menu.

Figure 198 Menu With Specific Placement

<!-- image -->

Figure 199 Menu With Hotkey Definitions

<!-- image -->

-menu "MyMenu-&gt;Nudge Right"

```
gui_set_hotkey -replace -hot_key Ctrl+Left \ -menu "MyMenu->Nudge Left"
```

If the hotkey is not previously assigned, you can assign it with the -hot\_key option to the gui\_create\_menu command. This example uses gui\_set\_hotkey -replace to overwrite an existing hotkey setting.

## Creating Toolbars and Toolbar Items

Use the gui\_create\_toolbar and gui\_create\_toolbar\_item commands to create new toolbars and add menu items to the toolbars. The following example creates a toolbar at the top and inserts toolbar items for the 'Nudge Left' and 'Nudge Right' menu items defined in the previous section.

```
gui_create_toolbar -name "MyTopToolbar" \ -title "My Top Toolbar" -dock_side Top gui_create_toolbar_item -toolbar MyTopToolbar \ -menu "MyMenu->Nudge Left" gui_create_toolbar_item -toolbar MyTopToolbar \ -menu "MyMenu->Nudge Right"
```

To view the toolbar, ensure that the new toolbar is selected by right-clicking in the window and enabling the menu selection. Alternatively, choose View &gt; Toolbars &gt; My Top Toolbar from the menu bar.

Figure 200 Toolbar Menu

<!-- image -->

You can dock a toolbar at the top, bottom, left, or right of the window. The following figure shows the GUI after creating a new toolbar at each dock location and adding toolbar items for the 'Nudge Left' and 'Nudge Right' menu items.

<!-- image -->

Figure 201 Toolbar Dock Locations for gui\_create\_toolbar

<!-- image -->

You can create a window toolbar to any view and populate it with custom controls.

To create a window toolbar, you must define a new window toolbar type by using the gui\_create\_window\_toolbar\_type Tcl command. Using this command you can populate the toolbar with the supplied Tcl procedures in the associated view. You can show or hide the window toolbar by using the gui\_show\_window\_toolbar or gui\_hide\_window\_toolbar commands or GUI control on the view title bar. You can set the toolbar side and switch between separate view toolbar types using the menu on the left side of the toolbar as shown.

<!-- image -->

<!-- image -->

<!-- image -->

The following code creates a new window toolbar to a charts view with many basic controls by using the gui\_create\_window\_toolbar\_type and

```
gui_show_window_toolbar commands: # called when text changed proc textChanged { clct } { echo "textChanged $clct"; echo [get_attribute $clct value] } # called when radio button changed proc radioChanged { clct } { echo "radioChanged $clct"; echo [get_attribute $clct value] } # called when check box changed proc checkChanged { clct } { echo "checkChanged $clct"; echo [get_attribute $clct value] } # initialization proc for toolbar proc add_charts_toolbar { clct } { echo "add_charts_toolbar $clct" # create text line edit set text [gui_create_user_widget_item -type text -name text] set_attribute $text value "Text" set_attribute $text changed_proc textChanged # create action button set window [gui_get_current_window -mru] set window_type [gui_get_window_attribute -window $window -attribute type] set menuRoot [gui_menu_root_from_window_type -window_type $window_type] set hotkeys [gui_create_user_widget_item -name hotkeys \ -type "action:${menuRoot}::Help->Report Hotkey Bindings"] # create radio button group set radio_group [\ gui_create_user_widget_group -type stamp -name radio -label Radio { set radio_one   [gui_create_user_widget_item -type radio -name radio_one] set radio_two   [gui_create_user_widget_item -type radio -name radio_two]
```

<!-- image -->

```
set radio_three [gui_create_user_widget_item -type radio -name radio_three] set_attribute $radio_one label "One" set_attribute $radio_two label "Two" set_attribute $radio_three label "Three" }] # connect to single radio state change on radio parent group set_attribute $radio_group changed_proc radioChanged # create check box set check [gui_create_user_widget_item -type check -name check] set_attribute $check label "Check" set_attribute $check changed_proc checkChanged } #---# create view toolbar type to add toolbar to Charts views gui_create_window_toolbar_type -type charts_toolbar -name "My Toolbar" \ -view_types Charts -command add_charts_toolbar #---# start gui gui_start # create charts view set view [gui_create_window -type Charts] # show toolbar gui_show_window_toolbar -window $view -toolbar charts_toolbar
```

## The resultant window toolbar to a charts view is as shown:

<!-- image -->

The following figure shows the Charts Toolbar Menu. You can select from the different toolbar types (default Charts toolbar and created toolbar type).

<!-- image -->

The following figure shows the Charts Toolbar Menu to set the Toolbar Side. You can place the toolbar on any side (left, right, top, bottom). By default, the tool displays the toolbar on the top.

<!-- image -->

## Creating Mouse Palette

You can create a mouse palette or a mouse toolbar and add custom controls to it.

To create a mouse palette or a mouse toolbar, you can use the gui.mouse\_tool\_config application option. This application option can be set to either toolbar or palette at runtime, and then the GUI updates the mouse tool to display as the toolbar or the palette.

The mouse toolbar is designed to occupy a single line and is positioned as the last toolbar at the top of the current window. The mouse palette is designed with the reorganization of the controls with toolbar at the top, presets at the bottom, and expandable 'more' section. The mouse tool palette supports placement on either the left or right side. By default, it appears on the right.

<!-- image -->

<!-- image -->

For example, the mouse toolbar and palette of the create RDL tool is as shown:

## Figure 202 Create RDL Tool Mouse Toolbar

<!-- image -->

Figure 203 Create RDL Tool Mouse Palette

<!-- image -->

## Adding Buttons to the Favorites Palette

Instead of creating a new toolbar, you can add buttons to the Favorites palette. To add a button item to the Favorites palette,

1. Press F10 to open the Favorites palette.
2. Click a button and drag it onto the Favorites palette.

To find a button item using command search and add it to the Favorites palette,

1. Press F10 to open the Favorites palette.
2. Click the magnifying glass to open command search.
3. Enter the command or task name.
4. Click the item in the result list and drag it onto the Favorites palette.

Figure 204 Dragging a Button to the Favorites Palette

<!-- image -->

## Highlighting Objects With Tcl Commands

Using Tcl commands, you can highlight objects in the GUI to display them in different colors for easy identification. You can also define a collection of objects to color.

- Highlight NAND2*, NAND3*, and NAND4* cells using three different colors.

```
gui_change_highlight -color yellow -collection [get_cells -hier -filter "ref_name=~NAND2*"] gui_change_highlight -color red -collection [get_cells -hier -filter "ref_name=~NAND3*"]
```

<!-- image -->

```
gui_change_highlight -color light_blue -collection [get_cells -hier -filter "ref_name=~NAND4*"]
```

Figure 205 Highlighted Cells

<!-- image -->

- Get a collection of red highlights.
- Remove red highlights. gui\_change\_highlight -color red -remove
- Remove all highlights. gui\_change\_highlight -all\_colors -remove

```
gui_get_highlight -color red
```

## Creating Annotations

To add information to the layout view, use annotations to create lines, rectangles, polygons, and text. Annotations are not saved to the design database and therefore are not persistent. Use the gui\_add\_annotation command to add annotations; use the gui\_remove\_annotations command to remove annotations. However, to create persistent annotations, use the create\_annotation\_shape command. For more information, see the Creating Persistent Annotations topic.

<!-- image -->

<!-- image -->

The following examples create different types of annotations. The final example removes all annotations.

- Add a line annotation

```
gui_add_annotation -window Layout.1 -type line -color yellow \ -width 4 {{67 2748} {636 2748}}
```

Figure 206 Line Annotation

<!-- image -->

- Add a gray line from the center of cell pad\_iopad\_40 to the center of cell left\_15\_2 and specify the color as hexadecimal value.

```
set cell1 [get_cells pad_iopad_40] set cell2 [get_cells left_15_2] gui_add_annotation -window Layout.1 -width 5 -color #999999 \ -type line [list [list $cell1 center] [list $cell2 center]]
```

Figure 207 Line Annotation Between Cells

<!-- image -->

- Add a rectangle annotation.

```
gui_add_annotation -window Layout.1 -type rect -color red \ -width 4 {{65 2700} {640 2800}}
```

Figure 208 Rectangle Annotation

<!-- image -->

- Add a text annotation. You must make sure that the bounding box is large enough to fit the text.

```
gui_add_annotation -window Layout.1 -type text -color white \ -text "RDL Route" {{65 2715} {640 2815}}
```

Figure 209 Text Annotation

<!-- image -->

- Add multiple annotations and include an infotip for each annotation.

```
set net pad[40] set shapes [get_shapes -q -of_objects $net] foreach_in_collection shape $shapes { set len [get_attribute $shape length] gui_add_annotation -window Layout.1 -type line \ -color yellow -width 4 \ -info_tip "RDL Route $net\nLength = $len" \ [get_attribute $shape points] }
```

Figure 210 Annotations With Infotip

<!-- image -->

<!-- image -->

- Add two circular annotations, each with a radius of 100.

```
gui_add_annotation -type circle -color yellow -width 2 \ -radius 100 {{0 0}} gui_add_annotation -type circle -color red \ -width 2 {{200 0} {300 0}}
```

Figure 211 Circular Annotation

<!-- image -->

- Create two circular rulers centered at (0, 0) and (400, 0) respectively.

```
gui_add_annotation -type circular_ruler \ -color light_green {{0 0} {100 0}} gui_add_annotation -type circular_ruler \ -color light_purple {{400 0} {500 0} {700 0}}
```

You can specify additional points to create additional circular rulers with the same center. The -text , -pattern , -width , and -line\_style options are ignored when creating circular rulers with the gui\_add\_annotation command.

Figure 212 Circular Rulers

<!-- image -->

- Create a circular ruler at a 45-degree angle.

```
gui_add_annotation -type circular_ruler -color light_purple \ {{0 0} {70.171 70.711} {141.421 141.421}}
```

<!-- image -->

Figure 213 Circular 45-Degree Ruler

<!-- image -->

- Remove all annotations from the current window.
- Remove all annotations from all windows.

```
gui_remove_annotations \ -window [gui_get_current_window -view -mru]
```

```
gui_remove_annotations [gui_get_annotations]
```

## Saving Annotations

To write out annotations created by the gui\_add\_annotation command, use the gui\_write\_annotations command. By default, the gui\_write\_annotations command writes out global annotations. To write out all current layout annotations, specify the command with the [gui\_get\_annotations] argument.

Use the following options with the gui\_write\_annotations command to control the output.

- -file file\_name : Specify the output file name.
- -append : Append the output to the specified file. By default, the command issues an error message if you specify an existing file with the -file option.
- -force : Overwrite the specified output file.
- -compress gzip : Compress the output file using gzip.
- annotations : Specify annotations to write to the output file.

The following example creates two annotations: a line annotation from (0, 0) to (200, 200) and a circle annotation at (0, 0). Note that the first annotation uses the -window option to specify the window while the second annotation does not.

<!-- image -->

```
gui_add_annotation -window Layout.1 -type line -color yellow \ -width 4 {{0 0} {200 200}} gui_add_annotation -type circular_ruler \ -color red {{0 0} {100 0}}
```

These commands create the following annotations in the layout:

Figure 214 Line and Circle Annotations

<!-- image -->

The gui\_write\_annotations -file file\_name [gui\_get\_annotations] command writes out all global and window-specific annotations.

```
icc2_shell> gui_write_annotations \ -file all_gui_annotations.tcl [gui_get_annotations] icc2_shell> sh cat all_gui_annotations.tcl ... set Layout_1 Layout.1 gui_add_annotation -window $Layout_1 -group global -type polyline \ -color yellow -pattern NoBrush -line_style SolidLine \ -width 4 {{0.000 0.000} {200.000 200.000}} gui_add_annotation -window global -group global \ -type circular_ruler -color red -pattern NoBrush \ -line_style SolidLine -width 1 {{0.000 0.000} {100.000 0.000}}
```

The gui\_write\_annotations -file file\_name command writes out only the global annotations (specified without the -window option).

```
icc2_shell> gui_write_annotations -file global_gui_annotations.tcl icc2_shell> sh cat global_gui_annotations.tcl ... gui_add_annotation -window global -group global \ -type circular_ruler -color red -pattern NoBrush \ -line_style SolidLine \ -width 1 {{0.000 0.000} {100.000 0.000}}
```

<!-- image -->

## Creating New Visual Modes

Visual modes highlight design information in colored overlays. Use visual modes to highlight different elements of your design and organize the elements into bins. The gui\_create\_vm and gui\_create\_vmbucket commands define new visual modes, create individual bins, and associate a collection with each bin.

The following example creates a new visual mode to color macros in different sections of the design hierarchy. The gui\_create\_vm command creates a new visual mode called Macros. The reload\_macros\_vm procedure is called when you click the Reload button after starting the Macros visual mode. The gui\_create\_vmbucket command assigns individual bins in the visual mode to specific collections. The gui\_show\_map command opens the Visual Mode palette and displays the new Macros visual mode. After the tool displays the Visual Mode palette, click the Reload button to color the macros. For more information about the Visual Mode palette, see Visual Mode Overview.

```
gui_create_vm -name Macros -update_cmd reload_macros_vm proc reload_macros_vm {args} { set vm Macros gui_remove_vmbucket -vmname $vm -all set collection_1 [get_cells -physical_context \ -filter "is_hard_macro && full_name=~I_CLOCK_GEN/*"] set collection_2 [get_cells -physical_context \ -filter "is_hard_macro && full_name=~I_ORCA_TOP/I_PCI_TOP/*"] set collection_3 [get_cells -physical_context \ -filter "is_hard_macro && full_name=~I_ORCA_TOP/I_CONTEXT_MEM/*"] set collection_4 [get_cells -physical_context \ -filter "is_hard_macro && full_name=~I_ORCA_TOP/I_RISC_CORE/*"] gui_create_vmbucket -vmname $vm -name clock_gen \ -title {clock_gen} -color red -collection $collection_1 gui_create_vmbucket -vmname $vm -name pci_top \ -title {pci_top} -color green -collection $collection_2 gui_create_vmbucket -vmname $vm -name context_mem \ -title {context_mem} -color blue -collection $collection_3 gui_create_vmbucket -vmname $vm -name risc_core \ -title {risc_core} -color yellow -collection $collection_4 } gui_show_map -map Macros -show true
```

<!-- image -->

<!-- image -->

Figure 215 Custom Visual Mode

<!-- image -->