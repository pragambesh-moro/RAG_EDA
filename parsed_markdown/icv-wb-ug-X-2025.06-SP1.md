## IC Validator WorkBench   User Guide

Version X-2025.06-SP1, September 2025

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

|    | Related Products and Trademarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                 | . 13   |
|----|-------------------------------------------------------------------------------------------------------------------------------------------|--------|
|    | Conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                 | .13    |
|    | Customer Support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                      | . 14   |
|    | Statement on Inclusivity and Diversity . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | 15     |
| 1. | Getting Started . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                     | .16    |
|    | Opening and Viewing Layouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                               | 17     |
|    | Accessing the Documentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                               | .18    |
|    | Starting the Application From the Command Line . . . . . . . . . . . . . . . . .                                                          | . 18   |
|    | Executing Startup Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                       | . 21   |
|    | Environment Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                         | .22    |
|    | License Checkout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                      | . 23   |
|    | Using the Graphical User Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | .23    |
|    | The Ribbon . . . . . . . . . . . . . . . . . . . . .                                                                                      | . 25   |
|    | . . . . . . . . . . . . . . . . . . . . . . . Collapsing and Expanding the Ribbon . . . . . . . . . . . . . . . . . . .                   | .26    |
|    | Using the Ribbon Search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                       | .26    |
|    | Customizing the Ribbon . . . . . . . . . . . . . . . . . . .                                                                              | .27    |
|    | . . . . . . . . . . . . Customizing the Quick Access Toolbar . . . . .                                                                    | . 32   |
|    | . . . . . . . . . . . . . . Saving the Ribbon and Quick Access Toolbar Settings . .                                                       | .34    |
|    | . . . . . Exporting and Importing the Ribbon and Quick Access Toolbar . . . . . . . . . . . .                                             | . 34   |
|    | Customizations . . . . . . . . . . . . . . . . . . . . . . . . . . Viewing the Contextual Select and Edit Options . . . . . . . . . . . . | 34     |
|    | Changing the GUI Mode Setting in the GUI . . . . . .                                                                                      | . 35   |
|    | . . . . . . . . . Changing the GUI Mode Setting on the Command Line . . . . . .                                                           | . 35   |
|    | Main Window . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                           | 35     |
|    | Grouping Cell Views . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                     | .36    |
|    | Controlling Dockable Views . . . . . . . . . . . . . . . . . . . . . . . . .                                                              | 36     |
|    | . . . . . . Undocking and Moving Views . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | . 36   |
|    | Docking Views . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                               | . 37   |
|    | . . . . . . . Tabbing Dockable Views . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                          | 37     |
|    | General Purpose Dockable Views . . . . . . . . . . . . . . . . . . . . . . . . . .                                                        | . 37   |
|    | Command Help . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                    | .37    |
|    | Command Pane . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                  | . 38   |
|    | Python Pane . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                 | .39    |

<!-- image -->

## Contents

<!-- image -->

|    | Task View . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                | . 39   |
|----|--------------------------------------------------------------------------------------------------|--------|
|    | Tree View and Open Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | .39 .  |
|    | Side Cells . . . . . . . . . . . . . . . . . . . . . . .                                         | 43     |
|    | Layout Layers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | .46    |
|    | Interrupt Capability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . 58   |
|    | Displaying the Status Bar . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | .58    |
|    | Synchronizing Views in Currently Running Sessions . . . . . .                                    | .59    |
|    | Adding a Custom Script to the GUI . . . . . . . . . . . . . . . . . . .                          | . 60   |
|    | Command Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | .60    |
|    | Creating, Managing, and Running Macros . . . . . . . . . . . . . .                               | .61    |
|    | Creating and Editing Macro Files . . . . . . . . . . . . . . . . . .                             | .61    |
|    | Managing and Running Macro Files and Built-in Scripts                                            | .62    |
|    | Socket Communications . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . 65   |
|    | Server Input . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               | . 66   |
|    | Server Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | .66    |
|    | Successful Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | .66    |
|    | Error Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               | 66     |
|    | Exit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . 66   |
|    | Running the Application in No Display Mode . . . . . . . . . . . .                               | .66    |
| 2. | Customizing the Environment . . . . . . . . . . . . . . . . . . . . . . . . .                    | . 68   |
|    | Modifying Default Settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | 68     |
|    | General Default Settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | .69    |
|    | Logging Settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . 70   |
|    | License Default Settings . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | .70    |
|    | Layout Default Settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | .70    |
|    | Annotations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . 72   |
|    | Cache . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . 72   |
|    | Compare . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | . 74   |
|    | Contour . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . 74   |
|    | Display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | .75    |
|    | DP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | . 76   |
|    | Edit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | 76     |
|    | File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | .77    |
|    | OASIS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | .78    |
|    | GDSII . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | 79     |
|    | LEF/DEF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                | .79    |
|    | Flag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | . 79   |
|    | Gauge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . 80   |

## Contents

| . . . . . . . . . . . .                | Highlight . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80   |
|----------------------------------------|------------------------------------------------------------------------------------------------------|
| Graphics . . . . . . . . . . . . .     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81 .             |
| Grid . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81                 |
| Layers . . . . . . . . . . . . . . .   | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82               |
| Markup Names . . . . . . . .           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83               |
| Model Image . . . . . . . . . .        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83               |
| Mouse . . . . . . . . . . . . . . .    | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84               |
| Net Tracing . . . . . . . . . . .      | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84               |
| Overlay . . . . . . . . . . . . . .    | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85               |
| Ruler . . . . . . . . . . . . . . . .  | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86               |
| Select . . . . . . . . . . . . . . .   | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87               |
| SEM Image . . . . . . . . . . .        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87               |
| Shape Info . . . . . . . . . . .       | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .88              |
| Side Cells . . . . . . . . . . . .     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88               |
| Synchronize . . . . . . . . . .        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .89              |
| Text . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89               |
| View . . . . . . . . . . . . . . . .   | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .89              |
| Modifying Layout Options . . .         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90               |
| General Option Settings .              | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91               |
| Edit Option Settings . . . .           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92               |
| Graphics Option Settings .             | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                 |
| Grid Option Settings . . . .           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93               |
| Net Tracing Option Settings            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93                   |
| Text Option Settings . . . .           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94               |
| User Modes . . . . . . . . . . . . .   | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .94              |
| ICVWB . . . . . . . . . . . . . .      | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .95              |
| HERCULES . . . . . . . . . .           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .95              |
| ICV . . . . . . . . . . . . . . . . .  | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95               |
| ICV64 . . . . . . . . . . . . . . .    | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96               |
| ICV_PLM . . . . . . . . . . . .        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .97              |
| SENTAURUS . . . . . . . . .            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97               |
| Opening and Browsing Layouts           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99                       |
| Opening Layouts and Cells .            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .100               |
| Opening GDS Layouts . . Opening        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102                |
| LEF/DEF and Saving                     | LEF Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .102                         |
| Saving LEF Files . . . . . .           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103                |

<!-- image -->

## Contents

| Cache . . . . . . . . . .                                                       | Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104                                         |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Reloading the Layout . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105                                                                       |
| The Layouts View . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106                                                                       |
| Browsing Cell Views . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107                                                                       |
| Browsing the Cell View with the Mouse                                           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .107                                                                              |
| Browsing the Cell View with the Middle Mouse Button                             | . . . . . . . . . . . . . . . . . . 108                                                                                                     |
| Browsing While Using Other Tools-Toggle-to-Browse                               | . . . . . . . . . . . . . . . . . . 108                                                                                                     |
| Zooming to Coordinates in the Cell View                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . .109                                                                                |
| Zoom With the Mouse Wheel in the Cell View                                      | . . . . . . . . . . . . . . . . . . . . . . . . .110                                                                                        |
| Using the Navigation View . . . . . . .                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                                                                       |
| Other Browsing Methods . . . . . . . .                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111                                                                       |
| Changing How Layers Are Displayed . .                                           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .111                                                                        |
| Layer Attributes . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .113                                                                        |
| Saving and Reloading Layer Attributes .                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116                                                                         |
| Marking Layers . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117                                                                       |
| Specify Which Levels of the Hierarchy To View                                   | . . . . . . . . . . . . . . . . . . . . . . . . . . . 118                                                                                   |
| Opening a Child Cell From the Cell View Context Menu .                          | . . . . . . . . . . . . . . . . . . . 121                                                                                                   |
| Transforming Cell Views . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123                                                                       |
| Standard Orientations Table . . . . . .                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .124                                                                        |
| Overlaying Cell Views . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124                                                                       |
| Using Drag to Set Up Overlays . . . . . . . .                                   | . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125                                                                                 |
| Using the Overlay Dialog Box to Set Up, Modify, and Delete Overlays             | . . . . . . 126                                                                                                                             |
| Deleting Overlays From the Layout Layers View . .                               | . . . . . . . . . . . . . . . . . . . . .126                                                                                                |
| Saving Images of your Design . . . . . . .                                      | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126                                                                       |
| Closing Layouts and Cells . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127                                                                       |
| Closing Views . . . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127                                                                       |
| Hiding Cells and Text . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127                                                                       |
| Getting Information About a Layout .                                            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130                                                                       |
| Getting a Report on Your Layout File . .                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .130                                                                        |
| Wizard                                                                          |                                                                                                                                             |
| Finding Objects . . . . . . . . . . . . . . . . . . . Finding Objects Using the | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131                                                                       |
| . Find Cell References . . . . . . . .                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132 |
| Find Shapes and Text . . .                                                      | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134                                                                         |
| . . . . Find Coordinates From a File .                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136                                                                     |

<!-- image -->

## Contents

|    |                                                                                       | Using the Find Field to Set Up a Find . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137                  |
|----|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
|    | Using the Find Information                                                            | View to Review and Navigate Results . . . . . . . . . .138                                                               |
|    | Getting information About Shapes                                                      | and Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140                                                  |
|    | Hierarchy to a Shape Using Expand Layouts .                                           | . . . . . . . . . . . . . . . . . . . . . . . . 140                                                                      |
|    | Information About Cell                                                                | Reference Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . .141                                               |
|    | Using Probe to Get Information About Shapes                                           | 142                                                                                                                      |
|    | Shape Info Tooltip and the                                                            | . . . . . . . . . . . . . . . . . . . . . . . . Information View . . . . . . . . . . . . . . . . . . . . . . . . . . 144 |
|    | Using tclcli to Get Information About Layouts Without Opening Them . . .              | . . . . . . .146                                                                                                         |
|    | Clearing Annotations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . . . . . . . . . . . . . . . . .148                                                                                   |
|    | Net Tracing . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148                                        |
|    | Point-to-Point Tracing . . . . .                                                      | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152                                        |
|    | Adding Connectivity Breakpoints . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . 153                                                                                                      |
| 5. | Working with Markups . . . . . .                                                      | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155                                        |
|    | Overview of Available Markups . . . . .                                               | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .155                                                 |
|    | Drawing Markups . . . . . . . . . . .                                                 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156                                        |
|    | Drawing a Flag . . . . . . . . . . Flag                                               | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157                                        |
|    | Moving a . . . . . . .                                                                | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .158                                       |
|    | Drawing a Gauge . . . . . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . . . . . . . . . . 158                                                                    |
|    | Drawing a Gauge Using Two Points . . . . . .                                          | . . . . . . . . . . . . . . . . . . . . . . . 158                                                                        |
|    | Drawing a Gauge with a Single Point . . .                                             | . . . . . . . . . . . . . . . . . . . . . . . . . 159                                                                    |
|    | Moving a Gauge . . . . . . . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . . . . .161                                                                               |
|    | Additional Options . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162                                                              |
|    | Drawing a Highlight . . . . . .                                                       | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162                                        |
|    | Drawing a Point . . . . . . . . .                                                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163                                        |
|    | Drawing a Ruler . . . . . . . . .                                                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164                                        |
|    | Drawing a Ruler Using Two Points . .                                                  | . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164                                                              |
|    | Drawing a Ruler with a Single Point . . . . . . . .                                   | . . . . . . . . . . . . . . . . . . . . . . . . . . 166 . . . . . . . . . . . . . . .                                    |
|    | Drawing a Circular Ruler . . . . . . .                                                | . . . . . . . . . . . 167                                                                                                |
|    | Moving a Ruler . . . . . . .                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .167                                         |
|    | Converting a Ruler into a Gauge . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . . . . .168                                                                             |
|    | Measuring Angles with the Protractor . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . . . . . 168                                                                                        |
|    | Drawing a Callout . . . . . . . .                                                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168                                        |
|    | Drawing a Stretch Object . .                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169                                        |
|    | Markups View . . . . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170                                                      |
|    | General Markups Behavior . . . . . . . . . . . Markup Names and Hierarchy . . . . .   | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171                                                            |
|    | Saving Markups . . . . . . . . .                                                      | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171                                              |

<!-- image -->

## Contents

6.

<!-- image -->

| Showing and Hiding Markups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | 172   |
|----------------------------------------------------------------------------------------------------------|-------|
| Zoom To . . . . . . . . . . . . . . . . . . . .                                                          | . 172 |
| Deleting Markups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | . 172 |
| Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                   | . 172 |
| Contours . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               | . 173 |
| Contour Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             | . 173 |
| Converting Contours to Polygons . . . . . . . . . . . . . . . . . .                                      | 173   |
| Naming Restrictions . . . . . . . . . . . . . . . . . . . . . . . . . . . .                              | . 174 |
| Saving Contours . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                            | .174  |
| Model Images . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     | . 175 |
| Model Image Properties . . . . . . . . . . . . . . . . . . . . . . . . .                                 | .175  |
| Saving a Model Image . . . . . . . . . . . . . . . . . . . . . . . . . .                                 | .176  |
| SEM Images . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     | . 176 |
| Loading a SEM Image . . . . . . . . . . . . . . . . . . . . . . . . . .                                  | . 177 |
| SEM Image Properties . . . . . . . . . . . . . . . . . . . . . . . . . .                                 | .177  |
| Changing the Placement of SEM Images . . . . . . . . . . . .                                             | . 177 |
| SEM Alignment Dialog Box . . . . . . . . . . . . . . . . . . . . . . .                                   | . 178 |
| SEM Placement using Hotkeys . . . . . . . . . . . . . . . . . . .                                        | . 179 |
| Saving and Loading a SEM Image Placement . . . . . . . . . . . . . . . . . . . . . . .                   | 179   |
| Highlighting SEM Images . . . . . . . . .                                                                | .179  |
| Loading Markups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                | .179  |
| Selecting Markups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                | .180  |
| Editing Markups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | .180  |
| Editing Layouts and Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                      | . 183 |
| Overview of Editing Functions . . . . . . . . . . . . . . . . . . . . . . . . . . .                      | 183   |
| Creating New Layouts and Cells . . . . . . . . . . . . . . . . . . . . . . . . .                         | 184   |
| Changing the Layout DBU and Resolution . . . . . . . . . . . . . . . . .                                 | .184  |
| Making Cells Editable and Read-Only . . . . . . . . . . . . . . . . . . . . .                            | . 186 |
| Showing or Hiding Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . 186 |
| Renaming, Replacing, and Deleting Cells and Their References                                             | .187  |
| Selecting Objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | 188   |
| Object Attributes View . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | .192  |
| Creating Shapes, Text, and References . . . . . . . . . . . . . . . . . . .                              | .193  |
| Creating Circles and Ellipses . . . . . . . . . . . . . . . . . . . . . . . .                            | . 194 |
| Creating Paths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                   | 194   |
| Creating Polygons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                      | .195  |
| Boolean Operations for Creating Shapes . . . . . . . . . . . . . . .                                     | .196  |

## Contents

<!-- image -->

|    | Using Boolean Modes When Drawing Shapes . . . . . . . . . .                                      | . 196   |
|----|--------------------------------------------------------------------------------------------------|---------|
|    | Using Boolean Operations on Existing Shapes . . . . . . . . . .                                  | .200    |
|    | Delete old shapes Option . . . . . . . . . . . . . . . . . . . . . . . . . . .                   | .200    |
|    | Applying Boolean Operations in Different Hierarchies . . . . .                                   | .201    |
|    | Creating References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | .201    |
|    | Creating Text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    | .202    |
|    | Creating Polygon Text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | 202     |
|    | Cut, Copy, and Paste Operations . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . 203   |
|    | Editing Shapes, Text, and References . . . . . . . . . . . . . . . . . . . . . . .               | . 204   |
|    | Editing Paths and Polygons . . . . . . . . . . . . . . . . . . . . . . . . . . . .               | . 205   |
|    | Aligning and Distributing Shapes . . . . . . . . . . . . . . . . . . . . . . . .                 | . 206   |
|    | Moving and Aligning Vertices . . . . . . . . . . . . . . . . . . . . . . . . . . .               | . 208   |
|    | Duplicating and Repeating Objects . . . . . . . . . . . . . . . . . . . . . .                    | 209     |
|    | Using the Snapping Feature . . . . . . . . . . . . . . . . . . . . . . . . . . . .               | .211    |
|    | Editing Text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . 212   |
|    | Converting Text to Polygon . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | 213     |
|    | Rounding Corners of Polygons . . . . . . . . . . . . . . . . . . . . . . . . . .                 | 213     |
|    | Converting an Arrayed Reference to Multiple Single References                                    | 213     |
|    | Creating a Unique Copy of a Referenced Cell Instance . . . . . . .                               | 213     |
|    | Editing Objects in a Cell Hierarchy with Multiple Instances . . . .                              | . 214   |
| 7. | Saving, Exporting, Merging, and Comparing Layouts . . . . . . . . .                              | 215     |
|    | Saving Layouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 215   |
|    | Exporting Layouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . 217   |
|    | Exporting Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | . 217   |
|    | Additional Export Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | .221    |
|    | Merging Layouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . 222   |
|    | Main Modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | 222     |
|    | Using the Main Modes Wizard . . . . . . . . . . . . . . . . . . . . . . .                        | .223    |
|    | Additional Modes (using the layout merge command) . . . . .                                      | 234     |
|    | Using the Additional Modes Merge Wizard . . . . . . . . . . . . .                                | . 236   |
|    | Command Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | . 238   |
|    | Comparing Layouts and Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | .238    |
|    | Comparing Two Layouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | .238    |
|    | Comparing Two Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . 240   |
|    | Viewing the Output Summary . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | .241    |
|    | Generating VUE Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . 242   |

<!-- image -->

|   8. | Using IC Validator with IC Validator WorkBench . . . . . . . . . . . . . .                        | . 246   |
|------|---------------------------------------------------------------------------------------------------|---------|
|      | ICV Live DRC for IC Validator WorkBench . . . . . . . . . . . . . . . . . . . .                   | .247    |
|      | Setting Up ICV Live DRC for IC Validator WorkBench . . . . . . . .                                | .247    |
|      | Configuring ICV Live DRC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . 248   |
|      | Setting up the IC Validator Live DRC Configuration Window                                         | .248    |
|      | Adding a Check Area . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . 249   |
|      | Setting the Capture Mode . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . 250   |
|      | Running ICV Live DRC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | .252    |
|      | Browsing Results and Highlighting Errors . . . . . . . . . . . . . . . . . .                      | . 252   |
|      | Highlighting Errors Using the ICV Live DRC Toolbar . . .                                          | .252    |
|      | . . . Highlighting Errors Using ICV Live DRC Violation Viewer . . .                               | . 253   |
|      | Creating Custom Recipes Using the Recipe Editor . . . . . . . . . . .                             | . 254   |
|      | Loading TechFiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 255   |
|      | Import CC or Laker Tech Files . . . . . . . . . . . . . . . . . . . . . . . . . . .               | .256    |
|      | Import ICC2 Tech Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | .257    |
|      | Import Layer Names From ICV Runset Files . . . . . . . . . . . . . . . .                          | .257    |
|      | Load ICV Layer Map Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . 258   |
|      | Loading and Viewing DRC Errors Using ICV VUE . . . . . . . . . . . . . . .                        | .258    |
|      | Running DRC, LVS, and PERC Using ICV Launch . . . . . . . . . . . . . .                           | . 261   |
|      | Using the ICVWB PYDB Error Data Viewer . . . . . . . . . . . . . . . . . . . .                    | . 263   |
|      | Loading PYDB Error Data in ICVWB . . . . . . . . . . . . . . . . . . . . . .                      | . 263   |
|      | PYDB Viewer Window . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . 264   |
|      | PYDB Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . 267   |
|      | Viewing PYDB Errors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . 269   |
|      | Loading and Viewing StarRC Opens and Shorts . . . . . . . . .                                     | .271    |
|      | Classifying and Commenting PYDB Errors . . . . . . . . . . . . . .                                | . 272   |
|      | Pushing Down Errors to Cells . . . . . . . . . . . . . . . . . . . . . . . . . . .                | . 273   |
|      | Viewing Errors From Root or Ancestor Cells . . . . . . . . . . . . . . . .                        | . 279   |
|      | Exporting the PYDB Error Records . . . . . . . . . . . . . . . . . . . . . . .                    | . 280   |
|      | Checking PYDB Data Correctness . . . . . . . . . . . . . . . . . . . . . . .                      | .287    |
|   9. | Working With ASCII Error Files . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . 289   |
|      | Loading DRC Error Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | .289    |
|      | Classifying and Commenting DRC Errors . . . . . . . . . . . . . . . . . . . . .                   | 290     |

<!-- image -->

|     | Saving DRC Error Records . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                    | . .291   |
|-----|-------------------------------------------------------------------------------------------------------------------------------------|----------|
| 10. | Synopsys Diagnostic Platform . . . . . . . . . . . . . . . . . . . . . . . .                                                        | . 292    |
|     | Collecting Data for Synopsys Diagnostic Platform . . . . . . . . . .                                                                | . 292    |
| A.  | Default Hotkeys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                             | . 293    |
|     | Hotkeys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                     | . 293    |
|     | Setting Hotkeys in the Ribbon Mode . . . . . . . . . . . . . . . . . .                                                              | . 293    |
|     | Setting Hotkeys in the Menu Mode . . . . . . . . . . . . . . . . . . .                                                              | . 295    |
|     | Adding a Hotkeys Configuration File . . . . . . . . . . . . . . . . . .                                                             | . 297    |
|     | List of Default Hotkeys . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                     | . 297    |
| B.  | Limitations of Layout Files . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                   | . 305    |
|     | Maximum Limits of GDSII and OASIS Files . . . . . . . . . . . . . . .                                                               | .305     |
| C.  | OASIS Files Compliance Checking . . . . . . . . . . . . . . . . . . . .                                                             | . 307    |
|     | The oasis_info Utility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                            | . .307   |
| D.  | Creating Standalone Cache Files with genCache . . . . . . . . .                                                                     | . 310    |
|     | runProg genCache . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                              | . 310    |
|     | Using the genCache DP Option . . . . . . . . . . . . . . . . . . . . . . . .                                                        | . 312    |
| E.  | Layout Format Conversion . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                      | . .316   |
|     | Converting GDS and OASIS to Optimized OASIS . . . . . . . . . .                                                                     | . 316    |
|     | Converting GDS and OASIS to Optimized OASIS in DP mode                                                                              | . 318    |
|     | Converting OASIS to GDS . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                   | . 319    |
| F.  | Using Python With the Application . . . . . . . . . . . . . . . . . . . .                                                           | . .320   |
|     | Python Scripting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                          | . 320    |
|     | iLayout Python Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                 | . 321    |
|     | API Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | . 321    |
|     | Reference . . .                                                                                                                     | 323      |
|     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . snps.ilayout.Layout class - representation of a layout file | . . .323 |

## Contents

<!-- image -->

| snps.ilayout.Cell class - representation of a cell . . . . . . . . . . . . . . . . . .                         | .324   |
|----------------------------------------------------------------------------------------------------------------|--------|
| snps.ilayout.Property class - representation of an OASIS-style property                                        | 325    |
| snps.ilayout.Poly class - representation of a polygon . . . . . . . . . . . . . .                              | . 325  |
| snps.ilayout.Path class - representation of a path; derived from Poly . .                                      | .326   |
| snps.ilayout.Ref class - representation of a reference . . . . . . . . . . . . . .                             | . 327  |
| snps.ilayout.Text class - representation of a text . . . . . . . . . . . . . . . . . .                         | . 327  |
| snps.ilayout.open (arg0: str, **kwargs) -> snps.ilayout.Layout . . . . . . . .                                 | .328   |
| snps.ilayout.save (arg0: object, arg1: str, **kwargs) . . . . . . . . . . . . . . . .                          | . 329  |
| snps.ilayout.children (cell) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . 329  |
| snps.ilayout.bbox (cell: object, layout: object) ) -> Tuple[int, int, int, int] .                              | .330   |
| Layout Creation Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                | .330   |
| Boolean Operations on snps.ilayout Objects . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . 331  |
| Functional Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | 332    |
| Layer/datatype Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | 332    |
| Flattening Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 333  |
| Creating Python GUI Widgets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | .334   |

## About This Guide

This guide describes the application and provides procedures for accessing the basic functionality through the GUI.

This preface includes the following sections:

- Related Products and Trademarks
- Conventions
- Customer Support

## Related Products and Trademarks

This guide refers to the following products:

Synopsys Hercules™

Synopsys IC Validator

Synopsys S-Litho™

Synopsys SolvNetPlus

OASIS®

## Conventions

The following conventions are used in Synopsys documentation.

| Convention   | Description                                                                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Courier      | Indicates command syntax.                                                                                                                                              |
| Italic       | Indicates a user-defined value, such as object_name .                                                                                                                  |
| Bold         | • Within syntax and examples, indicates user input-text you type verbatim. • Indicates a graphical user interface (GUI) element that has an action associated with it. |
| [ ]          | Denotes optional parameters, such as:                                                                                                                                  |

write\_file [-f filename ]

<!-- image -->

<!-- image -->

| Convention   | Description                                                                                 |
|--------------|---------------------------------------------------------------------------------------------|
| ...          | Indicates that parameters can be repeated as many times as necessary: pin1 pin2 ... pinN    |
| &#124;       | Indicates a choice among alternatives, such as low &#124; medium &#124; high                |
| \            | Indicates a continuation of a command line.                                                 |
| /            | Indicates levels of directory structure.                                                    |
| Edit > Copy  | Indicates a path to a menu command, such as opening the Edit menu and choosing Copy .       |
| Ctrl+C       | Indicates a keyboard combination, such as holding down the Ctrl key and pressing the C key. |

## Customer Support

Customer support is available through SolvNetPlus.

## Accessing SolvNetPlus

The SolvNetPlus site includes a knowledge base of technical articles and answers to frequently asked questions about Synopsys tools. The SolvNetPlus site also gives you access to a wide range of Synopsys online services including software downloads, documentation, and technical support.

To access the SolvNetPlus site, go to the following address:

[https://solvnetplus.synopsys.com](https://solvnetplus.synopsys.com/)

If prompted, enter your user name and password. If you do not have a Synopsys user name and password, follow the instructions to sign up for an account.

If you need help using the SolvNetPlus site, click REGISTRATION HELP in the top-right menu bar.

## Contacting Customer Support

To contact Customer Support, go to https://solvnetplus.synopsys.com.

## Statement on Inclusivity and Diversity

Synopsys is committed to creating an inclusive environment where every employee, customer, and partner feels welcomed. We are reviewing and removing exclusionary language from our products and supporting customer-facing collateral. Our effort also includes internal initiatives to remove biased language from our engineering and working environment, including terms that are embedded in our software and IPs. At the same time, we are working to ensure that our web content and software applications are usable to people of varying abilities. You may still find examples of non-inclusive language in our software or documentation as our IPs implement industry-standard specifications that are currently under review to remove exclusionary language.

<!-- image -->

1

## Getting Started

This chapter describes how to start the IC Validator WorkBench application.

The IC Validator WorkBench application allows for quick and easy viewing of layout data. With the application you can:

- View and edit large GDSII, OASIS, and compressed GDSII.
- View LEF/DEF files.
- Control which level of the design hierarchy is opened, viewed, or edited.
- Merge, extract, and save modified layouts.

For details about command usage, see the IC Validator WorkBench Command Manual .

This chapter includes these topics:

- Opening and Viewing Layouts
- Accessing the Documentation
- Starting the Application From the Command Line
- Executing Startup Files
- Environment Variables
- License Checkout
- Using the Graphical User Interface
- Command Interface

<!-- image -->

## Opening and Viewing Layouts

To load and view layout files:

1. Launch the application.
- From the Linux command line, enter:

icvwb

- On Windows operating systems, select the icvwb application.
2. Choose File &gt; Open . Select a layout from the list of recent files. The search bar lets you quickly find previously opened files, with an option to pin your favorites at the top for easy access. A delete button is also available to clear the list of previously opened files.

Alternatively, browse to a layout file and click Open .

You can also drag a layout file from a folder into the application window.

The layout file opens and its top cell is drawn.

3. Click Browse in the Tools group on the Home tab.

Using the Browse tool on the cell view:

- Zoom in by dragging upward.
- Zoom out by dragging downward.
- Zoom in by clicking.
- Zoom out by holding the Ctrl key and clicking.
- Use the scroll bars and arrow keys to move the view.
4. Click Ruler in the Tools group on the Home tab.

You can measure the size of an object by dragging in the cell view.

5. Move the cell view as follows:
- Click Pan in the Tools group on the Home tab and drag the view to place the view in a new position.
- In addition to using the Pan tool, you can press the Shift key and the middle mouse button and drag to pan the view with any other tool.
6. Choose File &gt; Exit to exit the application.

<!-- image -->

## Accessing the Documentation

Click the Help button on the right side of the ribbon to access documentation, including:

- What's New

Displays enhancements, new features, and changes in the current release.

- Release Notes

Displays the PDF version of the release notes. For the latest version of the release notes, check SolvNetPlus.

- Documentation

Displays the online help for the user guide, tutorial, command manual, and application notes. PDF versions of each document are available through a link on corresponding HTML pages. You can also press the F1 key to display the online help.

- Command Manual

Displays the PDF version of the command manual.

- User Guide

Displays the PDF version of the user guide.

You can control the viewer used for the HTML and PDF files (see Environment Variables).

- For PDF files, set the SNPS\_PDF\_VIEWER environment variable to your preferred viewer.

## Starting the Application From the Command Line

If the environment variable ICVWB\_LICENSE\_WAIT is set, then, when starting, the application waits until a license is available. If the variable is not set, then the application exits with an error if the license cannot be obtained.

If -nodisplay is specified, then the GUI does not open and commands are entered to a shell in the terminal. Otherwise, the application starts in GUI mode.

The options for starting the application are described here.

## Syntax

From a terminal window, enter any of the available options: star up com nd

```
icvwb  [-geometry AxB+C+D ] [-help | -h] [-menu] [-log filename ] [-run macrofile [-runnohalt]]
```

<!-- image -->

star up com

star up o

star up o

i

i

n

n

nd-ge

y

-geom try c

com

com

and-li

and-li

e h

e

and

p, st

p i

r u

u, st

r

p

helpcom

menuco

and- i

a

d-li star up com star up com nd-hel nd-

e

-help com

and

ti

<!-- image -->

```
[-socket [ address :] port ] [-version | --version | -v] [ layoutfile ] [-mac script ] [-startup=clean] [-nodisplay] [-python] [-exitOnError] [-cores number ] [-vue vuefile ] [-container]
```

## Description

The application passes through all command-line arguments when invoking the application without failing. The application does this so you can define your own command-line arguments for a script using the Tcl global variables argc and argv .

## Arguments

```
-geometry AxB+C+D
```

Specifies a window size from the window manager where A is the width, B is the height, C is the horizontal offset, and D is the vertical offset (from the upper-left screen corner).

```
-help, -h
```

Displays the help message and quits.

```
-menu
```

-menu  co

a

d

pti

Invokes the application in the menu GUI mode, which includes menus and toolbars. If omitted, the application will be launched in ribbon GUI mode.

```
-log filename
```

log fi es

t

r

d n w

k

c

y

star up com

nd-l

g

-log c m

and

pti

Forces the application log file to be named filename .

```
-run macrofile
```

star up com

nd-

-run com

a

d

pti

Loads and runs a macro command file. You can have multiple -run macrofile on the command line. The order in which -run script.mac layout.oas is processed is as follows: first, the script.mac file is run, and then the layout.oas file is loaded.

```
-runnohalt
```

macro-n

h

lt

p i star up com nd-

h

l

-run

ohalt c m

d

p i

If specified, then this option does not halt running the given macro command file (must be specified with the -run option) if errors are encountered.

```
-socket [ address :] port
```

star up com

versionc m

star up com

star up com

star up com

a

nd-

d-l

nd-l

nd-

nd-

y

ke

i

fi e

= le

l

y

-socket

m

star up com

-star up=cle

and

-nodisplay c m

nd

n  om

p i

d

-version c m

moden

-GUI

a

d

Displays the version of the application you are running.

layoutfile

<!-- image -->

Specifies a port number for socket communication. If the environment variable ICVWB\_SOCKET is set, then when the application is started, it will be in socket mode with a socket on the [ address :] port specified by the ICVWB\_SOCKET variable. Optionally, you can bind the socket to a specific IP address. The default address is the local host machine. port is the port number to use for socket communication by an application such as the IC Validator VUE tool.

```
-version, --version, -v
```

layoutfi e c m

nd-ve

i

p

i

pt

Loads the specified Tclrest i d mo ay u p layout file. You can specify multiple files on the command line.

-mac script

Provided script is executed after the layout loading is completed.

```
-startup=clean
```

Invokes the application and ignores configuration and user mode startup files.

```
-nodisplay
```

t

Invokes the application in non-GUI mode. When you run the application in -nodisplay mode, the application ignores any view commands. See Running the Application in No Display Mode.

-python

Specifies to switch the shell to a Python shell and run Python scripts using the Python interpreter. This option can be used only with the -nodisplay or -run command-line options. For example:

- -python -run script.py

Runs the script.py file using the Python interpreter.

- -python -nodisplay

The tool accepts Python input rather than Tcl input in the non-GUI mode.

-exitOnError

star up com

star up com

nd-exi O E

nd-

i

l

y

-exitOnEr o  c m

-nodisplay c m

a

d

t

p

moden

-GUI

<!-- image -->

Forces the application to exit with an error code of 1 if an error occurs for macro command files that are run ( -run macrofile ) when the application is launched.

-cores number

Specifies the maximum number of cores to be used when performing multithreaded operations. If unspecified, then the application can use all the cores on the machine. You can specify an integer from 1 through 256. If you specify a non-integer value for -cores , then it is ignored. If you specify an integer greater than 256, then the value of -cores is equal to 256.

-vue vuefile

Launches the ICV VUE application and loads the specified .vue file in the IC Validator VUE tool.

- -container

Runs the application within a container environment.

## Executing Startup Files

Table 1 describes the startup files and the order in which they are executed after entering icvwb at the command prompt.

Table 1 Startup files and order of execution

|   Order | Directories and Files                    | Description                                                                                                                                                                  |
|---------|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       1 | ICVWB_INSTALL_DIR/etc/icvw b_start.mac 1 | Site configuration file (installation startup macro file).                                                                                                                   |
|       2 | ICVWB_INSTALL_DIR/etc/user Modes.tcl 1   | User mode startup file. The mode that is run is determined by the environment variable ICVWB_USER.                                                                           |
|       3 | HOME/.synopsys/icvwb/*_rc.m ac 2         | Default settings of the application (icvwb_rc.mac, layout_rc.mac, and so on) are managed by the application and should not be edited manually, as they could be overwritten. |

Table 1 Startup files and order of execution (Continued)

|   Order | Directories and Files                   | Description                                                                            |
|---------|-----------------------------------------|----------------------------------------------------------------------------------------|
|       4 | HOME/.synopsys/icvwb/icvwb_ start.mac 2 | User configuration file (preferences, such as layer names, fill colors, and patterns). |
|       5 | ./.icvwb_start.mac                      | Configuration file of current working directory.                                       |
|       6 | layout_filename.mac                     | Macro file for the layout. For example, for a .gds this file would be a .gds.mac .     |

If any of these files exist, then the application runs them using the macro run command during startup. When you open a layout file, and a layout\_filename.mac exists in the same directory, that macro file is run after the layout file is loaded. This allows you to configure the application for a specific layout, for example, for specific layer attributes for that layout.

The precedence in the application is that layout preferences override user preferences, which override the site preferences.

## Environment Variables

You can change the behavior of the application by setting the environment variables listed in Table 2 before starting the application.

| Environment Variable   | Setting   | Description                                                                                                                                                                                                            |
|------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ICVWB_LICENSE_WAIT     | -         | If this environment variable is set, then the application waits for a license to be free. Otherwise, it exits if no license is available.                                                                              |
| ICVWB_HOME             |           | Use this environment variable to locate and save local configuration and startup files. If the selected directory is unavailable or not writable, the application defaults to the USER_HOME/.synopsys/ICVWB directory. |

Table 2 Environment variables

<!-- image -->

Table 2 Environment variables (Continued)

| Environment Variable   | Setting        | Description                                                                                                                                                                                                        |
|------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ICVWB_SOCKET           | [address:]port | The application connects to the specified [address:]port at startup.                                                                                                                                               |
| ICVWB_START            | Tcl string     | Takes a Tcl string as input, which is executed on startup after the .mac files are read and before executing -run scriptfile . For example: export ICVWB_START="default layout_cache off"                          |
| SNPS_PDF_VIEWER        | PDFViewer      | Use PDFViewer to specify the viewer for viewing PDF files, such as those included in the online help and those available from the Help menu. If you do not specify this variable, then the evince program is used. |

## License Checkout

When you run an instance of the IC Validator WorkBench application, one license is checked out. Licenses are checked out per instance and they do not depend on the number of cores utilized by the instance. The same applies when running the application in the distributed processing (DP) mode.

Other utilities such as genCache (for pre-generating layout caches) and Optimized OASIS (for converting other formats to the optimized OASIS file format) only check for existing IC Validator WorkBench licenses and do not check out additional licenses, even when the utilities are run in the DP mode.

The IC Validator WorkBench application includes a license timeout feature that allows you to set the idle time (minimum of 60 minutes) after which the license is released for other users. Use the default license\_timeout command to set the default timeout value in minutes.

## Using the Graphical User Interface

When you start the application in GUI mode, the GUI opens with a blank main window. If you load a layout, then it is displayed in the main window.

<!-- image -->

The GUI contains:

- The Ribbon

Appears at the top of the main window and contains groups of commands, which are organized by function, into four tabs. For additional information about the ribbon, see The Ribbon.

- Main window

This window consists of the area for viewing your open cell. Tables and plots can also be displayed in the main window. For more information, refer to the Main Window.

- Dockable views

The dockable views provide information about your layout and the tool status. You can move these views around the main window or make them floating. For more information, see Controlling Dockable Views and General Purpose Dockable Views.

- Status Bar

The status bar provides information about the status of the application. For detailed information, see Displaying the Status Bar.

You can control the position of new modal dialog boxes. The application remembers the position of the last modal dialog box and uses that position when creating new modal dialog boxes.

When you exit the application using File &gt; Exit , the dockable views and modal dialog box positions will automatically appear in their same location the next time you start the application. The new positions are not saved if you exit the tool using the exit command.

These topics are available:

- The Ribbon
- Main Window
- Controlling Dockable Views
- General Purpose Dockable Views
- Interrupt Capability
- Displaying the Status Bar
- Synchronizing Views in Currently Running Sessions
- Adding a Custom Script to the GUI

<!-- image -->

## The Ribbon

In addition to the Menu GUI mode, which contains toolbars and menus, IC Validator WorkBench includes a Ribbon GUI mode. When you work in the Ribbon mode, menus and toolbars are replaced with a ribbon, which appears at the top of the main window. The ribbon contains groups of actions, which are organized by function, into four tabs. Each tab in the ribbonFile , Home , Edit , and View -contains menu items, buttons, and fields you can use to perform tasks in the application.

<!-- image -->

When you launch the application in GUI mode, it opens in Ribbon mode by default. If you prefer to work in Menu mode, you can change the GUI mode setting either from within the GUI or from the command line when you launch the application.

## Note:

Changing the GUI mode setting from the GUI requires restarting the application for the change to take effect.

The following topics cover working with the ribbon:

- Collapsing and Expanding the Ribbon
- Using the Ribbon Search
- Customizing the Ribbon
- Customizing the Quick Access Toolbar
- Saving the Ribbon and Quick Access Toolbar Settings
- Exporting and Importing the Ribbon and Quick Access Toolbar Customizations
- Viewing the Contextual Select and Edit Options

<!-- image -->

- Changing the GUI Mode Setting in the GUI
- Changing the GUI Mode Setting on the Command Line

## Collapsing and Expanding the Ribbon

You can collapse the ribbon to display only the tab names and then expand it later.

To hide the ribbon:

- On the far-right side of the ribbon, click ( ) to collapse the ribbon.

The ribbon is collapsed and only the tab names are displayed. When you click a tab, the ribbon is temporarily displayed until you click anywhere outside the ribbon.

To show the ribbon:

- On the far-right side of the ribbon, click ( ) to expand the ribbon.

The ribbon is expanded.

You can also collapse or expand the ribbon using the gui ribbonbar configure command.

## Using the Ribbon Search

You can use the search function in the top-right corner of the application (left of the Synopsys logo) for quickly locating buttons and controls. To search for a button or control in the ribbon, start typing its name and the search function will suggest matching ribbon buttons. The search function also includes a help link that, when clicked, searches for the same term within the documentation.

<!-- image -->

<!-- image -->

## Customizing the Ribbon

You can customize the ribbon to create new tabs and add your most frequently used actions to them to help you work quickly and efficiently with the tool. You can also create new actions, hide and show tabs, rearrange tabs and groups, assign and reset shortcut keys, restore the ribbon to the default settings, and backup and export the ribbon customization to a file.

The following topics cover how to customize the ribbon:

- Opening the Ribbon Options Window
- Simplified Ribbon Mode
- Customizing Tabs in the Ribbon
- Customizing Groups in the Ribbon
- Customizing Actions in the Ribbon
- Setting Shortcut Keys for Actions
- Resetting the Ribbon

## Opening the Ribbon Options Window

To customize the ribbon, you need to open the Customize the Ribbon page in the Ribbon Options window.

1. From the main application window, right-click on any empty space in the ribbon.
2. Click Customize the Ribbon from the context menu.

<!-- image -->

The Ribbon Options page is displayed. The left section lists all the actions in the application and their corresponding shortcut key. You can filter the action list by each tab or by the actions that are not in the ribbon.

<!-- image -->

## Simplified Ribbon Mode

To use the simplified ribbon mode, from the main application window, right-click on any empty space in the ribbon and click Use Simplified Ribbon . The ribbon changes to the simplified mode.

## Customizing Tabs in the Ribbon

You can add custom tabs or change the order of the default tabs currently in the application. Custom tabs in the Customize the Ribbon list have (Custom) after the name, but the word (Custom) does not appear in the ribbon.

You can perform the following tasks when customizing the tabs in the ribbon.

| Task                                          | Procedure                                                                                                                                                                                                                                                   |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Add a new tab.                                | To add a new tab, under the Customize the Ribbon list, click the New Tab button. A new tab with the name New Tab (Custom) is added that includes a group New Group (Custom) .                                                                               |
| Edit the name of a custom tab.                | You can edit the name of a custom tab by right-clicking it and selecting Rename . In the Rename dialog window, enter the new name for the tab and click OK . Note: You cannot rename the default Home , Edit , and View tabs.                               |
| Change the order of existing and custom tabs. | You can change the order of the Home , Edit , and View tabs as well as of any custom tabs that you create. • Under the Customize the Ribbon list, click the tab you want to move, and then click the move up or down arrow to change the order of the tabs. |
| Hide a default or custom tab.                 | You can choose the tabs you want to display on the ribbon. • Under the Customize the Ribbon list, clear the check box of the tab you want to hide.                                                                                                          |
| Remove a custom tab from the ribbon.          | You can only remove custom tabs from the ribbon and not the default tabs. • To remove a custom tab, under the Customize the Ribbon list, select the custom tab and click Remove .                                                                           |

## Customizing Groups in the Ribbon

You can add custom groups or change the order of the default groups currently in the application.

You can perform the following tasks when customizing groups in the ribbon.

<!-- image -->

<!-- image -->

| Task                                            | Procedure                                                                                                                                                                                                                      |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Add a new group.                                | To add a new group, under the Customize the Ribbon list, click the New Group button. A new group with the name New Group (Custom) is added.                                                                                    |
| Edit the name of a custom group.                | You can edit the name of a custom group by right-clicking it and selecting Rename . In the Rename dialog window, enter the new name for the group and click OK . Note: You cannot rename the default groups.                   |
| Change the order of existing and custom groups. | You can change the order of the default and custom groups that you create. • Under the Customize the Ribbon list, click the group you want to move, and then click the move up or down arrow to change the order of the group. |
| Remove a group from the ribbon.                 | You can remove default as well as custom groups from the ribbon. • To remove a group, under the Customize the Ribbon list, select the group and click Remove .                                                                 |

## Customizing Actions in the Ribbon

You can create new custom actions, add or remove actions from default or custom groups, and change the order of actions.

<!-- image -->

<!-- image -->

| Task                        | Procedure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create a new custom action. | 1. In the Customize the Ribbon window, select a default or custom group under which you want to add the new action. 2. Click the New Action button. 3. In the Create Action dialog window, enter the following fields: • Title : Enter the title for the action that should appear on the ribbon. • Icon : Click to select an image file as the icon for the new action. • Tooltip : Enter the text that should appear when you hover the mouse over the action. • Statustip : Enter the text that should appear in the status bar when you select this action. • Enabled : Set whether the action should be enabled or disabled by default by providing a Tcl script. • Command : Enter a command you want the action to execute. For example: gui ribbon list . |

## 4. Click OK .

The new action is displayed on the ribbon under the group you the added the action.

5. In the Customize the Ribbon page, click OK .

<!-- image -->

| Task                                       | Procedure                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Add an existing action to a group in a tab | 1. From the right pane, select a group from the Customize the Ribbon list to which you want to add an action. 2. From the left pane, select an action from the Choose actions from list and click Add . Note: You can filter the list of actions as the following: an alphabetical list of all actions; the individual tabs they belong to; a list of actions not currently in the ribbon. 3. Click OK . The action is added to the ribbon under the selected group. |
| Remove an action from a group              | 1. Under the Customize the Ribbon list, select the group from which you want to remove an action. 2. Select the action click Remove . 3. Click OK . The action is removed from the selected group in the ribbon.                                                                                                                                                                                                                                                     |
| Change the Order of Actions in a Group     | 1. Under the Customize the Ribbon list, click the action you want to move within a group. 2. Click the up or down arrow buttons to change the order of the actions. 3. Click OK . The order of the actions is updated in the ribbon.                                                                                                                                                                                                                                 |

## Setting Shortcut Keys for Actions

You can assign, remove, and reset shortcut keys for actions from the Ribbon Options window.

To assign a shortcut key for an existing action or custom action:

1. In the Customize the Ribbon page, double-click the Shortcut cell next to any action in the left or right pane.
2. In the shortcuts dialog box, press the combination of keys you want to assign and click Assign .

If the key combination you entered is assigned to another action, you can choose to overwrite the existing assignment or change your key combination.

After assigning, the key combination is displayed under Current shortcuts .

3. Click Close and then click OK in the Ribbon Options window to apply the shortcut key combination.

To remove or reset shortcut keys:

- Double-click the Shortcut cell of the action.
- To remove a shortcut, select the key combination from the Current shortcut keys list and click Remove .
- To reset the shortcut key assignment to its default value, click Reset .

## Resetting the Ribbon

You can reset the tab to its original state and remove all customizations that have been made, or you can only reset the shortcut keys for the actions.

To reset the ribbon:

1. In the Customize the Ribbon page, in the Customizations area, click the Reset dropdown button.
2. Do one of the following:
- Click Reset All to reset all the customizations and restore the ribbon to its default state.
- Click Reset all shortcuts to reset only the customized shortcut keys set for the actions.
3. Click OK .

Based on the reset option selected, the ribbon is reset to its original state, or the shortcut keys for the actions are reset to the default values.

## Customizing the Quick Access Toolbar

The Quick Access Toolbar is a customizable toolbar where you can add a button that is on the ribbon for easy access. The Quick Access Toolbar is displayed in the upper left corner of the application by default. You can change this to display the Quick Access Toolbar below the ribbon.

The following topics cover working with the quick access toolbar.

- Adding Actions to the Quick Access Toolbar
- Resetting the Quick Access Toolbar

## Adding Actions to the Quick Access Toolbar

To add actions to the Quick Access Toolbar:

1. In the upper-left corner of the application, click the drop-down button to display the quick access toolbar menu.
2. From the menu, select the actions you want to display in the Quick Access Toolbar.

<!-- image -->

3. To add more actions, click More Actions .

The Ribbon Options window displays the quick access toolbar page. You can also open this page by right-clicking on an empty space in the ribbon and selecting Customize Quick Access Toolbar .

<!-- image -->

4. In the Customize the Quick Access Toolbar page, choose an action from the left pane and click Add . You can group the actions by adding a separator between the actions.

The actions added in the Quick Access Toolbar is displayed in the right pane. When adding actions from the left pane, you can choose to display the actions by each tab or display all the actions by selecting from the Choose actions from drop-down menu.

5. Click OK .

The action is added in the Quick Access Toolbar.

## Resetting the Quick Access Toolbar

You can reset the Quick Access Toolbar to its original state and remove all customizations that have been made.

To reset the Quick Access Toolbar:

1. In the Customizations area of the Quick Access Toolbar page, click the Reset button.
2. Click OK .

The Quick Access Toolbar is reset to its original state.

## Note:

The Quick Access Toolbar is reset only for the current session unless you save the configuration.

<!-- image -->

<!-- image -->

## Saving the Ribbon and Quick Access Toolbar Settings

You can save the customization made to the Ribbon and Quick Access Toolbar, so that when the application starts, the configuration is loaded.

To save the customization:

- In the Ribbon Options window, click Save .

The Ribbon and the Quick Access Toolbar configurations are saved to the HOME/.synopsys/icvwb/icvwb\_ribbon\_customizations.xml file. This file is automatically run the next time the application is started.

## Exporting and Importing the Ribbon and Quick Access Toolbar Customizations

You can export and import the ribbon and the quick access toolbar customizations as an XML file for different users to use and share the customizations. For the ribbons, you can also load a preset shortcut key (hotkey) configuration in the application.

To export or import the customizations:

- In the Ribbon Options window, click the Import/Export drop-down button.
- To import a customization, click Import customization file , choose the .xml customization file, and click Open .

The imported customization file is loaded in the application.

- To export a customization, click Export customization file , enter a file name for the .xml file, and click Save .

To import a shortcut key configuration:

1. In the Customize the Ribbon page, click the Import/Export drop-down button.
2. Select a hotkey configuration under Shortcut configuration : Default, CC\_hotkeys, ICC\_hotkeys, or V\_hotkeys.

For more information about hotkey configurations and for the list of default hotkeys in the application, see Default Hotkeys.

## Viewing the Contextual Select and Edit Options

When selecting or editing shapes, the corresponding select and edit options for the object that is selected or being edited are dynamically displayed in your current working tab. For example, in an editable cell when you click a polygon on the layout using the Select tool in the Edit tab, the Select Polygon Options group is automatically displayed when you move between the Home , View , and Edit tabs or even when you move to a custom tab.

<!-- image -->

Similarly, the Edit Polygon Options group is displayed in the your current working tab when you click the Polygon tool on the Edit tab.

## Changing the GUI Mode Setting in the GUI

To change to Menu GUI mode in the GUI:

1. Click the Settings button ( ) on the far-right side of the ribbon.
2. Select Options from the drop-down menu.

The Options dialog box opens.

3. In General settings, select the Menu option for GUI mode .
4. Click Save and then click OK .
5. Restart the application for the change to take effect.

## Changing the GUI Mode Setting on the Command Line

To change to Menu GUI mode on the command line when you launch the application:

- Enter icvwb -menu at the command prompt.

## Main Window

The main window is the central area in the GUI that displays the cell view (the view of the cell), tables, and so on, as well as any other windows. From the main window, you can analyze the layout and the markups and annotations you create in it.

Press Ctrl+Tab to toggle between windows in the GUI.

You can use the View tab to arrange the window views, select the window to display, and close one or all open windows.

To arrange windows, click Arrange in the Window group in the View tab and select one of the following options:

- Tile to tile your windows.
- Arrange Horizontal to arrange all your windows in a horizontal position.
- Arrange Vertical to arrange all your windows in a vertical position.
- Cascade to cascade your windows.

## Grouping Cell Views

You can group cell views under a single window by dragging the window frame of one layout over another layout's window. You can also use the gui frame move command to perform the same action.

To group and arrange cell views under a single window:

1. Click the restore icon on the main window or select View &gt; Arrange and choose an option to arrange the current open layouts.

All the open layouts are displayed in the central area.

2. Select the first layout's frame and drag it over the second layout's window.

The first frame tries to align either to the top, right, bottom, or left of the second layout's frame. After you place the frame in the desired location, the two frames now appear under a single window.

## Controlling Dockable Views

When you click Dockable in the Window group on the View tab, you can view a menu that enables you to open or close individual views.

To open specific view windows:

1. Click Dockable in the Window group on the View tab to see the list of dockable views.
2. Select a specific view from the menu to display it in the GUI (or if it is already visible, to hide it from view).

These topics describe how you can manipulate (move, undock, and so on) dockable views:

- Undocking and Moving Views
- Docking Views
- Tabbing Dockable Views

## Undocking and Moving Views

You can undock any of the view windows to move them around the application or dock them to a specific location. The view windows are placed around the main window by default.

To undock a view:

- Click the close button in the upper-right corner of the selected view.

<!-- image -->

To move a view:

- Drag that view's title bar to the desired location.

## Note:

The application attempts to snap the undocked view to a docked location if the view is placed in the vicinity of a docking location. To prevent automatic docking, press the Ctrl key when you drag the view to your desired location.

## Docking Views

To dock a view, either:

- Click the undock/dock button in the undocked view.
- Double-click the undocked view's title bar.
- Drag the view's title bar over the main window or a dockable view.

## Tabbing Dockable Views

You can combine dockable views in tabs. This is useful when you want to organize the look of the application to limit clutter on your desktop.

- Drag the view over the middle of another dockable view.

This puts the open views in a tabular format (Figure 1). Click the respective tabs at the bottom of the views to switch between them.

<!-- image -->

You can use the gui dockable commands to script which dockable views to show and where they will be placed.

## General Purpose Dockable Views

The application has a number of dockable views that are not specific to layout viewing and editing tasks. These dockable views are:

## Command Help

The Command Help view has all the available commands and defaults that can be used in the application. You can see the usage string of a command by hovering the mouse over it.

<!-- image -->

<!-- image -->

To view a command's associated Online Help file that contains syntax, description information and examples, double-click the command or right-click the command and select Show Help .

To use the command, right-click the command and select Insert Command . The command is entered into the command pane where you can add the arguments and use the command.

The Command Help view has two tabs: Commands and Index .

The Command tab has all the commands grouped by their module and subcommands where you can drill-down to a particular command. The Index tab displays an alphabetical list of all the available commands. This tab has an entry field where as you type the command, the list gets filtered automatically showing all commands that contain the typed text.

## Command Pane

The Command Pane includes the command history and the command-entry field. The command history displays current session commands and application-use history, including commands you type manually as well as those generated through GUI interaction or loading a macro file.

You can use the command-entry field to enter native and supported Tcl commands. Use the -h or -help option to display the command's usage statement. For example:

```
default anno_anchor -h # Usage: default anno_anchor [anchor]
```

When focus is on the command-entry field, you can:

- Press the Tab key to autoc mple nds autocomplete a supported command (including default commands) or display a list of possible choices. The arguments and options for supported commands (including default commands) are not included in the autocomplete.

For example, cell add p will autocomplete to cell add path (without arguments), but cell add path -la will not autocomplete.

For the source command, press the Tab key to autocomplete the file name or display a list of possible choices.

- Use the up and down arrow keys to cycle through commands entered in the commandentry field.
- Use the Shift key along with the up and down arrow keys to cycle through the command history similar to a Linux shell for commands entered in the command-entry field or through the GUI.

<!-- image -->

You have the option to copy and paste multiple lines of commands into the commandentry field and have the application execute them one-by-one, echoing the return values after each command as the application proceeds. From the command history or from a saved macro, you can select and copy the multiple lines of commands you want, and then paste these into the command-entry field. Press Enter and the application executes each command one-by-one, echoing the return values as it proceeds into the command history. You can also use the shortcut copy and paste keystrokes ( Ctrl + C and Ctrl + V , respectively) to copy text from the command-history window in the GUI and paste it in the command-entry window.

Save your command history to a file by right-clicking the command pane window and selecting Save Contents As from the context menu.

You can turn logging on or off by right-clicking the command pane window and selecting Turn Log On or Turn Log Off . This option can also be controlled from the Logging option under the General page in the Options dialog box.

## Python Pane

Using the Python Pane, you can script the application using Python. To enable the Python Pane, click Dockable in the Window group of the View tab, and select Python Pane .

For more information about using Python with IC Validator WorkBench, see #unique\_57.

## Task View

The Task view provides information about current tasks, such as the tasks you have initiated, their status, and the task description. You can delete tasks using the context menu.

## Tree View and Open Cells

The Tree view displays detailed information about the layout including the layout layers, the cell objects, open cells, and root cells as well as their descriptions. This is a general view containing all layout information. If you load additional modules, additional information is displayed in the Tree view, for example model files if the wb module is loaded.

## Note:

If the layout is not OASIS compliant, it appears with a red asterisk (*) mark in the Tree View . The File &gt; Info page displays a Non-compliant OASIS file section with the warning messages about compliance violation.

The Open Cells view shows the information in the Open Cells folder of the Tree view for the active layout. For each cell, all the cells referenced by it are listed under the Child Cells folder. If the listed child cell is not defined, then the cell appears shaded and in italic type.

The Tree view and Open Cells dockable views allow you to:

- #unique\_58
- Create a new dockable view showing a portion of the tree view (#unique\_59)
- Edit items, such as the database unit (DBU) of the layout in #unique\_60
- Clear cells of any shapes or delete cells and their references. #unique\_61
- Copy cell names and text from the description or properties column in the Treeview (and other dockable windows) to the clipboard by selecting the items and pressing Ctrl +C.
- Recursively expand and collapse a node, including all child-nodes, by right-clicking a node a selecting Expand All or Collapse All from the context menu.

Other dockable views, including the Layout Layers and #unique\_62 allow you to perform similar tasks.

## Find Items

You can find items in the Tree view, such as cells or markups. This is useful if you would like to find a particular cell when there are thousands of cells with similar names in your layout.

To search for specific objects:

1. Open the Tree view (if not already open) and expand the active layout in the tree.
2. Right-click the folder in which you want to search (cells, rulers, gauges, or other) and select Find from the context menu.
3. In the find entry field, enter the search string.

The application searches that folder and all open descendant nodes for the string you specified, highlighting the first result and moving the focus to that node.

4. Pressing either the Backspace or Delete key highlights the first item from the top of the folder that matches the shorter search string.
5. Pressing F3 highlights the next item that matches the search string.
6. Pressing Shift + F3 highlights the previous item that matches the search string.

## Tear-Off View

You can tear off part of the Tree view as a new dockable view. This makes it easier to get specific cell information from this tear off view while still being able to scroll up and down in the Tree View.

<!-- image -->

To create a tear-off view:

- Right-click a folder in the Tree view and select Tear Off from the context menu.

To close this view:

- Click the X button in the upper-right corner of the view.

## Editable Text Fields

The dockable views based on the Tree view contain two columns. Read-only fields have a white background in the left column and a dark blue background in the right column. Editable nodes have a light blue background.

To make a text field editable:

1. Click the desired text field to select it.
2. Click it again to put it in editable mode.

The text field changes to a white background, the text is selected, and the cursor is placed at the end of the text in the field (see Figure 2).

Figure 2 Editable and read-only text fields

<!-- image -->

## Clear and Delete Cells

You can clear cells of any shapes from the Tree View or Open Cells view. To do this:

1. Open a cell from the Tree View and make it editable.
2. Right-click the cell and click Clear from the context menu or right-click multiple editable cells and click Clear Selected .

<!-- image -->

<!-- image -->

The cell clear command is applied to the cell and it is cleared of any shapes in it.

## To delete cells from the Tree View :

1. Right-click any cell from the Tree View and click Delete or right-click multiple cells and click Delete Selected .
2. In the Delete Cell or Delete Selected Cells dialog box, choose one of the following options:
- Cell only : delete only the cell.
- References only : delete only the references of the cell.
- Cell and references : delete both the cell and its references.
- Cell, references, and unreferenced children : delete the cell and its references and all its child cells, which are not referenced elsewhere.

<!-- image -->

<!-- image -->

<!-- image -->

## 3. Click OK .

## Side Cells

The Side Cells dockable view shows the temporary cells that are attached to the current active cell in the application. These cells are created as the results of a Net Trace, Find, or any other layout or cell import operation. The Side Cells view lists these cells as collapsible nodes that you can expand or collapse to see the individual layers that make up the side cell. You can select and manipulate the side cells and their layers as required.

The side cells are displayed with a higher brightness and a tinting color than the active cell, so that you can easily distinguish them. You can adjust the brightness and color of the side cells and their layers, as well as the dimming of the active cell, in the Side Cells options. See #unique\_63 for more details.

The Side Cells view is automatically shown when you perform a Net Trace or Find operation. To show or hide the Side Cells dockable view, in the Window group on the View tab and choose Side Cells from the drop-down menu.

<!-- image -->

<!-- image -->

## Side Cell Operations

You can perform the following operations in the Side Cells view:

- Select which side cells and layers you want to see in the cell view by checking or unchecking the boxes next to the side cell names (collapsible nodes) and layer names. You can select multiple side cells or layers by holding Ctrl while clicking.
- Change the tint color, outline width, and brightness of a side cell or a layer by doubleclicking the Color column of the side cell or layer. By default, the side cell has no fill color and uses the layer colors of the original shapes.

The layer inherits the tint color and outline width of the shape layer unless you change them individually.

- Edit the name, fill color, pattern, transparency, outline color, style, and width of the side cells in the Side Cell Attributes dialog box or of the layers in the Side Cell Layers Attributes dialog box by clicking More . You can apply these attributes to one or more side cells at a time.

<!-- image -->

<!-- image -->

<!-- image -->

To remove any fill color, pattern, or outline attributes from the side cells, click No Fill .

## Note:

The side cell attributes override the side cell layer attributes and the layer attributes are only displayed when No Fill is selected for the side cell.

- For side cells, apply the tint color, pattern, and outline tint color, style, and width attributes to the side cells by checking the boxes for these options. If these options are unchecked, the side cells will use the fill color, pattern and style of the shape layer.

You can modify the fill color, pattern, transparency, outline color, style, and width of the side cell layers as you would do in the #unique\_65 dialog box. However, for side cell layers, you cannot change the attributes for multiple layers at once, unlike in the Layer Attributes dialog box.

- Control the brightness of the active cells by moving the Cell Dimming slider left or right.
- Sort the side cells by the either name or color columns.
- If the default show\_layer\_mark\_checkbox option is set to 1 , you can use the check boxes to mark or unmark the side cells.

When you right-click on a side cell or a side cell layer in the Side Cells view, you can perform various operations on it. The following table summarizes the available options and their effects:

| Option          | Effect                                                                 |
|-----------------|------------------------------------------------------------------------|
| Show / Hide All | Toggles the visibility of all side cells or side cell layers.          |
| Show/Hide Only  | Toggles the visibility of the selected side cells or side cell layers. |

<!-- image -->

<!-- image -->

| Option                                                   | Effect                                                                                                                                                           |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mark                                                     | Adds an X mark to the selected side cell or side cell layer.                                                                                                     |
| Mark Only                                                | Adds an X mark to the selected side cell or side cell layer and removes any marks from the rest.                                                                 |
| Mark/Unmark All                                          | Toggles the X marks on all side cells or side cell layers.                                                                                                       |
| Mark/Unmark Selected                                     | Toggles the X marks on the selected side cells or side cell layers.                                                                                              |
| Show/Hide Selected                                       | Toggles the visibility of the selected side cells or side cell layers.                                                                                           |
| Rename                                                   | Changes the name of the selected side cell or side cell layer.                                                                                                   |
| Attributes                                               | Opens the Side Cell Attributes dialog box for side cells or the Side Cell Layer Attributes dialog box for side cell layers to configure their properties.        |
| The following options are only available for side cells: | The following options are only available for side cells:                                                                                                         |
| Import Side Cell                                         | Opens the Import Side Cells dialog box to import a cell from another layout file as a new side cell.                                                             |
| Zoom To                                                  | Zooms in on the selected side cell (double-clicking also works).                                                                                                 |
| Show in Find Information                                 | Updates the find information table with the details of the selected side cell.                                                                                   |
| Export                                                   | Export the side cell to another layout file. Selecting this option opens the Save As dialog box where you can choose the name and format of the exported layout. |
| Export Selected                                          | Export the selected side cells to another layout file.                                                                                                           |
| Delete                                                   | Removes the selected side cell from the Side Cells view and the find information table.                                                                          |
| Delete All                                               | Removes all side cells from the Side Cells view and the find information table.                                                                                  |
| Delete Selected                                          | Removes the selected side cells from the Side Cells view and the find information table.                                                                         |

## Layout Layers

The Layout Layers view enables you to view, organize, and configure the layers of a layout file. In the Layout Layers view, you can configure layers by changing their name, fill color, pattern as well as their outline color, style, and width. You can apply these attributes to individual layers, to multiple selected layers, or to a group of layers.

<!-- image -->

To open the Layout Layers view, click Dockable in the Window group on the View tab and select Layout Layers from the drop-down menu. You can also open or close the view by pressing Shift+F2.

The Layout Layers view provides three modes for working with layersFilter for filtering layers as you type, Find for finding layers, and Group for working with layer group configurations. All these features enable you to quickly select the layers you need to work on.

Figure 3 Layout Layers view

<!-- image -->

## Working with Configurations

The Layout Layers view can support many independent layer configurations. In each configuration, layers can be grouped and configured differently, and you can easily switch between configurations while in the Group mode. You can save or load layer configurations by clicking the corresponding buttons in the header panel of the Layout Layers view. This panel can be activated or deactivated by right-clicking and selecting Show Find/Filter from the context menu.

<!-- image -->

You can create as many configurations as required. To delete the current configuration, click the X button on the header panel. To rename the current configuration, click the icon next the configuration name on the header panel.

## Working with Layer Groups

Layers can be organized into groups, which can be nested in an unlimited number of hierarchy levels. When you create a group, a new layer configuration is created if it does not already exist. In the Group mode, you can easily switch between configurations including the Flat View that shows all layers without grouping.

## Note:

You cannot group a layer that is present only in the overlaid layout and is not present in the main layout.

## To create a group:

1. In the Layout Layers view, select one or more layers that you want to add to a group. Hold down the Ctrl key to select multiple layers.
2. Right-click and choose More &gt; New Group from the context menu.
3. Type a name for the group or press Enter to use the default name groupName#1 .

A new collapsible folder is created under the Cell Outline node and the layers you selected are listed under this folder.

When you create a group, a group configuration is created with the default name group\_configuration#1 if no other group configurations exist. If a group configuration already exists, then new groups are automatically created under this configuration.

## Moving Layers to a Group

You can move a layer between groups by using the drag-and-drop operation. You can also move a layer to a group by right-clicking a layer and choosing More &gt; Move to Group , and then choosing the corresponding group or subgroup from the list.

## Editing Attributes of Layers and Layer Groups

You can edit attributes of layers such as the fill color and pattern as well as the outline color, width, and style in the Layout Layers view.

To change the layer attributes, double-click the layer preview (the fill color under the second column) of a layer or a group. A panel opens allowing you to change the fill color, pattern, and translucency as well as the outline stipple. If you select More in the panel, the Layer Attributes (or Group Attributes if group selected) dialog box opens where you can change a lot more attributes such as the layer name, outline color, width, and translucency and also select or enter a wide range of color codes. You can also use the right-click menu to open the Layer Attributes or Group Attributes dialog box. Similarly, you can change the attributes of a cell's bounding box by double-clicking the first preview box (for Cell Outline ) under the second column.

<!-- image -->

You can also embed this color panel in the Layout Layers view by right-clicking and selecting Show Patterns . You can use the panel to quickly change the fill and outline colors, fill patterns, brightness of layers and outlines, and the background color for layers. Click at the top right of the color panel to open the mouse button mapping table that lists mouse shortcuts for changing the fill and outlines colors of layers. Click at the bottom right of the color panel to open the complete color palette.

For more information about editing and changing layer attributes, see #unique\_88.

When you select multiple layers and open the Layer Attributes dialog box, the dialog box shows undefined or blank values if the selected layers have different values, and it shows the corresponding attributes if the selected layers have the same values.

## Synchronizing Layout Layers

You can enable or disable the layer synchronization across all open layouts and side cells by selecting the layer synchronization icon ( ) on the header panel and choosing either or both of the following options:

- Layers with Side Cells

When enabled, the layer's visibility settings is synchronized with side cells. That is, when you change the visibility of a layer in the Layout Layers dockable, the layer's visibility in the Side Cells dockable is also updated.

- Layers in open layouts

When enabled, the visibility, marking, and group configurations are synchronized across all open layouts.

If multiple layers have the same layer:datatype, the layer from the active layout (if present) or last opened layout is used. When layers synchronization is enabled, the Layout Layers view becomes common for all layouts, reflecting any layer or grouping changes across all layouts. Hierarchy level filters ( Levels , BBoxes , and Names ) are also applied to all open layouts.

When synchronization is disabled, the synced group information will remain in all opened layouts.

## Sorting and Ordering Layers

You can sort the layers in a layout by their name, by their layer:datatype value, or in any custom order. By default, the layers are displayed in an ascending layer:datatype order. To sort layers, click the Layout Layers column and choose one of the Sort by Name (A to Z or Z to A) or Sort by layer:datatype (ascending or descending) options from the context menu. You can also drag layers and create a custom sorting order. This sort order is temporarily saved in the Layer Order option available along with the sort by name and layer:datatype options.

<!-- image -->

Along with sorting the layers, you can also choose to group the layers depending on if they are hidden or visible. Select the Group by visible option from the context menu to group all the visible layers at the top and the hidden layers at the bottom.

<!-- image -->

## Showing and Hiding Layers and Groups

You can control which layers or layers groups to show or hide in the main layout view by using the check boxes provided to the left of layers or group names. Selecting the check box of a group shows all the layers in that group. You can also use the show/hide options when you use the right-click menu. The Show All option shows all the layers and layer groups listed under the root Cell Outline node. Hide All hides all the layers. Show Only shows only the selected layer or group and Hide Only hides only the selected layer or group.

You can also control whether to show all the configured layers in the application or show only the layers that are in the layout by right-clicking and selecting either Show Layers &gt; All Configured or Show Layers &gt; Layout Only from the context menu.

## Marking and Unmarking Layers or Groups

You can mark the layers with an X mark or unmark them using the options provided in the right-click menu. For more information about marking and unmarking layers, see #unique\_89.

## Ungrouping a Layer Group

To ungroup a layer group, right-click a layer group and select Ungroup from the context menu. The layers belonging to that group are moved up one level to the parent layer group. If there is no parent group, the layers are moved to the root level that does not belong to any group.

## Setting the Active Layer

You can set the active layer, which is used as the default layer when editing, by double clicking a layer or by right-clicking a layer and selecting More &gt; Set Active from the context menu. The layer that is currently active is emphasized in the Layout Layers view.

You cannot set the layer of an overlay as the active layer.

## Renaming Layers and Groups

You can rename a layer or a layer group by right-clicking it and choosing Rename from the context menu.

You cannot rename the layers of an overlay.

## Deleting a Layer

To delete a layer, right-click, and choose More &gt; Delete .

You cannot delete the layers of an overlay.

## Note:

If layer synchronization is enabled and you delete a layer, then the layer is deleted only from the current active layout.

## Creating New Layers

To create a new layer, select a layer, right-click, and choose More &gt; New Layer from the context menu. The Copy to New dialog box displays with pre-configured attributes according to the selected layer and you can enter the name and format (layer:datatype) for the new layer. You can also edit the attributes such as the color, pattern, outline color, style, and width of the layer. To create the new layer, click OK . The layer is added under the root layer in the Layout Layers view.

You cannot add new layers to an overlay.

## Copying Layer Contents

You can copy a layer's contents (that is, all objects on the layer) to a new or existing layer in the active layout. You can also copy it to a new or existing layer of a specific cell in an inactive layout. Additionally, you can provide optional offsets in the X and Y directions to be used when copying shapes.

To copy a layer's contents, select a layer, right-click, and choose More &gt; Copy To from the context menu. The Copy To dialog box (Figure 4) displays and you can provide the target layout, target cell, layer, datatype, and optional offsets (default is 0). After you click OK , the layer contents are copied to the designated layer in the specified layout and cell. The new layer might be created if the specified layer does not exist.

<!-- image -->

## Note:

You cannot copy layers that are part of an overlay.

Figure 4 Copy To dialog box for copying layer contents

<!-- image -->

## Filtering Layers

You can filter the layers displayed in the Layout Layers view by selecting Filter from the drop-down menu on the header panel. After you select Filter , type the text by which you want the layers to be filtered. The layers are filtered as you type the expression in the filter box. You can enter text that matches the layer name or its specifications. You can also use the wildcards "*", "?", and "[...]" for specifying different filtering criteria. Pressing the Enter key in the filter input box shows all the layers that match the filter criteria.

## Filtering Layers by Polygon Count

You can filter layers by the number of polygons a layer, which is calculated either hierarchically or by the total number of instances. For example, this can be used to find layers that have no shapes. In the Layout Layers view, you can create filtered groups of layers by selecting filtering criteria such as equal to, greater than, or lesser than, and then providing values for these criteria. You can also choose to hide or display the polygon count column that displays the polygon count of each layer either hierarchically or flattened. The filtered layers are automatically grouped based on the chosen criteria. Layers in these filtered groups cannot be manually added or removed. Otherwise, like regular layer groups, the groups can be shown or hidden and configured. The filtered layer groups are saved and reloaded when saving/loading a layer configuration.

To filter layers by the polygon count:

1. In the Layout Layers view, right-click and select Add Filter .
2. In the Specify Filter dialog box, select one of the following criteria from the drop-down list and provide a value for it:

| Criteria   | Description                                        |
|------------|----------------------------------------------------|
| Equals     | Filters polygons equal (==) to the provided value. |

<!-- image -->

<!-- image -->

| Criteria                    | Description                                                                    |
|-----------------------------|--------------------------------------------------------------------------------|
| Is between                  | Filters polygons between (-) the two provided values, including the endpoints. |
| Is less than                | Filters polygons less than (<) the provided value.                             |
| Is less than or equal to    | Filters polygons less than or equal to (<=) the provided value.                |
| Is greater than             | Filters polygons greater than (>) the provided value.                          |
| Is greater than or equal to | Filters polygons greater than or equal to (>=) the provided value.             |

## 3. Click OK .

The filtered layer group is created for the chosen criteria in the Layout Layers view. The layer group has an orange filter icon and the name of the group is the filter criteria that was chosen.

If the polygons are updated in the layout, all the filter group's icons change to red and the group name is displayed in italic font. You need to refresh the groups to update them for the new polygon count. To do this, right-click the group you want to update and then click Refresh from the context menu to update just that filter, or click Refresh All Filters to refresh all the filters you have added.

<!-- image -->

## Showing Polygon Count

You can choose to show or hide the polygon count column by right-clicking in the Layout Layers view and selecting Show Polygon Count from the context menu, or by setting the default layout\_layers\_view\_configure command. By default, the polygon count column is not displayed.

You can change the default polygon count calculation mode from hierarchical to flattened by right-clicking the polygon count column and deselecting the Hierarchical count check box. You can also set the default using the default layout\_layers\_filter\_mode command or by setting the Options &gt; Layers &gt; Polygon count mode to either Flat or Hierarchical . If you hover the mouse over the polygon count column, the tooltip displays the calculation mode being used.

You can also sort the layers by their polygon count by clicking the column or by rightclicking the column and selecting either ascending or descending.

<!-- image -->

## Finding Layers

You can find specific layers in your layout file by selecting Find from the drop-down menu on the header panel and entering the search criteria. After you select Find , type the search criteria in the search box. The search results are highlighted in the Layout Layers view as you type your search criteria. You can also use the wildcards "*", "?", and "[...]" for specifying different search criteria.

## Importing Technology Files

You can load IC Compiler II (ICC2), Custom Compiler (CC), Laker technology files, layer map files, and ICV runset files in IC Validator WorkBench by using the layout layers configuration button or by using the TechFiles drop-down button on the Home tab. See #unique\_91.

<!-- image -->

<!-- image -->

## Note:

When you load a layer map, the layer name and purpose will be joined with either a semicolon(:) or a dot(.), based on the defaults set by the layout\_layer\_datatype\_separator dot|colon command. This only applies when layers are imported, and changing this default later will not affect the names of already loaded layers

## Finding Shapes

You can find shapes in layers by specifying the region or properties of the shape.

To find shapes in layers:

1. Select a layer or multiple layers for which you want to find shapes.
2. Right-click and choose Find Shapes from the context menu.

The Find Settings dialog box displays.

3. To find shapes based on the region, specify the find criteria in the Select Region for Find page.
4. To find shapes by property, click Next , and enter the find criteria in the F ind by Property page.
5. Click Find .

The find results are displayed in the Side Cells dockable view.

## Setting a Custom Boundary Layer as the Cell Outline

In the Layout Layers view, you can set a custom boundary layer as a cell outline, which can be used for showing the cell boundary and cell-name in the hierarchy instead of the default cell bounding box (cell bbox).

<!-- image -->

To set a layer as the cell outline:

- In the Layout Layers view, right click the layer you want to set as the outline and then click More &gt; Set As Outline , or use the command layout cell outline by providing the layer:datatype value. For example: layout cell outline {layer 99:0}

<!-- image -->

The layer's bounding box is now set as the cell outline. The layer is removed from the list of layers and appears at the top as the Cell Outline. Layer actions such as show, hide, rename, mark, group, and delete are no longer available for this layer.

## To reset the outline:

- Right-click the cell outline and click Reset Outline from the context menu or specify cellBBox as the layer in the layout cell outline command. For example: layout cell outline {layer cellBBox}.

The outline of the layout is reset to the bounding box of the cell and the boundary layer is added back to layout layers as a regular layer.

The cell outline layer (and the cell-names) are not dimmed by default when a side-cell is viewed. You can dim the cell outline like other layers by right-clicking the outline and selecting the Dim Outline check box.

<!-- image -->

## Hiding and Showing Text

You can hide or show text appearing in the layout by selecting the Layer text visibility check box. You can select multiple layers and hide or show text by clicking the check box of any of the selected layers.

<!-- image -->

The commands for hiding and showing text are:

```
layout text hide layout text show
```

When using the command for hiding text, you can create text patterns using regular expressions and wildcards to hide specific text in specific layers. The check box for text hidden using regular expressions or wildcards appears shaded in black.

## Note:

When you hide text using text patterns and then hide some other text using text patterns, the previous text that was hidden get unhidden and is displayed.

If layout text objects are hidden (layout display view\_text\_show 0 ), showing or hiding individual layer's text object is disabled (the Layer's text objects check-box column is disabled). You can show or hide the layout text objects by clicking the icon in the layout layers table header. T

## Emphasizing Layers

You can emphasize layers by clicking that will dim the rest of the layers making the emphasized layer shapes easily noticeable. To de-emphasize a layer, click . You can deemphasize all previously emphasized layers by clicking or by choosing Deemphasize All from the right-click menu. If you do not want the emphasize layer options to appear in Layout Layers , uncheck the Show Emphasize Layer check box from the right-click menu.

<!-- image -->

<!-- image -->

## Interrupt Capability

You can interrupt foreground and background tasks.

To interrupt a tasking running in the foreground:

- Press the Esc key.

You also can use this feature if you need to interrupt the expansion of a cell folder in the Tree view (for example, a folder containing millions of cells).

To interrupt a background task, use the Task View:

1. Right-click the specific task to bring up the context menu.
2. Select Stop .

## Displaying the Status Bar

The status bar (see Figure 5) provides information about the last command executed, current application mode, status of the socket, and so on.

Figure 5 The Status Bar

<!-- image -->

The application includes a button on the status bar to indicate that a task is running in the background.

- When running a task in the background, a progress button ( ) appears in the status bar.
- When the task you are running completes, the button changes to . And when the task is paused, the button changes to .

<!-- image -->

<!-- image -->

Click the button and the Task View is displayed if it is hidden, even if no tasks are running. You can see which tasks are running or paused, which ones are stopped due to errors, and more.

The hierarchy control shows the filtering by hierarchy level and the hierarchy depth of the current active cell. If filtering by hierarchy level is disabled, then All is displayed instead of the filter-level. Hierarchy depth is calculated in the background and during the calculation the Hierarchy control displays NA for hierarchy depth.

You can change the hierarchy level filtering by clicking the hierarchy control.

When you open a socket, the image in the status bar changes from to . Once your socket is connected, the image changes to .

You can display or hide the Status Bar by selecting the Status Bar check box in the Window group on the View tab.

The center point of the pointer pixel is used for the coordinate calculation.

## Synchronizing Views in Currently Running Sessions

To synchronize views in multiple running sessions, select Sessions from the View tab or click the icon in the status bar. This action opens the Connect to Currently Running Session(s) dialog box, as shown in Figure 6. The dialog box lists all the running IC Validator Workbench sessions. Use the Sync toggle switch next to each session to enable or disable the synchronization. Views (all view commands), Layers (all layer configuration related commands), and Markups (drawing markups) are synchronized by default. Click the buttons in the Sync commands section to disable the corresponding synchronization. You can either select to synchronize the specific markup types or select all the markups types.

Figure 6 Connect to Currently Running Session(s) dialog box

<!-- image -->

## Adding a Custom Script to the GUI

You can create a script to add custom buttons to the tabs. This is useful for performing repeated tasks, such as changing your layer configuration or running a script. If you want each session to have the same custom values, you can make the creation of these values part of your startup macros.

For example, you can add a User button to the User group in the Home tab with the user\_btn command:

```
user_btn myFile {source myFile.tcl} -image myFile.png
```

This command creates the User button with the image in myFile.png , and when you click the button, the application uses the Tcl command source to run myFile.tcl .

Other ways to customize the GUI include:

- Adding a menu item that does not have a button on one of the tabs using the gui ribbon command . When you create a new menu item, including those you create with user\_btn , you can assign a shortcut key to it.
- Adding a context menu item to the cell view with the gui cellview menu add command. When you right-click your layout in the main window, you can select your item and run your script.

## Command Interface

The application supports the open source command set for the Tool Command Language (Tcl) to extend scripting capability to automate processes. The application supports Tcl version 8.5 as well as the patch version 8.5.12. These values are reported using the info tclversion and info patchlevel commands. The tcl\_precision variable is set to 12. The line continuation character (\) is not available when using the Command Pane ; however, it works for macros.

By using simple Tcl commands, complex scripts can be built and evaluated. For information about Tcl syntax, consult Tcl documentation or a website such as http:// www.tcl.tk/doc/.

The following topics describe the available Tcl features:

<!-- image -->

## Creating, Managing, and Running Macros

You can create complex scripts by recording commands from your session and editing the macro file. You can manage and run scripts using the Run window, which you can open from the View tab. Using the Run window, you can perform the following tasks:

- Run a script by browsing to its location if it is not included in the library.
- Organize your scripts library by adding script directories.
- Easily find, review, and execute your scripts.
- Access and run built-in scripts shipped with the application.
- Specify scripts to automatically run at application startup.

The following topics describe how to work with macro files and scripts:

## Creating and Editing Macro Files

You can create a macro file of your commands by using either the GUI or commands. You can also copy commands from your log file or copy commands from the command history in the Command Pane to create a macro file.

To create a macro file:

1. Start recording the macro file in one of the following ways:
- On the View tab, in the Macros group, click Record .
- Enter the macro record filename command on the command line, where filename is the file name for the recorded Tcl commands.

All of your actions are recorded to the macro file and the text box in the Command Pane appears yellow to indicate that the application is in macro-recording mode.

2. Perform operations or actions as required.
3. Stop recording the macro file in one of the following ways:
- On the View tab, in the Macros group, click Stop .
- Enter the macro stop command on the command line.

<!-- image -->

<!-- image -->

After you have created a macro file using commands, you should edit the file so that it will have the expected behavior. For example:

- Change background operations to foreground operations.

If you open a layout in background mode, then you cannot edit the layout before the loading is completed. Opening the layout in the foreground resolves this issue.

- Use Tcl variables to reference objects instead of constant strings.

For example, when you open a layout, the application returns an ID for that layout and the ID might change if you had opened the layout before you ran your macro file.

- Use the native Tcl update command to bring the application up-to-date by entering the event loop repeatedly until all pending events, including idle callbacks, are processed.
- Add a description for the script that will appear in the Description pane of the Run window when a script is selected. To add a description, place the text between a description block such as the following:

```
# ### Description # Place the description of your script here. ### Description #
```

## Managing and Running Macro Files and Built-in Scripts

The following topics describe how to manage and run macro files and scripts:

## Storing and Accessing Scripts

To add a scripts directory to the library:

1. On the View tab, in the Macros group, click Run .
2. In the Run window, click Add or right-click in the Locations pane and choose Add .
3. In the Add New Location dialog box, click to add a new location and provide a name (optional) for the location in the Name box.

If you do not provide a name for the location, then the last section of the path is considered as the name. For example, for the path /location/to/path/macros , the name of the location will be macros .

<!-- image -->

## 4. Click Add .

The folder is added as a location and all the script files ( .tcl , .mac , and .py ) in that folder are listed in the pane on the right.

The command for creating a script location is default framework\_scripts\_path .

5. In the Run window, click Save to save the changes for the following sessions.

## Note:

This will save all defaults, so changes made to other defaults will also be saved.

## To delete a location:

1. On the View tab, in the Macros group, choose Run .
2. In the Locations pane, right-click a location and choose Delete .
3. Click Save to save the changes for the following sessions.

## Note:

This will save all defaults, so changes made to other defaults will also be saved.

## Accessing Built-in Scripts

The application comes with built-in scripts that you can use. These scripts are available in the ICVWB\_INSTALL\_DIR/etc/fw/contrib folder that is easily accessible from the Run window.

To access stored macros or built-in scripts:

1. On the View tab, in the Macros group, click Run .
2. In the Locations pane, choose a folder.

The All folder lists all the scripts from all the folders. The contrib folder contains the built-in scripts that are sourced from the ICVWB\_INSTALL\_DIR/etc/fw/contrib folder.

You can search for a script by using the Search box. The search is limited to files in the chosen location. Click to perform a case-sensitive search.

<!-- image -->

You can do the following in the scripts pane:

- Click a script to view its description in the Description pane.

The brief description is extracted from the description block in the script.

- Double-click a script to open the script in the Tcl Debugger.

You can modify the script and save your changes here.

- Hover the pointer over a script to see its complete location path.

<!-- image -->

## Running Scripts Not Included in the Library

1. On the View tab, in the Macros group, click Run .
2. In the Run window, click Specify and run Tcl script and choose a script file (MAC, Tcl). 口
3. Click Open .

## Running Scripts From the Library

1. On the View tab, in the Macros group, click Run .
2. In the Run window, choose a folder or choose All from the Locations pane and select the script you want to run.

<!-- image -->

Press and hold the Ctrl key to select multiple scripts.

3. If the script you want to run requires input arguments, then enter them in the Input arguments box and click Apply .

For multiple selected scripts, the corresponding argument entered for each script is used. If you select multiple scripts, then enter the input arguments and click Apply , so that the same argument is applied to all the scripts.

<!-- image -->

4. Click the Run button that appears when you hover over a script to run the selected script or scripts.

## Running a Script on Startup

To add a script to run automatically during startup:

1. On the View tab, in the Macros group, click Run .
2. In the Run window, click a folder from the Locations pane and choose a script.
3. If the script you want to run requires input arguments, then enter them in the Input arguments box and click Apply .
4. Hover over the chosen script and click to add the selected script to startup.

The script and its arguments are added to the startup using the default framework\_addins command. You can add multiple scripts to the startup.

5. Click Save .

The script is added to the startup with the provided input arguments and is displayed at the top of the list with the icon. To remove a script to run on startup, click .

## Socket Communications

Because a command sent over a socket m uni a socket is evaluated in the Tcl interpreter, special Tcl syntax characters are interpreted normally. This means that if these characters exist in a normal string value, such as a cell name or text string, they need to be protected from interpretation by backslash substitution or enclosed by curly brackets {} . The special characters needing protection are the dollar sign $ (Tcl variable reference), square brackets [] (procedure invocation), and the open curly bracket { (syntax grouping; can only be protected by backslash substitution).

Results from the interpreter are defined as binary strings and require no protection. It does not perform end-of-line translations. By default, it uses standard buffering rather than line buffering.

<!-- image -->

<!-- image -->

These topics are available:

## Server Input

The client application sends the workbench server a complete script all at once. If the script is found incomplete using the Tcl/Tk command info complete , the workbench socket blocks awaiting further data to complete the script.

The calling application should manage all control flow logic and send basic user commands. However, it is supported and legal to send Tcl/Tk control code (such as if , for , while , and so on) as part of the script, just as in a standard macro command file.

## Server Output

Upon receiving a complete command on the input socket, it is evaluated on the command interpreter.

## Successful Result

On a successful result, the application returns the following data:

OK resultLength resultStr

Notice the structure of the return information; the string OK , followed by a space, followed by an ASCII integer value specifying the character length of the successful result, followed by a space, followed by the result (possibly binary) itself. The result is the command interpreter return string for the script.

## Error Result

On an error, the application returns the following data:

ERROR resultLength resultStr

This message follows the conventions previously described. The result is the command interpreter error string for the script. All script commands and their results are sent to the history and log following the same conventions as if the input had come from keyboard input into the command window.

## Exit

When the exit command is sent over the socket, the Tcl interpreter exits the application without returning any data over the socket.

## Running the Application in No Display Mode

When you invoke the application with the nodisplay m e -nodisplay argument, it is invoked without the GUI. You can save an image using the view save command with the -viewport and

<!-- image -->

<!-- image -->

-size options. The other view commands, including view active , view coords , and view zoom, are functional only when running in GUI mode. The Tcl history command is not supported in no display mode.

You can use the Tab key to autoc mple nds autocomplete supported commands (including default commands) or display a list of possible choices. The arguments and options for supported commands (including default commands) are not included in the autocomplete. For example, cell add p autocompletes to cell add path (without arguments), but cell add path -la does not autocomplete. In no display mode, the Tab key cycles through possible choices. For the source command, press the Tab key to autocomplete the file name or display a list of possible choices.

## Customizing the Environment

This chapter describes how you can customize your defaults and layout options.

The defaults specify preferences for global defaults and defaults for new layouts. Preferences for open layouts are described in Modifying Layout Options.

These topics are included in this chapter:

- Modifying Default Settings
- General Default Settings
- Layout Default Settings
- Modifying Layout Options
- User Modes

## Modifying Default Settings

You can modify the default application options through either the GUI or the command line.

To change application defaults using the GUI:

1. Click the Settings button ( ) on the far-right side of the ribbon and select Options from the drop-down menu. You can also click the lower-right launch button in the Tools group on the Home tab and select Options from the drop-down menu.

The Options dialog box opens.

2. Navigate the tree on the left to select a page.
3. Set the options.
4. Click OK .

The modified settings are applied to the current session.

To save the current configuration so it applies to future sessions, you can click Save in the Options dialog box. Your changes to the settings are saved in the HOME/.synopsys/icvwb (see Executing Startup Files). HOME on Windows is %UserProfile% .

<!-- image -->

<!-- image -->

You can reset the application configuration to the delivered installation defaults at any time by clicking Restore Defaults in the Options dialog box.

To modify default settings using the command line, refer to the default commands in the IC Validator WorkBench Command Manual . All of the default commands start with default .

## General Default Settings

The General page in the Options dialog box is used to set several GUI defaults.

Table 3 General default settings

| Option                                                | Description                                                                                                                                                                                    |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GUI Mode                                              | Controls whether the GUI opens in Ribbon or Menu mode.                                                                                                                                         |
| Autocomplete extensions                               | Controls whether the application adds an extension to a given file name if you have not provided one.                                                                                          |
| Autocomplete file path in the File Open/Save dialogs. | Controls whether to give file path continuation hints (if any) based on the letters typed in the Open File and Save As dialog boxes.                                                           |
| Ask to keep changes when exiting the application      | Controls whether a prompt should appear when exiting the application with unsaved changes made to the default settings.                                                                        |
| File history size                                     | Sets the number of files to display under the File menu.                                                                                                                                       |
| Title prefix                                          | Inserts a string at the beginning of the main window title.                                                                                                                                    |
| Focus on MDI Window on                                | Specifies whether the window focus is activated by clicking or hovering over the window with the mouse. You can set the minimum time for the mouse to hover over a window to change the focus. |
| Find                                                  | Specifies the outline color of the found object, the maximum number of items in the find list, and if found objects should be zoomed to when you navigate the list of found objects.           |
| Fonts                                                 | Controls the text font used in the Command Pane view (fixed-width font) and the other GUI features (default font).                                                                             |

Select History Colors in the options tree to set the display color for command text and error, warning, echo, and result messages in the Command Pane.

## Logging Settings

In the Logging page, you can control where to store the log files and turn logging on or off. To enable or disable logs, select the Turn on application log check box. This option can also be controlled from the command pane window by right-clicking on it and selecting Turn Log On or Turn Log Off from the context menu.

You can also set the Log directory where you want the log files to be stored. You can click the Manage button to view the details of the logs files and delete them if necessary.

## Note:

If the application was started with -log flag, then these settings have no effect. The log is saved in the file specified by the -log flag regardless of these settings.

## License Default Settings

Use these settings to control the license timeout. This setting provides capabilities to release the license if the application is in an idle state for a certain amount of time.

If the Never release the license check box is selected, the license timeout is set to 0, which means the timeout checking is off.

Deselect the check box and set the Timeout value to activate the license timeout. The allowed range is greater than or equal to 60 minutes.

If you select the Exit after timeout check box, the application exits if it has been idle for the specified timeout minutes.

## Note:

The license timeout feature is not available in the Windows environment.

## Layout Default Settings

You can set layout default opti nslay u e g settings by selecting Layout or any of its options from the tree.

From the Layout page, you can set the general defaults for the layout.

## Table 4 Layout default settings

| Option       | Description                                                                                                     |
|--------------|-----------------------------------------------------------------------------------------------------------------|
| Layout units | Set the layout units as Custom , DBU , angstrom , inch , meter , micrometer , mil , millimeter , or nanometer . |

<!-- image -->

Table 4 Layout default settings (Continued)

| Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Custom unit value         | For Custom layout units, specify the number of nm per custom value.                                                                                                                                                                                                                                                                                                                                              |
| Accuracy                  | Set the number of digits after the decimal point to appear in the GUI. The default is 4 for micron layout units.                                                                                                                                                                                                                                                                                                 |
| Visible Markups           | Specify which markups to display in various GUI elements. If you deselect a check box, the application does not show those entries in Options that occur on other pages and the button in the Tools group on the Edit tab to create those markups is not displayed. Also, the application does not show the folder in the Tree view if you turn on Show empty markup folders when no markups of that type exist. |
| Show empty markup folders | Select to show those markup folders that currently do not contain any objects. By default, the application does not display empty markup folders.                                                                                                                                                                                                                                                                |

The following layout default settings are available:

- Annotations
- Cache
- Compare
- Contour
- Display
- DP
- Edit
- File
- Flag
- Gauge
- Highlight
- Graphics
- Grid
- Layers

<!-- image -->

- Markup Names
- Model Image
- Mouse
- Net Tracing
- Overlay
- Ruler
- Select
- SEM Image
- Shape Info
- Side Cells
- Synchronize
- Text
- View

## Annotations

Select Annotations opti nsa l y u in the options tree under Layout to set specific font, color, and line width display defaults.

Table 5 Annotations default settings

| Option                        | Description                                                                                                             |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Text                          | Select the font, set the justification, and specify the text anchor location.                                           |
| Color, Pattern, and Linewidth | Specify standard coloring, select the fill pattern, and set the line width (line width must be a non-negative integer). |

## Cache

Select Cache opti nsca hel y u in the options tree under Layout to set caching defaults.

<!-- image -->

| Option                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Directory                     | Specify the directories to write and read cache files. Using the table, you can change, add, or delete cache file directories. If you are using cache files, then the application checks for existing cache files in the order of the directories. Cache files are written in the first writable directory. If you specify $layout for a directory, the cache file directory is the same as the layout's directory. When you open a symbolic link (shortcut) to a layout file, the cache is created in the same folder the link is pointing to. You can see your cache files in a directory and delete unwanted cache files by selecting Manage . Depending on the method you used for specifying the cache file directories, the application might list a cache file more than once.                                                                                 |
| Cache File Usage              | Select whether cache files are Read only or Read and write when you use them. If you select Read and write , you can also delete old versions of cache files when you open layout files using Delete old versions in the writable directory . Select None to turn off file caching. Note: If a cache file is available, opening a layout file is much faster. Cache files are not generated for layouts less than 10 MB in size. When loading a layout, the application creates a cache file with a temporary name and rename it when loading is complete. If you close the application before the layout is fully loaded, the application deletes this temporary cache file. Specify whether to maximize performance (such as browsing, probing, creating rulers, and so forth), but with higher memory usage by selecting Maximize performance (uses more memory) . |
| Automatic Deletion at Startup | By days : Select to delete cache files not used in the set amount of days. The default is to delete cache files that were not touched for the last 30 days. By disk space : Select to delete the oldest files if total disk space for cache files exceeds the specified space. The oldest cache files used are deleted first. The default is to delete cache files so that the total space is at most 100 GB Delete incompatible versions : Select to delete old cache file versions that this program cannot read. The default is not to delete incompatible versions.                                                                                                                                                                                                                                                                                               |

Table 6 Cache default settings

<!-- image -->

## Compare

Select Compare opti nsc m arel y u in the options tree under Layout to set the default layout compare and cell compare options.

Table 7 Compare default settings

| Option                        | Description                                                                                                                                                                                                         |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Properties for Layout/Cell.   | Choose whether to include the layout and cell properties when comparing two layouts or two cells.                                                                                                                   |
| Number of output differences  | Set the limit for the number of different objects reported in a Tcl-format output file when comparing layouts or cells. This option applies only to Tcl-format output files and does not affect other format files. |
| Canonical path ends           | Use this option to eliminate the ambiguity in some layout formats about the extension styles of paths and their accompanying extension lengths before layout or cell comparison.                                    |
| Canonical polygon coordinates | Select this option to enable shape coordinate order canonization when comparing layouts or cells.                                                                                                                   |
| Keep arrays                   | Use this option to control the expansion of array repetitions into individual objects (shapes or instances).                                                                                                        |
| Honor object property order   | Select this option to consider the order of object properties during layout or cell comparison.                                                                                                                     |

## Contour

Select Contour opti nsc urlay in the options tree under Layout to set contour defaults.

| Option                  | Description                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------|
| Show contours with fill | Specify whether you want your contours displayed with a fill pattern.                           |
| Color and Fill Pattern  | Specify the color, fill pattern, and line width for any new contours created from model images. |

Table 8 Contour default settings

<!-- image -->

## Display

Select opti nsd lay u Display in the options tree under Layout to set display and filter settings for newly opened layouts. For open layouts, select General from the options tree in the Layout Options dialog box (see General Option Settings).

| Option                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter (pixels)                  | Draw cells larger than : Specify the minimum cell size to display. This speeds up the display process as cell contents whose width or height is smaller than the specified pixel size are not rendered. The application draws filtered cells in their highest layer color. Default is 20. Draw markups larger than : Specify the minimum markup size that the application displays (speeds the display process). Default is 4 pixels.                                                                                   | Draw cells larger than : Specify the minimum cell size to display. This speeds up the display process as cell contents whose width or height is smaller than the specified pixel size are not rendered. The application draws filtered cells in their highest layer color. Default is 20. Draw markups larger than : Specify the minimum markup size that the application displays (speeds the display process). Default is 4 pixels. |
| Layout Order                     | Allows you to switch between the following layout order modes: Layer Order - Always renders layers in ascending layer:datatype order. Custom Layer Order - Renders layers in the order shown in the Layout Layers view. Color By Cell - Renders all instances of each cell in a different color. Layer Color OR - Renders overlapping layers with a blended color.                                                                                                                                                      | Allows you to switch between the following layout order modes: Layer Order - Always renders layers in ascending layer:datatype order. Custom Layer Order - Renders layers in the order shown in the Layout Layers view. Color By Cell - Renders all instances of each cell in a different color. Layer Color OR - Renders overlapping layers with a blended color.                                                                    |
| Dimming                          | Use the slider to control the percentage of dimming.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use the slider to control the percentage of dimming.                                                                                                                                                                                                                                                                                                                                                                                  |
| Brightness                       | Use the slider to control the percentage of brightness.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use the slider to control the percentage of brightness.                                                                                                                                                                                                                                                                                                                                                                               |
| Show detailed hierarchy controls | Sets the default GUI hierarchy control mode (Combined or Detailed) for displaying cell names and bounding boxes and filtering layers.                                                                                                                                                                                                                                                                                                                                                                                   | Sets the default GUI hierarchy control mode (Combined or Detailed) for displaying cell names and bounding boxes and filtering layers.                                                                                                                                                                                                                                                                                                 |
|                                  | Combined Control Mode (Default) • Show by Hierarchy Level This is the default mode. Select the options to which a common hierarchy level should be applied: Layers , Cell bounding boxes , and Cell names . Use the Min Level and Max Level boxes to specify a common hierarchy level. • Show cell names and bounding boxes Sets the default behavior for displaying cell names and bounding boxes. You can display cell names and bounding boxes for a specified range of levels, or only the highest level (default). | Detailed Control Mode • Select the Show detailed hierarchical controls check box to view the detailed control options. This mode allows you to specify separate hierarchy levels for Layers , Cell bounding boxes , and Cell names . These levels can be a single value, a range, or a list of ranges such as "1 3 5-12".                                                                                                             |

Table 9 Display default settings

<!-- image -->

Table 9 Display default settings (Continued)

| Option   | Description                                                                                                                                                                                                                                                                                                                                                           |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          | In both modes, by default only the cell bounding box option is selected, without displaying cell names or filtering hierarchy levels. Use the Show cell orientation check box to turn the cell orientation indicator on or off. Cell orientation indicators only apply to cells that have defined outlines. That is, the Cell bounding boxes option must be selected. |

## DP

Select DP opti nsd in the options tree under Layout to set parameters for the distributed processing (DP) mode defaults.

Table 10 DP default settings

| Option               | Description                                                                                                                      |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| OASIS, GDSII loading | Select this option to enable distributed processing system for OASIS and GDSII loading.                                          |
| OASIS saving         | Select this option to enable distributed processing system for OASIS saving.                                                     |
| Host filename        | Specify the host file for using during distributed processing. You can specify the file name or browse and select the host file. |

## Edit

Select Edit opti nsed lay u in the options tree under Layout to set parameters for editing your layout and for creating paths and text.

| Option                 | Description                                                                                       |
|------------------------|---------------------------------------------------------------------------------------------------|
| Shape constraint angle | Set the constraint angle for creating and editing shapes with the GUI. The default is 90-degrees. |

Table 11 Edit default settings

<!-- image -->

Table 11 Edit default settings (Continued)

| Option                  | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference flipping      | Specifies the default relative position when you change the orientation of a reference cell in the GUI. • Center : Orients the referenced cell relative to its current position (in-line). This is the default behavior. • Origin : Orients the referenced cell relative to its origin. Note: This applies only when changing the orientation of a selected reference in the GUI.                             |
| Path                    | Specify the settings for the path's type (default is Half extension), extension length for variable extension paths (default is 5 nm for both Begin and End), and width (default is 10 nm).                                                                                                                                                                                                                   |
| Snap to Shapes          | Select the check box to enable snapping when moving and editing shapes, or when adding highlights. • Radius : Specifies the distance (in pixels) from the target edge that the mouse pointer must fall within to snap to it. Default is 20 pixels. • Space : Specifies the space (in layout units) to track (in passive snapping mode) or keep between the edges or vertices when snapping. The default is 0. |
| Snap layout changes to  | Specify the DBU amount for which to snap layout changes for newly opened layouts. The default is 5. For open layouts, see Edit Option Settings.                                                                                                                                                                                                                                                               |
| Undo stack size         | Specify the undo stack size. The default is 100. Be aware that if you set the stack size to unlimited, the memory consumption can increase.                                                                                                                                                                                                                                                                   |
| Dog cursor              | Select the check box to turn the dog cursor on for editing. The dog cursor shows the point that is used for creating and editing shapes, text, and references using the GUI.                                                                                                                                                                                                                                  |
| Open cells in edit mode | Select the check box to open cells in edit mode by default.                                                                                                                                                                                                                                                                                                                                                   |

## File

Select opti nsf le ay u File in the options tree under Layout to set global behaviors associated with opening layout files.

| Option          | Description                                                           |
|-----------------|-----------------------------------------------------------------------|
| File Extensions | Specify default file extensions, including those for GDSII and OASIS. |

Table 12 File default settings

<!-- image -->

Table 12 File default settings (Continued)

| Option                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| New Layout Files                                | Specify the default DBU and user units for new layouts.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Interpret array references as single references | When this option is selected, all array references are treated as a set of single references that can be selected and edited individually. If unchecked (default), array references are preserved as is and can only be selected and edited as one single object.                                                                                                                                                                                                 |
| File Open Options                               | Select Improve performance to open layouts in a high capacity mode for faster rendering and response. Select Read instance properties to read instance properties before opening your layout file. Note: If you use cache files and a cache file is available for your layout, then the File Open Options used to create the cache file is used. If you would like to use your current settings, delete the old cache file before opening the layout (see Cache). |
| Maximum warnings reported                       | Specify the Maximum warnings reported to limit the number of reported warnings. You can specify a non-negative integer or all . Default is 5. Note that this property has no effect if you are reading a layout from the cache file.                                                                                                                                                                                                                              |

This option is available:

- OASIS

## OASIS

opti nsf le OASI ay u OASIS is an option under File in the options tree under Layout to specify OASIS file default settings.

| Option                  | Description                                                                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default coordinate size | Select the coordinate size of 32-bit or 64-bit for OASIS files.                                                                                                |
| Number of cores         | Define the maximum number of cores to use when opening OASIS files. The default is 8.                                                                          |
| Load LAYERNAME records  | Controls loading of layer names from OASIS files. When selected, the OASIS file layer names are loaded and it overwrites the preset layer names in the layout. |

Table 13 OASIS default settings

<!-- image -->

Table 13 OASIS default settings (Continued)

| Option   | Description                                                                                                                   |
|----------|-------------------------------------------------------------------------------------------------------------------------------|
| Saving   | Specify conditions for saving OASIS files: the amount of compression (default 6) and if compaction and modals should be used. |

## GDSII

GDS is an option under File in the options tree under Layout for specifying default settings for GDS files.

Table 14

| Option                   | Description                                                                                                                                                                         |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GDSII box elements       | Choose whether you want to load the GDSII box items as polygons or not load them at all.                                                                                            |
| Performance Optimization | Choose to perform faster rendering and search by converting GDSII to optimized OASIS. You can also specify if you do not want to generate the optimized OASIS if cache file exists. |

## LEF/DEF

opti nsLEF/D lay u LEF/DEF is an option under File in the options tree under Layout to specify the default settings when loading or saving LEF/DEF files.

Table 15 LEF/DEF default settings

| Option                                          | Description                                                                                                   |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Load only those layers defined in the layer map | Loads only layers defined in the layer map when opening LEF or DEF files. This option is selected by default. |
| Write VIA section                               | Saves additional VIA information to the LEF file when saving LEF files.                                       |

## Flag

Select Flag opti nsflag y u in the options tree under Layout to set the default flag color by clicking the flag color button and selecting the color from the pop-up window. You can change the display of flag comments in the Comment group box to not show the comments, show the comments with a mouse hover over the flag (default), or to always show the comments.

<!-- image -->

## Gauge

Select opti nsgau el y Gauge in the options tree under Layout to set gauge defaults.

Table 16 Gauge default settings

| Option                   | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Gauge Angle              | Select the gauge angle: angle - Snaps to the specified angle, perpendicular to the angle, as well as to angle+45 and its perpendicular. Default is 45. 90 - Snaps gauge created with the GUI to 90-degree angles. Perpendicular to edge - The gauge snaps perpendicular to an edge. This has a lower priority for snapping than to shapes, references, and contours. Any - Allows the gauge to be drawn at any angle. |
| Snap to all markups      | Select to snap the gauge line to the markup edge.                                                                                                                                                                                                                                                                                                                                                                     |
| One Click Gauge Creation | The options control how single-point gauges are created with the GUI. Extension - the extension past the shape edge. Centered - specifies if the gauge should be centered on the shape or at the click point.                                                                                                                                                                                                         |
| Edit grid size           | Specifies the grid size to snap new gauges created with the GUI for new layouts. For open layouts, see Edit Option Settings. The grid size should be a multiple of 1/16 nm for gauges that is used for Proteus lithography simulation.                                                                                                                                                                                |
| Show X,Y lines           | Select to show the x-axis and y-axis measurements of the gauge, along with the length.                                                                                                                                                                                                                                                                                                                                |
| Draw X,Y lines           | Select to render the x-axis and y-axis measurements when a gauge is drawn.                                                                                                                                                                                                                                                                                                                                            |

For specific information about gauges, see Working with Markups.

## Highlight

Select opti nsgau el y Highlight in the options tree under Layout to set highlight defaults.

| Option          | Description                           |
|-----------------|---------------------------------------|
| Highlight color | Specifies the color of the highlight. |

Table 17 Highlight default settings

<!-- image -->

Table 17 Highlight default settings (Continued)

| Option         | Description                                                                                |
|----------------|--------------------------------------------------------------------------------------------|
| Show X,Y lines | Select to show the x-axis and y-axis measurements of the highlight, along with the length. |
| Draw X,Y lines | Select to render the x-axis and y-axis measurements when a highlight is drawn.             |

## Graphics

Select opti nsgra h c l y u Graphics in the options tree under Layout to specify graphics settings for newly opened layouts. For open layouts, select Graphics from the options tree in the Layout Options dialog box (see Graphics Option Settings).

Table 18 Graphics default settings

| Option            | Description                                                                                                                                                                                                                                                                                                                      |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Crosshair Cursor  | Shows crosshair cursor.                                                                                                                                                                                                                                                                                                          |
| Cell reference    | Shows a marker at the origin of all cell references. If you display cell bounding boxes for hierarchy levels one or higher, the cell reference marks are only shown on those levels of the hierarchy with cell bounding boxes (see Display).                                                                                     |
| Markup names      | Show markup names within the main window. The options are: all - the names of all markups are drawn. The lengths of all rulers are displayed. selected - only names of selected markups are drawn. Only the lengths of selected rulers are displayed. none - no markup names are drawn. The lengths of all rulers are displayed. |
| Show Cell Names   | Select whether you want cell names displayed horizontal and constant in size, have the name to fit the cell's bounding box, or have the name fit the visible part of the cell's bounding box.                                                                                                                                    |
| Display of Shapes | Winding - Specifies how to display self-intersecting shapes in the cell view. A sample of how the application renders self-intersecting shapes is shown. Windpath - Specifies an additional option to display paths in the cell view. A sample of how the application renders the path is shown.                                 |

## Grid

Select Grid opti nsgr dlay u in the options tree under Layout to specify grid settings.

<!-- image -->

Table 19 Grid default settings

| Option         | Description                                                                                                                                                                          |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Show view axis | Turns the X-axis and Y-axis lines on or off.                                                                                                                                         |
| Show XY scale  | Turns the XY scale on or off.                                                                                                                                                        |
| Show grid      | Select this box to show the grid for newly opened layouts. For open layouts, use the Grid page in the Layout Options dialog box (see Grid Option Settings).                          |
| Grid Table     | Applies the shape and spacing of grid markers you specify for newly opened layouts. For open layouts, use the Grid page in the Layout Options dialog box (see Grid Option Settings). |

## Layers

Select opti nslayer u Layers in the options tree under Layout to specify settings for the Layout Layers view and the color scheme for new layouts.

| Option                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Layout Layers Format                   | Specify the format of the Layout Layers view. You can show the layer:datatype name, name, name (layer:datatype), or layer:datatype. The name (layer:datatype) is the default.                                                                                                                                                                                                                                                                     |
| Show Layers                            | Specify if all configured layers should be shown in the Layout Layers view or only layers that are in the layout.                                                                                                                                                                                                                                                                                                                                 |
| Show layer mark check boxes            | Specify if a check box is shown in the Layout Layers view for marking layers.                                                                                                                                                                                                                                                                                                                                                                     |
| Synchronize layers in all open layouts | Select if you want to synchronize the visibility, marking, and configurations of layout layers across all open layouts.                                                                                                                                                                                                                                                                                                                           |
| Layout color scheme                    | Select whether you want the layer color scheme to be dynamic or static for newly opened layouts. dynamic - the most vivid colors are assigned first, beginning with red for the first layer no matter what the layer number is. static - default layer colors are assigned for all layouts based on the layer number. The static mode trades on a color's contrast or differentiation for consistency on the list of layers and in the cell view. |

Table 20 Layers default settings

<!-- image -->

Table 20 Layers default settings (Continued)

| Option                      | Description                                                                                                                                                                                                                                                                                  |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default layer configuration | Specifies how layers are configured by default in a newly opened layout. If you choose Solid , solid alpha-blended fill patterns and solid 1-pixel-wide outlines with 60% transparency are used. If you choose Fill with pattern , layers are configured to be rendered using fill patterns. |

## Markup Names

Select opti nsmarku e l y Markup Names in the options tree under Layout to specify the naming conventions for creating gauges, highlights, rulers, and so on. The application replaces the # character with the ID.

When you specify a name for an object, use one or more ASCII characters; however, do not use the following: "'", \n, \r, \t, \v, \a, \b, \f, "\", "*", "?", "[", "]", "{", "}", and " ". Markup names cannot be the same as an ID (positive integers without leading "0"s are not allowed). The "/" character is used to define hierarchy for markups. The name cannot have "/" or "-" for the first character or "/" for last character.

Show markup names : Display markup names within the main window.

The options are:

- all - the names of all markups are drawn. The lengths of all rulers are displayed.
- selected - only names of selected markups are drawn. Only the lengths of selected rulers are displayed.
- none - no markup names are drawn. The lengths of all rulers are displayed.

## Model Image

Select opti nsm del ag y u Model Image in the options tree under Layout to specify settings for model images.

| Option                   | Description                                                    |
|--------------------------|----------------------------------------------------------------|
| Show color legend        | Show the color legend for all model images.                    |
| Model image transparency | Specify the transparency for model images. The default is 25%. |

Table 21 Model Image default settings

<!-- image -->

Table 21 Model Image default settings (Continued)

| Option                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Color Scheme            | The color scheme determines which signal values are set to the maximum and minimum color. For changing how signal values are set to the maximum and minimum color for existing model images see Model Image Properties. Dynamic - the full range of the signal-to-color mapping is used for new model images. This setting gives the greatest range of colors for a model image, but two model images with the same color may have different signal values. Static - the specified maximum and minimum bounds of the signal is used for new model images. New model images created with this setting has the same signal value for the same color, but does not give the greatest range of colors for the model images. |
| Signal-to-color mapping | Set the signal-to-color mapping for new model images. Specify at least two values. You cannot change the settings for existing model images. You can also adjust the transparency of the chosen color by using the slider provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Mouse

Select opti nsm u elay Mouse in the options tree under Layout to assign predefined actions or Tcl commands to the right and middle mouse buttons..

Table 22 Mouse default settings

| Option               | Description                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------------|
| Time: Click          | Set the time for a single click of the mouse in milliseconds. The default is 300.                    |
| Time: Double click   | Set the time for a double-click of the mouse in milliseconds. The default is 400.                    |
| Button Mapping Table | Specifies the predefined actions or Tcl commands associated with the middle and right mouse buttons. |

## Net Tracing

Select Net Tracing opti ns e   rac gl y u in the options tree under Layout to specify net tracing settings.

<!-- image -->

Table 23 Net Tracing default settings

| Option                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Color list                        | Specify the color list for the net tracing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Automatically open Task dock view | Select this check box to automatically open the Task View dockable window when a net trace task is performed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Preview net traced objects        | Select this option to enable intermediate updates to the cell view with the current trace results. The default update frequency is 3 seconds and can be changed using the seconds box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Limit to current view             | Select this check box to limit net tracing to the current view.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Limit traced objects              | Select from the drop-down menu or enter a limit for the number of objects found during net tracing. If the number of objects found exceeds this limit, net tracing stops. The default is unlimited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Layer Connectivity Tables         | Specify a list of the connectivity name and its layers for newly opened layouts. For layers, specify one or more layer:datatype or layer values. If you do not specify a datatype, the application treats all shapes on that layer as on the same connectivity layer. Layers are connected based on their order in the table. Additionally, you can specify cut layers to stop the tracing when it crosses cut poly. A cut-layers specification is a list of two lists of layer patterns. The first list of layer patterns describes the layers to cut, while the second list of layer patterns describes the layers to be cut by. Together this describes the cut layer on the connectivity layer. If you have an empty row between layers, those layers are not treated as being connected. For open layouts, use the Net Tracing page in the Layout Options dialog box (see Net Tracing Option Settings). |

## Overlay

Select opti ns verlay u Overlay in the options tree under Layout to specify overlay settings.

Table 24 Overlay default settings

| Option                       | Description                                                                                                                                                              |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mode                         | Set the overlay mode as AND, Mask, OR, or XOR for a new overlay.                                                                                                         |
| Find objects across overlays | Find objects across overlays. This is on by default. If you do not select this check box, the application does not find objects in any overlays you have in your layout. |

See Overlaying Cell Views for more information about overlays.

<!-- image -->

## Ruler

Select Ruler opti nsrule ay in the options tree under Layout to define ruler options available in the application. The defaults are only used when you create rulers using the GUI and not with the ruler add command. See Drawing a Ruler for detailed information about how to create a ruler using the GUI.

| Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ruler Angle               | Select the ruler angle: angle - Snaps to the specified angle, perpendicular to the angle, as well as to angle+45 and its perpendicular. Default is 45. 90 - Snaps rulers created with the GUI to 90-degree angles. Perpendicular to edge - The ruler snaps perpendicular to an edge. This has a lower priority for snapping than to shapes, references, and contours. Any - Allows the ruler to be drawn at any angle.                                                                                                                                    |
| Snap to                   | In the order of priority, options to snap your ruler are: Shapes - Use to snap the ruler to the closest shape's vertex, edge, or center point. Snapping to a vertex is a higher priority than snapping to an edge. References - Use to snap the ruler to shown cell bounding boxes. Markups - Use to snap the ruler to the closest markup. DBU - Use to snap the ruler to the layout DBU. This is useful when editing shapes in order to measure a distance to extend the shape in DBU units. For the case of an overlay, the application uses either the |
| Show X,Y Lines            | Use to display the X and Y measurements of the ruler line when drawing non-Manhattan lines. The status bar displays the delta-X, delta-Y, and distance measurements dynamically as you draw the ruler.                                                                                                                                                                                                                                                                                                                                                    |
| Draw X,Y Lines            | Select to render the x-axis and y-axis measurements (projections) when a ruler is drawn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Multiple measurement mode | Select to create a multiple-measurement ruler. The default is to create a single ruler (not selected).                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Snap radius               | Specify the radius for snapping the ruler. The snap radius is the distance (in pixels) from an object that a mouse click must fall within to snap to it. The application default is 8.                                                                                                                                                                                                                                                                                                                                                                    |

Table 25 Ruler default settings

<!-- image -->

## Select

Choose Select opti ns el c ay u in the options tree under Layout to set selection capabilities in the application.

Table 26 Select default settings

| Option             | Description                                                                                                                                                                                                                                                                                                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Markups            | Specify the markups you can select in your layout. Available markups include contours, flags, gauges, highlights, model images, points, rulers, SEM images, and stretches.                                                                                                                                                    |
| Shapes             | Specify the shapes you can select in your layout. These shapes include polygons, , and text.                                                                                                                                                                                                                                  |
| References         | Specify the references you can select in your layout. These references include all, single, or array references.                                                                                                                                                                                                              |
| Edit depth         | Specify how far down in the hierarchy edit-in-place selects shapes, text, and references.                                                                                                                                                                                                                                     |
| Mode               | Specify the mode to use for selecting objects. • Enclosed : Default mode. Selects all objects that are fully enclosed within the selected area. • Intersecting : Selects all objects that intersect with or are completely enclosed within the selected area. • Line : Selects all objects that intersect the selection line. |
| Selection emphasis | Specify to have the application highlight selectable objects when you are using the Select tool and move the pointer over objects. Additionally, select Brush value to be None , Normal , or Bright . You can also change the color, style, and width of the emphasis.                                                        |

See Selecting Objects for additional information about selection.

## SEM Image

Select SEM Image opti nsSEM  magel y u in the options tree under Layout to set defaults for manipulating SEM images with hotkeys and sets the transparency for all SEM images. For additional information about manipulating SEM images with hotkeys, see SEM Placement using Hotkeys.

| Option   | Description                                                               |
|----------|---------------------------------------------------------------------------|
| Move     | Set the value for fine (minor) and course (major) distance using hotkeys. |

Table 27 SEM Image default settings

<!-- image -->

Table 27 SEM Image default settings (Continued)

| Option       | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| Rotate       | Set the degree of fine (minor) or course (major) rotation using hotkeys.  |
| Scale        | Set the factor for fine (minor) and course (major) scaling using hotkeys. |
| Transparency | Set the value of SEM image transparency.                                  |

## Shape Info

Select Shape Info opti ns ha e f l y u in the options tree under Layout to specify the Shape Info tooltip settings such as Tooltip Display time and Tooltip transparency.

Table 28 Shape Info default settings

| Option       | Description                                                                                                                                           |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transparency | Set the transparency percentage for tooltips.                                                                                                         |
| Display Time | Set the tooltip display time in seconds. This is the amount of time in which the tooltip is displayed if you do not move your mouse or press any key. |

## Side Cells

Select Side Cells side c l opt n in the options tree under Layout to specify the default side cell settings such as the fill and outline colors, patterns, and other settings. The defaults can also be set using the default layout\_side\_cell\_options command.

| Option                           | Description                                                                                                                                              |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Automatically open the dock view | Select the check box to open the Side Cells dockable view when a new side cell is created. The check box is selected by default.                         |
| Brightness                       | Set the brightness of the side cell. Default is 60%.                                                                                                     |
| Tint color and Pattern           | Set the tint (fill) color and pattern of the side cell. Default tint color is No Fill and the transparency is set to 50%. The default pattern is empty . |

Table 29 Side Cells default settings

<!-- image -->

Table 29 Side Cells default settings (Continued)

| Option                               | Description                                                                                                                                                                                                    |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outline Tint Color, Style, and Width | Set the outline color, style and width of the side cell. The default outline color No Fill . The default outline style is solid and width is 1 pixel. The width must be a positive number in the range 1 to 5. |

## Synchronize

Select Synchronize opti ns y chr zela u in the options tree under Layout to configure which markups to synchronize or share between open cells. Markups include contours, flags, gauges, and rulers. Changing the synchronizing of markups only changes them for newly opened cells.

## Text

Select Text opti ns ex lay u in the options tree under Layout to specify text settings for newly opened layouts. For open layouts, use the Text page in the Layout Options dialog box (see Text Option Settings).

Table 30 Text default settings

| Option      | Description                                                                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Show        | Select those objects in the application you want shown. Options include: Layout text - Shows text. Text markers - Shows markers at text origins.                                         |
| Display     | Specify the text remains a Constant size and what the size is, or have the Text scale and to the magnification you specify. The application displays text in units of DBU.               |
| Orientation | Specify whether to display layout text horizontally always ( Always horizontal ), or to use information from the layout to compute text orientation ( Use information from the layout ). |

## View

Select View opti nsv ewlay u in the options tree under Layout to specify general view, synchronize, and zoom.

<!-- image -->

Table 31 View default settings

| Option                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Background color                             | Specify the background color of the cell view using the color picker.                                                                                                                                                                                                                                                                                                                                                                                                                |
| GUI flashpoint time                          | Specify the time that the application uses when showing a flashpoint in the cell view.                                                                                                                                                                                                                                                                                                                                                                                               |
| Interrupt Drawing On                         | Specify the conditions for interrupting drawings as any key or mouse click or Ctrl+I , Esc key , or any mouse click in the cell view .                                                                                                                                                                                                                                                                                                                                               |
| Pan delta                                    | Specify the percentage of movement across your cell view that is associated with the arrow keys.                                                                                                                                                                                                                                                                                                                                                                                     |
| Synchronize cell views                       | Select to synchronize cell views.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Show reference selection in Layout dock view | Select to highlight the corresponding cell node in Layouts dock view when a cell reference is selected in cell view.                                                                                                                                                                                                                                                                                                                                                                 |
| Zoom mode                                    | Specifies the mode in which the application zooms to a location as either halo (default), radius , or pan . With halo mode the application uses an extra percentage padding specified by the zoom halo; with radius , the application uses an extra distance specified by the zoom radius; and with pan the application recenters the view but does not change the zoom level in the cell view. These zoom mode settings are also available from the Find Information dockable view. |
| Zoom factor                                  | Sets the default scaling factor for the zoom-in and zoom-out functions. The zoom factor does not apply when zooming using a mouse drag because the zoom factor is relative to the size of the drag rectangle.                                                                                                                                                                                                                                                                        |
| Zoom halo                                    | Specifies the extra view padding distance to be added when zooming to a specific region of a layout. This is used in Zoom To and find operations (1-D and 2-D objects such as text, highlights, rulers, polygons, and so on).                                                                                                                                                                                                                                                        |
| Zoom radius                                  | Specifies the extra view padding to be added when zooming to a specific point of a layout. This parameter is always used for 0-D objects, such as point markups.                                                                                                                                                                                                                                                                                                                     |
| Zoom stroke                                  | Specifies the direction to zoom in using the mouse. The default is north-to-south.                                                                                                                                                                                                                                                                                                                                                                                                   |

## Modifying Layout Options

You can use the Layout Options dialog box to specify various layout display settings. To open this dialog box, click the lower-right launch button in the Hierarchy group on the Home tab and select Options from the drop-down menu. You can also click the Settings button ( ) on the far-right side of the ribbon and select Display Options from the dropdown menu. The following options that you specify in this dialog box apply to the active layout only:

<!-- image -->

<!-- image -->

<!-- image -->

- General Option Settings
- Edit Option Settings
- Graphics Option Settings
- Grid Option Settings
- Net Tracing Option Settings
- Text Option Settings

To configure settings for newly opened layouts, see Modifying Default Settings.

## General Option Settings

General options control display and filter settings for open layouts.

Table 32 General layout options settings

| Option          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hierarchy       | Show cell names and bounding boxes, and filter layers by their hierarchy based on the levels you specify. The levels can be a single value, a range, or a list of ranges such as " 1 3 5-12 ". Use the Show cell orientation check box to turn on or off the cell orientation indicator. Selecting this check box helps you identify the orientation of a cell in the cell view for the current layout by displaying an F symbol in the bounding box of the cell. The F symbol is oriented according to the cell's placement in its bounding box. For example, for a straight-placed cell, the F symbol appears at the top-left corner of the cell's bounding box and if a cell is rotated by 90-degrees, the F symbol appears at the bottom-left corner of the cell's bounding box. The cell orientation indicator applies only to cells with visible outlines as defined in BBoxes in the Hierarchy group on the Home tab. |
| Filter          | For Draw cells larger than specify the minimum cell size to display (this speeds the display process by not rendering cell contents smaller in width or height than the specified pixel size). The application draws filtered cells in their highest layer color. For Always draw markups larger than specify the minimum markup size that the application always displays (speeds the display process).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Show Cell Names | Select whether you want cell names displayed horizontal and constant in size, or size the name to fit the cell's bounding box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

Table 32 General layout options settings (Continued)

| Option      | Description                                                                                                                                                                                                                                                                                                                                                       |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Layer Order | Allows you to switch between the following layer order modes: Layer Order - Always renders layers in ascending layer:datatype order. Custom Layer Order - Renders layers in the order shown in the Layout Layers view. Color By Cell - Renders all instances of each cell in a different color. Layer Color OR - Renders overlapping layers with a blended color. |

## Edit Option Settings

Select Edit in the options tree to specify editing options for open layouts.

Table 33 Edit layout options settings

| Option                 | Description                                                                                           |
|------------------------|-------------------------------------------------------------------------------------------------------|
| Gauge grid size        | Specifies the grid size to snap new gauges created with the GUI. For newly opened layouts, see Gauge. |
| Snap layout changes to | Specifies the size of the edit grid in multiples of the DBU. For newly opened layouts, see Edit.      |
| DBU                    | Specifies the DBU of the layout. For new layout files, see File.                                      |

## Graphics Option Settings

Select Graphics in the options tree to set graphics options for open layouts.

| Option           | Description                                                                                                                                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Crosshair cursor | Shows crosshair cursor.                                                                                                                                                                                                                                       |
| Cell reference   | Shows a marker at the origin of all cell references. If you display cell bounding boxes for hierarchy levels one or higher, the cell references marks are only shown on those levels of the hierarchy with cell bounding boxes (see General Option Settings). |
| Layer            | Specifies how to mark layers: none , active , all , or user specified .                                                                                                                                                                                       |
| Show Cell Names  | Select whether you want cell names displayed horizontal and constant in size, or size the name to fit the cell's bounding box.                                                                                                                                |

Table 34 Graphics layout options setting

<!-- image -->

Table 34 Graphics layout options setting (Continued)

| Option            | Description                                                                                                                                                                                                                                                                                      |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Display of Shapes | Winding - Specifies how to display self-intersecting shapes in the cell view. A sample of how the application renders self-intersecting shapes is shown. Windpath - Specifies an additional option to display paths in the cell view. A sample of how the application renders the path is shown. |

## Grid Option Settings

Select Grid in the options tree to configure grid settings for open layouts.

Table 35 Grid layout options settings

| Option     | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| Show grid  | Select this box to show the grid for open layouts.                          |
| Grid Table | Applies the shape and spacing of grid markers you specify for open layouts. |

## Net Tracing Option Settings

Select Net Tracing in the options tree to set net tracing options for open layouts.

| Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Layer Connectivity Tables | Specify a list of the connectivity name and its layers for the open layouts. For layers, specify one or more layer:datatype or layer values. You can also browse for layers and filter layers in the Specify Layers for Connectivity window. If you do not specify a datatype, the application treats all shapes on that layer as on the same connectivity layer. Layers are connected based on their order in the table. Additionally, you can specify cut layers to stop the tracing when it crosses cut poly. A cut-layers specification is a list of two lists of layer patterns. The first list of layer patterns describes the layers to cut, while the second list of layer patterns describes the layers to be cut by. Together this describes the cut layer on the connectivity layer. |

Table 36 Net Tracing layout options settings

<!-- image -->

## Text Option Settings

Select Text to set text options for open layouts.

Table 37 Text layout options settings

| Option      | Description                                                                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Show        | Select those objects in the application you want shown. Options include: Layout text - Shows text. Text markers - Shows markers at text origins.                                         |
| Display     | Specify the text remains a Constant size and what the size is, or have the Text scale and to the magnification you specify. The application displays text in units of DBU.               |
| Orientation | Specify whether to display layout text horizontally always ( Always horizontal ), or to use information from the layout to compute text orientation ( Use information from the layout ). |

## User Modes

The application provides specialized user modes user mod , that are designed to better support groups of users with different needs. Additionally, this allows you to switch between modes dynamically without closing/opening the session.

You can choose the user mode in which you want to work from the User group on the Home tab, or set the ICVWB\_USER environment variable to one of the following before starting the application:

- ICVWB
- HERCULES
- ICV
- ICV64
- ICV\_PLM
- SENTAURUS

## Note:

ICV is the default mode of the application when no user mode has been selected or if the ICVWB\_USER environment variable has not been defined.

User modes are not available in the Windows environment.

<!-- image -->

## ICVWB

To invoke this user mod ICWBEV mode:

1. In the User group on the Home tab, click the Modes options button.
2. Choose ICVWB from the menu.

<!-- image -->

## HERCULES

To invoke this user mode:

1. In the User group on the Home tab, click the Modes options button.
2. Choose HERCULES from the menu.

This user mod H c l user mode performs these tasks:

- Create a button ( ) that allows you to set up the socket and launch the Hercules program vue .
- Creates a user button ( ) in the ICV group of the View tab to mark vertices. Click this button and then click a location on the layout. All of the vertices of shapes under the cursor are then marked with a point markup object. The cell hierarchy of the shapes is also an output in the command history in the Command Pane.

## ICV

The ICV mode enables you to run IC Validator tools such as ICV Launch and ICV VUE from IC Validator WorkBench and import technology files.

<!-- image -->

To invoke this user mode:

1. In the User group on the Home tab, click the Modes options button.
2. Choose ICV from the menu.

This user mode user mod ICV enables you to perform these tasks:

- TechFiles

<!-- image -->

Import the following in IC Validator WorkBench:

- CC/Virtuoso technology file: import layer names, configurations, and layout connectivity.
- ICC2 technology file: import layer names, configurations, and layout connectivity.
- Layer Map: import layer names.
- ICV Runset: import layer names.

See Loading TechFiles

- ICV\_VUE

<!-- image -->

Launch the IC Validator VUE application to review DRC results. See Loading and Viewing DRC Errors Using ICV VUE

- ICV Launch

<!-- image -->

Start ICV Launch in the DRC or LVS mode to initialize ICV check runs. See Running DRC, LVS, and PERC Using ICV Launch

## ICV64

To invoke this user mode:

1. In the User group on the Home tab, click the Modes options button.
2. Choose ICV64 from the menu.

This user mode user mod ICV64 performs these tasks:

<!-- image -->

- Creates a user button ( ) that sets up the socket and launch the IC Validator application icv64\_vue .
- Adds a TechFiles button ( ) from where you can import the following in ICVWB:
- CC/Virtuoso technology file: import layer names and configurations.
- ICC2 technology file: import layer names, configurations, and layer connectivity.

<!-- image -->

- Layer Map: import layer names.
- ICV Runset: import layer names.

See Loading TechFiles.

- Adds the ICV Launch button ( ), from where you can start ICV Launch in DRC or LVS mode to initialize ICV check runs. See Running DRC, LVS, and PERC Using ICV Launch.
- Creates a user button ( ) in the ICV group of the View tab to mark vertices. Click this button and then click a location on the layout. All of the vertices of shapes under the cursor are then marked with a point markup object. The cell hierarchy of the shapes is also an output in the command history in the Command Pane.

## ICV\_PLM

To invoke this user mode:

1. In the User group on the Home tab, click the Modes options button.
2. Choose ICV\_PLM from the menu.

This user mode performs these tasks:

- Creates a user button ( ) that sets up the socket and launch icv\_plm .

## SENTAURUS

To invoke this user mode:

1. In the User group on the Home tab, click the Modes options button.
2. Choose SENTAURUS from the menu.

This user mode user mod S nta performs these tasks:

- Changes the naming convention for highlights to SIM3D# .
- Changes the naming convention for gauges to SIM2D# .
- Changes the naming convention for points to SIM1D# .
- Enables the stretch markup.
- Loads the Sentaurus module. You can save information needed by the Sentaurus Process or the markup information by clicking the Export button in the Sentaurus group, which is to the right of the Mode button in the User group on the Home tab.

<!-- image -->

- Sets the layout unit for the GUI to nm.
- Sets default bop\_vertex\_max to 50.
- Allows highlights, stretches, and points to snap to the DBU when you draw them.

<!-- image -->

## 3

## Opening and Browsing Layouts

This chapter describes how to open layouts and cells, control how graphics are rendered, and browse layouts.

These topics are included in this chapter:

- Opening Layouts and Cells
- Opening LEF/DEF and Saving LEF Files
- Cache Files
- Reloading the Layout
- The Layouts View
- Browsing Cell Views
- Changing How Layers Are Displayed
- Saving and Reloading Layer Attributes
- Marking Layers
- Specify Which Levels of the Hierarchy To View
- Opening a Child Cell From the Cell View Context Menu
- Transforming Cell Views
- Overlaying Cell Views
- Saving Images of your Design
- Closing Layouts and Cells
- Closing Views
- Hiding Cells and Text

<!-- image -->

## Opening Layouts and Cells

To open a layout file:

- Select File &gt; Open .

The layout file opens in the background (see Displaying the Status Bar and Task View).

Once the layout is open, the root cell-if there is only one-will open and display. If there is more than one root cell, the Select Root Cell dialog box opens and you can select a root cell to open.

You can use the wildcards * or ? to help narrow the number of files listed in the Open File dialog box. If you type a portion of the file name or extension you are looking for along with the wildcard (for example, *.gds ) and press the Enter key, the application narrows the list of available files in the dialog box.

The application has auto-completion functionality to assist with opening a file. As you type the name in the File name entry, the application assists with file selection by autocompleting the file name. You can enter the directory from which to open the file using Look in: the drop-down list. Use the Enter key to move the cursor to the end of the text and open that directory. You can enter text for the file name from which to open a file in the File name entry. Click Enter to open the file that the autocomplete matches.

## Note:

For systems with slow or dead links, using the auto-completion functionality may result in poor performance.

When opening an illegal strict OASIS file, which is actually not-strict, ICVWB will error-out according to the OASIS specification requirements. If the default layout\_oasis\_strict is set to 1 (the default is 0), the application will display a warning and continue loading the OASIS file.

You can also open a layout with the layout open command. The command allows you to:

- Open the layout in foreground or background.
- Open and display a specific cell.
- Open and display the first root cell.
- If there is one root cell, open it. Otherwise, you can select a root cell to open from the Select Root Cell dialog box.
- Open the layout without opening any cells.

If you specify a layout that is already open, the application makes it active. For an active cell, the application creates a new view for it (if the view does not already exist). If there is

<!-- image -->

<!-- image -->

no active cell, the application opens the cell that was opened the first time you opened the layout and creates a view for it.

You can open additional cells by:

- Double-clicking a cell in the Layouts view (see The Layouts View). If the cell is already open, that cell will become active and its view will be shown in the main window.
- Clicking Open in the Cell group on the Home tab. The Open Cell dialog box opens where you can filter cells as you type in the Match field and then choose a cell to open. If you select the Regular expression check box, you can filter the cell list using regular expressions. If you select Case sensitive and type in the Match field, the cell list is filtered based on the case (uppercase or lowercase) of the cell name. See Figure 7.
- Selecting Root Cells from Open in the Cell group on the Home tab. The Select Root Cell dialog box opens where you can select the root cell to open using the same options that are available in the Open Cell dialog box.
- Entering the cell open command to open a specific cell.

Figure 7 The Open Cell dialog box

<!-- image -->

Limitations for GDS and OASIS files are described in Limitations of Layout Files. You can check if an OASIS file complies with the OASIS spec by running the oasis\_info command from the terminal (see OASIS Files Compliance Checking for more information).

## Opening GDS Layouts

When opening GDS layouts, IC Validator WorkBench creates an Optimized OASIS file and uses it as a new version of the cache file for data queries, thereby improving the performance.

Even if an old cache file exists, the Optimized OASIS cache is generated.

The following changes are applied to the loaded GDS file:

- The text magnification, rotation, and justification are ignored for text objects.
- Paths with rounded end-style are converted to polygons.
- Path objects with widths that are not even-numbered multiples of the database unit are converted to polygons (for example, a 3 nm wide path is converted to a polygon in a 1 nm DBU layout).

## Opening LEF/DEF and Saving LEF Files

To open a LEF file:

- Select File &gt; Open .

After the LEF file is opened, the root cell (if there is only one) will open and display. If there is more than one root cell, the Select Root Cell dialog box opens and you can select a root cell to open.

Layer specification is assigned automatically because LEF/DEF only contains records for layer names. To control the layer name and specification mapping, you can use the lefdef layer map command. For more information about this command, see the IC Validator WorkBench Workbench Command Manual .

When loading LEF/DEF files, only the layers defined in the layer map are loaded. You can change this by using the default lefdef\_load\_all\_layers command or by changing the setting in Options &gt; Layout &gt; File &gt; LEF/DEF . See LEF/DEF.

To import LEF/DEF:

1. Select File &gt; Import LEF/DEF

The Open LEF/DEF dialog box opens, which is shown in Figure 8, where you can browse for LEF files and optionally specify DEF files, layer map file, and object map file. You can import only one DEF but multiple LEF files at a time.

If you want to load all layers instead of only those defined in the layer map, deselect the Load only layers defined in the layer map option. If selected, the tool issues warnings for LEF layers that are not present in either the layer map file or the object map file and were not loaded.

<!-- image -->

<!-- image -->

Figure 8 Open LEF/DEF dialog box

<!-- image -->

2. If the LEF file is missing the UNIT section or you want to override it, you can select the DBU check box and choose a DBU value from the list.
3. Unselect the Load only layers defined in the layer map option, if you want to load all layers and not only the layers defined in the layer map.

## Note:

When you import a LEF/DEF file, the layer name and purpose will be joined with either a semicolon(:) or a dot(.), based on the default set by the layout\_layer\_datatype\_separator dot|colon command.

## Saving LEF Files

To save a LEF file:

1. Select File &gt; Save As .
2. In the Save As window, select the LEF tab.
3. If you need to save additional VIA information to the LEF file, select the Write VIA section check box.
4. Click Save As to save the file as a LEF (.lef) file.

When you open LEF files, additional information is available in the LEF that is not directly supported by IC Validator WorkBench. This information is stored as layout, cell, and shape properties in the LEF file and is required when saving and exporting the LEF file.

The following additional properties are stored in the LEF file:

- SNPS\_LEF\_VERSION, SNPS\_LEF\_SITE, SNPS\_LEF\_SITE\_CLASS, SNPS\_LEF\_SITE\_SYMMETRY, SNPS\_LEF\_SITE\_DIMENSIONS, and SNPS\_LEF\_USEMINSPACING are stored as layout properties.
- RESISTANCE is added to LEF and DEF Via cells as a cell property.
- SITE, CLASS, and SYMMETRY are added to LEF Macro cells as cell properties.
- PIN\_DIRECTION, PIN\_USE, and PIN\_PORT\_CLASS are added to all LEF Macro and Via cells, and DEF Via cells as cell properties.
- LAYER, PIN, PORT, and MASK are added to LEF pin shapes as shape properties.
- SPACING is added to OBS layer shapes as a shape property.
- All PINs have a text object containing the PIN's name added to the layout.

When saving to a LEF file (for example, OUT\_FILE\_NAME.lef ), an auxiliary macro file having the extension .lef.layerMap.tcl is saved in the same directory ( OUT\_FILE\_NAME.lef.layerMap.tcl ). This file contains layer mapping that can be used when loading the saved LEF file. See the lefdef layer map command for more information.

## Cache Files

By default, the application stores information about your layout on the hard drive in cache files. This allows the application to quickly display your layout with low virtual memory and much faster performance for each subsequent time you open the layout. If you normally only open a layout once, it is recommended that you turn cache files off.

## Note:

Cache files are not generated for layouts less than 10 MB in size.

You can control the behavior of caching in the Options dialog box (see Cache). You can change your settings by selecting Cache under Layout in the options tree.

From this dialog box, you can:

- Turn using cache files on or off. The default layout\_cache controls this setting. OASIS .gz files always create a zipped file on the hard drive ( *.sgz file extension). If you have cache files on , the *.sgz file is stored in your first writable cache file directory. If you have turned off using cache files, the *.sgz file is stored in your current working directory as an unlinked file. The file will not be listed in your directory and will be automatically deleted when you close the layout.

<!-- image -->

<!-- image -->

- Maximize performance by keeping more information from the cache files in memory. The default layout\_cache\_memory\_lock controls this setting.
- Select to use cache files in a read-only or read and write mode. For both modes, the application uses existing cache files. If the cache file is not available or is an old version and you are using the read and write mode, the application will create a new cache file. The default layout\_cache controls this setting. If the application creates a new cache file, you can choose to delete the old version. The default layout\_cache\_options with the delete\_old\_versions argument controls this behavior.
- You can control how the cache files are automatically deleted with your session on the Layout &gt; Cache &gt; Delete page, based on the number of days, total disk space for cache files, and deleting old cache file versions that cannot be read. These settings are controlled by the layout\_cache\_time and layout\_cache\_options defaults. You can update your settings and apply them without restarting the application using the Delete Now button or the layout cache delete command.
- You can specify where to store cache files on the Layout &gt; Cache &gt; Directory page. You can list any number of directories for cache files. This is useful if the cache files are shared between users. If you create a cache file, it will be written to the first directory which must be writable. The cache file can be stored in the same directory as the layout file if you specify $layout for the directory name. The Manage button allows you to see all of your cache files in a directory, their size, the last date they were touched, and delete unneeded files.

You can also create a cache file from the terminal window using the genCache program (see Creating Standalone Cache Files with genCache).

## Reloading the Layout

If your layout has changed on a hard drive outside of the application (by other processes), then you will be prompted to either reload the layout or close it to avoid negative results, such as the application terminating.

When the layout is reloaded, the layout specific settings such as transformations, overlay information, and markups will be preserved.

For GDS layouts, the Layouts dockable view displays changed layouts in italic type. You can continue to work with these layouts, ignoring the changes to the file, or you can reload them. To reload the layouts in the application, right-click a layout and click Reload or rightclick all the changed layouts and click Reload Selected .

<!-- image -->

## The Layouts View

The layout file and its open cells are shown in the Layouts and Tree View dockable views. Features in the Tree View, such as Find and Tear Offs, are also available in the Layouts view (see Tree View and Open Cells, Find Items, and Tear-Off View for more information). The Layouts view (shown in Figure 9) displays information about layouts and their cells and the cell hierarchy of your open layouts.

Figure 9 Layouts view with the cell hierarchy expanded

<!-- image -->

## The Layouts view:

- Lists all the open layouts. The file and its layout ID are shown. If you hover your pointer over a layout file, the full path to the file is displayed.
- Lists all of the open cells under each layout.
- Enables you to expand a cell to see its children. If the listed child cell is not defined, then it appears shaded and in italic type.
- If you double-click a cell, that cell is made active. If the cell is not open, it will be opened.

<!-- image -->

<!-- image -->

- If you right-click a layout or cell, a context menu is shown. From the context menu, you can:
- Select a cell to open.
- Display a folder in the Layouts view with all of the root cells.
- Rename a cell.
- Replace a cell with a different cell.
- Highlight, find, or zoom to a cell.
- Export a cell into a new layout.
- Create a new view of a cell.
- Close a cell or layout.
- Reload a changed layout.
- Recursively expand and collapse a node, including all child-nodes.

## Browsing Cell Views

Once you have opened your layout and cell, you can browse your cell shown in the main window. Browsing operations include:

Once you have opened your layout and cell, you can browse your cell shown in the main window. Browsing operations include:

- Browsing the Cell View with the Mouse
- Browsing the Cell View with the Middle Mouse Button
- Browsing While Using Other Tools-Toggle-to-Browse
- Zooming to Coordinates in the Cell View
- Zoom With the Mouse Wheel in the Cell View
- Using the Navigation View
- Other Browsing Methods

## Browsing the Cell View with the Mouse

You can browse your cell by clicking Browse in the Tools group on either the Home or Edit tabs. When Browse is the active tool, the pointer changes to a magnifying glass ( ).

<!-- image -->

## Using the pointer:

- Click to magnify the view by your zoom factor centered at your pointer location. You can change how much you zoom in from the Options dialog box by selecting the View option under Layout or by using the default zoom\_factor command.
- Control-click to zoom out by your zoom factor centered at your pointer location.
- Drag downward, or north-to-south, to zoom in the cell view, fitting the area defined by the drag's bounding box into the zoomed view. You can change the direction for zooming in on the Options dialog box by selecting the View option under Layout page or by changing default zoom\_stroke .
- Drag in the opposite direction, or south-to-north, to zoom out the cell view, fitting the current view area into the area defined by the drag's bounding box. When you drag the mouse, the "+" sign in the pointer changes to a "-" to indicate that you are zooming out.
- Push the center view hotkey C with your pointer over the location that you would like to center in the cell view.

## Browsing the Cell View with the Middle Mouse Button

In addition to using the Browse tool with the left mouse button, you can use the middle mouse button with any tool to browse your cell view.

## Using the middle mouse button:

- Click to center the view at your pointer location.
- Ctrl +click to zoom out by your zoom factor centered at your pointer location.
- Press Shift + the middle mouse button and drag to pan the view with any other tool.
- Drag downward to zoom in the cell view.
- Drag in the opposite direction to zoom out the cell view.

## Browsing While Using Other Tools-Toggle-to-Browse

You can use toggle-to-browse functionality to browse the layout when using another tool. The V hotkey works as an escape from the active tool to a temporary browse mode.

To use the toggle-to-browse hotkey:

1. Press the V key.

This temporarily escapes the current tool and puts you in browse mode.

2. Browse to the intended location.

<!-- image -->

## 3. Press the V key.

This returns you to the previous tool mode.

For example, if you are drawing a ruler that you want to extend past the current cell view, you can press the V key, scroll to the new location in the cell view, press the V key again, and continue drawing your ruler.

## Zooming to Coordinates in the Cell View

To zoom or pan to specific coordinates in the cell view, you can:

- Click the lower-right launch button in the View group on the Home tab to open the Go To dialog box (Figure 10).
- Enter coordinates directly into the Go To box in the View group on the Home tab.
- Enter coordinates directly into the Find box in the Find group on the Home tab
- Use the view , view at , and view pan commands.

In the Go To dialog box, you can enter coordinates and zoom to that location. If you enter only one X/Y coordinate, you can specify the height for the zoom or pan the view to the specified coordinate. The Go To dialog box can be used as follows:

- Enter four numbers (region coordinates) to zoom to a specific location.
- Enter two numbers (X,Y coordinate) to pan to a specific location.
- Enter three numbers (X,Y coordinate and a radius) to zoom to a specific point with the given radius.

You can also select a coordinate value from the history list in the drop-down menu. The application zooms or pans to that location when you click Apply or press Enter.

You can continue working in the application with the Go To dialog box open and paste coordinates from other applications. The application ignores parentheses and commas.

<!-- image -->

Figure 10 Go To dialog box

<!-- image -->

<!-- image -->

The application will zoom to the coordinates you enter in the Find text entry box in the Find group on the Home tab. For more information see Using the Find Field to Set Up a Find.

## Zoom With the Mouse Wheel in the Cell View

You can also spin the mouse wheel to zoom in and out along with any tool.

To use the mouse wheel:

1. Move the mouse cursor to a location of your interest.
2. Spin the mouse wheel up to zoom in and down to zoom out.

## Using the Navigation View

The Navigation view displays the fitted view of your active cell in a dockable view with a white rectangle showing where you are browsing (see Figure 11). You can zoom to a region in your active cell by dragging the pointer in the navigation view. You can refresh the Navigation view by right-clicking on it and selecting Refresh .

Figure 11 The Navigation view

<!-- image -->

## Other Browsing Methods

Other general browsing operations include:

- Increasing the magnification of the cell view-click Zoom In in the View group on the Home tab.
- Decreasing the magnification of the cell view-click Zoom Out in the View group on the Home tab.
- Fitting a design to the extent of the cell view-click Fit in the View group on the Home tab.
- Zooming to a selected object-click Selected in the View group on the Home tab.

You can also pan the display by:

- Pressing the arrow keys with the focus on the cell view OR
- Clicking the scroll bars

OR

- Clicking Pan in the Tools group on the Home tab.

The application stores the history of the most recent views. You can:

- Restore the preceding view by clicking Previous View in the View group on the Home tab.
- Display the next view in the history by clicking Next View in the View group on the Home tab.
- Refresh your view by clicking Refresh in the View group on the Home tab.

## Changing How Layers Are Displayed

You can change how layers are displayed from the Layout Layers view. If you overlay a cell from another layout on the active cell, the layers from the other layout will also be shown (see #unique\_150). The Layout Layers view also shows layers from all imported side cells (for additional information, see cell side\_cell import in the IC Validator WorkBench Command Manual ). Figure 12 shows an example of the Layout Layers view for a standard case and with an overlay.

<!-- image -->

Figure 12 Layout Layers for no overlays and with an overlay

<!-- image -->

You can modify how the Layout Layers view is shown (see #unique\_127) so that:

- The text in the left column shows the layer name only if it is available or if the layer:datatype is followed by the name.
- Only layers in the layout with shapes or text are shown instead of all layers configured layers. Showing only layers with shapes or text can greatly reduce the number of layers shown and the amount of scrolling needed.
- A layer mark check box (see #unique\_89) is shown in the right column to the left of the layer preview.
- The order of layers can be rearranged. The layers that you turn on and off can be grouped together. You can move layers by clicking the layer node, then dragging and dropping it where you want it placed.

<!-- image -->

To change the name of a layer:

1. Right-click the layer name.
2. Select Rename .
3. Enter a new name.

To change the layer attributes:

1. Double-click the layer preview. A panel opens allowing you to quickly change the fill and outline color and translucency, the pattern or stipple, and the outline style (see Figure 13). You can also embed the color and pattern panel in the Layout Layers view by selecting Show Patterns from the Layout Layers view context menu. Patterns with a black triangle in the upper-right corner have additional fill patterns that you can select if you right-click on the pattern.

Figure 13 Partial Layer Attributes dialog box for Layers and Cell Outlines

<!-- image -->

<!-- image -->

Partiall C:M++V toc dialoc

2. Click a color or fill pattern to apply changes to the layer configuration, or move the slider to adjust the transparency. To close the dialog box, click a color or fill-pattern or press the Esc key or click outside the dialog box.

## Layer Attributes

If you select More in the panel, the Layer Attributes dialog box opens allowing you to select additional colors and different fill and outline colors (see Table 38). To change layer attributes for multiple layers at once, select the layers in the Layout Layers view, rightclick, and choose Attributes from the context menu. The Layer Attributes dialog box opens allowing you to apply the same attributes to the selected layers. Similarly, you also move the transparency sliders and apply just the transparency settings to the selected layers.

<!-- image -->

<!-- image -->

Clicking More Colors will open a panel that contains the 216 web-safe colors. Doubleclick a color to dismiss the panel.

Figure 14 Layer Attributes dialog box

<!-- image -->

You can specify the transparency percentage using the slider that is underneath the pattern picker panel. You can also enter the #AARRGGBB color code in the edit boxes under the More Colors button.

Available fill patterns include those in Table 38, plus "empty" and "solid". You can also define custom fill patterns with the layout fill add and layout fill load commands. You can define custom line styles with the layout line add command.

<!-- image -->

The Render in reverse tone check box enables you to reverse the rendering of a layout. The reverse tone rendering of a layer shows its filled polygons as empty and the complement of the polygons as filled (see Figure 15 and Figure 16). To render a layer in reverse tone, select the check box and click Apply . You can also select multiple layers and apply this setting to all the selected layers.

Figure 15 Layer rendered in normal tone

<!-- image -->

Figure 16 Layer rendered in reverse tone

<!-- image -->

Table 38 Predefined patterns

<!-- image -->

Table 38 Predefined patterns (Continued)

<!-- image -->

## Saving and Reloading Layer Attributes

If you made changes to one or more layer attributes in a layout or to the cell outline layer, you can save these changes and use them in a future session.

To save your layer attributes:

1. In the Layout Layers window, click the Save button to open the Save Layers Configuration dialog box.
2. For new layouts, enter a file name and click Save . For existing layouts, you can use the suggested current layout name with the .mac extension or type a new name.

This saves your changes, including the cell outline layer configuration, to the file you specified.

<!-- image -->

<!-- image -->

You can apply the layer attributes that you saved to another layout or to all newly opened layouts. Apply the layer attributes to another opened layout by clicking Run in the Macros group on the View tab or by selecting File &gt; Open , and then select and run your macro file.

To load a layer configuration:

1. Click the load layers configuration button ( ) on the header panel of the Layout Layers view.
2. Select the configuration file (.mac) and click Open .

This loads your saved layer configuration including the cell outline layer configuration.

To apply the layer attributes to a specific layout that you do not have open:

1. Put the layer configuration file in the same directory as the layout file.
2. Rename the layer configuration file with the same name as your last layout with a " .mac " suffix.

For example, if your layout is my\_layout.gds , you should name the layer configuration file my\_layout.gds.mac . When the application loads your layout, it will also run the macro file.

To always use the layer attributes for all newly opened layouts:

- Run the macro file when there is no active layout.

A simple way to do this is to include the layer configuration file in your HOME/.synopsys/icvwb/icvwb\_start.mac script. HOME on Windows is %UserProfile% .

## Marking Layers

If you have two similar layouts, you can find the differences with a Boolean XOR. The differences could be slivers that are difficult to find at low magnification. You can see those layers more easily by marking those layers.

When you mark a layer, an X is drawn at the upper left of existing shapes and at the first point for new shapes (see Figure 17). The X is drawn at a constant pixel size so that the shape can be found at low magnification. If you mark layers with a large number of shapes, the rendering performance will degrade.

<!-- image -->

<!-- image -->

You can mark layers from the Layout Layers view context menu, the Layout Layers view using the layer mark check boxes (see Layers), or marking the active layer (see Graphics Option Settings).

To use the context menu to mark layers:

1. Select a layer or layers.
2. Right-click and select Mark (or Mark Selected if you select multiple layers) from the context menu.

By turning on and selecting the check boxes in the right column, you can mark a layer or layers. See Layers to turn on the layer mark check boxes.

## Specify Which Levels of the Hierarchy To View

For specifying the cell hierarchy level, cell outlines, and cell names, you can use either the combined or detailed hierarchy mode controls. The default is the combined mode. You can use the GUI to control these settings by using the Options dialog box (see Display) for new layouts or the Layout Options dialog box (see General Option Settings) for the current layout. You can also control these by selecting options on the Home and View tabs or the hierarchy control in the Status Bar.

Hierarchy Controls allow filtering of shapes, cell boundaries, and cell names by hierarchy levels. Additionally, text filtering by hierarchy levels controls can also be shown in the ribbon by clicking the icon and selecting Show text filtering controls . If shape filtering is enabled, text objects are first filtered by the shape hierarchy range and then only by text hierarchy filtering range (if enabled).

<!-- image -->

## Combined Mode

The combined mode combines the shape-level and reference-level controls. It has buttons to turn the display on or off for hierarchy levels, bounding boxes, and cell names. It also has two spin boxes to set the lowest (min) and highest (max) levels of the hierarchy to be displayed. The combined mode works as follows:

- Click the buttons to choose what you want to display and use the spin boxes to enter or set the min and max hierarchy levels. The cells, cell outlines, and cell names are displayed accordingly and as per the specified range.
- If the min level is increased beyond the current max level, the max level will automatically increase to match it. The same happens if the max level is decreased below the min level - the min level will decrease to match it.
- For cell names and bounding boxes, you can set whether to display them for all levels in the specified range or only for the highest level. You can do this by clicking Show cell names and bounding boxes in the Hierarchy group menu button and then choosing either All levels for the specified range or Only for the highest level . The default is to show cell names and bounding boxes only for the highest level.
- Click the Show text filtering controls to show text hierarchy filtering buttons in the ribbon. Text filtering range is independent on the shape and reference hierarchy range.

Figure 18 Hierarchy Control - Combined Mode

<!-- image -->

## Note:

- When in the combined mode and you use the layout display command (or run scripts) with the layer\_hier\_level , cell\_name\_hier\_level , cell\_outline\_hier\_level options, the application will switch to the detailed mode.
- When switching from the combined to detailed mode, certain values will be changed to match the detailed mode settings.

## Detailed Mode

Figure 19 Hierarchy Control - Detailed Mode

<!-- image -->

Click the Levels , BBoxes , or Names buttons to enable or disable hierarchical layer level display. You can specify the layers in the adjacent box. The application shows shape data, cell names, or cell bounding boxes for the specified levels of hierarchy. For example, if you set Layers to 3 and 5, the application shows shape data only for levels 3 and 5 of the hierarchy under the root cell. Click the Show text filtering controls to show text hierarchy filtering buttons in the ribbon.

The detailed mode has the following options on the Home and View tabs:

- Cell Outline : Toggle this on or off by checking the Cell Outline check box in the Layout group on the View tab. The cell outline layer is used to draw cell bounding boxes and cell names. By default, cell bounding boxes are used as cell outlines. See Setting a Custom Boundary Layer as the Cell Outline for information on how to set a custom boundary layer as a cell outline.
- Levels : Enable or disable this for layers in the layout by clicking Levels in the Hierarchy group on the Home tab. Specify the levels to display in the adjacent text entry box.
- BBoxes : Show or hide these by clicking BBoxes in the Hierarchy group on the Home tab. Specify the levels of cell bounding boxes to display in the adjacent text entry box.
- Cell Orientation Indicator : Turn this on or turn off by checking the Cell Orientation check box in the Layout group on the View tab. This helps identify a cell's orientation in the cell view for the current layout by displaying an 'F' symbol in the cell's bounding box. The 'F' symbol's orientation corresponds to the cell's placement in its bounding box. For instance, for a straight-placed cell, the 'F' symbol will appear at the top-left corner of the cell's bounding box. If a cell is rotated by 90-degrees, the 'F' symbol will appear at the bottom-left corner of the cell's bounding box. The cell orientation indicator applies only to cells with visible outlines as defined in BBoxes in the Hierarchy group on the Home tab.
- Names : Show or hide these by clicking Names in the Hierarchy group on the Home tab. Specify the levels of cell names to display in the adjacent text entry box.

<!-- image -->

## Note:

- When in the detailed mode and you use the layout display command with the hier\_levels option, the application will switch to the combined mode.
- The value of the hier\_levels option is updated to match the layer\_hier\_level option's value.

## Hotkeys For Controlling Hierarchy Levels

Hotkeys are available to quickly control the range of hierarchy levels of layers shown. The factory defaults for the hotkeys are described in Table 39. See Default Hotkeys for information about how to view your current hotkeys settings and modify them.

Table 39 Default hierarchy hotkeys

| Hotkey   | Result                                                                 |
|----------|------------------------------------------------------------------------|
| #        | Sets the maximum level to #, where # is [0-9], for example "1".        |
| Ctrl -#  | Sets the minimum level to #, where # is [0-9], for example " Ctrl +2". |
| *        | Sets the minimum level to 0 and the maximum level to 99.               |
| <        | Decreases the maximum level by 1.                                      |
| >        | Increases the maximum level by 1.                                      |
| Ctrl +<  | Decreases the minimum level by 1.                                      |
| Ctrl +>  | Increases the maximum level by 1.                                      |

When you change the range of levels using the hotkeys, the cell outline and cell bounding boxes levels update automatically. Cell names can be shown for the level of hierarchy below the deepest level shown for shapes. Cell bounding boxes can be shown for that level and the top cell.

## Switching Between Combined and Detailed Hierarchy Controls

To switch to the detailed mode, select the Show detailed hierarchy controls check box from the Options &gt; Layout &gt; Display settings page or from the hierarchy button menu in the Hierarchy group on the Home tab.

## Opening a Child Cell From the Cell View Context Menu

You can get the list of child cells at a certain point in your layout and open a child cell from that list.

<!-- image -->

1. Right-click on the preferred point in the layout
2. Select Open Child Cell . If there is only one child cell at the point, then you will see an Open Child Cell: cell\_name item in the context menu. Select it to open that cell.

Figure 20 Cell View Context Menu

<!-- image -->

If there are multiple child cells at the clicked point, the context menu will display the list of all cells available at the clicked point in hierarchical form.

If there are multiple references of the same cell at the clicked point, the context menu will only display a single instance of that cell name.

Figure 21 Cell View Context Menu, Multiple Child Cells

<!-- image -->

3. Click a cell from the list to open it.

By default, only the first 18 cells found in the first 300 milliseconds of the search are displayed in the context menu. This restriction is designed to prevent a lag in the context menu response time. You can use default cell\_open\_menu to control these settings. This default also enables you to control which cells you want to be displayed in the context menu. You can select to show the cell name only if the cell boundary is drawn or if the cell name is displayed in the Open Cells view. You can also control the indentation type to be used to display the cell hierarchy. Three spaces are used by default. For more information about default cell\_open\_menu , see the IC Validator WorkBench Command Manual .

<!-- image -->

## Transforming Cell Views

When you view a cell, sometimes it is useful to change the orientation or offset the view. You can transform your cell view by selecting Transform in the Cell group on the View tab (which opens the Transform dialog box shown in Figure 22) or by using the cell transform command.

When you transform a cell, you can change:

- The scale
- The X and Y offset
- The rotation and mirror, including standard orientations
- Whether the view will be re-centered with your transform

Figure 22 Transform dialog box

<!-- image -->

After you complete the transform, you can save or extract the layout with the transformation. See Saving Layouts or Exporting Layouts for steps on saving or exporting your layout.

<!-- image -->

## Standard Orientations Table

The following table maps the standard orientations to OpenAccess and DEF formats:

| Orientation          | LEF/DEF   | OpenAccess   | Virtuoso   |
|----------------------|-----------|--------------|------------|
| Angle: 0             | N         | R0           | R0         |
| Angle: 90            | W         | R90          | R90        |
| Angle: 180           | S         | R180         | R180       |
| Angle: 270           | E         | R270         | R270       |
| X-Mirror, Angle: 0   | FS        | MX           | MX         |
| X-Mirror, Angle: 90  | FW        | MX90         | MXR90      |
| X-Mirror, Angle: 180 | FN        | MY           | MY         |
| X-Mirror, Angle: 270 | FE        | MY90         | MYR90      |

## Overlaying Cell Views

To make a quick comparison of two or more cells or to see how the merge cells would look, you can perform a cell overlay. The cell overlay allows you to compare two images and is much faster than doing a Boolean XOR or merging the layout files. Unlike a Boolean XOR, the image-based overlay could miss small differences in rendering at low magnification and display cut lines in shapes as differences.

The different raster modes of overlays are:

- Mask - Overlays the image data blocking the previous image.
- OR - Overlays a pixel-based OR of the images.
- XOR - Overlays a pixel-based XOR of the images.
- AND - Overlays a pixel-based AND of the images.

You can probe shapes from an overlay and if you draw rulers, they will snap to shapes from an overlay. After placing your overlay, its shape information is available when using Shape Info functionality (see Shape Info Tooltip and the Information View).

<!-- image -->

These topics describe functions for overlaying cells:

- Using Drag to Set Up Overlays
- Using the Overlay Dialog Box to Set Up, Modify, and Delete Overlays
- Deleting Overlays From the Layout Layers View

## Using Drag to Set Up Overlays

You can drag a cell on the active cell. Likewise, you can drag a layout file to overlay it on the active layout.

1. Select the cell or layout file you want to overlay from the Tree View.
2. Drag that cell or layout file over to the targeted layout in the main window with your choice of raster mode. See Figure 23.
3. If you overlay a layout file with more than one cell open or used in an overlay, the Open Cells dialog box displays and you can select which cells you want to overlay.

Figure 23 Setting up an overlay by dragging and dropping a layout to a cell view

<!-- image -->

<!-- image -->

<!-- image -->

## Using the Overlay Dialog Box to Set Up, Modify, and Delete Overlays

You can manage overlays by clicking Overlay from the Cell group on the View tab. The Overlay dialog box opens, where you can:

- Add new overlays.
- Modify existing overlays, including the raster mode, cell, brightness, and layout.
- Change the order of overlays.
- Delete overlays.

## Deleting Overlays From the Layout Layers View

To delete an overlay from the Layout Layers view:

- Right-click an overlay name and select Delete Overlay as shown in Figure 24.

Figure 24 Delete Overlay Option

<!-- image -->

## Saving Images of your Design

You can save images of your design.

To save an image of your cell view in the PNG format:

1. Select Save Image in the Layout group on the View tab.
2. Specify your output filen ame and click Save .

You can save images in scripts using the view save command.

## Closing Layouts and Cells

You can close your active layout(s) by selecting File &gt; Close . You can also close the active and inactive layouts by selecting Close in the Layouts view context menu or by using the layout close command. When you close a layout, all overlays that refer to it are automatically deleted.

You can close cells by selecting Close Cell in the Layouts view context menu or by using the cell close command.

## Closing Views

You can close view windows by clicking Close or Close All in the Window group on the View tab or you can use the Windows page by selecting File &gt; Windows . You can also close views by using the view close command. When you close the view window, the layout and cell remain open.

In the Windows page, you can also do the following:

- Close all or only selected view windows (both active and inactive). To close a view, select the view window and click Close Selected or right-click the view and select Close window from the menu. You can press Ctrl and select multiple views or press Shift and select a range of views, and then click Close Selected or right-click and select Close windows to close the selected views.

To close all open view windows in the application, click Close All .

- Make a view active by right-clicking the view and selecting Active from the menu. The view which is currently active has a check mark against it. The Windows page also shows which views are editable or read-only.

## Hiding Cells and Text

You can hide and unhide cells or text from appearing in the layout. The hidden cells or text will not be visible in the cell view, in the find results, and other operation results. When opening a cell that has references to hidden cells, the references are hidden as well. Hidden cells or text are not lost when saving, merging, and extracting the layout. You can perform operations such as opening, renaming, and replacing hidden cells and also change their properties.

<!-- image -->

<!-- image -->

Hiding cells is a visual operation and the following operations are impacted when hiding cells and text:

- The find operation will not return hidden cell references or return any objects from the hidden cell.
- When probing cells, hidden cells and text will be skipped.
- You cannot select object from hidden cells.
- The Shape Info tooltip will not display information for hidden cells.

Hiding cells also impacts hierarchical views in the following ways:

- When a cell is hidden, it will be hidden from all cell views that have references to the hidden cell.
- References to hidden cells will be hidden through any hierarchy.

You can easily hide or unhide cells by using the GUI or by using commands. To hide a cell or cells from the layout:

- Right-click a cell in the Layouts , Probe , Open Cells , or Tree View dockable views or right-click a cell in the cell view and select Hide from the context menu.

To hide multiple cells, press Ctrl and select the cells you want to hide from the dockable view, and then right-click and select Hide Selected from the context menu.

The selected cells are hidden from the layout and displayed with a strikethrough in the Layouts , Probe , Open Cells , and Tree View dockable view.

<!-- image -->

The command for hiding cells is layout cell hide .

## To display hidden cells:

- Right-click a hidden cell (with a strikethrough) in the Layouts , Probe , Open Cells , or Tree View dockable views and clear the Hide check box from the context menu.

To display multiple hidden cells, press Ctrl and select the cells, and then right-click and select Show Selected from the context menu.

<!-- image -->

The selected cells are displayed in the layout and the strikethrough is removed in the Layouts , Probe , Open Cells , and Tree View dockable views.

The command for showing hidden cells is layout cell show .

For hiding text, see #unique\_86.

<!-- image -->

## 4

## Getting Information About a Layout

This chapter describes how to get information about your layout.

These topics are included in this chapter:

- Getting a Report on Your Layout File
- Finding Objects
- Getting information About Shapes and Cells
- Using tclcli to Get Information About Layouts Without Opening Them
- Clearing Annotations
- Net Tracing

## Getting a Report on Your Layout File

You can get a report layoutrep on your layout by selecting File &gt; Info &gt; Save Report . The Info window lists various attributes of the active layout. The data includes database units, number of cells, cell and array references, vertices, layout type, layout properties, cache files (if any) used, and so on.

From the Info window, you can save the report by clicking Save Report . You can use a script to save a report on the active layout using the layout report command.

## Note:

If a shape or reference is repeated N times, it contributes N to the corresponding object count. References and text do not contribute to the vertex count. Shapes contribute the number of vertices in an open boundary, that is, the boundary-closing vertex is not included. Path contributes the number of centerline vertices to the vertex count.

The report shows information relevant to the time when the layout was opened. To view an updated layout report following an editing session, you must close then re-open the edited layout file. If the layout file has just been created, no information is available.

<!-- image -->

## Info

<!-- image -->

|            | Layout                                     | soc_lib_nt.gds                                                                                                           |
|------------|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
|            | Path                                       | Desktop/icwb_demo                                                                                                        |
|            | Layouttype                                 | GDSIl/Optimized                                                                                                          |
|            | File size                                  | 135168bytes                                                                                                              |
| SaveReport | Lastmodified                               | Fri Dec1514:31:182017                                                                                                    |
|            | Databaseunit                               | 1e-09m                                                                                                                   |
|            | Userunit                                   | 1e-06m                                                                                                                   |
|            | Layercount(including alldatatypes)11       | Layercount(including alldatatypes)11                                                                                     |
|            | Loadtime                                   | elsp(0:0:0.05)user(0:0:0.08)sys(0:0:0.01)s                                                                               |
|            | Cells                                      |                                                                                                                          |
|            | Numberofcells                              | 24                                                                                                                       |
|            | Cellreferences                             | 750                                                                                                                      |
|            | Non-Manhattanreferencecount                | 0                                                                                                                        |
|            | Arrayreferences                            | 22                                                                                                                       |
|            | Empty cell count                           | 0                                                                                                                        |
|            | Undefinedcell count                        | 0                                                                                                                        |
|            | Shapes                                     |                                                                                                                          |
|            | Polygons                                   | 107                                                                                                                      |
|            | Rectangles                                 | 682                                                                                                                      |
|            | Trapezoids                                 | 0                                                                                                                        |
|            | Circles                                    |                                                                                                                          |
|            | Boxes                                      |                                                                                                                          |
|            | Paths                                      | 869                                                                                                                      |
|            |                                            | 0                                                                                                                        |
|            | Vertices                                   |                                                                                                                          |
|            | Round-endedpaths                           |                                                                                                                          |
|            | Oddwidthpaths                              | 0                                                                                                                        |
|            | File-LevelProperties                       |                                                                                                                          |
|            | OASIS_LIB_REVISION SYNOPSYS_SEG_FW LIBNAME | SynopsysOASISLibraryT-2022.03-SP1.1128994 versionT-2022.03-SP1(1142395)layout_server_versionT-2022.03-SP1 soc_lib_nt.gds |

## Finding Objects

You can find and zoom to shapes, cells, text, and coordinates in your cell. After specifying what to find you can navigate and review the found objects.

You can find objects in several ways:

## Finding Objects Using the Wizard

You can search for objects using the Find Set gs w zar Find Settings wizard.

<!-- image -->

To open the Find Settings wizard, click Find in the Find group on the Home tab or press Ctrl+F.

You can do the following using the Find Settings wizard:

<!-- image -->

## Find Cell References

To find cell references using the Find Settings wizard:

1. In the Select Type to Find page, choose Cell References and then select the type of reference you want to find:
- All : Finds every reference to a cell. If you have one 2x2 array reference and one single reference, the application will find 5 objects.
- Array : Finds only GDSII array references and OASIS array types of 1, 2, 3, 8, and 9. For one 2x2 array reference, the application will find one object.
- Single : Finds only GDSII structure references and OASIS array types of 4, 5, 6, 7, 10, and 11.
2. (Optional) Change the default Maximum number of items to find value from the list.
3. In the Select Cells to Find page, choose from the following options:

| Options   | Description                        |
|-----------|------------------------------------|
| All cells | Search in all cells in the layout. |

Table 40 Select Cells to Find options

<!-- image -->

<!-- image -->

Regular expression

| Options   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cell Name | Constrain the search to specific cells by entering the cell name. You can perform a case-insensitive search and use wildcards or regular expressions for searching cell names. ◦ Use " * ", " ? ", and " [...] " for a wildcard search. For example: ▪ To find all cells that start with STD_INV , enter STD_INV* as the wildcard expression or STD_INV.* for the regular expression. ▪ To find all cells from cell0 to cell999 , you would enter cell[0-9]{1,3} for the regular expression. ◦ To search for multiple cells, use a space-separated list of cell names. For example, cell1 cell[234] fillcell.* ◦ When searching multiple cells, the generated command uses the regular expression syntax. The -regexp option is automatically applied even though the Regular expression option is not selected from the GUI: find init -type ref -string (cell1&#124;cell\[234\]&#124;fillcell.*) -regexp The input cell names are treated as regular expressions. For example, if you have '*' or other related regexp characters in the cell names, they are treated accordingly. When you enable the Regular expression option in the GUI, then the provided input for Cell Name is treated as is. So, for multiple cell names, you should not use a space-separated list, but a correctly formatted regexp syntax. For example, to search for cells starting with N or M, enter either 'N.* M.*' in the Cell Name field without selecting the Regular expression option or 'N.*&#124;M.*' in the Cell Name and enable the Regular expression option. |

Select cells Constrain the search to specific cells by choosing the cells. In case of overlays, the Find Settings wizard groups all cells by the names of the layout to which they belong. By hovering over a name of a layout, you will see the full path of that layout in the tooltip.

<!-- image -->

4. In the Select Region and Hierarchical Depth for Find page, choose from the following options:

Table 41 Select Region and Hierarchical Depth options

| Option            | Description                                                                                                                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Everywhere        | Search for cells anywhere in the layout.                                                                                                                                                              |
| Current view only | Constrain the search to the current view only.                                                                                                                                                        |
| Vertex            | Constrain the search to the specified vertex coordinates.                                                                                                                                             |
| Region            | Constrain the search to a region by specifying the lower-left and upper-right X and Y coordinates. You can also click the Pick button and drag to define a region to limit the search in that region. |

Select the Hierarchy Levels check box to limit the search to the specified hierarchy levels. Choose Custom and enter a non-negative integer, a range of non-negative integers (for example 3-5), or a list of non-negative integers and ranges. Or choose All to search in all hierarchy depths.

5. In the Find by Property page, constrain the search to find object properties by name or by value using regular expressions and wildcards.
6. Click Finish .

## Find Shapes and Text

To find shapes using the Find Settings wizard:

1. In the Select Type to Find page, choose Shapes and Text and then select the Shapes check box.
2. Choose one of the following options:
- All : Finds all shape types.
- Custom : Select particular shape types to be searched: Circle , Path , Polygon , Rectangle , xTrapeziod , and yTrapeziod . You must select at least one shape
3. (Optional) Change the default Maximum number of items to find value from the list.
4. In the Select Layers to Find page, constrain your search by specifying the layers you want to find.

Use the check boxes to select the layers to be found and use the Filter box to filter the layers. You can also right-click the header or a specific layer and choose whether to

<!-- image -->

- include or exclude the layer, include or exclude all layers, include or exclude filtered layers, or include only visible layers in the search
5. In the Select Region and Hierarchical Depth page, choose the options as described in Table 41 .
6. In the Select Vertices, Area, and Edge Length for Find page, choose the following options:
- Vertices : To search for shapes based on the number of vertices, select the Vertices check box and enter the minimum and maximum number of vertices. For a single vertex element, enter the exact vertex count.
- Area : Select the Area check box and enter the minimum and maximum values for the area to be searched. If the area is a single element, then enter the exact area.
- Edge Length : To search for shapes based on their edge lengths, select the Edge Length check box and enter the length to be searched. You can enter a minimummaximum range or a positive number. Select the Report edges individually check box to list each edge of each shape individually in the search results.
7. In the Find by Property page, constrain the search to find object properties by name or by value using regular expressions and wildcards.
8. Click Finish .

To find text:

1. In the Select Type to Find page, choose Shapes and Text and then select the Text check box.
2. (Optional) Change the default Maximum number of items to find value from the list.
3. In the Select Text page, choose one of the following options:
- All text : Finds all text.
- String : Find text that matches a string while using wildcards and regular expressions.

Use " * ", " ? ", and " [...] " for a wildcard search. For example, to find all text that starts with Vcc , enter Vcc.* as the regular expression or Vcc* as the wildcard expression. You can find the characters 0-9 that occur exactly once with the regular expression [0-9]{1,1} or with the wildcard expression [0-9] .

<!-- image -->

To find a space-separated text string, for example, 'all text', enter all text in the String field. The following command is generated:

<!-- image -->

4. Set the search criteria for layers, region and hierarchy, and object properties as described in the earlier procedure for finding shapes.

## Find Coordinates From a File

When finding findco r ates g coordinates from a file, the file must be in one of these formats:

- A text file with each line in the file containing a vertex or region, such as " 50 50 " and " 200 300 400 600 ". Separate the numbers by one or more commas, spaces, or tab characters. Use nanometers as units.
- A coordinate ( .cld ) file
- An XML ( .xml ) file.
- A CSV ( .csv ) file (default).

The coordinate ( .cld ) file must be:

- Tab separated.
- The optional first line specifies the units. The default is μm.
- The next line must list all of the column names.
- The following lines list the data values. Based on the column names, the data is either vertex or bounding box in the file.

- For vertex, the column names "X" and "Y" are required.
- For a bounding box, the column names "X1", "Y1", "X2", and "Y2" are required. These will map to the "LLX", "LLY", "URX", and "URY" columns based on the data values.

The following is an example of a coordinate ( .cld ) file:

```
units=nm X1   Y1   X2   Y2   Design 8253 2345 8252 2600 aL-Bracket 5253 2345 3252 2600 bL-Bracket 1253 2345 1252 2600 dL-Bracket 0.253      2345 9252 2600 vL-Bracket
```

## Using the Find Field to Set Up a Find

You can set up a find and navigate your results using the Find f el Find text entry box in the Find group on the Home tab.

You can find the following items using the Find text entry box:

- Cell references-enter the name of the cell.
- Coordinates:
- Enter an X and Y coordinate to zoom to a vertex; for example, 350 500 .
- Enter two X and Y coordinates to zoom to a region; for example, 100 100 200 200 .
- Enter an X and Y coordinate, at , then a height to zoom to the center of the view to the X and Y coordinate with the specified height; for example, if you enter 150 150 at 100 and your view size is square, it is the same as entering 100 100 200 200 .
- In the coordinate entry field, you can copy and paste information from the output of other programs. For entered coordinates, a comma or a space can be used as a delimiter. Special characters, such as the open " ( " and close " ) " parentheses, are ignored.
- Shapes - enter a layer:datatype. The datatype is required.
- Text
- Use single quotation marks ( ' ) to perform a case-insensitive search for text.
- Use double quotation marks ( " ) to perform a case-sensitive search for text.

<!-- image -->

In addition to finding new objects using the Find text entry box, you can:

- Navigate the found results.
- Save the found results.
- As you navigate to results, they are highlighted. You can also pan to the new results by selecting the highlight and pan. When you highlight new results, the old annotations are automatically removed.

## Using the Find Information View to Review and Navigate Results

A summary of your find results is available in the Find Information viewsF nd I format dockable view. The Find Information view will be raised or shown if it is hidden. The Find Information view has a find toolbar on its header with the following options:

- A find field to help you start a new find. See #unique\_190.
- Navigation buttons (First, Previous, Next, and Last) to help you navigate the found results.
- A highlight/zoom mode toggle button. As you navigate the results, they are highlighted and the cell view is zoomed to the found object. You can control the zoom mode by choosing Halo , Pan , or Radius from the drop down menu of the button. Selecting Off only highlights the object without changing the view.
- A Save as button to save the found results. You can save your results in a tabseparated XML file (.xml), CSV file (.csv), or coordinate file (.cld). If you save the file as XML, you can use a spreadsheet program to read the saved file.
- Clear all annotations by clicking

<!-- image -->

Information of found objects includes the bounding box, hierarchy, type of object, the vertices, angle, mirroring, magnification, and properties. You can select one or more rows in the table to navigate between found objects. If you click the left-most cell in the header row (to the left of the Layer column header), you can highlight all found objects.

The right-click Select option is disabled in the Find Information view for objects that are not selectable, such as the following:

- Reference instances that are part of array references.
- Shapes from overlaid layouts.
- Objects that are not set as selectable using the default select\_types command.
- Objects on a hidden layer.

<!-- image -->

<!-- image -->

- Objects in the hierarchy deeper than set by the default edit\_depth command.
- Net trace side-cells or imported side-cells shown in the Find Information view.

Right-click the record of a found object and select Show in Layouts dockable to view the location of its instance path in the Layouts dockable window.

<!-- image -->

The following commands can be used to retrieve information from the findTable . See Conventions to Specify Table Sheets, Columns, Rows, and Cells in the IC Validator WorkBench WorkBench Command Manual :

- table cell modify
- table column get
- table row get

## Example

```
# open a layout # layout open tut2/chip200_twophase.gds STD_NOR2 #-> 1 # # find shapes # find init -type {shape} #-> 16 # # get the first column data from findTable (Note that the first data-column is the column 2) # table column get 1:1:2 #-> 1:0 1:0 1:0 1:0 2:0 2:0 2:0 3:0 3:0 3:0 3:0 3:0 3:0 3:0 3:0 3:0 # # get the first row data from findTable (Note that the column header is not a row, i.e. first data row is the row 1) # table row get 1:1:1 #-> Layer 1:0 {LL X (nm)} 0 {LL Y (nm)} 4500 {UR X (nm)} 1600 \ {UR Y (nm)} 4700 Hierarchy STD_NOR2 Type Polygon \ {Vertices (nm)} {(0 4500) (1600 4500) (1600 4700) (0 4700)}\ Properties {} #
```

<!-- image -->

```
# get findTable cell at the row 2, column 3 (Note, that data-column 3 is the column 4) # table cell modify 1:1:4:2 #-> 4700 # # load findTable row information into tcl array for easy access # the example below loads 5th row into obj5 tcl array # then accesses the "LL X (nm)" column and "Hiearchy" column # array set obj5 [table row get 1:1:5] echo $obj5(LL X \(nm\)) # 1600 echo $obj5(Hierarchy) # STD_NOR2
```

## Getting information About Shapes and Cells

You can get information about shapes and cells in your cell view, including:

- Hierarchy to a Shape Using Expand Layouts
- Information About Cell Reference Numbers
- Using Probe to Get Information About Shapes
- Shape Info Tooltip and the Information View

## Hierarchy to a Shape Using Expand Layouts

When you are debugging a layout issue, it can be useful to understand the hierarchy to a shape. To view the hiera c y to s p hierarchy to a shape:

1. Right-click the location in the cell view on which you want the hierarchy information.
2. Select Expand Layouts from the context menu.
3. The hierarchy information is displayed for your location in the Layouts dockable view.

The Layouts view is raised or shown if it is hidden (see Figure 25). The hierarchy path to the shape that you clicked on is expanded and bold.

<!-- image -->

Figure 25 Layouts view after selecting Expand Highlights from the context menu

<!-- image -->

## Information About Cell Reference Numbers

In the Description column of the Tree view for Cells , Open Cells , and Root Cells , you can see the number of times each cell has been referenced in the layout and in its parent cell (see Figure 26). This is given in the format Ref Count: total &lt;&gt;, parent &lt;&gt; . For example, for the cell a under Cells , the cell d has the description Ref Count: total 6, parent 1 . This means that cell d has been referenced 6 times totally in the whole layout and has been referenced once in its parent cell a .

Figure 26 Tree view - Cell Reference Numbers

<!-- image -->

## Using Probe to Get Information About Shapes

Probing a location in the GUI lists data for that location. The results of the probe are displayed in the Probe view and include information from visible side cells (see Figure 27).

<!-- image -->

Figure 27 Probe view

<!-- image -->

The cell hierarchy, including cell placement and attributes, and any shape and text information, is expanded. The Attributes folder for a cell contains information about mirror, rotation, and magnification when the cell is mirrored, rotated, or has a magnification other than 1. The shape and text information lists the type of object, layer, and vertex information for the object. Text objects also show the text string.

You can view the object coordinates and other attributes relative either to its parent cell or its absolute coordinates (coordinates relative to the current active cell). Click the Absolute button to switch on or switch off the absolute coordinates. By default, it is on.

To probe probe a l c ti n a location:

1. Right-click the location in the layout for which you want the probe information.
2. Select Probe from the context menu.

The location you selected is probed and the information is displayed in the Probe view. The Probe view will be raised or shown if it is hidden. The information is also available in the Probe folder for the active cell in the Tree view and Open Cells views.

After you have probed a location, you can use the context menu to access various options for the objects in that probe location. Depending on the item from the Probe view that you right-click, the context menu options include Tear Off , Find , Zoom , Highlight , View Cell , and Edit Cell . If you highlight a shape or cell reference, you can delete the outline by clicking the Clear Annotations ( ) button in the Find group on the Home tab.

<!-- image -->

## Note:

If your layout has changed on the hard drive, reload it prior to running a cell probe. You could experience negative results, such as the application terminating, if you do not reload the layout prior to running a probe.

## Shape Info Tooltip and the Information View

When you select Info from the Tools group on the Home tab, the tooltip to l ip functionality for shape information is enabled (see Figure 28). Tooltip information appears when the pointer hovers over a selectable object's edge or vertex in the cell view. The tooltip snaps to vertices within an 8-pixel range, making it easier to get vertex information. The hotkey for toggling the shape information tooltip on or off is Ctrl-D . When the tooltip is active, you can press Ctrl-C to copy content to the clipboard.

## Note:

The tooltip information is displayed only for objects that are selectable (the object type is set as selectable using the default select\_types command) and the hierarchy depth is editable (see the default edit\_depth command).

When the mouse pointer hovers over a point where there are multiple shapes, you can use the Tab key to cycle through the individual shapes and view the tooltip information. The order when cycling through the shapes is as follows: side cell shapes are first, then the shapes form the overlaid layouts, and then the shapes from the active layout. When the shape information is displayed for a shape from a side cell or an overlay, then you cannot select shapes from the active layout by using the Select tool.

You can also get shape information relative to any of the ancestor cells. When displaying shape info, you can cycle through all the ancestor cells relative to which you want to get the information by pressing Ctrl+Shift.

<!-- image -->

Figure 28 Shape Info tooltip and the Information view

<!-- image -->

The tooltip information always appears in the application's current mode (browse, select, ruler, highlight, and so on). The tooltip information also appears for overlays and side cells. When displaying tooltips for objects from a side cell or an overlay, the tooltip displays "Side Cell:" or "Overlay [OVERLAY\_ID]: OVERLAID\_LAYOUT" correspondingly. Tooltip information includes the type of object (such as a polygon or a cell), layer information (if it is a shape), whether it is a vertex or a segment (along with which one it is in the total number of vertices or segments), vertex or segment information in layout units, object attributes (such as path width, circle radius, reference rows/columns, and so on), hierarchy, and properties. Note that segment numbers start at 1. Displayed text is limited to the first 32 characters.

The application displays a yellow line in the main window to indicate the segment (for bright background colors, the line is drawn in black), vertex, or text bounding box. Additionally, the application displays a red rectangle on the cell bounding box so you can easily determine the extent of the cell in which the shape is located.

The tooltip information can also be displayed in the Information dockable view by selecting the Show Tool Tip Label on Layout check box. This view supplies information about specific polygons or segments in the information view, which you can then cut and paste into another application. The information view is not limited to 32 characters, as is the limitation in the tooltip.

<!-- image -->

<!-- image -->

You can use the shape info command to change the tooltip information content. You can change the formatting or apply some filtering mechanism to display only the information you need.

You can easily convert a Shape Info tooltip to a callout by pressing Alt+C while viewing the tooltip. You can use this to pin several Shape Info tooltips to a layout and compare the data. You can also move only the callout box while it is pinned to the same point by right-clicking the callout box and selecting Move Callout Text Box . To edit the data in the callout text box, right-click the callout and select Edit Callout .

Figure 29 Several Shape Info Tooltips (Callouts) Pinned to a Layout

<!-- image -->

## Using tclcli to Get Information About Layouts Without Opening Them

tclcli (Tcl command-line interface) is a command-line utility that you can use to quickly query a layout and get information such as the layout's dbu, cells, root cell, layers, and other details without opening the layout file.

## Syntax

```
tclcli command -files /path/to/files tclcli "command1; command2;..." -files /path/to/files
```

## Note:

```
You can provide a list of files (for example, -files /path/to/file1 /path/ to/file2 /path/to/file3 ) as well as use the shell pattern matching (for example, -files /path/to/dir/*.oas )
```

The following are some of the commands you can use to query layouts:

```
cell bbox -cell cell_name cell bbox -root cell layers -cell cell_name cell hierarchy cell properties layer bbox layer configure layer name layout cells layout child_to_parent layout dbu layout format layout layers layout properties layout report layout root cells shape boundary
```

You can also query multiple layouts at once and use a combination of commands to get specific details of the layouts.

The following are some examples of how you can use the tclcli command-line utility.

```
# get layout cells % tclcli layout cells -files /path/to/my_layout.oas /path/to/my_layout.oas cell1 cell2 cell3 # get layout layer names - note how asterisk is escaped % tclcli "layer configure \* -name" -files /path/to/my_layout.oas /path/to/my_layout.oas 0:0 layer_name1 1:0 layer_name2 # get layout dbu and layout format for layouts in a specified directory % tclcli "layout dbu; layout format" -files /path/to/dir/* /path/to/dir/my_layout.oas 1e-9 oasis /path/to/dir/my_layout.gds 2.5e-10 gds # get layout dbu for all gds files % tclcli layout dbu -files /path/to/dir/*.gds
```

<!-- image -->

```
/path/to/dir/my_layout_1.gds 1e-9 /path/to/dir/my_layout_2.gds 2.5e-10
```

## Clearing Annotations

You can clear clear n ot i s annotations in your active layout by clicking the Clear Annotations ( ) button in the Find group on the Home tab. Annotations can be text, lines, vertices, polygons, and rectangles.

## Net Tracing

Net tracing Net  racing is useful when checking whether or not shapes are connected, creating shorts, or opens.

## Connectivity Lists

Connectivity lists are groups of layers in the layout that are on the same electrical layer or are touching each other. You can define multiple connectivity lists to keep the connectivity of certain features separate from each other. You can set up the connectivity list on the Net Tracing page of the Layout Options dialog box (See Net Tracing Option Settings) or you can use the layout connectivity command.

<!-- image -->

<!-- image -->

You can edit the connectivity list name by clicking and delete the connectivity list by clicking . X

<!-- image -->

## To trace a net:

1. Define the connectivity lists for your layout.

When there is no connectivity defined, it is indicated by the mouse pointer .

<!-- image -->

2. Click Net Trace ( ) in the Tools group on the Edit tab.

<!-- image -->

<!-- image -->

<!-- image -->

## 3. Use the Net Trace Options group to do the following:

- Click the Stack drop-down button and select the connectivities that should be active during the net trace operation.
- Limit the number of objects traced during net trace by selecting or entering a limit in the Limit traced objects list.
- Enter a region (X/Y coordinates) in the Region text box or click the pick button and select a region in the cell view to limit the net trace to only the selected region.
- Select the Limit to current view check box to limit the search during net trace to the current view.
- Use the Name box to specify a new name for the new side cell, which will hold the flattened shapes connected to the selected shape. The side cell name should be unique within the layout and cannot be the same as any existing cell names.
4. Click a shape in your layout in the cell view.

<!-- image -->

<!-- image -->

## Note:

When you click within a layout to start tracing, the tool checks if there are shapes at that location that are included in the layout connectivity. And if no shapes are found, a message is displayed. Also, if the tracing region is limited and you try to select a trace startpoint outside of the region, a message displays.

<!-- image -->

<!-- image -->

<!-- image -->

If you click a location with multiple shapes, you can choose between the layers from the drop-down menu. Cut layers (when two layers are specified inside curly braces) are indicated as Cut Layer (connectivity name) .

<!-- image -->

The tool dims the layout and highlights the connectivity of the selected polygon and the net trace results are shown in the Side Cells view. You can expand the side cell to display their individual layers. You also can change the attributes for these layers individually and they can be shown, hidden, or marked independently.

Figure 30 Net Trace results in the Side Cells view

<!-- image -->

5. Similarly, click another polygon to draw a new net trace.

Another side cell is created and the previous net trace is no longer displayed. In the Side Cells view, you can select the tracing results you want to view by clicking the corresponding check box of the side cell.

Net tracing runs in the background without blocking the GUI. You can run multiple net tracing tasks at the same time. You can view the status or control running tasks in from the Task View dockable. The net trace side-cell and the cell view are updated periodically with new data as the net tracing progresses. The status bar displays the count of traced shapes, which is updated at regular intervals as the task progresses. When a net trace is in progress, the side cell displays a progress icon ( ), and when paused, it displays a pause icon ( ).

## Note:

The tool does not support simultaneous net tracing on the windows platform.

The Task View dockable automatically opens when a net trace task is performed and you can pause, stop, or resume the task from here.

<!-- image -->

<!-- image -->

<!-- image -->

## Note:

While the tracing is in progress, layout editing and the corresponding sidecell editing are not allowed.

When you right-click a highlight in the Tree View or Open Cells view, the Net Trace action is available from the context menu. When selected, the coordinates of the highlight are auto populated in the Region box of the Net Trace Options group.

<!-- image -->

## Point-to-Point Tracing

You can use the point-to-point tracing feature of the net trace tool to detect if there is a short or an open between any two shapes on your layout and trace the path between the two connected shapes.

To trace between two shapes on a layout:

1. Define the connectivity list as described in Step 1 of tracing a net. You can click the NetTrace arrow and select Connectivity from the drop-down menu to open the Net Tracing page in the Layout Options window.

When there is no connectivity defined, it is indicated by the mouse pointer

.

<!-- image -->

2. After setting up the connectivity list, click the NetTrace arrow and select point-to-point tracing ( ) from the drop-down menu.
3. Select the start shape and the end shape you want to trace on your layout. If the two shapes are on the same net, the short is highlighted (through a side cell) . The following example illustrates the point-to-point net tracing between two dockable view to dim the layout layers and adjust

and the Command Pane prints the message # Short: the two shapes are on the same net shapes. You can use the Side Cells the brightness of the traced path.

<!-- image -->

<!-- image -->

If the two shapes are not on the same net, the Command Pane prints the message # Open: the two shapes are on different nets.

## Adding Connectivity Breakpoints

When performing a net trace you can specify breakpoint layers to limit the tracing up to (or down to) some layer. This simplifies the debugging process by limiting the number of traced objects without losing the original connectivity.

You can set breakpoints from the Net Tracing page in the Layout Options window. Click the corresponding Br cell for the connectivities that you want to add breakpoints. A red marker is added to that connectivity indicating that tracing will not propagate to the shapes on breakpoint layers.

<!-- image -->

<!-- image -->

<!-- image -->

## Working with Markups

This chapter describes the markups in the application and how to create and use them.

These topics are included in this chapter:

- Overview of Available Markups
- Drawing Markups
- Markups View
- Loading Markups
- Selecting Markups
- Editing Markups

Full details of command usage are in the IC Validator WorkBench Command Manual . Defaults and options for open layouts are described in Customizing the Environment.

## Overview of Available Markups

The application provides the markups listed in Table 42.

| Markup      | Description                                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Contour     | A set of lines that defines an object, such as one exposure intensity.                                                                    |
| Flag        | A flag allows you to mark a certain location in your layout and annotate a comment to it. When you browse your cell, all flags are shown. |
| Gauge       | A gauge is a precise means by which to identify a 1-D layout region.                                                                      |
| Highlight   | A highlight is a bounding box that you can use to identify a 2-D layout region.                                                           |
| Model Image | A 2-D image with intensity at each pixel. Model images are commonly used to show the results of a lithography simulation.                 |

Table 42 Markups

<!-- image -->

Table 42 Markups (Continued)

| Markup     | Description                                                                                                                                                                                        |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Point      | Points help to identify 0-D regions in your layout. When you browse your layout, all points are shown.                                                                                             |
| Ruler      | Creating rulers on the layout allows you to measure the widths and distances of shapes.                                                                                                            |
| SEM        | A SEM image. Supported formats include *.jpg , *.jpeg , *.png , *.bmp , and *.tif .                                                                                                                |
| Stretch    | A stretch is a 1-D markup with a direction arrow. You typically use a stretch with the SENTAURUS user mode to indicate where to stretch extracted 1-D and 2-D layout regions in Sentaurus Process. |
| Protractor | The protractor tool is used to measure the angle between two edges of the same or different shapes.                                                                                                |

Depending on how you customize the application, not all tools and their GUIs are available (see Layout Default Settings).

## Drawing Markups

You cannot create contours and model images using a tool with this application. Other applications, such as the Proteus WorkBench application allow you to create those objects using tools. However, SEM images can be loaded.

To draw markups, select the appropriate tool, such as Flag , which is in the drop-down menu when you click the lower-right launch button in the Tools group on either the Home or Edit tabs. Press the Esc key to interrupt creating a markup. After you create a markup, it is listed in its folder in the Markups view (see Markups View).

All markups have a name and a unique ID. You can specify a naming convention for new markups (see Markup Names). IDs are global across your session; therefore, the serial numbering of flags, gauges, highlights, shapes, references, and so on, continues even after you make another layout active.

In addition to creating markups with the GUI, you can also use commands, such as flag add , gauge add , highlight add , and so on.

These topics describe the ways to draw specific markup objects in your layout:

- Drawing a Flag
- Drawing a Gauge

<!-- image -->

- Drawing a Highlight
- Drawing a Point
- Drawing a Ruler
- Measuring Angles with the Protractor
- Drawing a Callout
- Drawing a Stretch Object

## Drawing a Flag

To draw a flag:

1. Click the lower-right launch button in the Tools group on either the Home or Edit tabs.
2. Select Flag from the drop-down menu.

The Flag button appears to the left of the Info button and remains visible until you deselect it from the drop-down menu.

3. Click a point in the cell view.

The application inserts the flag.

4. In the Flag Edit Options group on the Edit menu, you can:
- Change the flag name in the Name text box.
- Enter a flag comment in the Comment text box. The information you enter in the text box appears whenever you hover your pointer over the flag. Comments are limited to printable ASCII character codes plus the space and tab characters.
- Select the desired flag color by clicking the Color drop-down menu. Setting the flag color is useful to easily recognize and categorize flags.
5. Click in the cell view to add the flag.

You can click the drop-down arrow for the Flag tool and do the following:

- Select Delete All Flags to delete all the flags drawn on the layout.
- Select Options to open the Flags options page.

<!-- image -->

## Moving a Flag

To move a flag:

1. On the Edit tab, click the Select tool and select a flag in the cell view.

The Flag Select Options group appears on the Edit tab.

2. Enter an offset (X/Y coordinates) in the Move text box or click the pick button and select an offset in the cell view.

## Drawing a Gauge

You can draw a gauge by selecting either two points or one point in the cell view. Figure 31 illustrates the different parts of a gauge.

<!-- image -->

Gauges drawn with the GUI snaps to the gauge grid (see Edit Option Settings).

These topics are available:

- Drawing a Gauge Using Two Points
- Drawing a Gauge with a Single Point
- Moving a Gauge
- Additional Options

## Drawing a Gauge Using Two Points

To draw a gauge using two points:

1. Click the lower-right launch button in the Tools group on either the Home or Edit tabs.
2. Select Gauge from the drop-down menu.

The Gauge button appears to the left of the Info button and remains visible until you deselect it from the drop-down menu.

3. Click a point in the cell view, drag, and release where you want the gauge's endpoint to be located.

<!-- image -->

<!-- image -->

By default, gauges drawn with the GUI snap to 45-degrees (see Gauge). When drawing a gauge, the mouse snaps to the vertices, edges, mid-points of edges, and to the center point of rectangles and circles. The snapping preview is indicated by a yellow line (for edges) or a small yellow rectangle (for vertices, edges, mid-points, and center points). You can disable snapping by clicking the button in the Gauge Edit Options group. You can temporarily enable or disable snapping by pressing Ctrl+Alt when drawing a gauge. *

<!-- image -->

<!-- image -->

<!-- image -->

The snapping radius is the distance (in pixels) from the target snap-point that the mouse pointer must fall within to snap to it. The application default is 20 pixels. You can change this from the Gauge Edit Options or from the Edit options in the Options window.

<!-- image -->

## Drawing a Gauge with a Single Point

To draw a gauge between shapes with one point:

1. Click the lower-right launch button in the Tools group on either the Home or Edit tabs.
2. Select Gauge from the drop-down menu.

The Gauge button appears to the left of the Info button and remains visible until you deselect it from the drop-down menu.

## 3. Place your pointer in the cell view and:

## ◦ Shift +click

The tool creates a horizontal gauge between the closest objects to the left and right of the click.

<!-- image -->

OR

## ◦ Ctrl + Shift +click

The tool places a vertical gauge between the closest objects above and below the click.

<!-- image -->

OR

## ◦ Ctrl +click

The tool places gauges between objects to the right and left, and above and below.

<!-- image -->

<!-- image -->

OR

- Double-click

The tool generates the shortest gauge between parallel edges of the closest objects to the double-click point. It places a gauge between the two closest objects that are not aligned to the X or Y axis.

<!-- image -->

You can control the extension of the gauge past the shape edge and center the gauge on the shapes in the Options dialog box. Click the Settings button ( ) on the far-right side of the ribbon or click the lower-right launch button in the Tools group on the Home or Edit tabs and then select Options from the drop-down menu. In the Options dialog box, select the Gauge option under Layout and adjust your settings (see Gauge).

## Moving a Gauge

To move a gauge:

1. On the Edit tab, click the Select tool and select a gauge in the cell view.

The Select Options group appears on the Edit tab.

2. Enter an offset (X/Y coordinates) in the Move text box or click the pick button and select an offset in the cell view.

<!-- image -->

You can also move the gauge by right-clicking the gauge and selecting Move from the context menu. Move the cursor and then click to place the gauge at that point.

<!-- image -->

## Additional Options

You can click the drop-down arrow for the Gauge tool and do the following:

- Select Delete All Gauges to delete all the gauges drawn on the layout.
- Select Options to open the Gauge options page.

## Drawing a Highlight

To draw a highlight:

1. Click Highlight in the Tools group on either the Home or Edit tabs.
2. Place your pointer in the cell view and do one the following:
- Drag the pointer to create a highlight with the first point as the corner.
- Click two points in the cell view.
- Press Ctrl and then drag the pointer to create a highlight where the clicked point is the center of the highlight.
- Press Ctrl+Shift and then drag the pointer to create a square highlight where the clicked point is the center of the highlight.
3. When drawing a highlight, you can do the following using the Highlight Edit Options group:
- Change the color of the highlight by selecting a color from the drop-down menu.
- Enable or disable snapping of highlights and set the snapping radius. By default, snapping of highlights is enabled and when drawing a highlight, it automatically snaps to the vertices, mid-points of edges, and to the center points of rectangles and circles. The snapping preview is indicated by a small yellow rectangle when snapping to vertices, mid-points of edges, and center points of rectangles. You can press Ctrl+Alt when drawing a highlight to temporarily enable of disable snapping.

The snap radius is the distance (in pixels) from the target snap-point that the mouse pointer must fall within to snap to it. The application default is 20 pixels. You can change this from the Highlight Edit Options or from the Edit options in the Options window.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

4. When selecting highlights, you can do the following using the in the Highlight Selection Options group:
- Change the color of the highlight by selecting a color from the drop-down menu.

You can also change the color by clicking the down arrow under Highlight and selecting a color from the color palette; click More to view additional color choices.

- Move the highlight by specifying an offset (X/Y coordinates) or by clicking and picking an offset in the cell view.

You can also move the highlight by right-clicking the highlight and selecting Move from the context menu. Move the cursor and then click to place the highlight at that point.

## Drawing a Point

To draw a point:

1. Click the lower-right launch button in the Tools group on either the Home or Edit tabs.
2. Select Point from the drop-down menu.

The Point button appears to the left of the Info button and remains visible until you deselect it from the drop-down menu.

3. Click in the cell view.

You can also click the drop-down arrow for the Point tool and do the following:

- Select Delete All Points to delete all the points drawn on the layout.
- Select Options to open the Markup Names options page.

## Drawing a Ruler

You can use the Ruler tool to draw a ruler. You can also create rulers using the right mouse button (right-click+drag and Ctrl +right-click). You can change the ruler settings by clicking the drop-down arrow under Ruler , which is in the Tools group on the Home tab, and then selecting Ruler Options from the drop-down menu (see Ruler).

Additional options are available with the Ruler tool. Click the arrow under Ruler to select options from the drop-down menu:

- Multi-measurement Ruler : switch between single and multiple measurement modes for rulers drawn using two points.
- Circular Ruler : create a circular ruler.
- Delete All Rulers : delete all rulers in your cell

If your cell view shows an overlay from another cell, the ruler can snap to shapes in the overlaid cell. If shapes from different layouts are within the snap radius, shapes from the active layout take precedence. See Overlaying Cell Views for information about overlaying cells.

These topics are available:

- Drawing a Ruler Using Two Points
- Drawing a Ruler with a Single Point
- Drawing a Circular Ruler
- Moving a Ruler
- Converting a Ruler into a Gauge

## Drawing a Ruler Using Two Points

To draw a ruler using two points:

1. Click Ruler in the Tools group on either the Home or Edit tabs.
2. Place your pointer in the cell view and:
- Click, drag, and release where you want to place your ruler.

OR

- Click two points in the cell view.

OR

- Use a right-click+drag action to create a ruler with the right mouse button.

<!-- image -->

## Ruler Snapping

When drawing a ruler, the GUI previews the snapping start point and snaps the points to objects based on your snapping options (see Ruler). The tool snaps to shape vertices with a higher precedence than shape edges. When drawing a ruler, the mouse snaps to the vertices, edges, mid-points of edges and paths, center point and center lines of rectangles, and to the center of circles. The snapping preview is indicated by a yellow line (for edges) or a small yellow rectangle (for vertices, edges, mid-points, and center points). You can turn off snapping to objects by pressing the Shift key when you start or complete a drag operation. The ruler angle between the first and second point is constrained based on your ruler angle options.

Figure 32 Snapping to the center point and center line of a rectangle

0.9489910um

## Horizontal and Vertical Projections

When drawing a ruler you can preview the x-axis and y-axis projections and choose to have them rendered after the ruler is drawn. In the Ruler options, select the Show X,Y lines option to preview the horizontal and vertical projections (see Figure 33). To have these projections rendered, select the Draw X,Y lines option (see Figure 34). The rendered projections appear as dashed lines.

Figure 33 Ruler with Show X,Y lines enabled

<!-- image -->

0.4100000um A single ruler will be created unless the multiple measurement mode is selected. In multiple-measurement mode, measurement points are added at intersections with all shapes (rectangle, polygon, path, circle) and visible cell bounding boxes (see Figure 35).

<!-- image -->

<!-- image -->

<!-- image -->

Figure 34 Single and multiple-measurement ruler with Draw X,Y lines enabled

<!-- image -->

<!-- image -->

Figure 35 Single (top) and multiple measurement (bottom) rulers

<!-- image -->

## Drawing a Ruler with a Single Point

Additionally, you can draw a ruler between shapes, contour, and visible cell bounding boxes with one point when you have the Ruler tool selected or using the right mouse button.

To draw a ruler using a single point:

1. Click Ruler in the Tools group on either the Home or Edit tabs.
2. Place your pointer in the cell view and:
- Shift+click

The tool creates a horizontal ruler between the closest objects to the left and right of the click.

OR

- Ctrl+Shift+click

<!-- image -->

The tool places a vertical ruler between the closest objects above and below the click.

OR

- Ctrl+click

The tool places rulers between objects to the right and left, and above and below.

OR

- Double-click

The tool generates the shortest ruler between parallel edges of the closest objects to the double-click point. It places a ruler between the two closest objects that are not aligned to the X or Y axis. This is useful for measuring the distance between shapes at any angle, including polygonal and curvilinear shapes.

<!-- image -->

Single point rulers snap to shape edges even if you have deselected snapping to edges, if the tool cannot snap to any other objects.

## Drawing a Circular Ruler

To draw a circular ruler:

1. Select the Circular Ruler option from the Ruler drop-down menu.
2. Click in the cell view to specify a center point of the ruler.
3. Drag to specify the radius and then click to draw the ruler.

## Moving a Ruler

To move a ruler:

1. On the Edit tab, click the Select tool and select a ruler in the cell view.

The Select Options group appears on the Edit tab.

<!-- image -->

2. Enter an offset (X/Y coordinates) in the Move text box or click the pick button and select an offset in the cell view.

You can also move the ruler by right-clicking the ruler and selecting Move from the context menu. Move the cursor and then click to place the ruler at that point.

## Converting a Ruler into a Gauge

You can easily create a gauge from a ruler by right-clicking a ruler and selecting Create Gauge from Ruler . You can also create a gauge from a multi-measurement ruler. For each segment of the multi-measurement ruler, a separate gauge is added.

## Measuring Angles with the Protractor

You can use the Protractor tool to measure the angle between two edges. You can also draw a three point protractor of the required angle. You can use the Protractor tool by selecting it from the Tools section in the Edit tab and perform one of the following actions:

- Measuring the angle at the shape corner : When you hover the pointer over a corner of a polygon, the adjacent edges and vertex are highlighted. Double-clicking the corner adds a protractor at that location, that displays the angle between the highlighted edges.
- Measuring the angle between any two edges : When you hover the pointer over an edge, the edge is highlighted. Click to select the first edge. Next, hover over a different edge and click to select it as the second edge. The selected edges can belong to different shapes. After you select the second edge, a protractor appears and displays the angle between the two selected edges.
- Measuring the angle formed by three points : Click three separate points to define the angle. After you click the third point, a protractor appears and displays the angle formed by these three points.

## Drawing a Callout

To draw a callout:

1. Click the lower-right launch button in the Tools group on either the Home or Edit tabs.
2. Select Callout from the drop-down menu.

The Callout button appears to the left of the Info button and will remain visible until you deselect it from the drop-down menu.

<!-- image -->

3. Place your pointer in the cell view and click, drag, and release where you want to place your callout markup.

You will see a cursor inside the callout markup where you can then enter text for your callout.

## Note:

You can instantly convert a shape info tool tip to a callout by pressing Alt+C when viewing the tooltip.

The Callout Options group on the Edit tab contains options that you can use to configure your callout such as text size and color, outline width and color, fill color, width of the line from the callout, and whether or not there is an arrow at the end of that line. If you want to change any of these attributes later, you can use the Select tool to select the callout and the Callout Options group opens and you can make your changes.

## Moving a Callout

To move a callout:

1. Right-click the selected callout(s) and select Move , or double-click the callout.
2. Move the mouse pointer and click to place the callout.

To move only the callout text while keeping the callout pointer unchanged, right-click the selected callout(s) and select Move Callout Text Box .

## Editing a Callout

You can edit the properties of a callout such as its name, text, line color, text color, coordinates, and so on from the Object Attributes dockable window.

You can also edit the callout text by right-clicking the callout and selecting Edit Callout .

## Drawing a Stretch Object

A stretch is a 1-D markup with a direction arrow. You typically use a stretch with the SENTAURUS user mode to indicate where to stretch extracted 1-D and 2-D layout regions in Sentaurus Process.

## Note:

Ensure that you have selected the Stretch check box in the Visible Markups section on the Layout page in the Options dialog box before you begin drawing your stretch object. (See Layout Default Settings).

## To draw a stretch object:

1. Click Stretch in the Tools group on either the Home or Edit tabs.
2. Place your pointer in the cell view and:
- Click, drag, and release where you want to place your stretch object.

OR

- Click two points in the cell view.

Stretches are constrained to be horizontal or vertical.

## Markups View

The Markups view displays information about the markups in the active cell (see Figure 36). If you show empty markup folders, all the markup folders are always shown (see Layout Default Settings). Otherwise, folders are only shown if your active cell has those markups. The Markups view is based on the Tree view (see Tree View and Open Cells). You can find items, create a tear off, and edit items similar to the Tree View.

Figure 36 Markups view

<!-- image -->

## These topics are covered:

- General Markups Behavior
- Contours
- Model Images
- SEM Images

<!-- image -->

## General Markups Behavior

These topics are covered:

- Markup Names and Hierarchy
- Saving Markups
- Showing and Hiding Markups
- Zoom To
- Deleting Markups
- Properties

## Markup Names and Hierarchy

The name and ID of each markup are listed in the left column in the Markups view. You can change the name by double-clicking the editable field (light blue) and entering a new name.

You can group the markups into subfolders:

- Change the markup name to start with the subfolder name, such as a/renamed .
- Drag a markup into an existing folder. You can create new markup folders with the gui markup folder make command.

When you specify a name for an object, use one or more ASCII characters except for one of the following: "'", \n, \r, \t, \v, \a, \b, \f, "\", "*", "?", "[", "]", "{", "}", and " ". Markup names cannot be the same as an ID (positive integers without leading "0"s are not allowed). The "/" character is used to define hierarchy for markups. The name cannot have "/" or "-" for the first character or "/" for last character.

## Saving Markups

To save markups using the Markups view:

1. Right-click one or more markups or a markup folder.
2. Select Save or Save Selected (if you selected more than one markup) from the context menu.

The Save File dialog box for the type of markup you want to save opens.

3. Enter a file name for your markup and click Save .

<!-- image -->

<!-- image -->

4. To save all markups for your cell, select the folder in the Markups view and then select Save All from the context menu.

Only one type of markup can be saved at a time.

## Showing and Hiding Markups

To show or hide markups in the Markups view:

1. Right-click one or more markups or a markup folder in the Markups view.
2. Select Show or Show All from the context menu.

Hidden markups names are shown in italics .

## Zoom To

To zoom to markups:

1. Right-click one or more markups, or a markup folder.
2. Select Zoom To from the context menu.
3. You can also double-click a markup or a markup folder to zoom in on the markup.

## Deleting Markups

To delete markups:

1. Right-click one or more markups, or a markup folder.
2. Select Delete from the context menu.
3. You can delete all markups by right-clicking on the Object header in the Markups view and selecting Delete All .

## Properties

Markup properties are shown in the right column or in subfolders for each markup.

To change attributes, including coordinates:

1. Double-click the editable field.
2. Enter a new value.

## Contours

These topics are covered:

- Contour Properties
- Converting Contours to Polygons
- Naming Restrictions
- Saving Contours

## Contour Properties

A contour markup from the Markups view is shown in Figure 37.

Figure 37 Contour markup in the Markups view

<!-- image -->

From the contour folder you can:

- Change the contour color and fill by double-clicking the contour's color box in the right column.
- See the conditions used to generate the contour including the layout file, cell, and parameters. The parameters shown for your contour depends on how your contour was created, such as created from a model image or simulated in Proteus WorkBench.

## Converting Contours to Polygons

You can convert generated contours to polygons only when the cell is editable (see Making Cells Editable and Read-Only for details about putting a cell in an editable state).

<!-- image -->

To convert one or more contours to polygons:

1. Select one or more contours, or folders of contours, right-click and select Convert to Polygon .
2. Use the Convert to Polygon dialog box to specify your output layout, cell, and layer, and which contours to convert (see Figure 38).

Figure 38 Convert to Polygon dialog box

<!-- image -->

The application has limitations on converting contours to polygons. The limitations include holes in contours are filled in.

## Naming Restrictions

In addition to the naming restrictions for general markups (see Markup Names and Hierarchy), contours cannot have a plus (+) or a minus (-) character as the first character in their name.

## Saving Contours

To save one or several contours to polygons:

1. Select one or more contours or folders of contours.
2. Right-click and select Save or Save All .

<!-- image -->

<!-- image -->

3. Use the Convert Save dialog box to specify your output layout, cell, and layer, and which contours to convert (see Figure 39).

Figure 39 Contour Save All dialog box

<!-- image -->

## Note:

The application has limitations on saving contours as a GDS or OASIS layout. The limitations include holes in contours are filled in for both GDS and OASIS, and contours with more than 8191 vertices cannot be saved as GDS.

## Model Images

These topics are covered:

- Model Image Properties
- Saving a Model Image

## Model Image Properties

A model image markup from the Markups view is shown in Figure 40.

Figure 40 Model images markup in the Markups view

<!-- image -->

From the model image you can:

- Change the signal range for the contour image intensity.
- See the conditions used to generate the model image including the layout file, cell, and other parameters. The parameters shown for your model image depends on how your model image was created.

## Saving a Model Image

You can save your model image as an image file or in the xml format by selecting Save from the context menu of one or more model images or the model image folder. You can only store one image in an image format. Supported formats are bmp , jpeg , jpg , png , ppm , xbm , and xpm . One or more model images can be stored in the xml format. The application uses .txt as the file extension for xml model images.

## SEM Images

These topics are covered:

- Loading a SEM Image
- SEM Image Properties
- Changing the Placement of SEM Images
- SEM Alignment Dialog Box

<!-- image -->

- SEM Placement using Hotkeys
- Saving and Loading a SEM Image Placement
- Highlighting SEM Images

You can control whether SEM images are opaque or semi-transparent (see SEM Image).

## Loading a SEM Image

SEM image file formats include *.jpg , *.jpeg , *.png , *.bmp , *.tif , and *.tiff . You can load SEM images using File &gt; Open , or the Load context menu item for a folder of SEM images or the Object header for the Markups view. Placement information is not available in SEM images and so they are fitted to the extent of the cell view.

## SEM Image Properties

A SEM image from the Markups view is shown in Figure 41.

Figure 41 SEM images markup in the Markups view

<!-- image -->

From the SEM image you can:

- Change the name, position, rotation, mirroring, and size of the SEM image.
- Lock or unlock the aspect ratio of the SEM image.

## Changing the Placement of SEM Images

You can change the placement of you SEM image in a number of ways:

- By changing the SEM image properties or issuing commands, such as sem width .
- Using the SEM Alignment Dialog Box from the context menu of a SEM image.
- With hotkeys (see SEM Placement using Hotkeys).
- Using the mouse to edit a SEM image in the cell view (see Editing Markups).

<!-- image -->

## SEM Alignment Dialog Box

The SEM Alignment dialog box can be used to quickly align SEM images to your layout or contours.

To show the SEM alignment dialog box:

- Right-click a SEM image and select Alignment from the context menu.

Or in the Markups view, right-click a SEM image and select Alignment .

The dialog is non-modal which allows you to browse your layout and select a different SEM image without closing the dialog (see Figure 42).

Using the SEM Alignment dialog you can:

- Move, scale, and rotate the SEM image by a specified amount.
- Mirror the SEM image around the X- or Y-axis.
- Change the opacity of all SEM images.

<!-- image -->

Figure 42 SEM alignment dialog box

<!-- image -->

## SEM Placement using Hotkeys

You can change the placement of your SEM image using hotkeys. The hotkeys are listed in the Hotkeys section in the Options dialog box on the Hotkeys &gt; Layout hotkeys page with the values set on the Layout &gt; SEM Image page.

Using the hotkeys you can:

- Move your SEM image in one of eight directions-down, left, left and down, left and up, right, right and down, right and up, and up.
- Rotate your image to the left (counter clockwise) or to the right (clockwise).
- Increase or decrease the size of your SEM image.
- Move, rotate, or change the size of your image by a course (major) or fine (minor) amount.

## Saving and Loading a SEM Image Placement

To save the placement of your SEM images:

- Select Save from the context menu of SEM images and folders of SEM images in the Markups view.

This allows you to load and place the SEM image in the same location, magnification, mirror, and rotation in a new session.

## Highlighting SEM Images

To create a highlight around SEM images:

- Select Highlight from the context menu for SEM images and folders of SEM images in the Markups view.

## Loading Markups

You can load markups by:

- Selecting File &gt; Open and then selecting the Files of Type for your markup file.
- Clicking Run in the Macros group on the View tab to run markup files stored as macros, such as rulers and SEM images.
- In the Markups view, selecting Load from the context menu of the markup's folder.
- In the Markups view, selecting Load from the context menu of the Object column header.

<!-- image -->

## Selecting Markups

You can select markups from the cell view by clicking Select in the Tools group on either the Home or Edit tabs. See Table 43 for information about how to perform different selection operations using the mouse.

Table 43 Different selection operations using the mouse

| Selection Operation                | Description                                                                                                                                                                                                                                                                     |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select one object                  | Ctrl +click to select an object under your pointer. This action deselects any selected objects                                                                                                                                                                                  |
| Select objects in an area          | Use drag to select everything contained in the drag's bounding box. This is useful when you want to select numerous objects in a certain area and clicking each object to select it is inefficient. This action deselects any selected objects outside the drag's bounding box. |
| Toggle a selected object           | Use Ctrl +click to toggle your selection. The application selects objects that are not currently selected, and deselects those that were selected.                                                                                                                              |
| Toggle selected objects in an area | Use Ctrl +drag to toggle the selection state within the drag's bounding box. This is useful if you applied certain settings or manipulations to the already selected objects, and now want to apply different settings to some of the selected objects.                         |
| Add objects to those selected      | Use Shift+click to add that object to the list of already selected objects. Use Shift+drag to add several object to the list of already selected objects.                                                                                                                       |

You can specify which types of markups you can select (see Select). When you create markups, they are automatically selected.

You can select all objects by pressing Ctrl+A .

To des l ct obj ing deselect all selected objects, right-click in the cell view and select Deselect from the context menu.

## Editing Markups

Markups must be selected before you can edit them.

<!-- image -->

To delete a markup:

1. Select the markup.
2. Click Edit in the Cell group on the Edit tab.
3. Select the markup, right-click, and select Delete from the context menu.

To move the vertex of a selected gauge, highlight, ruler, SEM image, or stretch:

1. Click the Select tool in the Tools group on either the Home or Edit tabs.
2. Move your pointer over the vertex that you would like to move. The pointer changes to a circle ( ) to indicate that you can move the vertex.
3. Drag to move the vertex. If the object has an angle constraint, such as a 45° requirement for gauges, the movement may be constrained.

To move the edge of a selected highlight or SEM image:

1. Click the Select tool in the Tools group on either the Home or Edit tabs.
2. Move your pointer over the edge that you would like to move. The pointer changes to a double arrow ( or ) to indicate that you can move the edge.
3. Drag to move the edge. Unlock the aspect ratio lock to move the edge of a SEM image (see SEM Image Properties).

To move a gauge, highlight, ruler, SEM image, or stretch:

1. Click Select in the Tools group on either the Home or Edit tabs.
2. Right-click and select Move from the context menu.
3. Move the pointer to move the object. If you press the Shift key, the object snaps horizontally, vertically, or at 45-degree angles only.
4. Click to complete your move.

If you select a SEM image and right-click, from the context menu you can:

- Mirror the image about the X- or Y-axis
- Rotate the image 90° to the right (clockwise) or left (counter-clockwise).
- Rotate the image using the mouse.

<!-- image -->

You can cut, copy, and paste markups:

- You can cut, copy, and paste by selecting those items from the cell view context menu or by using the respective hotkeys.
- You need to enter a reference point. The difference between the cut and copy, and paste points is used to determine the final position of your object.

<!-- image -->

## Editing Layouts and Cells

This chapter describes the editing functions for the application.

These topics are included in this chapter:

- Overview of Editing Functions
- Creating New Layouts and Cells
- Changing the Layout DBU and Resolution
- Making Cells Editable and Read-Only
- Showing or Hiding Cells
- Renaming, Replacing, and Deleting Cells and Their References
- Selecting Objects
- Object Attributes View
- Creating Shapes, Text, and References
- Cut, Copy, and Paste Operations
- Editing Shapes, Text, and References

Full details of command usage are in the IC Validator WorkBenchCommand Manual . Defaults and options for open layouts are described in Customizing the Environment.

## Overview of Editing Functions

You can edit shapes, text, and references of large layout files, such as:

- Creating and deleting shapes.
- Creating new cells and layouts.
- Undo and Redo.
- Moving and editing the coordinates of a shape in a lower level of the hierarchy.

<!-- image -->

- Copying and pasting shapes and references.
- Changing the layout DBU and scale.

IDs are global across your session. Therefore, the serial numbering of flags, gauges, highlights, shapes, references, and so on will continue even after you set another layout to be active.

## Creating New Layouts and Cells

You can create a layoutcre n w new layout by selecting File &gt; New .

The New Layout window opens, where you can specify the:

- The Layout name that is shown in the Layouts view.
- The Root cell name.
- The Database unit ( DBU )-The DBU specifies the length of a database tick, in meters.
- The User units -The user units are the coordinate units in which you prefer to work and this value is stored as an attribute in GDS layouts. Typically, this is less than one, because you use more than one database unit per user unit. For example, database units can be in nanometers, but user units can be in microns (1000 times larger, with a resolution of 0.001).

You can also create a new layout with the layout new command. See File for specifying the defaults for the DBU and user units.

You can create a new cell by clicking New in the Cell group on the Edit tab or by using the cell new command.

## Changing the Layout DBU and Resolution

You can change the layout layoutDBU resolution, change the DBU, or change the DBU and scale the layout. Changing the resolution changes the DBU value of your layout and still preserves physical dimensions and the database's user unit (typically a micron) at their original levels. You can make these changes from the Resolution dialog box, which you can access either by selecting Resolution in the File menu or by pressing Shift+E (see Figure 43).

<!-- image -->

Figure 43 Resolution dialog box

<!-- image -->

To change the resolution only:

1. Select the Lock original layout size check box.
2. In the DBU entry box, specify a new DBU value. Changing layout DBU allows for Boolean operations between layouts that initially had different DBUs.
3. Click OK .

## Note:

If you increase the resolution of the layout to a larger value than the layout file's original DBU, the application might not render the layout correctly.

When you have changed the layout resolution, after saving and reloading the layout, there might be a slight offset of arrays.

To change the DBU of the layout:

1. Deselect the Lock original layout size check box.
2. In the DBU entry, specify a new DBU value.
3. Click OK .

To change the scale and DBU of the layout:

1. Deselect the Lock original layout size check box.
2. In the Scale entry, specify a value to scale the layout.
3. In the DBU entry, specify a new DBU value.
4. Click OK .

<!-- image -->

## Making Cells Editable and Read-Only

When you open a layout, all of the cells are read-only by default. However, you can select and view the object properties of read-only cells. You can create and edit markups, such as rulers, but you cannot edit or create shapes.

To make a cell cel mak dit b editable:

1. Click Edit in the Cell group on the Edit tab.

OR

2. Place your pointer in the cell view, right-click, and select Set Cell Editable from the drop-down menu.

OR

3. Press Ctrl + E .

Cells will remain editable until you either click the Edit button again or select Set Cell Read Only from the drop-down menu.

4. You can also make cells editable by default when you open them (see Edit).

To make a cell cel mak r d-on y read-only:

1. Click Edit in the Cell group on the Edit tab if it was clicked previously and is enabled.

OR

Right-click and select Set Cell Read Only from the drop-down menu if that item has been selected previously and is enabled.

2. If you selected the Open cells in edit mode check box in the Options dialog box, deselect it, click Save , click OK , and restart the application to save your changes (see Edit).

You can make cells editable, read-only, or determine the edit state using the cell edit\_state command.

## Showing or Hiding Cells

When you open a layout all layout cells are visible. You can specify cells to hide or show previously hidden cells using the Show/Hide Cells dialog.

To show or hide cells cel mak dit b :

1. Select Hide in the Cell group on the Home tab.

The Show/Hide Cells dialog appears.

<!-- image -->

Figure 44 Show/Hide Cells

<!-- image -->

2. To hide the cells, you can search for cells in the Show Cells section, select the desired cells, click Move to right and click OK .

This hides the selected cells.

You can also click Move to right all to move all the cells to hide.

To show the hidden cells:

1. Select Hide in the Cell group on the Home tab.

The Show/Hide Cells dialog appears.

2. To show the hidden cells, you can search for cells on the Hide Cells section, select it, click Move to left and click OK .

This shows the selected hidden cells.

You can also click Move to left all to move all the cells to show.

## Renaming, Replacing, and Deleting Cells and Their References

To rename a cel r nam cell:

1. Right-click the cell in the Layouts view.
2. Select Rename from the context menu.
3. Enter a new name for the cell.

Renaming a cell makes it editable. You can also rename a cell using the layout cell rename command.

<!-- image -->

<!-- image -->

To replace a cell cel r p a ont s with the contents of another cell in the same or a different layout:

1. Right-click the cell in the Layouts view.
2. Select Replace from the context menu.
3. Select the replacement cell and its layout.

You can also replace a cell using the layout cell replace command.

You can delete a cell from your layout using the layout cell delete command. When you delete a cell that has been referenced by another cell, the referenced cell appears shaded and in italic type in the Tree view.

You can delete all references to a cell using the cell delete reference command.

## Selecting Objects

You can select shapes, text, and cells from active cells using the Select tool. To select these objects:

- The object must be selectable (see Select).
- The cell can be either editable or read-only (see Making Cells Editable and ReadOnly).
- You must be able to see the shape (see Changing How Layers Are Displayed and General Option Settings).
- The object must not be deeper in the hierarchy than the edit depth (see Select). By default, the edit depth is unlimited and you can select objects with full depth in the hierarchy.

Click the Polygon , Text , Reference , and Markup check boxes available on the ribbon to make these objects either selectable or unselectable. If only certain shape, markup, or reference types are selected in the Select options page, the Polygon , Reference and Markup check boxes will appear partially checked. If you hover the mouse over these check boxes, a tooltip will display the selected types.

<!-- image -->

You can select only a single instance of a shape, and if another instance of the same shape is added to the selection in another hierarchy, then the previously selected shape is deselected. For example, if you select a shape S in cell A, and there is another instance of the same cell A from which you add to the selection the same shape S, then the earlier selected shape S is deselected.

Also, when you select a shape and you add to the selection any parent cell instance of that shape, the shape is deselected. For example, if you select a shape S in cell A which is in cell B, and then you add any instance of the cell A (or cell B or any other parent cell instance higher in the hierarchy) to the selection, then the shape S is deselected.

If you select a single object, then there are no any hierarchical limitations. Hierarchical selection rules are applicable when selecting by region, adding objects to a selection, or when modifying selection objects by toggling the selected objects. When you attempt to make such selections, the conflicting object is automatically deselected.

## Selection Modes

You can choose the mode to use when selecting objects. Click the down arrow under Select and choose one of the following modes:

- Enclosed : This is the default mode when you select objects. This mode selects all objects that are fully enclosed within the selected area.
- Intersecting : This mode selects all objects that intersect with or are completely enclosed within the selected area.

<!-- image -->

<!-- image -->

<!-- image -->

- Line : This mode selects all objects that intersect the selection line.

<!-- image -->

## To select sel ctobj ing objects:

1. Click Select in the Tools group on the Home or Edit tabs.
2. Click the down arrow under Select to display the drop-down menu where you can select Edit Depth options: Root , Level 1 only , Level Root to 10 , or Unlimited .

This drop-down menu also contains additional items: Options enables you to open the Options dialog box. Selectable enables you to specify whether or not polygons, text, references, and arrays are selectable. You can also select the check boxes available on the ribbon to make polygons, text, and references either selectable or unselectable.

Table 44 shows different selection operations you can perform with the mouse.

| Selection Operation   | Description                                                                            |
|-----------------------|----------------------------------------------------------------------------------------|
| Select one object     | Ctrl +click to select an object This action deselects any previously selected objects. |

Table 44 Selection Operations Using the Mouse

<!-- image -->

Table 44 Selection Operations Using the Mouse (Continued)

| Selection Operation                | Description                                                                                                                                                                                                                                                                                |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select objects in an area          | Use drag to select everything contained in the drag's bounding box. This is useful when you want to select numerous objects in a certain area and clicking each object to select it is inefficient. This action deselects any previously selected objects outside the drag's bounding box. |
| Toggle a selected object           | Use Ctrl +click to toggle your selection. The application selects objects that are not currently selected, and deselects any previously selected objects.                                                                                                                                  |
| Toggle selected objects in an area | Use Ctrl +drag to toggle the selection state within the drag's bounding box. This is useful if you applied certain settings or manipulations to the already selected objects, and now want to apply different settings to some of the selected objects.                                    |
| Add objects to those selected      | Use Shift +click to add that object to the list of already selected objects. Use Shift+click+drag to add several object to the list of already selected objects.                                                                                                                           |

When using the Select tool and if the selection emphasis is enabled, then when you move the pointer over a selectable shape or reference, the shape or reference is highlighted with a brush effect and a dashed green outline. When hovering over multiple overlapping shapes you can also press TAB to cycle over the shapes to choose which one to select or get info with shape info tool. And if you click the object, that object is selected. You can change the emphasis brush setting, the color, width, and style of the emphasis, or turn the selection emphasis off in Options &gt; Layout &gt; Select (see Select).

You can use the mouse to select one or more objects at once. When two or more objects could be selected, the tool uses the following priority to determine which shape to select:

- Vertex
- Edge
- Center

To des l ct obj ing deselect all selected objects

- Right-click the cell view, and select Deselect from the context menu.

<!-- image -->

## Object Attributes View

You can view and edit (for editable cells) the objectspr i and u properties and attributes of selected shapes, markups, and cell references using the Object Attributes view. When no shape is selected, the Object Attributes view shows the active cell's bounding box coordinates and cell properties, if any. Click Dockable in the Window group on the View tab and select Object Attributes from the drop-down menu to show the Object Attributes view (see Figure 45). You can also show or hide the Object Attributes dockable view by right clicking anywhere in the cell view and selecting the Show Object Attributes check box.

Figure 45 Object Attributes view

<!-- image -->

Using the Object Attributes Object Prop i s v w view you can:

- Step through each of the objects using the first, previous, next, and last buttons.
- Jump to an object using the drop-down list with the object's ID and type and see the number of objects selected.
- View the object coordinates and other attributes relative either to its parent cell (default) or its absolute coordinates (coordinates relative to the current active cell). Click the Absolute button to switch on or switch off the absolute coordinates. By default, it is off.

<!-- image -->

<!-- image -->

- See and edit (if the cell is editable) all the attributes of the object (shape, text, markup, reference, and array): hierarchy, coordinates, layer, text, referenced cell, rotation, magnification, path width, circle radius, and so on where available.
- Markup attributes are always editable.
- For each item, changes are applied after pressing Enter or when another item is selected.
- See the outline coordinates (perimeter) of the shape (including circle and path). For rotated references, the rotated boundary coordinates are displayed rather than the horizontal bounding box coordinates. For rectangle and polygon, it is the same as coordinates.
- View object properties, and also create and change properties for editable cells:
- You can create additional properties for editable cells from the context menu of the Properties folder. The entry in the first column, or key, must be a non-negative integer less than or equal to 65,535 and the second column is a string. An object can have multiple properties, but the same key cannot be used more than once for an object.
- You can delete a property of an editable cell by right-clicking a property and selecting Delete from the context menu, or delete all properties by selecting Delete All from the context menu of the Properties folder.
- See cell properties of the active cell.
- Copy items and also paste items into the editable fields.

## Creating Shapes, Text, and References

You can create shapes, references, and text using the tools in the Tools group on the Edit tab. Before you begin, ensure that your cell is editable. Otherwise, these tools are not available.

After you select your tool, the options for that tool open in a group to the right of it on the tab. When you create objects, they are selected only if the object is selectable (see #unique\_134).

For objects created with the GUI, the vertices snap to the edit grid (#unique\_141). You can constrain the angle for paths and polygons to 90° only, multiples of 45°, or any angle (see #unique\_120).

The following sections describe how to create shapes, references, and text in your layout:

## Creating Circles and Ellipses

<!-- image -->

You can use the Circle tool to create circles or ellipses in the cells in your layout. When you select Circle from the drop-down menu in the Tools group on the Edit tab, the Circle Edit Options group for this tool opens to the right of it on the tab and you can specify the layer on which the circle is going to be created; the Radius and Coords fields display the radius and center of the circle being created.

To draw a circle:

1. Click the More button in the Tools group on the Edit tab.
2. Select Circle from the drop-down menu.

<!-- image -->

The Circle button appears to the right of the Text button and remains visible until you deselect it from the drop-down menu.

3. Drag in the cell view.

Press the Esc key before releasing the mouse button to undo drawing the circle.

You can delete the circle by pressing the Delete key.

To draw an ellipse:

1. Enable ellipse editing by setting default layout\_ellipse\_edit to 1 .
2. Select the Circle tool.
3. Press Shift while you drag in the cell view.

You can adjust the x-axis and y-axis radius of the drawn ellipse using the Radius field in the Circle Select Options group.

You can also draw an ellipse using the cell object add command as follows:

cell object add ellipse {coords {275 300} xradius 285 yradius 100} .

## Creating Paths

The Path tool enables you to create paths in the cells in your layout. When you click Path in the Tools group on the Edit tab, the Path Edit Options group for this tool opens to the right of it on the tab.

These options enable you to specify:

- the layer on which the path is going to be created
- the path width

<!-- image -->

- where the path begins and ends
- the path end style:
- Abut -no extension
- Half extension -half the path width
- Variable extension -you can specify the amount of begin and end extension for the path.
- Circular extension -circular extension
- the constraint angle for paths. You can set the constraint angle to multiples of 45° or 90°, or set the angle to 0.

## To create creat p h ing a path:

1. Click Path in the Tools group on the Edit tab.
2. Place your pointer in the cell view and click in the area where you want to create the path vertices.
3. Press the Shift key to constrain the next point either vertically or horizontally related to the last point.
4. Press the Ctrl key to ignore the geometry constraint.
5. Move the pointer to the last point in the path and double-click to finish the path.
6. Press the Esc key to undo the entire path.
7. Press the Delete key to delete the entire path.

You can move vertices and path segments of selected paths using the Path tool. If you move the pointer over a vertex or a centerline of a path, the pointer changes. Drag to move the vertex or path segment.

## Creating Polygons

When you click Polygon in the Tools group on the Edit tab, the Polygon Edit Options group for this tool opens to the right of it on the tab. These options enable you to specify the layer on which the polygon is going to be created and the geometry constraint. Three or more unique vertices are required to create a polygon.

As you draw your shape, the application provides a preview and displays:

- The distance to the previous vertex next to the pointer.
- The delta-X, delta-Y, and distance to the previous vertex in the status bar.

<!-- image -->

## To create a rectangle:

- Drag the pointer in the cell view to create a rectangle.
- Press Ctrl and then drag the pointer to create a rectangle where the clicked point is the center of the created rectangle.
- Press Ctrl+Shift and then drag the pointer to create a square where the clicked point is the center of the created square.

## To create a creat polyg n i polygon:

1. Place your pointer in the cell view and click in the area where you want to create the polygon vertices.
2. Move the pointer to the last point in the polygon and double-click to finish the polygon. During drawing, the tool provides a preview of how the polygon is going to look when finished by showing a yellow dashed line connecting the first drawn point and the current point.
3. You can move vertices and segments of selected polygons by moving the pointer over a vertex or a segment of a polygon, and then dragging to move the vertex or segment.
4. You can delete the last drawn point by pressing the Delete key.
5. Press the Shift key to constrain the next point either vertically or horizontally related to the last point.
6. Press the Ctrl key to ignore the geometry constraint.
7. Press the Esc key to undo the entire polygon.
8. Press the Delete key to delete the entire polygon.

## Boolean Operations for Creating Shapes

When drawing shapes or when working with existing shapes, you can combine them and create new ones by using any of these Boolean operations: AND , OR , NOT , and XOR . You can apply the Boolean operations to shapes on different layers and to shapes in different hierarchy levels. You can also choose to keep or delete the input shapes.

## Using Boolean Modes When Drawing Shapes

When drawing shapes, you can use the Boolean modes to create new shapes on the same layer as the input layers. The Boolean operations are available in the Mode feature in the edit options of the Polygon , Path , and Circle shape tools.

<!-- image -->

To select the required mode:

1. Choose a shape tool from the Edit menu.
2. In the &lt;Tool&gt; Edit Options group, choose an operation from the Mode list.
3. Select from the following and then draw the required shape.
- #unique\_278\_Connect\_42\_add\_mode
- #unique\_278\_Connect\_42\_and\_mode
- #unique\_278\_Connect\_42\_or\_mode
- #unique\_278\_Connect\_42\_not\_mode
- #unique\_278\_Connect\_42\_xor\_mode
4. If you want to keep the existing shapes after the operation, uncheck the Delete old shapes check box. See #unique\_280.

<!-- image -->

## Note:

The selected mode is retained during the session. When you start the application, the default mode is always the ADD mode.

## ADD Mode

This is the default mode for creating shapes. When using this mode, the new shape is added without affecting the existing shapes.

The corresponding command is cell object add .

Figure 46 ADD Mode-the blue hatched shape indicates an existing shape in the layout and the blue dashed shape is the preview of the shape being added (before the operation is finished). In the ADD mode, the added shape is not interacting with the existing shapes, so the final added shape matches the preview.

<!-- image -->

<!-- image -->

<!-- image -->

## AND Mode

This mode creates an intersection of the new and existing shapes. The resulting shape contains only the overlapping areas of the new and existing shapes.

The corresponding command is cell object and .

<!-- image -->

## OR Mode

This mode combines the new shape with the existing shapes to create one shape. The resulting shape is a union of the new and existing shapes, including all the overlapping and non-overlapping areas.

The corresponding command is cell object or .

<!-- image -->

## NOT Mode

This mode is the opposite of the OR mode and creates a shape by subtracting the overlapping areas of the new shape from the existing shapes. The resulting shape contains only the nonoverlapping areas of the existing shape.

The corresponding command is cell object not .

<!-- image -->

## XOR Mode

This mode is the opposite of the AND mode and it creates a shape by excluding only the overlapping areas. The resulting shape contains only the nonoverlapping areas of the new and existing shapes.

The corresponding command is cell object xor .

<!-- image -->

<!-- image -->

## Using Boolean Operations on Existing Shapes

You can apply the AND, OR, and XOR Boolean operations to shapes in the layout. The shapes can be on the same or different layers and they can be on different hierarchy levels.

To apply the Boolean operations on existing shapes:

1. Select the shapes from the cell view on which you want to apply the Boolean operations.

You must select exactly two shapes for the AND and XOR operations and two or more for the OR operation.

2. Set the active layer.

The resulting shapes from the operation are created on the active layer. You can change the active layer, if required, by double-clicking the layer in the Layout Layers dockable.

3. Right-click, point to Boolean , and choose an operation you want to apply from the submenu.

If you want to retain the original shapes, clear the Delete old shapes check box. The cell must be editable for the Boolean submenu to appear.

<!-- image -->

## Delete old shapes Option

By default, the shapes in the layout are combined with the new shape as per the chosen mode. The original input shapes are deleted and only the shape created in a result of the Boolean operation is added to the layout.

If this option is unchecked, then the existing shapes are retained and the new shapes resulting from the Boolean operations are created on the current cell and layer.

<!-- image -->

## Note:

Only shapes in the current active cell are deleted and shapes in hierarchy are always kept intact.

## Applying Boolean Operations in Different Hierarchies

You can apply Boolean operations to shapes in different hierarchy levels and combine them to create new shapes. When using the GUI, the shapes participating in the operation must be on the same layer for the operation to work.

The resulting new shape is added either in the current active cell or in the cell specified with the -cell CELL argument when using the cell object commands corresponding to the Boolean operations.

In the following example, the red-dashed shape (on the left) shows the shape preview drawn in the OR mode on the red layer (0:0). It interacts with the top-left red square in the hierarchy (cell a) and the bottom-left square in the current active cell.

After the shape is drawn in the OR mode, the three shapes are combined together into a new shape on the current layer (0:0)-the red shape with thick outline (on the right).

<!-- image -->

If the Delete old shapes option is enabled, then the bottom-left shape in the active cell is deleted. However, the top-left shape in the hierarchy is kept as shapes in hierarchy are not deleted.

## Creating References

When you click Reference in the Tools group on the Edit tab, the Reference Edit Options group for this tool opens to the right of it on the tab.

<!-- image -->

These options enable you to specify:

- The reference cell name-You can enter the value or select a cell in the layout.
- The number of columns and rows for an arrayed reference-Enter 1 for the columns and rows to create a single reference.
- The column and row pitch for arrayed references-When you change the cell name, or delete the DX or DY values, the DX and DY values are set to the cell height and width so that the arrayed cells will abut.
- A drop-down list to specify the orientation-If you would like a magnification different than one or a different angle, select Custom .

When you change the orientation of a reference cell, the cell is oriented relative to its current position by default. You can change the default behavior and orient the cell relative to its origin by changing the Reference flipping setting in the Options &gt; Layout &gt; #unique\_120 page to Origin .

- The coordinates to create the reference-The value tracks the pointer coordinates in your layout. Enter values and press the Enter key to create a reference at the location you specify.

See #unique\_193 for mapping the standard orientations to OpenAccess and DEF formats.

## Creating Text

When you click Text in the Tools group on the Edit tab, the Text Edit Options group for this tool opens to the right of it on the tab.

You can use these options to specify:

- The layer on which the text is going to be created.
- The X and Y position.

To create creat x ing text:

1. Place your pointer in the cell view where you want to add text.
2. Enter your text.
3. Press the Enter key.

## Creating Polygon Text

Polygon Text tool allows adding polygon shapes in form of specified text string.

<!-- image -->

<!-- image -->

When you click Polygon Text in the Tools group on the Edit tab, the Polygon Text Edit Options appear to the right of it on the tab.

You can use these options to specify:

- The layer on which the polygon text is going to be created.
- The X and Y position. Type the coordinates and press Enter key.
- The cell. By default, the text shapes are added to the current active cell. If you specify a cell-name, then a new cell is created with that name, the text shapes are added to that cell and it's placed in the current active cell. You cannot specify an existing cell name.
- The font for the polygon text. It can be PressStartK, OneSize, or Pixel. PressStartK font satisfies the following design rules checks at 2 um height and bigger:
- Minimum space: 0.2 um
- Minimum width: 0.2 um
- Minimum area: 0.12 um sq.
- Minimum enclosed area: 0.36 um sq.

OneSize and Pixel fonts satisfy first three of these checks.

- The height of the polygon text.

To create creat x ing polygon text:

1. Place your pointer in the cell view where you want to add the polygon text or type the X Y coordinates in the Coords control and press Enter key.
2. Enter your text.
3. Press the Enter key.

## Cut, Copy, and Paste Operations

The application enables you to cut, copy, and paste shapes, most markups, and references within a layout and between layouts. You can cut, copy, and paste all markups except for contours and model images. If you copy shapes, text, or references from a child cell, the objects will be placed in the top cell when you paste the object.

In the GUI, you can use the Ctrl+X , Ctrl+C , and Ctrl+V hotkeys or the context menu in the cell view. Selecting this menu item also enables you to specify the pasted layer and the X/Y offset. For scripting, you can use the select cut , select copy , and select paste commands. You can also copy cell names and text (from the description or properties column) in the Treeview, Layouts, and other dockable windows to the clipboard by selecting the items and pressing Ctrl+C.

<!-- image -->

The application places pasted objects at a location relative to the reference point used when cutting or copying the objects and the paste click reference point. For GUI operations, this means the application pastes objects the same distance from the pointer as when performing the earlier cut or copy action.

You can also copy or delete all the shapes and texts on a layer using the context menu in Layout Layers view. Right-click on a layer and select Copy To to copy all shapes and texts to another layer. A dialog box will open that enables you to select the layer to copy to and the offset for pasting.

Select Delete to delete the layer from the layout along with all objects drawn on that layer. To delete multiple layers, select the layers you want to delete, right-click, and choose Delete Selected from the context menu.

## Editing Shapes, Text, and References

Objects must be selected before you can edit them. To specify which objects are selectable, click the down arrow under Select in the Tools group on the Edit tab and choose the objects that you want to be selectable from the drop-down menu. You can also click the Polygon , Text , Reference , and Markup check boxes available on the ribbon to make these objects selectable or not.

You can select all shapes, references, or text by pressing Ctrl+A or by clicking and dragging over the objects to select them.

All selected objects can be deleted by pressing the Delete key. You can also delete selected objects by selecting Delete from the context menu in the cell view.

You can change the layer of text and shapes to the active layer (see #unique\_88) by selecting Set Layer from the cell view context menu.

You can move shapes, references, and text by clicking the object and selecting Move from the right-click context menu in the cell view. You can select multiple objects by pressing Ctrl. Move your pointer to move the shapes with a preview. Click in your cell view when you have finished moving the shapes. You can also move objects by pressing Ctrl and using the arrow keys to move the objects around. You can set the move offset by using the layout edit grid\_size command. If you press Shift while moving objects, the movement is restricted to only the horizontal, vertical, or 45-degree diagonal directions.

Additional options for editing shapes and text in the cell view are in the following sections:

## Editing Paths and Polygons

To move a movep lyg n s t , i segment of a selected path or the movep lyg n d , i edge of a selected polygon:

1. Click Select in the Tools group on either the Home or Edit tabs.
2. Move your pointer over the edge that you would like to move. The pointer will change to a double arrow ( or ) to indicate that you can move the edge.
3. Drag to move the edge.

From the context menu in the cell view, you can also:

- Split an object. Select two points and the object will be split between the two points.
- Split an edge. A new vertex will be created on the edge.
- Specify the amount to move an edge. Select Edit Edge and enter the amount to move the edge or pick two points in the Cell view.

When you are using the Select tool, additional editing options are available for paths and polygons:

- When you select a Path, the Path Select Options group opens, and you can specify an offset to move the path, and you can also change the Layer , Angle , Style , Width , Begin , and End attributes.
- When you select a Polygon, the Polygon Select Options group opens, and you can specify an offset to move the polygon, change the Layer attributes, and set the Snap distance. Also, when you start moving an edge or vertex, you can specify an offset to move just the edge or vertex.
- Clicking the Layer button when editing or selecting paths or polygons opens the layer edit filter dialog box where you can select the active layer, filter layers using wildcards and regular expressions, and create a new layer. The layer filter dialog box has the following options:
- Case sensitivity ( Aa ): Choose this option to enable case sensitivity when filtering layers.
- The recently used layers are displayed on the top in italics.
- Wildcards : Use wildcards for matching layer names.
- Any character except *, ?, and [...] matches itself. For example, c matches the character c.
- ?: Matches any single character and is the same as '.' in regular expression.
- *: Matches any number of characters. Is the same as .* in regular expression.

<!-- image -->

<!-- image -->

- [...]: Set of character can be represented in square brackets, similar to regular expressions.
- Regular expression : Use regular expressions for filtering layer names. A regular expression is a pattern for matching sub-strings in text.
- New Layer : Opens the New Layer dialog box for creating a new layer.
- Layout Only : Filter only the layers that are in the current layout.
- All configured : Filter all the configured layers in the application.

<!-- image -->

## Aligning and Distributing Shapes

The Align tool allows you to quickly align and distribute shapes at specified distances from one another in your layout.

## To align shapes

1. Using the Select tool, select two or more shapes you want to align. To select multiple shapes, press and hold Shift for adding shapes or Ctrl for toggling between shapes.
2. In the Polygon Select Options group on the Edit tab, click Align and then select one of the commands from the menu.

<!-- image -->

## Note:

The Align button is enabled only if two or more objects are selected.

The following table describes the commands in the Align menu with examples. The examples show the result of the commands when applied to the following shape arrangement:

<!-- image -->

| Option      | Description                                                     | Example   |
|-------------|-----------------------------------------------------------------|-----------|
| Align Left  | Aligns shapes along the left-most edge of the selected shapes.  |           |
| Align Right | Aligns shapes along the right-most edge of the selected shapes. |           |

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

| Option       | Description                                                            | Example   |
|--------------|------------------------------------------------------------------------|-----------|
| Align Center | Aligns shapes vertically along the centers of the selected shapes.     |           |
| Align Top    | Aligns shapes along the top-most edge of the selected shapes.          |           |
| Align Middle | Aligns shapes horizontally through the middle of the selected objects. |           |
| Align Bottom | Aligns shapes along the bottom-most edge of the selected shapes.       |           |

## To distribute shapes at equal distances from one another

1. Using the Select tool, select two or more shapes you want to distribute. To select multiple shapes, press and hold Shift for adding shapes or Ctrl for toggling between shapes.
2. In the Polygon Select Options group on the Edit tab, click Align , and then enter a spacing distance (in layout units) in the Spacing text box. If you do not provide a spacing distance value, the shapes are distributed evenly at equal distances from one another.
3. Do one of the following:
- Click Distribute Horizontally to arrange the shapes horizontally.
- Click Distribute Vertically to arrange the shapes horizontally.

## Moving and Aligning Vertices

You can use the Vertex tool on the Edit tab to move vertices of multiple shapes at a time.

To move the vertices of a selected movepath ing path or movep lyg n i polygon:

1. Click Vertex in the Tools group on Edit tab and select the shape or shapes whose vertices you want to move.
2. To select several vertices at once, drag the mouse pointer over the vertices of the selected shapes, or click on the edge to select both vertices at its ends.

You can also press and hold Shift (for adding) or Ctrl (for toggling) vertices or edges.

3. Move your pointer over a selected vertex ( ) and when the pointer changes to a crosshair ( ), drag the pointer to move the selected vertex or vertices. When you move a vertex, the vertex offset is displayed next to the mouse pointer, and the offset and distance are displayed on the status bar.

You can use the following options in the Vertex Edit Options group to move the vertices:

- Move : Enter an offset (X/Y coordinates) in the Move text box or click the pick button and select an offset in the cell view.
- Angle : If you set the shape's constrain angle (such as at 45° or at 90°), the vertex movement will be constrained (see #unique\_120).

You can also do the following from the right-click context menu:

- Move or delete vertices.
- (For multiple vertices only) align vertices vertically or horizontally.
- Insert a vertex on an edge.

## Duplicating and Repeating Objects

You can easily duplicate shapes or create arrays of objects from selected objects by using the GUI or the command-line.

To duplicate shapes:

1. In the cell view, select the shape or shapes you want to duplicate.

Press and hold Ctrl to select multiple shapes.

2. Right-click and choose Duplicate from the context menu.

<!-- image -->

<!-- image -->

The shapes are duplicated on the same layer of the selected shapes. You can move the shapes to separate the selected and duplicated shapes.

## Note:

Duplicated objects are added to the current active cell even when duplicating objects deeper in hierarchy.

## To create an array of objects:

1. In the cell view, select the shape or shapes you want to repeat.
2. Right-click and choose Repeat from the context menu.
3. In the Repeat objects dialog box, enter the following:
- Columns : Enter the number of columns you want the object to repeat. For the Offset Vector , enter the X and Y coordinates you want the columns to be offset. To offset the columns horizontally, enter a single value X (equivalent to X 0 ) that will be used as the column pitch. By default, the column offset vector is set so that the repeated objects are created abut to each other horizontally.
- Rows : Enter the number of rows you want the object to repeat. For the Offset Vector , enter the X and Y coordinates you want the rows to be offset. To offset the rows vertically, enter a single value Y (equivalent to 0 Y ) that will be used as the row pitch. By default, the row offset vector is set so that the repeated objects are created abut to each other vertically.
- Move : Enter the X and Y coordinates you want the array to be offset from the original location (including the selected original shapes). By default, the offset is 0 0 .
4. Click Repeat to create the array.

<!-- image -->

## Note:

Repeated objects are added to the current active cell even when repeating objects deeper in the hierarchy. If you repeat objects with a non-zero offset, then the selected objects are moved in their hierarchy level (while the repeated objects are created in active cell).

The corresponding command for repeating objects is cell object repeat.

## Using the Snapping Feature

You can use the snap-to-shapes feature to align the edges of shapes accurately with the nearest polygon, circle, reference, path, or cell's bounding box. The snapping feature allows you to set the snapping distance and provides visual guides when moving or editing the edges or vertices of shapes.

The snap-to-shapes feature is enabled by default. Use the Edit options under Layout Default Settings (see #unique\_120) to change the following default settings for this feature:

- Snapping Space

The space (in layout units) to track (in passive snapping mode) or keep between the edges or vertices when snapping. The default is 0.

- Snapping Radius

The distance (in pixels) from the target edge that the mouse pointer must fall within to snap to it. The default is set to 20 pixels.

## To use the snap-to-shape feature

1. Click the Select tool on the Edit tab to enable the Snap option in the Polygon Select Options group.
2. (Optional) In the Snap text box, enter a snapping space (in layout units).

If you do not set a snapping space, the edge you or vertex you are moving snaps exactly to the target edge or vertex.

3. You can snap shapes in two ways:
- Active Snapping

Press and hold Ctrl while moving the edge or vertex of the shape towards the target edge or vertex using the mouse. The pointer automatically jumps to the target edge or to the set snapping distance while displaying the preview box highlighted in yellow.

Release the mouse button at the chosen preview box to snap the shape's edge to the target edge.

- Passive Snapping

Move the edge or vertex of the shape towards the target shape. Snapping preview boxes are displayed indicating where snapping is possible and the distance from the target shape.

<!-- image -->

<!-- image -->

If the snapping space is set, red highlighted boxes indicate that the distance is less than the provided spacing.

Yellow highlighted boxes indicate the point at which the snapping will occur. You can increase the snapping radius to increase the snapping field around the pointer.

A highlighted gray edge indicates the edge where the snapping will occur.

<!-- image -->

## Editing Text

To edit x ng edit the selected text, select Edit Text from the cell view context menu.

## You can:

- Change the text string.
- Press Esc to cancel the changes.
- Press Enter confirm the changes and exit Edit Text mode.

When you select text that you want to edit, the Text Select Options group is displayed on the Edit tab and you can edit the selected text.

## You can:

- Specify an offset to move the selected text.
- Change the layer of the text.
- Change the text string.

## Converting Text to Polygon

You can convert text objects in the layout to polygons. Select a text, right click and select Convert to Polygon . You can modify the text string as well as the conversion options in the Polygon Text Edit Options , such as the font or the height of the text polygons. Press the Enter key or click outside of text object to convert the text.

## Rounding Corners of Polygons

You can round the corners of the selected polygons by right clicking and choosing Round Corners and specify the rounding radii (same or different) for either concave or convex or both types of corners in the Specify radius fields. Click Apply or press Enter to round the corners of the polygons.

## Converting an Arrayed Reference to Multiple Single References

To convert an arrayed reference to multiple single references, select Break Arrayed Reference from the cell view context menu. This operation applies to the selected arrayed reference under the mouse cursor only.

## Creating a Unique Copy of a Referenced Cell Instance

If you need to edit a cell instance without affecting other instances of the same cell, you can replace the current instance of the cell with a unique copy of it. You can make the cell unique in the whole layout or make the cell unique only in its parent cell.

<!-- image -->

<!-- image -->

To create a unique copy of the selected reference, right-click the instance and do the following:

- Choose Make Cell Unique &gt; &lt;cell name&gt; in parent cell to make the cell unique only in its parent layout.
- Choose Make Cell Unique &gt; &lt;cell name&gt; hierarchically to make the cell unique in the whole layout.

The corresponding command for making a cell unique is cell object make unique .

This creates a unique copy of the referenced cell and the current selected cell reference is replaced with a reference to the newly created cell.

## Editing Objects in a Cell Hierarchy with Multiple Instances

When you edit or delete an object in a cell hierarchy that has multiple instances, the tool displays the Object Modify dialog box where you can choose how to handle the changes. You can choose from the following options:

- Make the reference unique : Makes the object's hierarchy unique, so the changes only apply to that instance.
- Modify the cell : Edits the object without making them unique, so all instances of that object will be updated across cells.

If you select the Don't show this dialog again check box, the option you chose will become the default setting and will be automatically applied the next time you edit an object with multiple instances.

<!-- image -->

You can edit the default setting by using the default layout\_reference\_uniquify interactive|yes|no command or from the Tools → Options → Layout → Edit settings page.

## 7

## Saving, Exporting, Merging, and Comparing Layouts

This chapter describes how to save, export, merge, and compare layouts.

These topics are covered:

- Saving Layouts
- Exporting Layouts
- Merging Layouts
- Comparing Layouts and Cells

Full details of command usage are in the IC Validator WorkBench Command Manual . Defaults and options for open layouts are described in Customizing the Environment.

## Saving Layouts

You have two options for saving your layout: you can save the active file to its current location, or you can save your edited file with a new name or to a different location.

You can save the layout to GDSII, GDSII.GZ, OASIS, or OASIS OPT. You can also save the layout as a LEF file.

OASIS OPT is an optimized, OASIS-compliant format and is the default format for saving OASIS files and when saving new layout files. It provides better rendering, searching, editing, and probing capabilities. You can also create an OASIS OPT layout from an existing GDSII or OASIS layout using the Optimized OASIS converter utility (see Layout Format Conversion).

OASIS files are much smaller than GDSII and GDSII files in gzip format. You should not gzip OASIS files, because OASIS files are already compressed and performing a gzip will delay opening and rendering the file later.

When you save a layout as an OASIS file, your settings for compaction and compression will be used (see OASIS).

<!-- image -->

## Note:

The application compacts the layout when saving so that there are no duplicate shapes (same coordinates, layer:datatype, and so on).

Due to limitations in GDSII, the application cannot output polygons with more than 8191 points as a GDSII layout. If your polygon has more than 8191 points, save the output as an OASIS file.

To save your file:

1. Select File &gt; Save to save the active file to its current location.

OR

2. Select File &gt; Save As to save your edited file with a new name or to a different location.

The Save As window opens. It contains three tabs.

- In the OASIS tab, specify conditions for saving OASIS files:
- whether or not to save properties and instances.
- whether or not to exclude (omit) all text objects from the layout when saving the layout file.
- the amount of compression (the default is 6) and if compaction should be used.
- In the GDSII tab, specify conditions for saving your layout as a GDSII file, such as whether or not to save properties and instances, whether or not to exclude (omit) all text objects from the layout when saving the layout file, and the library name (LIBNAME) of the file.
- In the LEF tab, you can save the layout as a .lef file and also specify if you want the additional VIA information to be stored in the file.
3. If you are saving your file in the GDSII, LEF, or OASIS format, specify the options for those file types in the respective tabs.
4. Click Save As .
5. The Save As dialog box opens and you can browse to recently opened folders by clicking the arrow in the Look in drop-down list.
6. Browse to the new location for the file. The application keeps the directory you last accessed in memory.
7. Enter the new file name in the File name field.

<!-- image -->

8. Select the file type. It is the same as your current file type by default.
9. Click Save .

## Exporting Layouts

You may want to export a new layout file from parts of another layout or change the layers in a layout in your design flow. You can do this by selecting File &gt; Export . Additionally, you can select Export from the context menu of a cell in the Layouts view, highlights in the Markups view, or by using the layout extract command. In addition to exporting your results to a new file, you can also export your results to the paste buffer or to a new cell.

These topics are available:

- Exporting Options
- Additional Export Options

## Exporting Options

If you select File &gt; Export , the Layout Export wizard opens and you can choose your options for export (see Figure 47).

- If you select By Cell , then on the next page of the wizard, you can select a cell from a list of cells in your layout you want to export.

You can filter cells as you type in the Match field and then choose a cell to export. If you select the Regular expression check box, you can filter the cell list using regular expressions. If you select Case sensitive and type in the Match field, the cell list is filtered based on the case (uppercase or lowercase) of the cell name.

The specified cell and all of its descendant cells will be included in the exported file.

- If you select By Region , then on the next page of the wizard, you can select a rectangular region to export.
- If you select Entire File , all cells will be included in the exported file.

<!-- image -->

Figure 47 Layout Export wizard - Choose How to Export

<!-- image -->

In the Select Layers to Export page of the wizard, you can select the layers to export and map the layers (see Figure 48). You can use the Filter box to filter layers and then include or exclude the filtered layers when exporting. If you deselect the check box for Select Layer, the layer will not be output. You can map layers in the input layout to layers in the output layout by specifying the layer:datatype of the output layouts in the Map To Layer column. If you do not specify a datatype, datatype 0 is used. Additionally, when exporting as an OASIS file, you can use the Map Name column to map a new layer name for the output layer. The name specified for the output layer overrides the original output layer name (if any).

You can select one or more rows of the table and right-click to select items from the context menu:

- Include

The check box for the layer is selected. You can also do this for all layers.

- Exclude

The check box for the layer is deselected. You can also do this for all layers.

- Revert Mapping

The Map to Layer and Select Layer values will be the same for the layer. You can also do this for all layers or for the filtered layers.

- Include All

All layers are selected.

<!-- image -->

- Exclude All

No layers are selected.

- Include Filtered

Only the filtered layers are selected.

- Exclude Filtered

The filtered layers are not selected.

- Include Visible Only

Check boxes for visible layers will be selected and for hidden layers will be deselected.

Figure 48 Layout Export wizard - Select Layers to Export

<!-- image -->

If you click the layoutexp r Pick b n Pick button on the Specify a Region to Export dialog box (see Figure 49), this will hide the wizard and allow you to select a region in the Cell View. Click and drag to define the region that you want to export.

<!-- image -->

Figure 49 Layout Export Wizard - Select Layers to Export

<!-- image -->

On the next page of the wizard, you can select an output file. For all output formats, you can specify whether to open the exported layout upon completion. If the output format is OASIS, you can also specify the compression and compaction values.

On the last page of the wizard, you can select output transformation options:

The options depend on your choice for how you want to export.

- For all options, you can specify the following:
- Whether to convert paths to polygon in the extracted layout
- Whether to delete duplicate references
- Whether or not to exclude (omit) all text objects in the extracted layout
- Delete empty cells and references to empty cells using the -deleteEmptyCells flag for the layout extract command.

Converting paths to polygon and dropping duplicate references are not supported in the LEF format.

- If you select By Cell , you can also choose to flatten the hierarchy and specify the hierarchy levels to extract. Flattening the hierarchy is not supported in the LEF format. When retaining the hierarchy, you can choose to output empty cells or delete them after extraction.
- If you select By Region , you can either export the results to a new layout file or output the results to the paste buffer. If you export the results to a new layout file, you can

<!-- image -->

<!-- image -->

choose to flatten or retain the hierarchy in your region and specify a top cell name. You can also specify the hierarchy levels to extract.

- When retaining the hierarchy, you can output empty cells or delete them after extraction.
- Select the Protrude shapes option to export layout regions without cutting (trimming) the shapes at the region boundaries. This mode prevents false DRC errors from appearing on the extracted region.
- When Retain hierarchy is not selected, you can specify the anamorphic magnification by entering two values for horizontal and vertical magnification.

You can save the layout to GDSII, GDSII.GZ, LEF, OASIS, or OASIS OPT (default).

## Note:

Due to limitations in the GDSII format, the application cannot output polygons with more than 8191 points as a GDSII layout. If your polygon has more than 8191 points, save the output as an OASIS file.

## Additional Export Options

In addition to exporting using File &gt; Export , you can:

- Right-click a cell in the Layouts view and select Export from the context menu. You can then select layers to export using the Layout Export wizard.
- Right-click a highlight, group of highlights, or a folder containing highlights in Markup view or Open Cells view and select Export from the context menu. You can then select layers to export using the Layout Export wizard.
- Right-click a highlight or a group of highlights and select Export from the context menu.

## Merging Layouts

You may need to merge several layout files into a new one in your design flow. You can do this using the Layout Merge wizard or the merge command.

You can merge layouts of different formats with different database units (DBU) and save the output to any format with any DBU. You can merge open layouts, layouts on the disk, or layouts in a directory by matching the provided wildcard patterns. All individual input layouts and the output merged layout can be modified during the merge operation using the various transformation commands.

You can access the Layout Merge wizard by clicking File &gt; Layout Merge .

This section includes the following topics:

- Main Modes
- Additional Modes (using the layout merge command)

## Main Modes

The Main Modes consist of the library , new\_top , and prime merge modes.

- library mode-Use this mode to merge IP blocks into the design layout. Cells with the same name, but with different content are renamed. You can also use this mode to replace existing blocks with a newer version. When you use the overwrite conflict resolution, cells with the same name are overwritten.
- new\_top mode-Use this mode to place selected top cells into a new top cell at the specified location and orientation. Unplaced top cells from input layouts (cell D in this example) appear as additional top cells in the merged layout or they can be dropped using the extract transformation. By default, cells with the same name but with different content are renamed.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

- prime mode-Use this mode to place fill layout top cells in the design top cell at the specified location and orientation. By default, cells with the same name but with different content are renamed.

<!-- image -->

## Using the Main Modes Wizard

To perform a library merge, new\_top merge, or prime merge, use the Main Modes merge wizard as follows:

1. In the Select Merge Mode page, choose a merge mode under Main Modes .

When using the merge command, use the argument mode to specify a mode.

The Input Layouts page has three main areas:

- Layout files table: This area includes a table of the inputs layouts and the layout options that have been applied to them. The table columns in bold indicate that the column is editable. Columns in the table can be dynamically added or removed. By default, the Layout Files , DBU (m) (read-only), Cell Map , Layer Map , and Include/ Exclude Layers columns are displayed.
- Side buttons: These buttons can be used to arrange the order of the layouts, add or remove layouts, add a layout directory, and choose the columns to display in the layout files table.

<!-- image -->

<!-- image -->

- Options: This area includes the additional options that you can apply to multiple layouts. You can set the options and use the Apply to Selected button to apply the layout options to the selected layouts.
2. In the Input Layouts page, do the following:

<!-- image -->

Use the layout files table to specify the input layouts.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

| Input Options   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | command-line argument   |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Cell Map        | Specify the convention for mapping the input cell names with the output cell names. You can enter the cell mapping in the following ways: ◦ Double-click the Cell Map field and enter the cell mapping. For example, 'A A1 B B1' maps the input cell A to the output cell name A1 and B to B1. ◦ Double-click the Cell Map field and provide the path to a file that has the cell mapping specified. ◦ Double-click the Cell Map field and click to open the cell mapping dialog. Do one of the following: ▪ Choose Select Map File and then browse and select a file that has the cell map specified. ▪ Choose Specify Cell Mapping and then enter the name of the cell you want to map in the Cell column and the name of the cell in the Map to Cell column. ◦ You can also enter the cell mapping in the Cell Map field under Options and then click Apply to Selected to apply mapping to the selected layouts. Note: The Cell Map option is mutually exclusive with the Suffix/Prefix options. | cell_map {A A1 B B1}    |

<!-- image -->

<!-- image -->

| Input Options   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | command-line argument       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Layer Map       | Specify the convention for mapping the input layers with the output layers. You can enter the layer mapping in the following ways: ◦ Double-click the Layer Map field and enter the cell mapping. For example, '0:0 1:0 2:2 4:3' maps the input layer 0:0 to the output layer 1:0 and 2:2 is mapped to layer 4:3. ◦ Double-click the Layer Map field and provide the path to a file that has the layer mapping specified. ◦ Double-click the Layer Map field and click to open the layer mapping dialog. Do one of the following: ▪ Choose Select Map File and then browse and select a file that has the layer mapping specified. ▪ Choose Select Layers and select the layers you want to map from the Select Layer column, and enter the corresponding output layer in the Map to Layer column. ▪ Use the Filter box to filter layers. ▪ Right-click and use the options to either include or exclude the selected layer, include or exclude all layers, include or exclude filtered layers, revert the mapping for the selected layer, filtered layers, or for all layers, and include only the visible layers. ◦ You can also enter the layer mapping in the Layer Map field under Options and then click Apply to Selected to apply mapping to the selected layouts. Note: The Layer Map option is mutually exclusive with the Layer Offset option. | layer_map {0:0 1:0 2:2 4:3} |

<!-- image -->

<!-- image -->

| Input Options          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | command-line argument              |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Include/Exclude Layers | Specify the layers you want to either include or exclude using the Include/Exclude Layers field when performing a merge. If you do not specify the layers, all the layers for that layout are included in the merge operation. You can select the layers for including or excluding in the following ways: ◦ Double-click the field and choose either Include Layers or Exclude Layers from the drop-down, and then enter a list of layer:datatype values or a range of layers and datatypes, such as 5, 7:2, 8:4-5 or 12-15. You can also click and filter the layers you want to select. ◦ Under Options , enter the layers to include or exclude and then click Apply to Selected to apply the selection to the selected layouts. ◦ Right-click and use the options to either include or exclude the selected layer or all layers, and include only the visible layers. | exclude_layers {5 7:2 8:4-5 12-15} |

<!-- image -->

Select the layout(s) in the layout files table and then use Options to specify additional options for the input layouts:

<!-- image -->

| Additional Options   | Description                                                                                                                                                                                                                                                                                                                              | command-line argument               |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| Extract              | Type the cell name you want to extract or click to use the filter and select the root cell. Click Apply to Selected to apply the option.                                                                                                                                                                                                 | extract {TOP}                       |
| Prefix/Suffix        | Use this to rename all cells in the given layout by prefixing or suffixing cell names with the given string. Set the drop-down to Prefix or Suffix and enter the string. Click Apply to Selected to apply the prefix or suffix to the selected layouts. Note: The Prefix/Suffix options are mutually exclusive with the Cell Map option. | cell_prefix PREF_ cell_suffix _POST |
| Layer Offset         | Specify the layer:datatype to offset the layers. Layer and datatype are non-negative integers. Click Apply to Selected to apply the offset to the selected layouts. Note: The Layer Offset option is mutually exclusive with the Layer Map option.                                                                                       | layer_offset 3:4                    |

<!-- image -->

| Additional Options                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | command-line argument                                                                                                    |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| ◦ Paths to Polygons ◦ Omit text ◦ Omit Cell Properties ◦ Omit Fig Properties | To apply these options, select the check box of the option and click Apply to Selected to apply the option to the selected layouts. ◦ If Path to Polygons is selected, then the paths in the selected input layouts are converted to polygons. ◦ If Omit Text is selected, text objects are dropped from the selected input layouts. ◦ If Omit Cell Properties is selected, cell properties are dropped from the selected input layouts. ◦ If Omit Fig Properties is selected, the fig properties are dropped from the selected input layouts. | omit_text true paths_to_polygons true omit_properties all omit_properties cell_propertiesomit_prope rties fig_properties |

## 3. Click Next .

## 4. In the Specific Merge Options page, do the following

<!-- image -->

| Specific Merge Option                   | Description                                                                                                                                                                                                                                                                                    | command-line argument   |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| For prime and new_top merge modes only: | For prime and new_top merge modes only:                                                                                                                                                                                                                                                        |                         |
| Cells                                   | Specifies the cell to be placed in merged layout. Double-click and enter the cell name from the input layout, or click and use the filter to select a cell name. For prime mode, the Cells column for the first layout is not editable. You can set the prime-cell in the Output Options page. | cell {TOP}              |

<!-- image -->

<!-- image -->

<!-- image -->

| Specific Merge Option        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | command-line argument                                                                                      |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Conflict Resolution Strategy | Specifies the action to take during cell conflict: ◦ Overwrite : The application overwrites conflicting cells with ones coming from a later input layout. ◦ Auto-Rename : Specifies the suffix to use for automatically renamed cells in Auto-Rename mode. The application implies content-based conflict resolution to determine when two cells conflict. Cell with the same name and same contents are not considered conflicting and are not duplicated in the output. The cell name is suffixed with a signature to alter the conflicting cell name uniquely. ▪ Auto Rename Suffix : Specifies the suffix to use for automatically renamed cells. Use the # character to indicate where to place the hash string. If # is not specified, the hash string is appended to the end of the suffix. For example, _RN_# renames the cell CELL to CELL_RN_1234 (where 1234 is the cell hash). Command-line argument: -autorename_suffix auto_suffix ◦ Join Shapes (Polygons and Text) / Join Shapes and References : The application joins the contents of the cell coming from library layouts (second and the rest of the layouts) with the contents of the cell from the design layout (first input layout). You can specify whether a library layout contributes only shapes or the whole cell content by choosing either Join Shapes or Join Shapes and References . ◦ Error Out : The application issues an error message containing information on conflicting cells and terminates the merge operation without producing an output. | - conflict_resolution { overwrite&#124; rename_conflicts &#124; join_shapes &#124; join_all &#124; error } |
| Error on Warning             | If selected, then warnings that appear while merging the layouts are treated as errors and the merge operation is stopped. Layout server warnings on input layouts, such as warnings about undefined cells in input layouts are not treated as errors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | -error_on_warning 1                                                                                        |

## 5. Click Next .

## 6. In the Output Options page, enter the following options:

| Output Option                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                | command-line argument       |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Output DBU                           | Choose an output DBU option from the drop-down: ◦ Specify DBU: Specify the DBU of the merged output layout. ◦ Smallest Layout DBU: matches the smallest DBU from the input layouts. ◦ Greatest Common Divisor: (default) uses the greatest common divisor (GCD) of all input layouts.                                                                                                                                                                      | -dbu 1e-09                  |
| Cells to Extract (library mode only) | Specify the top cells to extract for the library mode.                                                                                                                                                                                                                                                                                                                                                                                                     | extract A                   |
| Top cell name (new_top mode only)    | Specify the new top cell name for the new_top mode.                                                                                                                                                                                                                                                                                                                                                                                                        | -top TOP                    |
| Prime Cell (prime mode only)         | Specify the prime cell name. The specification is only available for the first input layout for the prime mode. Note: The application errors out in case the prime cell name is not specified for a multi-root prime layout. In case of single root prime layouts, the prime cell might be omitted and the only root cell is used as the prime cell. Note: Specifying the cells for prime and input-layouts allows the tool to process the layouts faster. | prime_cell TOP              |
| File format                          | Choose the file format of the output merged layout. The default is OASIS OPT (Optimized OASIS).                                                                                                                                                                                                                                                                                                                                                            | -format oasis_opt           |
| Compression                          | Use this option to set the compression level for the OASIS file you save. The default is 6.                                                                                                                                                                                                                                                                                                                                                                | -compression 4              |
| Compaction                           | Select this option if you want to compact the OASIS file you save. The default is off .                                                                                                                                                                                                                                                                                                                                                                    | -compaction 1               |
| Output filename                      | Specify the output file name.                                                                                                                                                                                                                                                                                                                                                                                                                              | -out {path/out2.opt.oas is} |
| Open output layout file              | Select this option to open the output layout file when the merge is completed.                                                                                                                                                                                                                                                                                                                                                                             |                             |

<!-- image -->

<!-- image -->

| Output Option                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  | command-line argument                                                                                                    |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Cell Content Handling ◦ Covert paths to polygons ◦ Omit text ◦ Omit fig properties ◦ Omit cell properties | To apply these options, select the check box of the option. ◦ If Convert paths to polygons is selected, then path objects are converted to polygons in the merged layout. ◦ If Omit text is selected, text objects are dropped in the output layout. ◦ If Omit fig properties is selected, the fig properties are dropped from the output layout. ◦ If Omit cell properties is selected, cell properties are dropped from the output layout. | omit_text truepaths_to_polyg ons true omit_properties all omit_properties fig_properties omit_properties cell_properties |
| Diagnostics                                                                                               | Diagnostics                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                          |
| Info                                                                                                      | If selected, a table with detailed information about all the cells is added to the log when the merge operation completes. Can be used in any merge mode.                                                                                                                                                                                                                                                                                    | -verbose {info}                                                                                                          |
| Undefined Cells                                                                                           | If selected, a table with cells that remain undefined after the merge operation completes is added to the log.                                                                                                                                                                                                                                                                                                                               | -verbose {undefined_cells}                                                                                               |
| Renamed cells                                                                                             | If selected, a table with cells that get renamed after the merge operation completes is added to the log.                                                                                                                                                                                                                                                                                                                                    | -verbose {renamed_cells}                                                                                                 |
| Application log                                                                                           | Select this option if you want the output information sent to the application log file.                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                          |
| File                                                                                                      | Choose a file for storing the output information.                                                                                                                                                                                                                                                                                                                                                                                            | -log file_path                                                                                                           |

## 7. Click Finish .

The merge operation is completed.

## Additional Modes (using the layout merge command)

The additional merge mode has the overwritingCells , newTopCells , and adding merge modes. You can use the additional modes merge wizard or the layout merge command to perform the merge operation.

<!-- image -->

- overwritingCells mode-This mode combines root cells of two layouts and overwrites cells of the same name. Use this mode only with exactly two input layouts. Cells from the second input layout overwrite cells from the first layout, with two exceptions:
- Cells in the first layout may be 'protected' from being overwritten by cells from the second layout by putting them in a 'preserve cells' list.
- The first root cells of the two input layout are combined together, rather than obeying the 'overwrite' rule, the combined output cell is given the name of the first root cell of the first input layout.
- newTopCells mode-This mode merges two layouts into a new top cell similar to the new\_top mode; in addition, it combines first root cells and preserves chosen cells. Use this mode only with exactly two input layouts. A new top cell is created and references to cells from the two input layouts are added to it. Cells in the first layout may be 'protected' from being overwritten by cells from the second layout by putting them in a 'preserve cells' list. If the first root cells of the two input layouts have the same name, then they will be combined together instead of obeying the 'overwrite' rule.
- adding mode-This mode combines root cells of two layouts, resolving conflicts for child cells by providing cell prefixes. Use this mode only with exactly two input layouts. The output layout will have exactly one root cell. The combination of the first root cells of the two input layouts, named after the first root cell of the first input layout. All cells from the hierarchies of the first root cells of both layouts are saved, using the second input layout's mandatory prefix to resolve cell name conflicts. If either layout 'protects'

<!-- image -->

<!-- image -->

<!-- image -->

a cell by putting it on its 'preserve cells' list, then that layout's version of the cell will be saved.

<!-- image -->

## Using the Additional Modes Merge Wizard

To perform an overwritingCells merge, newTopCells merge, or adding merge, use the additional modes wizard as following:

1. In the Specify Layouts to Merge page, provide layouts for merging in the Layout Filename column.

You can enter a file name manually or, if there are layouts currently open, you can choose from the list of currently open layouts by double-clicking in the cell. You can also click the Browse button ( ) to open the Select Input File dialog box to choose one or more layout files. You can change the order of the files using the arrow keys, and you can remove a file from the list by clicking the Delete button ( ).

2. You can provide layer offsets for each layout in the Layer Offset column.

Layer offsets will be added to the original layers in the layout. For example, if you specify a layer offset of 1:2, the input layer 3:4 would become 4:6 in the merged layout. If you specify a layer offset of 0:0, the input layer will not be changed in the output layout.

3. After you have entered all layout file names and layer offset amounts, click Next
2. .
4. In the Specify How to Merge Cells page, provide data for each input layout in the following columns:
- Offset (X,Y) nm (for newTopCells mode only) - Cells will be put into the new top cell of the output layout with the provided offset. The value 0,0 means that cells will be output in their same places as in the input layouts.
- Scale (for newTopCells mode only) - Cells will be put into the new top cell of the output layout with the provided scaling. The value 1 means that the cells will be output without scaling, as in the input layouts.
- Prefix (for adding mode only) -You can add a prefix to the secondary layout's cell names to avoid possible cell name conflicts.

<!-- image -->

- Preserved Cells - Provide the cells to preserve from each layout. You can enter a cell name manually, or, if the layout for which you're providing the cell is currently open, you can click the Browse button at the right of this field, choose a cell name, select the check box beside the cell name, and click OK .
5. After you have chosen the cell, click Next .

In the Specify Output page at the top, you will see a read-only table listing your chosen layouts and the DBUs (only for currently open layouts). In the Output group below, you will provide output options.

6. Specify the DBU of the output layout in the Output DBU: field.

The output DBU can be different from that of the input layouts.

## Note:

If the input file DBUs are not integer multiples of the output file DBU, then some distortions may occur as the shapes and references will snap to the output DBU.

7. Select the output file format by clicking the Down Arrow button on the right of the File format: drop-down list.

You can save the layout to GDSII, GDSII.GZ, OASIS, or OASIS OPT (default).

## Note:

Due to limitations in GDSII, the application cannot output polygons with more than 8191 points as a GDSII layout. If your polygon has more than 8191 points, save the output as an OASIS file.

8. Specify the output file name.

You can enter a file name or click the Browse button on the right of the Output filename: text entry field, which will open the Select Output File dialog box where you can select an output file.

9. Select Omit text to exclude all text objects from the extracted output layout file.
10. Select Show results from the merge operation in the command history window to write a report for each input cell to the command history and log file.

The information includes the status of the cell, the output name of the cell, and the source layout of the cell.

11. Select Open output layout file to open the output layout file after you complete the merge operation.
12. Click Finish to complete the merge operation.

## Command Options

Additional options available for merging layouts using the layout merge command include:

- Specifying mapping for individual layers using the layer\_map option.
- Specifying mapping for individual cells using the cell\_map option.
- Specifying an angle and mirror for new top mode using the angle and mirror options.
- Specifying OASIS save options for compression, compaction, and modals using the -compression , -compaction , and -modals flags. If these options are not specified, the settings of default layout\_oasis\_save\_options is used.
- The -info flag will write information about each input cell to the command history and log file. The information includes the input cell name and file name, if it is saved to the output file, and the cell's name in the output file.

For additional information about these commands and options, see The IC Validator WorkBench Command Manual .

## Comparing Layouts and Cells

You might want to compare two layouts of the same or of different formats and see the differences. You also might want to compare two cells belonging to the same or different layouts, and get their differences. You can accomplish these tasks by using the Layout Compare window on the File menu or by using the Cells option available in the Compare group on the Home tab. You can also compare cells by dragging a non-active cell over the active cell's layout.

You can also compare layouts and generate the output as a VUE file. You can then open this VUE file in the PYDB Viewer or the IC Validator VUE tool and visually browse through each difference in the compared layouts.

You can also compare layouts or cells by using the lacoto layout compare and lacoto cell compare commands in the Command Pane. These commands are described in detail in the IC Validator WorkBench Command Manual .

The following topics describe how to compare two layouts or two cells and view the differences:

## Comparing Two Layouts

To compare two layouts from the command-line, use the lacoto layout compare command.

<!-- image -->

To compare any two layouts:

1. On the File menu, click Layout Compare .

The Layout Compare window opens.

2. Under Input Layouts , select the layouts that you want to compare.

<!-- image -->

Click and then choose the layout files for the First and Second layouts. All layouts files that ICVWB can read are supported for comparison including the following:

- GDSII (.gds)
- GDSII GZ (.gds.gz)
- OASIS (.oas)
- OASIS GZ (.oas.gz, .oasis.gz)
- OASIS OPT (.opt.oasis)
- LEF 5.8 (.lef)
- LEF 5.8 GZ (.lef.gz)

You can also compare open layouts or newly created layout files that have not been saved on disk. The list of open layout files appear in the drop-down menu of the First and Second input layout fields.

3. Under Output Options , select the format and destination of the output files:
- Format : Select the format of the output layout files from the drop-down menu. The available formats are: GDSII , GDSII.GZ , OASIS , OASIS OPT , TCL , and VUE .
- Objects not in second layout : This layout file will contain only the objects in the first layout that do not match any objects in the second layout. If required, change the name and destination of the output file. By default, the name of the output file is the name of the input file suffixed with \_diff1 followed by the format extension as selected by you. For example, if your first input layout file is layout1.gds , and you selected OASIS as the output format, then the corresponding output layout file name will be layout1\_diff1.oas .
- Objects not in first layout : Similarly, select the format of the second output file from the drop-down menu and modify its name and destination, if required.
4. Select the Open output layout files check box to open the output files in the application after the comparison is done.
5. Set the Options before comparing your layout files.

<!-- image -->

<!-- image -->

These options are described in the #unique\_116 option section. The defaults for these options can be set in the Compare options from the Options dialog box.

6. Click Compare to compare the two layouts.

Under Summary , you can see the output summary of the compared layouts. It shows the number of unmatched objects and unmatched cells (if any) between the two layouts.

Click the Home tab to view the output files. For viewing the Tcl-format output files, you can use the Tcl Debugger or open the files using any text editor.

## Comparing Two Cells

You can compare cells either by dragging a cell over another cell or by using the compare option available on the ribbon. If you want to compare two cells by using the commandline, see the lacoto cell compare command.

To compare two cells:

1. Open the layout file or files whose cells you want to compare.
2. In the Compare group on the Home tab, set the compare options by clicking the down arrow under Cells and selecting Options .

The compare options are displayed in the Options dialog box. These options are described in the #unique\_116 section. You can set the defaults for these options here.

3. To compare the two cells, do one of the following:
- Click Cells in the Compare group on the Home tab.

The Compare Cells With dialog box opens and lists the active layout's cells. Choose the Layout whose cell you want to compare with the active layout's cell. Type the cell name in the Match field or select the cell from the list and click OK .

<!-- image -->

- From the Tree View or the Layouts View , drag the non-active cell, which you want to compare, over the layout of the active cell, and choose Compare from the context menu.

<!-- image -->

The unmatched objects in the two compared cells are displayed as side cells. For example, if an object that is available in cell A, but not in cell B, the Side Cells view displays that extracted object as not\_in B\_1 . Similarly, if an object in cell B is unmatched in Cell A, then the side cell will be not\_in\_A\_1

4. In the Side Cells view, change how you want the unmatched objects to display.

See the #unique\_55 section on how to use side cells.

## Viewing the Output Summary

After you compare two layouts, you get an output summary in the Command Pane such as the following:

```
#-> first_layout {unmatched_fig_count 1} second_layout {unmatched_cell_count 1 unmatched_fig_count 1}
```

<!-- image -->

<!-- image -->

When you select one of the standard output formats, these differences (unmatched objects) are extracted and saved as layout files. You can choose to open these layout files after you compare two layouts.

If you select Tcl as the output format, the differences are stored as a list of key-value pairs in a .tcl file that can be easily converted into Tcl arrays. For more information on the Tcl list of key-value pairs, see Key-Value Pairs in Tcl Output of Compared Layouts in the IC Validator WorkBench Command Manual .

When comparing cells, the GUI displays the output only using the Side Cells view and does not display a summary. You need to use the lacoto cell compare command to see the differences summary. For more information on the Tcl list of key-value pairs, see KeyValue Pairs in Tcl Output of Compared Cells in the IC Validator WorkBench Command Manual .

## Generating VUE Output

When comparing layouts, you can also generate the output as a VUE file that can be opened using the PYDB Viewer feature or the IC Validator VUE tool. Generating the compared output as a .vue file allows you to visualize and review the layout differences one-by-one on the original layout using PYDB Viewer , navigate through the differences, group differences by their type or cell, and categorize them.

## Viewing Compared Layouts in PYDB Viewer

To view the layout differences in PYDB Viewer :

1. Select the input layout files you want to compare.
2. Under Output Options , select the format as VUE .
3. For Object differences , you can modify the auto-generated .vue file name and folder. The PYDB file will be saved in the same directory as the .vue file and will be prefixed

by PYDB\_.

4. Select the Open output file check box if you want the .vue file to load in the PYDB Viewer after the layouts are compared.
5. Set the compare Options as described in the #unique\_116 section.
6. Click Compare .

<!-- image -->

The PYDB Viewer window opens with the generated VUE file loaded and the original (first) layout opened. If the compared layouts have more than one root cell, choose the root cell from the Select Root Cell dialog box.

## Layout Compare

<!-- image -->

## Navigating Layout Differences in PYDB Viewer

The layout differences are categorized into the following types and are displayed in the Violation Browser when you expand a cell:

- Extra\_figures : The original (first) layout has extra figures that are not there in the compared (second) layout.
- Missing\_figures : Figures are missing from the original layout but are there in the compared layout.
- Extra\_cells : The original layout has extra cells that are not there in the compared layout.

When you click a cell, all the layout differences are listed in the Error List pane for that cell. If you expand a cell in the Violation Browser pane and choose a particular difference type, then only those differences are listed in the Error List . The Error List pane shows the details of the extra or missing cells and figures such as, coordinates, vertices, and comments for the differences. The Violation Details pane shows the description of the currently selected violation and errors.

<!-- image -->

- When you right-click a cell and select Highlight , all the layout differences for that cell are highlighted in the opened layout.
- When you right-click a difference type and select Highlight , only those differences are highlighted in the opened layout. For example, if you right-click Missing\_figures from the Violation Browser and select Highlight , only the missing figures are highlighted in the opened layout.

## Note:

Highlighting is done on the first layout, so when an object appears only on the second layout and is missing from the first layout, the difference is highlighted on the first layout in place of the missing property or object.

<!-- image -->

<!-- image -->

- When you right-click a record in the Error List pane and select Highlight , that difference is highlighted in the opened layout. If the show information option is enabled (Ctrl+D), then the tooltip shows the details when you hover over the highlighted figure.
- See the following sections for information on navigating, viewing, and searching violations in the PYDB Viewer, and setting the PYDB options:
- #unique\_311
- #unique\_312
- #unique\_313
- #unique\_314

<!-- image -->

<!-- image -->

## Using IC Validator with IC Validator WorkBench

This chapter describes how to use IC Validator tools such as ICV Live DRC, ICV VUE, and ICV Launch from IC Validator WorkBench and how to work with PYDB Error Data.

This chapter includes the following topics:

- ICV Live DRC for IC Validator WorkBench
- Loading TechFiles
- Loading and Viewing DRC Errors Using ICV VUE
- Running DRC, LVS, and PERC Using ICV Launch
- Using the ICVWB PYDB Error Data Viewer

## ICV Live DRC for IC Validator WorkBench

The IC Validator Live DRC tool enables you to run DRC directly within IC Validator WorkBench helping you find and fix DRC violations actively and therefore reducing the DRC runtime significantly. Using the ICV Live DRC tool, you can set up an area and run incremental DRC check runs for that area on your layout. You can then browse and highlight the errors and also setup recipes (a list of rules to be checked) in IC Validator WorkBench.

The following topics cover the workflow for using ICV Live DRC:

- Setting Up ICV Live DRC for IC Validator WorkBench
- Configuring ICV Live DRC
- Adding a Check Area
- Running ICV Live DRC
- Browsing Results and Highlighting Errors
- Creating Custom Recipes Using the Recipe Editor

## Setting Up ICV Live DRC for IC Validator WorkBench

Before starting IC Validator WorkBench, set the ICV\_HOME\_DIR environment variable using a command such as the following:

```
setenv ICV_HOME_DIR /root_dir/icv
```

You can also set the variable after starting ICVWB by using the following command in the Command Pane :

```
set ::env(ICV_HOME_DIR) /root_dir/icv
```

You can also set the ICVWB\_ICVLIVE\_SOCKET environment variable to run ICV Live on a specific port. If ICVWB\_ICVLIVE\_SOCKET is not set, a random socket port is used.

```
set ::env(ICVWB_ICVLIVE_SOCKET) 33893 #-> 33893
```

When you start the ICVWB application, the ICV Live DRC tool is available in the ICV Live DRC tab. However, to use the tool, the IC Validator environment variable (ICV\_HOME\_DIR) needs to be set.

<!-- image -->

## Configuring ICV Live DRC

For running ICV Live DRC, you only require the runset file. However, you can also configure other ICV Live DRC settings such as setting the halo size, applying rule recipes (if you want to skip any rules), and selecting the highlight color in the IC Validator Live DRC Configuration window.

## Setting up the IC Validator Live DRC Configuration Window

<!-- image -->

To open the IC Validator Live DRC Configuration window, click the ICV Live DRC tab and on the Violations/Recipes group, click .

In the IC Validator Live DRC Configuration window, you can configure the run settings, check filter, and the highlighting preferences. The following table describes the fields in the IC Validator Live DRC Configuration window.

<!-- image -->

<!-- image -->

| Field         | Description                                                                                                                                                                                                                                                                                                                                                                          |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Configuration | Select a different configuration from the drop-down menu or create a new one for the storing the default settings. The configuration file is stored as a .icvlc file.                                                                                                                                                                                                                |
| Run Settings  |                                                                                                                                                                                                                                                                                                                                                                                      |
| Runset File   | Select the runset (.rs) file for running the DRC checks. The window by default loads the last opened runset file. You can control whether or not to load layers names from the runset by selecting the Load layer configuration check box in the Violations/Recipes group. By default, when the runset is set here, the layout layer names are updated according to the runset data. |
| Halo Size     | Set the size of the halo (in um). It is used when capturing the check area. The default is 1.00 um.                                                                                                                                                                                                                                                                                  |
| CLF File      | Use this filed to add command-line options to your DRC run using a text file.                                                                                                                                                                                                                                                                                                        |
| Check Filter  |                                                                                                                                                                                                                                                                                                                                                                                      |
| Check Layers  | Select the layers you want to include in the check run: • All Layers: Polygons in all the layers of the check area will be included in the check run. • Visible Layers: Only the polygons in the visible layers of the check area will be included in the check run.                                                                                                                 |
| Rule Recipe   | Select a recipe file from the list. • Click to select a recipe file. • Click to refresh the contents of the list. • Click to create a new recipe file or click to edit the selected recipe file.                                                                                                                                                                                     |

<!-- image -->

<!-- image -->

| Field                 | Description                                                                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exclude Density Rules | Selecting this option excludes density rules from the runset file when running a check.                                                                                                                                                                                         |
| Preference            | Preference                                                                                                                                                                                                                                                                      |
| Highlight Control     | Keep Existing Highlights: if checked, the previous highlight is not cleared when new highlights are created.                                                                                                                                                                    |
| Follow Mode           | Set how to follow the error marker when highlighting errors. • Zoom with Factor: Zooms to the highlight shape with the set factor value. • Pan: Pans to the center of the highlighted shape without changing the zoom. • Off: Does nothing. The follow mode is switched off.    |
| Auto Color Change     | Set color selection when highlighting errors. • Per Highlight: The color changes for every highlight. • Per Rule: The color changes only when the current highlight and the previous highlight do not belong to the same rule. • Fixed: Choose a color to highlight the errors. |

## Adding a Check Area

After configuring the ICV Live DRC settings, you can select the area on which you want to run the DRC check. You can select an area from a list, specify the coordinates for the check area, or manually select an area on your layout.

To add a check area:

1. On the ICV Live DRC tab, in the Run group, click the add check area button.
2. In the IC Validator Live DRC Add Check Area window, provide a name for the check area.

This area is stored for the current session and is available from the list in the Run group.

3. Provide the coordinates for the check area using one of the following:
- Provide the lower-left or upper-right coordinates (X/Y) of your current layout.
- Click the Select Area button and then drag the mouse on your layout to select an area.

<!-- image -->

- Click the User Current Area to select the current view-port coordinates of your layout.

<!-- image -->

## 4. Click OK .

5. You can also choose an area from the list in the Run Group :
- Current view: Sets the current view-port as the check area.
- Cell: Sets the current opened cell's bounding box as the check area.
- Area: latest: Sets the area of your last run as the check area.
- Area:&lt; area name &gt;: Sets a custom area you have created as the check area.

<!-- image -->

## Note:

When a check area is selected, the view is updated accordingly.

You can also zoom to the latest check area by clicking .

## Setting the Capture Mode

<!-- image -->

In the Run group, you can set the capture mode to one of the following by clicking either or : 口

- Protrusion On : Polygons within the check area and intersecting with it are included entirely in the check run. From the example in Figure 50, the check area will include Polygon 1 (entirely), Polygon 2, and the Cell's polygons, but not Polygon 3. This is the default mode.

<!-- image -->

- Protrusion Off : Polygons within the check area are included entirely in the check run, and polygons intersecting with the check area are cropped at the check area boundary. From the example in Figure 51, the check area will include a part of Polygon 1 within the check area, Polygon 2, and the Cell's polygons, but not Polygon 3.

You can set the size of the halo in the IC Validator Live DRC Configuration window.

Figure 50 Capture Mode: Protrusion On

<!-- image -->

Figure 51 Capture Mode: Protrusion Off

<!-- image -->

## Running ICV Live DRC

To run an incremental DRC run on the selected area using ICV Live DRC:

- On the ICV Live DRC tab, in the Run group, click the Run Check button . The Running ICV Live DRC dialog box displays.

<!-- image -->

When the run is completed, a message such as the following is displayed in the Command Pane :

- # [ICV Live DRC] Check success with 14 violated rules in 2 second

## Browsing Results and Highlighting Errors

After running ICV Live DRC for an area on your layout, you can browse and highlight errors using the options available in the Highlighting group of the ICV Live DRC tab or using the options available in the ICV Live Violation Viewer window.

## Highlighting Errors Using the ICV Live DRC Toolbar

You can also use the options available in the Highlighting group of the ICV Live DRC tab to browse and highlight errors. The Highlighting group includes a Rules list that lists the rules having errors as configured in the IC Validator Live DRC Configuration window. The Rules list displays the current error rule that you are browsing. You can click the dropdown and select a different rule to browse the errors of that rule.

<!-- image -->

In addition to the Clear All Highlights , Highlight Previous , and Highlight Next buttons that are available in the ICV Live DRC Violation Viewer , the Highlighting group includes a Highlight All and a Highlight Current buttons. Highlight All highlights all the errors on the layout and the Highlight Current button highlights the current error. +

<!-- image -->

<!-- image -->

## Highlighting Errors Using ICV Live DRC Violation Viewer

To open the Violation Viewer, click in the Violations/Recipes group. The ICV Live DRC Violation Viewer window lists all the rules with errors as configured in the Check Filter options of the IC Validator Live DRC Configuration window. The lower-left and upperright coordinates for the errors and the description for the rules are also displayed.

The following table list the actions you can perform for browsing and highlighting errors using the ICV Live DRC Violation Viewer .

Table 45 ICV Live DRC Violation Viewer Options

<!-- image -->

| Option   | Description                                                                                                                                                                                                                                                                                                                                         |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          | Filter Box. Enter the full or partial name of the item or rule you want to select. Click the case sensitive button to perform a case-sensitive match.                                                                                                                                                                                               |
|          | Zooms to the last checked view port.                                                                                                                                                                                                                                                                                                                |
|          | Highlights the previous error from the rule list.                                                                                                                                                                                                                                                                                                   |
|          | Highlights the next error from the rule list.                                                                                                                                                                                                                                                                                                       |
|          | Clears all the highlights of all rules.                                                                                                                                                                                                                                                                                                             |
|          | Keep or remove existing highlights when browsing the errors. If selected, a highlight is created for every error and all the previous highlights are retained in the Side Cell view. When unselected, only a single highlight is displayed in the Side Cell view and the previous highlights are not retained.                                      |
|          | Zooms to the last highlight.                                                                                                                                                                                                                                                                                                                        |
|          | Sets how to follow the error marker when highlighting errors. • Zoom : Zooms to the highlight shape with the set factor value. You can set the zoom factor in the IC Validator Live DRC Configuration window. • Pan : Pans to the center of the highlighted shape without changing the zoom. • Off : Does nothing. The follow mode is switched off. |

Table 45 ICV Live DRC Violation Viewer Options (Continued)

<!-- image -->

## Creating Custom Recipes Using the Recipe Editor

Recipe is a file specifying the rules that will be checked during the run. ICV Live DRC allows you create custom recipes so you can select the rules defined in the runset file that you want to be checked during the run.

To create a custom recipe:

1. In the IC Validator Live DRC Configuration window, click the Create new recipe button available under the Check Filter options.
2. In the Create Recipe dialog box, enter a name for the recipe.

You can copy a recipe by selecting an existing recipe file from the Copy from list.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

3. In the Recipe Editor , enter the following information:
- Recipe file description : This description is displayed in the recipe list in the Violations/Recipes group.
- Recipes : The recipe name.
- Filter : Enter the full or partial name of the item or rule you want to filter. Click to perform a case-sensitive match.
4. Add the rules from the Unselected column to the Selected column that should be included in your recipe.

The Unselected column lists the rules obtained from the runset file.

5. Click Save to save the new recipe file on your system.

The recipe file is stored as a .icvrcp file.

6. In the IC Validator Live DRC Configuration window, click the refresh to refresh the current loaded recipes in ICV Live DRC. C

The recipe is also added to the Recipes list in the Violations/Recipes group on the ICV Live DRC tab.

## Loading TechFiles

You can load IC Compiler II (ICC2), Custom Compiler (CC), and Laker technology files, layer map files, and ICV runset files in IC Validator WorkBench using the TechFiles drop-down button on the Home tab or by using the layers configuration button from the Layout Layers view.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Import CC or Laker Tech Files

1. In the User group, click TechFiles &gt; CC/Laker .
2. In the Import Technology File dialog box, choose the technology format: Custom Compiler (CC) or Laker .
3. Do one of the following:
- Select Specify Directory and select a directory that contains the display files (.drf for CC and .dsp for Laker), layermap files (.map or .layermap), and the technology (.tf) files.
- Select Specify Files and provide the Technology , Display resources format , and Layer map files separately.

<!-- image -->

4. For CC only:
- a. Enter the Preferences file for controlling the layout connectivity, if required.
- b. Enter the display name or leave it blank to use the default display name.
5. Under Apply to , choose whether you want to apply the configuration to the current layout or on all layouts.
6. Select the Configure layout layers only check box to configure existing layers only and not create new layers.
7. Click OK .

## Import ICC2 Tech Files

1. In the User group, click TechFiles &gt; ICC2 .
2. In the Import ICC2 Technology File dialog box, do the following:
- a. Click the browse button ( ) and select a technology (.tf) file.
- b. Optionally, you can also provide a layer map file. Click the browse button ( ) and select a layer mapping (.map or .txt) file.
- c. Click OK .

The ICC2 layer configurations and layer connectivity are loaded in the ICVWB application.

## Import Layer Names From ICV Runset Files

1. In the User group, click TechFiles &gt; ICV Runset .
2. In the Browse to ICV Runset File dialog box, select an ICV runset (.rs) file and click Open .

You can also import layer names from the ICV runset file using the following command: drc runset import /path/to/runset.rs

The layer names are loaded from the ICV runset file.

<!-- image -->

## Load ICV Layer Map Files

1. In the User group, click TechFiles &gt; Layer Map .
2. In the Browse to Layer Map File dialog box, select a layer map file (.map or .txt) and click Open .

Layer names are loaded from the ICV layer map file. You can also import an ICV layer map file using the layer import command. You can find a sample layer map file in the layer import command help.

## Loading and Viewing DRC Errors Using ICV VUE

You can load and review DRC results by opening the IC Validator VUE tool directly from IC Validator WorkBench and then loading a results (a .vue) file.

## Note:

To start ICV VUE from IC Validator WorkBench, you need to set the ICV\_HOME\_DIR environment variable before starting IC Validator WorkBench. For example, from the command-line, enter:

```
setenv ICV_HOME_DIR <path to ICV_VUE> <path to ICV WorkBench>/bin/icvwb
```

To load and review DRC results:

1. In the User group, click ICV\_VUE ( ).

The VUE application starts with the Load Results tab opened.

You can also open VUE in multi-DRC mode by clicking the drop-down arrow on the VUE button and selecting Multi DRC DB . Multi-DRC mode allows you to open tabs to view and review multiple DRC errors in the same window. You can load multiple databases (VUE files) at the same time and run multiple simultaneous ICV VUE connections.

<!-- image -->

<!-- image -->

2. In the Load Results tab of VUE, click the browser icon in the Results File box and select a .vue file.

The browser displays only the directories and *.vue files.

After you load the VUE file, the Run Summary tab provides a high-level summary of the errors. If DRC errors exist, a summary of each error and count are given. If LVS errors exist, a count of passed and failed equivalence points is given.

The layout specified in the .vue file is loaded by default. To skip loading the layout specified in the .vue file and instead highlight the errors in the current open layout, enter VUE::SetLoadVUELibrary 0 in the IC Validator WorkBench command pane. You can also preset this command in the start-up files.

<!-- image -->

Chapter 8: Using IC Validator with IC Validator WorkBench Loading and Viewing DRC Errors Using ICV VUE

<!-- image -->

The DRC Errors tab provides an organized tree list of layout cells and DRC and device extraction violations. This section includes the Violation Browser, Error List, Violation Detail, classification and unmatched error browser. These sections are similar to the ones in the PYDB Viewer Window.

<!-- image -->

<!-- image -->

<!-- image -->

For more information about ICV VUE, see the IC Validator VUE User Guide .

## Running DRC, LVS, and PERC Using ICV Launch

You can configure and run IC Validator checks such as DRC, LVS, and PERC from the IC Validator WorkBench application and review the results using ICV VUE.

## Note:

You need to set the ICV\_HOME\_DIR environment variable before running ICV Launch.

To run DRC, LVS, or PERC from IC Validator WorkBench:

- In the User group of the Home tab, click ICV Launch ( ) and then choose either DRC , LVS , or PERC from the drop-down menu.

<!-- image -->

For more details, see the IC Validator Launch User Guide .

<!-- image -->

## Using the ICVWB PYDB Error Data Viewer

IC Validator WorkBench allows you to load PYDB error data directly in the application and work with the data. This error data is generated by the IC Validator tool and stored in the PYDB database. When you load PYDB error data in IC Validator WorkBench for a particular layout, the violations in the cells of the layout are overlaid on the layout. You can also directly load an IC Validator - Visualization User Environment (VUE) file in IC Validator WorkBench. You can then perform tasks such as the following:

- Navigate through errors and review them
- Update the status or comments of the errors
- Push down top-level errors into child cells
- View the errors from the root cell or from an ancestor cell
- Generate HTML reports of the errors
- Export the complete PYDB error data or only selected cell or violations to a CSV file

The following topics cover how to load and work with the PYDB error data:

- Loading PYDB Error Data in ICVWB
- PYDB Viewer Window
- Viewing PYDB Errors
- Pushing Down Errors to Cells
- Viewing Errors From Root or Ancestor Cells
- Exporting the PYDB Error Records
- Generating HTML Reports
- Checking PYDB Data Correctness

## Loading PYDB Error Data in ICVWB

To load and view the PYDB error data for a layout:

1. Open the layout file whose corresponding error data you need to load.
2. In the ICV group of the View tab, click PYDB Viewer .

<!-- image -->

<!-- image -->

3. In the PYDB Viewer window, click File &gt; Open and select the PYDB file you want to open.

PYDB Viewer supports reading VUE files and you can directly open a .vue file from the main application window or from the PYDB Viewer window. Opening a .vue file automatically loads the layout file and its corresponding PYDB error file.

After you load the PYDB error file, the error data is overlaid on the layout file and the detailed error information in the layout is displayed in the PYDB Viewer window.

Figure 52 PYDB Error Data Loaded in ICVWB

<!-- image -->

## PYDB Viewer Window

The PYDB Viewer window has three dockable panes for displaying the error information: Violation Browser, Error List, and Violation Details. It also has a navigation toolbar for easily browsing through the errors and a toolbar for controlling the view options. The topright corner of the window has a settings button where you can change the default PYDB options.

## Violation Browser

The Violation Browser pane lists all errors grouped by cells (default) with the violations listed under each cell. The root cell is displayed at the top and highlighted in bold type for easier identification and the child cells are displayed below the root cell. You can rightclick the Cell/Violation column to change the grouping to either Violation/Cell or Topcell/Violation . Setting the grouping to top-cell/violation displays only the top cell and its violations. You can select multiple violations under a cell by pressing Ctrl and selecting the violations. A tab created in Error List for each selected violation containing the errors from each violation.

<!-- image -->

The Violation Browser also displays the statistics for the errors such as the total number of errors and the number of errors in each classification. You can choose the type of error you want to display by right clicking the column and selecting the error type.

The Flat Errors column is hidden by default and can be enabled by right clicking a column and selecting Flat Errors . Flat errors is the number of unclassified errors (errors with status="Error") of a particular cell/violation from the top cell.

The Unlimited column displays all errors, while the Total column shows the error count limited by the -elpc option of the IC Validator application during PYDB generation.

<!-- image -->

## Error List

When you select a cell from the Violation Browser , the violation records for that cell are listed in the Error List pane. The Error List pane lists the details of the errors such as the coordinates, area, layer, vertices, and the comments added for the errors. It also displays a Hierarchy column that lists the cell in which the error occurs when the grouping is set to Top-cell/Violation .

<!-- image -->

<!-- image -->

For antenna errors, PYDB Viewer filters and loads only gate information from the antennatype error databases. The Error List table dynamically displays the Net , Layer , and &lt;ReportVariable&gt; columns when the antenna violation node is selected in the Violation Browser . &lt;ReportVariable&gt; is a variable-named parameter that indicates the value for a given report variable.

You can select individual records or multiple records (by pressing and holding Ctrl when selecting) and then perform tasks such as updating the status and comments for the records and generating HTML reports for the errors.

## Violation Details

The Violation Details pane displays details of the violations such as the name, description, and function of the selected error records separated by a line. It provides details of the violation as described in the runset file. For multiple selected violations, details for each violation is separated by a double line.

<!-- image -->

## Navigation Toolbar

You can easily navigate through the PYDB errors by using the navigation buttons available on the navigation toolbar of the PYDB Viewer window. You can change the zoom mode by clicking and selecting Halo , Pan , or Radius from the menu. Selecting Off only highlights the error without changing the view. L

## View Options Toolbar

The view options toolbar has the following options for error viewing:

- : When checked, shows only the layers belonging to selected violations and hides all other layers when selected. +
- : This button has two working modes. When auto-highlighting is on ( ), it clears annotations. When auto-highlighting is off ( ), it deletes the side cells. FK

<!-- image -->

<!-- image -->

- : Controls whether to keep previously created side cells when creating a new side cell for the cell.. 21
- : Controls whether to highlight errors in a single cell or in all cell placements from the top cell view. Is available only in the Top-cell/Violation mode.
- : Opens the PYDB Highlighting options for setting the default highlight color, pattern, and outline width when browsing PYDB errors.
- : indicates that a fixed color is used for all errors.

<!-- image -->

<!-- image -->

<!-- image -->

: indicates that the highlight colors change automatically for each error.

<!-- image -->

- : indicates that the highlight colors change automatically for each violation.

## Searching and Filtering Violations

You can search and filter violations by the cell name or by the violation using the search bar provided in the PYDB Viewer window. The Violation Browser dynamically filters the cells or violations list as you type the search query.

<!-- image -->

- Choose to search by the cell name.
- Choose to search by the violation.
- Click to enable or disable case-sensitive search.

## Status Bar

The status bar displays information about the current command executed and a progress bar to indicate the current running operation progress, such as PYDB file loading. You can hide the status bar by clicking View menu and selecting Status Bar .

<!-- image -->

## PYDB Options

You can set the PYDB settings by clicking the settings icon in the top-right corner of the PYDB Viewer window.

Setting

Error List

Single click to highlight

Pan to violations Description When selecting error records from the

<!-- image -->

, specifies whether the

Error List

enabled when auto-highlight is turned off.

errors are highlighted in the layout when clicked. This feature is only

If this option is off, you can manually highlight an error by right-clicking

menu.

an error record in the

Error List

pane and selecting

Highlight

from the

Specifies whether to zoom in when clicking an error record. As you

zoomed to the error. You can control the zoom mode by choosing

navigate the error results, they are highlighted and the cell view is

, or

Pan Radius from the drop down menu of the

Off

only highlights the error without changing the view.

## Settings for highlighting new violations

<!-- image -->

<!-- image -->

<!-- image -->

| Auto highlight                          | Specifies if violations in the Violation Browser should be highlighted automatically when clicked. Selecting this option creates a side cell for the violation. Selecting this option also regenerates the highlight. If this option is off, you can manually highlight a violation by right-clicking an error record in the Violation Browser pane and selecting Highlight from the menu.   |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Keep existing highlights                | Controls whether to keep previously existing side cells when creating a new side cell for the cell. This option can also be controlled from the view options toolbar by clicking the button.                                                                                                                                                                                                 |
| Show violation layers only              | Specifies whether to show only the layers that belong to selected violations and hide all other layers, or display all layers. This option can also be controlled from the view options toolbar by clicking the button.                                                                                                                                                                      |
| Highlight errors in all cell placements | Specifies whether to highlight the errors in all cell placements or in a single cell placement from the top cell view. This option can also be controlled from the view options toolbar by clicking the button.                                                                                                                                                                              |
| Violation layers                        |                                                                                                                                                                                                                                                                                                                                                                                              |
| Create layer configuration              | Specifies whether a PYDB layer group configuration is created for error layers or the current active layer group configuration is used.                                                                                                                                                                                                                                                      |
| Classification                          |                                                                                                                                                                                                                                                                                                                                                                                              |
| Suppress comment edit dialog            | Specifies to suppress the comment dialog box when classifying errors. By default, the comment dialog is displayed when classifying an error.                                                                                                                                                                                                                                                 |

Halo

button. Selecting

,

<!-- image -->

| Setting                   | Description                                                                   |
|---------------------------|-------------------------------------------------------------------------------|
| Show user comment history | Select this option to show the comment history section in the Comment dialog. |

## Highlighting

The following table lists the settings for the fill color, pattern, and outline width when highlighting PYDB errors.

| Setting      | Description                                                                                                                                                                                                                                                                                                                                                                |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cycle colors | Specifies how the highlight colors should change when browsing PYDB errors. Select Per Error or Per Violation to auto-change the highlight colors (for each error or violation) based on the color sequence of the list. If you select Off , the highlight colors do not change and a fixed color is used for all errors.                                                  |
| Color list   | Specifies the highlight fill color for the PYDB errors. If Cycle colors is Off , the selected color is used for all errors. The default color is yellow. If Cycle colors is set to Per Error or Per Violation , the highlight fill colors change according to the selected colors in the list. You can deselect the colors that you do not want to use for cycling colors. |
| Pattern      | Specifies the fill pattern for the PYDB errors. The default is the plus2 pattern.                                                                                                                                                                                                                                                                                          |
| Line width   | Specifies the outline width of the highlighted error in pixels. It can be between 0 (no outline) and 10. The default width is 1.                                                                                                                                                                                                                                           |

## Viewing PYDB Errors

The following procedures describe viewing the PYDB errors using the default PYDB options.

To highlight the violations in a cell:

- Double-click the cell or violation you want to highlight, or right-click the cell or violation and select Highlight . To select multiple violations, hold down the Ctrl key while selecting the violations, and then right-click and select Highlight.

All violation errors are grouped at the top of the Layout Layers view. When an error is highlighted, the corresponding violation layers are set as visible while the other violation layers are hidden.

<!-- image -->

A single side cell is created for the selected cell and its violations, and the violations are highlighted on the layout. When a violation is highlighted, the side cell displays the violation's name. When multiple violations are highlighted, the side cell is named Multiple\_violations . You can use the Side Cells dockable view to adjust the brightness and color of the errors to easily distinguish the errors on the layout. You can also dim the side cell for better viewing of the errors.

To highlight individual errors from the Error List pane:

1. Select a record or press and hold the Ctrl key to select multiple records.
2. Right-click and select Highlight .

A single side cell is created for the selected records and the errors are highlighted on the layout.

For antenna violations, you can highlight the net by right-clicking an error or several selected errors in the Error List pane and selecting Highlight Net Layers . You can also highlight the nets of multiple violations by right-clicking cell violations in the Violation Browser and selecting Highlight Net Layers .

When violations are highlighted, the violation properties are displayed in the Shape Info tooltip.

<!-- image -->

<!-- image -->

## Loading and Viewing StarRC Opens and Shorts

You can import StarRC opens and shorts files in the PYDB Viewer and review them. You can also trace the opens and shorts after defining a layout connectivity.

To load and view StarRC files in PYDB Viewer:

1. Click File → Load Opens/Shorts .
2. In the Load StarRC Opens/Shorts dialog box, do the following:
- a. Click the Input Files button, select the StarRC files ( .sum ) to import, and then click Open .

You can select multiple files by pressing and holding the Ctrl key.

- b. Optionally, enter the Output Database fields:
- Location : Enter the path where the generated PYDB file will be written. If left empty, the PYDB file will be written in the current location.
- Name : Enter the name for the generated PYDB file. If left empty, then the default name PYDB\_starrc will be applied.
- VUE file : Enter the name for the VUE file to generate from the new PYDB database. If left empty, then no VUE file is generated. The default name is PYDB\_starrc.vue .
- c. Click Load .

The StarRC opens and shorts errors are loaded in the PYDB Viewer.

3. In the Error List pane, right-click an error or right-click multiple selected errors and choose Highlight from the context menu.

The selected opens and shorts are highlighted on the layout.

<!-- image -->

<!-- image -->

4. To trace a short or open, right-click an error from the Error List pane and choose Net Trace from the context menu.

You need to define the layout connectivity to perform a net trace. See the layout connectivity command.

<!-- image -->

## Classifying and Commenting PYDB Errors

You can update the status and comment the errors, or only add comments for the errors in the PYDB Viewer window. You can set the status of one or more errors to one of the following: Error , Fixed , Ignore , Waive , or Watch .

To classify the errors and add comments, do one of the following:

- In the Violation Browser pane of the PYDB Viewer window, right-click a cell and choose a status from the context menu. In the dialog box, enter a comment and click OK .

This updates all the violations in that cell with the selected status and comment.

## Note:

You can change the default behavior of adding comments when classifying errors by selecting the Suppress comment edit dialog option in the #unique\_314 page. Selecting this option allows you to classify errors without adding comments. You can also use the default pydb\_options {suppress\_comment\_dialog 1} command to suppress comments.

- In the Error List pane, select a single record or multiple records, right-click and choose a status from the context menu. Enter a comment and click OK .

The status and comment for all the selected records are updated.

<!-- image -->

- To only add comments to errors, right-click a cell or violation in the Violation Browser pane or right-click the error records from the Error List pane and select Comment . The comments for the selected records are updated.

Figure 53 Updating Comments for Violations

<!-- image -->

## To classify errors in a region:

1. In the Violation Browser pane of the PYDB Viewer window, right-click a cell or violation, and then select Classify in Region .
2. Specify the Lower-left and Upper-right X, Y coordinates, or click the Pick button and drag your mouse to define the region you want to classify.
3. Select the error status to categorize errors in the selected region and add comments if necessary.
4. Click OK .

## Pushing Down Errors to Cells

The PYDB Viewer window has an error push down feature that enables you to push core errors and interface errors from the top-level cell (chip level) down to the sub-cells (block level). This allows you to instantiate work-in-progress blocks into the main chip design to perform incremental physical verification without complicating chip-level debugging. It simplifies chip-level debugging while allowing you to debug and fix errors at the blocklevel.

Interface errors are split into two parts. The part that falls inside the cell is pushed down into it while the rest (interface part) is left at the original cell.

<!-- image -->

<!-- image -->

After push down, error markers are distributed among cells:

<!-- image -->

<!-- image -->

To push errors down from the root cell to sub-cells:

1. In the Violation Browser pane, right-click a cell and choose Push Down .

The push down wizard allows you to set the input and output options for pushing down errors.

2. In the Select Inputs Options page of the wizard, enter the following fields:

| Field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Source cell    | Displays the name of the selected cell you want to push from. Click the browse button to browse and select a different cell in the layout from which the errors need to be pushed down. To push errors from all ancestor cells of the specified target cells, select the All ancestor cells of target cell(s) check box.                                                                                                                                              |
| Target cell(s) | Type or select the child cells of the selected root cell to which the errors need to be pushed down. Click the browse button to browse and then select one or more child cells. You can click Select All to choose all the listed child cells for error push down. If you select the Match Patterns check box, you can enter child cell names matching the exact pattern. You can choose to match patterns using by selection either Wildcards or Regular expression. |

<!-- image -->

| Field         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cells file    | Specify a text file containing the target cell names where errors can be pushed down to. The cell names must be separated by space and can be specified in multiple lines.                                                                                                                                                                                                                                                                                                                       |
| Level         | Specify a level up to which errors must be pushed down.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Boundary      | By default, the cell bounding box is used as the boundary layer. To select another layer, uncheck the Use cell bounding box option and click the browse button to select another layer.                                                                                                                                                                                                                                                                                                          |
| Violation(s)  | Select the violation or violations that need to be pushed down. Click the browse button to browse and then select violations to push down. You can click Select All to select all the violations in the root cell to push down. If you do not select any violation, all violations are pushed down. If you select the Match Patterns check box, you can enter violations matching the exact pattern. You can choose to match patterns using by selection either Wildcards or Regular expression. |
| Cell Instance | Select to distinguish pushed errors by cell reference instance name and specify the cell instance property name.                                                                                                                                                                                                                                                                                                                                                                                 |

Figure 54 PYDB Push Down Wizard Select Input Options Page

<!-- image -->

3. Click Next .

## 4. In the Select Push Down Options page, enter the following fields:

| Field                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select status types to push                                      | Choose the status types that you want to push down. Only the errors with the selected status types are pushed, and at least one status type must be selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Copy errors to                                                   | Select this option to copy the pushed down errors to either the target cells or every intermediate cell in the hierarchy. If not selected, the error is entirely moved from the source to the target cell. ◦ Target cell(s) only : Choose this option to copy the pushed down errors only to the target cells specified in the Select Input Options page. For example, for the hierarchy TOP→A→B , if you are pushing errors to the target cell B , the errors from TOP is copied only to cell B Note: For multi-shape violations, even if a single shape of the multi-shape error intersects with the target cells, all shapes of the multi-shape error are copied into the target cell. ◦ All intermediary hierarchy cells : Choose this option to copy the errors to all the intermediate cells in the hierarchy regardless of whether you are working with a list of cells or levels. For example, when pushing to cell B in the hierarchy TOP→A→B , the errors are copied from TOP to the target cell B and to the intermediate cell A . |
| Omit errors with area bigger than <...>% of the source cell area | Select this option to omit errors that have a larger area than the specified percentage of the source cell area. For example, if you specified the percentage as 1, then all errors that have an area larger than 1% of the source cell area are omitted during the push down.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Push interface errors only                                       | Select this option to push down only the interface errors to the child cells and not the core errors. By default, this option is unselected and both interface and core errors are pushed down to child cells.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Split interface errors                                           | Select this option to split the interface errors during push down. When Split interface errors is selected, it has the following behavior based on the Copy errors to option selection: ◦ If Copy errors to is unselected, then part of the interface error that covers the target cells is moved from the source cell, and the rest of the interface error remains in the source cell. ◦ If Target cell(s) only or All intermediary hierarchy cells is selected, then part of the interface errors that covers the target cell is copied from the source cell to the target cell (or also to all the intermediate cells). The error remains in the source cell without changes. When Split interface errors is not selected, the interface errors are copied or moved similar to the core errors.                                                                                                                                                                                                                                            |
| Match error layers                                               | Select this option to push down errors only if all the error-related layers exist in the child cell. The errors are retained if the target cell does not have all the error layers. This option is unselected by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

<!-- image -->

<!-- image -->

| Field                                        | Description                                                                                                                                                                                                                                                            |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Extend or shrink target cell bounding box by | Select this option to extend or shrink the target cell outline by a specified size. Errors that show up at the edge of the adjusted outline are treated as interface errors. Enter a positive number to extend or a negative number to shrink the target cell outline. |

Figure 55 PYDB Push Down Select Push Down Options Page

<!-- image -->

5. In the Select Output Options page of the wizard, the options are shown based on if errors need to be pushed down to a single PYDB file or multiple PYDB files.

To push down errors to one or more PYDB files, follow these steps:

- a. Select the One database per cell check box to export each target cell to a separate PYDB file, or uncheck to keep pushed down errors to a single PYDB file

## Note:

This option is available only if the ICV\_HOME\_DIR environment variable is set before running IC Validator WorkBench

| Push down to separate PYDB files                                                           | Push down to a single PYDB file                                                                                                                                   |
|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Output directory : Enter the path where you want the individual PYDB files to be exported. | Database : The output of the pushed down errors is stored as another PYDB database file. Specify the path and name for the database file. This field is required. |

<!-- image -->

| Push down to separate PYDB files                                                                                                          | Push down to a single PYDB file                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create files : Select the VUE and ASCII Error DB check boxes if you want to generate these files, in addition to the PYDB files.          | VUE file : Save the output as a .vue file (for opening with the IC Validator VUE application)                                                                                                                                         |
| Include all descendants of target files : Select this check box to include all descendant cells of the target cell in the same PYDB file. | ASCII Error DB File : Saves the output as an ASCII error database file for loading in implementation tools such as IC Compiler and Fusion Compiler. Note: This option is available only when the ICV_HOME_DIR environment variable is |
|                                                                                                                                           | set. Open output database file : Select this option                                                                                                                                                                                   |
|                                                                                                                                           | to open the output PYDB database file after push down is completed.                                                                                                                                                                   |

<!-- image -->

- b. Use the Comment field to add comments to the pushed violations. This helps to differentiate between cell level errors and the ones pushed from the source cell. If a violation already has a comment, your comment are added after the original comment with a semicolon (default) between them.
- c. Select the Save new errors only option to create an output database with only the errors pushed down to the target cells. If you clear this option (default), the output database includes the errors from both the source and target cells.
- d. To see the results of the push down operation in the command history window, select the Show results from the push down operation in the command history window option. This option displays a table log with the cell name, core error count, and interface error count. You can also use the -info option of the push command to show the same information.

## 6. Click OK .

The violations you selected are pushed down to the selected cells. These cells are displayed in the Violation Browser pane of the PYDB Viewer window. When you select this cell, all the violations records for this cell are displayed in the Error List pane.

By default, a VUE file for the pushed down PYDB is saved in the location of the original VUE file.

## Viewing Errors From Root or Ancestor Cells

Similar to how you can push down errors from the root cell to the child cells, you can view the errors from either the root cell or the ancestor cell. When viewing errors from the root or ancestor cell, all instances of the child cell violations are displayed from the top cell view or the specified ancestor cell, respectively.

To view errors from the root cell:

- In the PYDB Viewer window, right-click a child cell and select View from &gt; Root .

Or in the Side Cells view, right-click a child cell violation and select View from &gt; Root .

The block-level violations are overlaid on the root cell for all instances of the child-cell. A new side cell is created in the Side Cells view with the name of the child cell suffixed with \_TOP.

<!-- image -->

Figure 56 Side Cells - Viewing a Cell From the Root

<!-- image -->

To view errors from an ancestor cell:

1. In the PYDB Viewer window, right-click a child cell and select View from &gt; Cell .

Or in the Side Cells view, right-click a child cell violation and select View from &gt; Cell .

2. In the View &lt;cell\_name&gt; from ancestor cell dialog box, select the ancestor cell from which you want to view the violations, and click OK .

The violations are overlaid on the ancestor cell for all instances of the child-cell. A new side cell is created in the Side Cells view with the name of the child cell suffixed with name of the ancestor cell.

Figure 57 PYDB Viewer - Viewing a Cell From an Ancestor Cell

<!-- image -->

## Note:

The side cell is overwritten when viewing the same cell from the root or ancestor cell twice.

## Exporting the PYDB Error Records

You can export the listed errors in the Error List pane to a CSV, CLD, or XML file or you can export the complete PYDB database to a CSV file. You can also export the error classification data to an error classification database (cPYDB). You can do this for the complete PYDB database or for the selected cell and its violations.

<!-- image -->

## Exporting Cell Errors to a Separate PYDB

To export a cell to a database:

1. In the PYDB Viewer window, right-click a cell in the Violation Browser and choose Export Errors .

## Note:

You must set the ICV\_HOME\_DIR environment variable before starting the application, otherwise this option is unavailable.

2. In the Export &lt;cell&gt; to new database dialog window, enter the following:
- Output Directory : The directory where you want to export the database.
- Database Name : Name of the database. By default, the generated database name has the prefix PYDB\_ and suffix \_&lt;cell name&gt; attached to the VUE file name.
- ASCII Error DB File : Use this to create an ASCII Error DB file when exporting errors.
- Do not merge - overwrite existing database : When selected, the existing database is overwritten. When unselected (default), the errors for this cell are merged into the new database from the input database.
- Include all descendants of the cell : Includes all the descendants of the cell in the output database. When unselected (default), all the descendants of the cell are excluded from the database output.
3. Click Export .

<!-- image -->

The cell violations are exported a new database.

<!-- image -->

## Exporting Errors to cPYDB

To export the error data to a cPYDB database:

1. In the PYDB Viewer window, click File &gt; Classification &gt; Export to cPYDB .

## Note:

You must set the ICV\_HOME\_DIR environment variable before starting the application, otherwise this option is unavailable.

2. In the Export to cPYDB dialog window, enter the following:
- Output Directory : The directory where you want to export the cPYDB database.
- Database Name : Name of the cPYDB database. By default, the generated database name has the prefix PYDB\_ and suffix \_cdb attached to the VUE file name.
- Do no merge - create new or overwrite existing cPYDB : When selected (default) and the database does not exist, then a new database is created. If the output database exists, it is overwritten.

If unselected and the output database does exist, then the errors are merged into the existing database from the input database.

- Include matched errors : Select this option to include matched errors. The default is to export only newly classified errors. When merging into an existing error classification database, this option specifies whether to include matched errors from error classification databases other than the destination.

<!-- image -->

## 3. Click Export .

The database is exported to either a new or existing cPYDB database. For more information about error classification databases, see the IC Validator User Guide .

## Exporting Error Classification to a CSV File

To generate an error classification report:

1. In the PYDB Viewer window, click File &gt; Classification &gt; Generate Report .
2. In the Generate Classification window, choose the cells and violations that you want to include or exclude in your report.

<!-- image -->

<!-- image -->

3. Choose the status types you want to export: Error, Fixed, Waive, Ignore, and Watch.
4. Enter the name or path for exporting the CSV file and click Export .

<!-- image -->

## Exporting Errors to a CSV or CLD File

To export the PYDB errors:

- In the PYDB Viewer window, click File &gt; Export to export the error records listed in the Error List pane. To export the complete set of errors from the PYDB database, click File &gt; Export All .

The Export PYDB information into file dialog box opens where you can save the information to a CSV or CLD file, if you selected the Export button. If you selected Export All , you can export the data only to a CSV file.

## Generating HTML Reports

After you work on the PYDB errors, you can generate an HTML report of selected PYDB records to easily review the errors. The HTML report has the following features:

- Generates a detailed summary of the selected errors that is easy to read
- Provides screenshots for each of the reported errors
- Links to specific sections of the report
- Legend about the layers visible under an error region

## To generate an HTML report:

1. In the Violation Browser pane, right-click a cell and choose HTML Report from the context menu.

This selects all the error records in that cell and its descendant cells for including in the report.

If you want to generate the report only for a few records, right-click the error records from the table on right-pane and choose HTML Report &gt; Selected only from the menu.

2. In the HTML Report for &lt;cell\_name&gt; dialog box, enter the following fields:

<!-- image -->

| Field           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Output filename | Enter the name for report and select a folder to save the report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Custom template | By default, the HTML report is generated using the built-in template. Select the check box to customize the default template settings of the HTML report stored in the ReportConfiguration.ini file. Click to edit the ReportConfiguration.ini file in the IDE. ◦ Generate the report without the error snapshots by setting ShowErrorSnapshot=false . ◦ Generate an HTML report that includes only the screenshots of errors by setting html=false . ◦ Generate an image representing the error distribution from the top cell along with original snapshot of the errors using the option SnapshotZoom=top . ◦ Generate a summary-only HTML report that contains no error snapshots or layer information. |
| Record types    | You can select the records you want to include in your report. By default,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

<!-- image -->

<!-- image -->

| Field                 | Description                                                                                                                                                                                               |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Open generated report | By default, the report is automatically opened using the application's built-in browser once generated. However, you can choose to not open it automatically and open the report using any other browser. |

Figure 58 HTML Report Dialog Box

<!-- image -->

## 3. Click OK .

The HTML report is generated and opened in the built-in browser.

<!-- image -->

Figure 59 PYDB Sample HTML Report

<!-- image -->

## Figure 60 PYDB HTML Summary-Only Report

| Error Name                                    | Cell Name   |   Error Count |
|-----------------------------------------------|-------------|---------------|
| L45D1_Baseline xorL45D1_Check,output to(45;1) | CHIP        |            79 |
|                                               | MMZCIO1     |             9 |
|                                               | MMZIO       |            12 |
|                                               | CHIP        |            67 |
| L46D1_BaselinexorL46D1_Check,output to(46;1)  | MMZCI01     |            25 |
|                                               | MMZIO       |             8 |

<!-- image -->

## Checking PYDB Data Correctness

You can use the command-line utility, pydbChecker , to verify the correctness of foreign keys, indexes, views, and table data, ensuring database integrity. You can also output the count of error-polygons for debugging purposes. The utility also checks the logical consistency of PYDB by performing cross-table validations to ensure data consistency across tables and to confirm that there are no missing records or errors.

To use this utility, run the following command directly from the &lt;ICVWB\_INSTALL\_DIR&gt;/bin directory:

```
pydbChecker database [-quick-check | -integrity-check] [-print-polygon-count] [-help | -h]
```

## Arguments

database

Specifies the path to the input PYDB database.

<!-- image -->

-quick-check

Performs a quick integrity check on the database. This option performs all the checks performed by the -integrity-check option except validating the UNIQUE constraint and ensuring that the contents of the index match the contents of the table.

## -integrity-check

Performs a full integrity check on the database. This option checks for the following:

- Table or index entries that are not in the correct order.
- Incorrectly formatted records.
- Missing pages.
- Missing or excess index entries.
- UNIQUE , CHECK and NOT NULL constraint errors.
- Freelist integrity.
- Sections of the database that are used more than once or not at all.

-print-polygon-count

If specified, prints the number of polygons for each error in the database.

<!-- formula-not-decoded -->

Displays command usage help.

<!-- image -->

## Working With ASCII Error Files

This chapter describes how to load and work with ASCII error files.

After you load a layout, you can load its corresponding DRC error files in the IC Validator WorkBench application to quickly view and analyze DRC errors. DRC error data is overlaid on the active layout where you can easily view the errors on the layout and its details in the DRC Information window. You can then classify the errors either individually or as a group and also add comments for each error record. You can also save your session and continue working with the classification in a future session.

The following topics cover how to view, classify, and save DRC error data.

- Loading DRC Error Data
- Viewing DRC Error Data
- Classifying and Commenting DRC Errors
- Saving DRC Error Records

## Loading DRC Error Data

To load DRC error data for a layout:

1. Click File &gt; Open and open a layout.
2. Click File &gt; Import ASCII Error Database .

The DRC Files dialog box opens.

3. Select a DRC error file ( .db , .rdb , or .cdb files).
4. Click Open .

Alternatively, you can use the drc file open filename on the command line.

The DRC error data is loaded as a single side cell in the Side Cells window and is also loaded in the DRC Information window. The layers in the error file are loaded in the Layout Layers window as a group.

<!-- image -->

## Viewing DRC Error Data

When you load a DRC error file, the DRC Information window displays the violations grouped by the cell in the left pane and the individual violation records in the right pane.

In the left pane, you can choose to display the violations grouped by the cell or by the violation. The left pane also displays a summary of the violations and their total count.

The right pane has columns that displays the error records and their details such as the hierarchy, type of object, vertices, properties, rule description and, comments. It also displays the status of the errors and any comments that you have added.

To navigate the DRC records, use the navigation buttons on the header of the DRC Information window. As you navigate the results or select any of the DRC records, the violations are highlighted and zoomed in to by default on the layout. You can change this by clicking and selecting to only annotate the violation and not zoom in. You can also zoom in to a violation by right-clicking a record in the right pane and choosing Go To .

When you load a DRC error file, the DRC error data is also loaded as a side cell in the Side Cells window. You can adjust the brightness and tone of the DRC violations and the dimming of the background layout error file to easily view the errors on the layout. When you load multiple DRC error files, you can select which file you need to view in the DRC Information window by right-clicking the side cell and choosing Show in DRC Table .

## Classifying and Commenting DRC Errors

After you load and view DRC errors, you can classify the errors by giving them a status while also providing comments in the DRC Information window. You can choose to give an error one of the following statuses: Error , Fixed , Ignore , Waive , Watch , or Unclassified .

You can classify or add comments from either the left or right panes of the DRC Information view.

To classify the DRC errors and add comments, do one of the following:

- In the left pane, right-click a violation group and choose a status from the context menu, or click Comment .

This will update all the violations in that cell group with the selected status and comment.

If you selected Comment , then the Classify DRC Records dialog box opens. Here you can add a comment for the selected violation group and also select a status for it.

<!-- image -->

<!-- image -->

- In the right pane, select one record or multiple records, right-click and choose Classify . The Classify DRC Records dialog box opens.

You can apply a status or comment to the selected DRC records, and you can then see this information in the Status and Comment columns.

## Saving DRC Error Records

After you classify and add comments to DRC records, you can save this information as a CBD file and load it on the corresponding layout in a future session with all the information intact.

To save DRC error records:

1. On the header of the DRC Information view, click the Save As button.

The Save DRC information to file dialog box opens

2. Save the information as CDB file.

You can then load this .cdb file by clicking File &gt; Import ASCII Error Database .

## 10

## Synopsys Diagnostic Platform

This chapter describes how to collect data for the Synopsys Diagnostic Platform tool to debug runtime issues that are not reproducible in the Synopsys environment.

The Synopsys Diagnostic Platform (SDP) tool is used to collects diagnostic data from the user environment to debug runtime issues that cannot be reproduced in the Synopsys environment. It also includes profiling information about command execution to help diagnose the performance of specific scenarios.

## Collecting Data for Synopsys Diagnostic Platform

To enable SDP tool, load the SDP module:

```
module load fwsdp
```

To start collecting information, execute the sdp start command before running the commands that should be profiled and provide a directory path where the collected data will be stored:

```
sdp start /path/to/storage
```

To stop collecting information execute:

sdp stop

<!-- image -->

<!-- image -->

## A

## Default Hotkeys

This appendix describes the preset hotkey defaults provided with the application.

## Hotkeys

hotkeys Hotkeys define keystrokes that are preset. You can view and configure hotkeys when running the application either in the ribbon mode or menu mode. You can also load preset hotkeys configurations such as CC\_hotkeys, CC\_hotkeys, and Virtuoso ® configurations that are provided with the application.

This section contains the following topics:

- Setting Hotkeys in the Ribbon Mode
- Setting Hotkeys in the Menu Mode
- Adding a Hotkeys Configuration File
- List of Default Hotkeys

## Setting Hotkeys in the Ribbon Mode

When running the application in the ribbon mode, you can view and configure hotkeys from the Ribbon Options window. You can assign, remove, and reset shortcut keys for actions from the Ribbon Options window.

To assign a shortcut key for an existing action or custom action:

1. In the Customize the Ribbon page, double-click the Shortcut cell next to any action in the left or right pane.
2. In the shortcuts dialog box, press the combination of keys you want to assign and click Assign .

If the key combination you entered is assigned to another action, you can choose to overwrite the existing assignment or change your key combination.

<!-- image -->

<!-- image -->

Once assigned, the key combinations is displayed under Current shortcuts .

3. Click Close and then click OK in the Ribbon Options window to apply the shortcut key combination.

To remove or reset shortcut keys:

- Double-click the Shortcut cell of the action.
- To remove a shortcut, select the key combination from the Current shortcut keys list and click Remove .
- To reset the shortcut key assignments to its default, click Reset .

To import a shortcut key configuration:

1. In the Customize the Ribbon page, click the Import/Export drop-down button.
2. Select a hotkey configuration under Shortcut configuration : Default, CC\_hotkeys, ICC\_hotkeys, or V\_hotkeys.

The following is a list of default keyboard shortcuts in the application.

Figure 61 Ribbon Options Window

<!-- image -->

## Setting Hotkeys in the Menu Mode

When running the application in the menu mode, click Tools &gt; Options and select Hotkeys in the Options window. The actions are listed to the right of each hotkey. The menu mode Hotkeys page also includes additional hotkey options for Layout , FindTable , Net Tracing , lefdef , and FwIDE .

To assign or change hotkeys using the Hotkeys page:

- Click the cell to the right of the hotkey action and press the desired keyboard keys. You can enter more than one key for each action.

To unassign a hotkey:

1. Click the cell to the right of the action.
2. Right-click the cell and select Delete shortcuts .

<!-- image -->

## Note:

You cannot reassign the Esc key, the Ctrl+I key, or the Ctrl+W key to different hotkey designations.

To save new, added, or modified hotkeys:

- Use the default save command.

For more information, see the IC Validator WorkBench Command Manual .

To import a shortcut key configuration:

1. Click Tools &gt; Macro &gt; User Hotkeys .
2. Select a hotkey configuration from the list: Default, CC\_hotkeys, ICC\_hotkeys, or V\_hotkeys.

<!-- image -->

Figure 62 Hotkeys page in Options dialog box

<!-- image -->

## Adding a Hotkeys Configuration File

You can also add a hotkeys configuration file in the application from the menu mode or ribbon mode. To add a hotkeys configuration file, place your my\_hotkeys.tcl file in the ICVWB\_INSTALL\_DIR/etc/fw/contrib directory. The my\_hotkeys.tcl configuration file name is then included in the Shortcut configuration list from the ribbon mode or in the Tools &gt; Macro &gt; User Hotkeys list from the menu mode.

After you select any item in the drop-down list, the appropriate script from ICVWB\_INSTALL\_DIR/etc/fw/contrib is executed. For example, if you select my\_hotkeys, the tool executes the ICVWB\_INSTALL\_DIR/etc/fw/contrib/ my\_hotkeys.tcl script. If that script is not found, the application tries to run the ICVWB\_INSTALL\_DIR/etc/fw/contrib/my\_hotkeys.mac .

## List of Default Hotkeys

The following table lists all the default shortcuts in the ICVWB application.

| Action                              | Keystroke   |
|-------------------------------------|-------------|
| Center View                         | C           |
| Command entry focus                 | :           |
| Delete                              | Del         |
| Edit->Cell->Copy                    |             |
| Edit->Cell->Edit                    | Ctrl+E      |
| Edit->Cell->New                     |             |
| Edit->Clipboard->Copy               | Ctrl+C      |
| Edit->Clipboard->Cut                | Ctrl+X      |
| Edit->Clipboard->Paste              | Ctrl+V      |
| Edit->Tools->Circle                 |             |
| Edit->Tools->NetTrace               | N           |
| Edit->Tools->NetTrace->Connectivity |             |
| Edit->Tools->Path                   |             |
| Edit->Tools->Polygon                | D           |
| Edit->Tools->Reference              |             |

<!-- image -->

| Action                      | Keystroke    |
|-----------------------------|--------------|
| Edit->Tools->Text           |              |
| File->Close                 |              |
| File->Exit                  | Ctrl+Q       |
| File->Import LEF/DEF        |              |
| File->Layout Export         | Shift+X      |
| File->Layout Reload         |              |
| File->Layout Resolution     | Shift+E      |
| File->Load ASCII Error File |              |
| File->New                   | Ctrl+N       |
| File->Open                  | Ctrl+O       |
| File->Save                  | Ctrl+S       |
| File->Save As               | Ctrl+Shift+S |
| Grid                        |              |
| Hierarchy Filter Max 0      | 0            |
| Hierarchy Filter Max 1      | 1            |
| Hierarchy Filter Max 2      | 2            |
| Hierarchy Filter Max 3      | 3            |
| Hierarchy Filter Max 4      | 4            |
| Hierarchy Filter Max 5      | 5            |
| Hierarchy Filter Max 6      | 6            |
| Hierarchy Filter Max 7      | 7            |
| Hierarchy Filter Max 8      | 8            |
| Hierarchy Filter Max 9      | 9            |
| Hierarchy Filter Max 99     | *            |
| Hierarchy Filter Min 0      | Ctrl+0       |
| Hierarchy Filter Min 1      | Ctrl+1       |

<!-- image -->

| Action                            | Keystroke   |
|-----------------------------------|-------------|
| Hierarchy Filter Min 2            | Ctrl+2      |
| Hierarchy Filter Min 3            | Ctrl+3      |
| Hierarchy Filter Min 4            | Ctrl+4      |
| Hierarchy Filter Min 5            | Ctrl+5      |
| Hierarchy Filter Min 6            | Ctrl+6      |
| Hierarchy Filter Min 7            | Ctrl+7      |
| Hierarchy Filter Min 8            | Ctrl+8      |
| Hierarchy Filter Min 9            | Ctrl+9      |
| Hierarchy Max Down                | <           |
| Hierarchy Max Up                  | >           |
| Hierarchy Min Down                | Ctrl+<      |
| Hierarchy Min Up                  | Ctrl+>      |
| Home->Cell->Open                  |             |
| Home->Cell->Open->Root Cells      |             |
| Home->Compare->Cells              |             |
| Home->Compare->Cells->Options     |             |
| Home->Find->Clear Annotations     |             |
| Home->Find->Find                  | Ctrl+F      |
| Home->Find->First                 | Ctrl+Home   |
| Home->Find->Last                  | Ctrl+End    |
| Home->Find->Next                  | F3          |
| Home->Find->Previous              | Shift+F3    |
| Home->Find->Show Find Information |             |
| Home->Hierarchy->BBoxes           |             |
| Home->Hierarchy->Levels           |             |
| Home->Hierarchy->Names            |             |

<!-- image -->

| Action                                            | Keystroke   |
|---------------------------------------------------|-------------|
| Home->Tools->Browse                               | B           |
| Home->Tools->Browse->View Options                 |             |
| Home->Tools->Callout                              |             |
| Home->Tools->Flag                                 | F           |
| Home->Tools->Gauge                                | G           |
| Home->Tools->Highlight                            | H           |
| Home->Tools->Info                                 | Ctrl+D      |
| Home->Tools->Pan                                  | Shift+P     |
| Home->Tools->Point                                | P           |
| Home->Tools->Ruler                                | R           |
| Home->Tools->Ruler->Delete All Rulers             |             |
| Home->Tools->Ruler->Multi-measurement Ruler       |             |
| Home->Tools->Ruler->Options                       |             |
| Home->Tools->Select                               | S           |
| Home->Tools->Select->Edit Depth->Level 1 only     |             |
| Home->Tools->Select->Edit Depth->Level Root to 10 |             |
| Home->Tools->Select->Edit Depth->Root             |             |
| Home->Tools->Select->Edit Depth->Unlimited        |             |
| Home->Tools->Select->Options                      |             |
| Home->Tools->Select->Selectable->Array            |             |
| Home->Tools->Select->Selectable->Polygon          |             |
| Home->Tools->Select->Selectable->Reference        |             |
| Home->Tools->Select->Selectable->Text             |             |
| Home->Tools->Stretch                              | Shift+S     |
| Home->User->Mode                                  |             |

<!-- image -->

## Action

## Keystroke

Home-&gt;User-&gt;Mode-&gt;HERCULES

Home-&gt;User-&gt;Mode-&gt;ICV

Home-&gt;User-&gt;Mode-&gt;ICV\_PLM

Home-&gt;User-&gt;Mode-&gt;ICV64

Home-&gt;User-&gt;Mode-&gt;ICVWB

Home-&gt;User-&gt;Mode-&gt;SENTAURUS

Home-&gt;View-&gt;Fit

Home

Home-&gt;View-&gt;Go To

Home-&gt;View-&gt;Next View

Shift+Right

Home-&gt;View-&gt;Previous View

Shift+Left

Backspace

Home-&gt;View-&gt;Refresh

F5 Ctrl+R

Home-&gt;View-&gt;Selected

Shift+A End

Home-&gt;View-&gt;Zoom In

Ctrl+= PgDown

Home-&gt;View-&gt;Zoom Out

Ctrl+- PgUp

Mirror-&gt;X

X

Mirror-&gt;Y

Y

Options

O

Pan Down

Down

Pan Left

Left

Pan Right

Right

Pan Up

Up

Redo

Ctrl+Y

Rotate-&gt;Left 90

Shift+L

Rotate-&gt;Right 90

Shift+R

Select All

Ctrl+A

<!-- image -->

| Action                       | Keystroke    |
|------------------------------|--------------|
| Select Move Down             | Ctrl+Down    |
| Select Move Left             | Ctrl+Left    |
| Select Move Right            | Ctrl+Right   |
| Select Move Up               | Ctrl+Up      |
| SEM Move Down                |              |
| SEM Move Down More           |              |
| SEM Move Left                |              |
| SEM Move Left and Down       |              |
| SEM Move Left and Down More  |              |
| SEM Move Left and Up         |              |
| SEM Move Left and Up More    |              |
| SEM Move Left More           |              |
| SEM Move Right               |              |
| SEM Move Right and Down      |              |
| SEM Move Right and Down More |              |
| SEM Move Right and Up        |              |
| SEM Move Right and Up More   |              |
| SEM Move Right More          |              |
| SEM Move Up                  |              |
| SEM Move Up More             |              |
| SEM Rotate Left              | /            |
| SEM Rotate Left More         | Ctrl+/       |
| SEM Rotate Right             |              |
| SEM Rotate Right More        | Ctrl+*       |
| SEM Scale Down               | -            |
| SEM Scale Down More          | Ctrl+Shift+- |

<!-- image -->

| Action                                               | Keystroke    |
|------------------------------------------------------|--------------|
| SEM Scale Up                                         | +            |
| SEM Scale Up More                                    | Ctrl++       |
| ShapeInfo Clone                                      | Alt+C        |
| Toggle to Browse                                     | V            |
| Undo                                                 | Ctrl+Z       |
| View->Cell->Overlay                                  | Shift+O      |
| View->Cell->Transform                                |              |
| View->Layout->Layout Options                         | L            |
| View->Layout->Save Image                             |              |
| View->Layout->Scale                                  | Ctrl+Shift+X |
| View->Layout->Cell Outline                           | Ctrl+J       |
| View->Layout->Text Orientation->Horizontally         |              |
| View->Layout->Text Orientation->Use info from layout |              |
| View->Macros->Record                                 |              |
| View->Macros->Run                                    |              |
| View->Macros->Stop                                   |              |
| View->Macros->Tcl Debugger                           |              |
| View->Synchronize->Markups->All                      |              |
| View->Synchronize->Markups->Callouts                 |              |
| View->Synchronize->Markups->Contours                 |              |
| View->Synchronize->Markups->Flags                    |              |
| View->Synchronize->Markups->Gauges                   |              |
| View->Synchronize->Markups->Highlights               |              |
| View->Synchronize->Markups->Model Images             |              |
| View->Synchronize->Markups->Points                   |              |

<!-- image -->

| Action                                                                    | Keystroke     |
|---------------------------------------------------------------------------|---------------|
| View->Synchronize->Markups->Rulers View->Synchronize->Markups->Sem Images |               |
| View->Synchronize->Markups->Stretch                                       |               |
| View->Synchronize->Views                                                  |               |
| View->Window->Arrange->Arrange Horizontal                                 |               |
| View->Window->Arrange->Arrange Vertical                                   |               |
| View->Window->Arrange->Cascade                                            |               |
| View->Window->Arrange->Tile                                               |               |
| View->Window->Close                                                       | Ctrl+F4       |
| View->Window->Close All                                                   | Ctrl+Shift+F4 |
| View->Window->Dockable->Command Help                                      | Shift+F1      |
| View->Window->Dockable->Command Pane                                      | F2            |
| View->Window->Dockable->DRC Information                                   |               |
| View->Window->Dockable->Find Information                                  |               |
| View->Window->Dockable->Information                                       | F11           |
| View->Window->Dockable->Layout Layers                                     | Shift+F2      |
| View->Window->Dockable->Layouts                                           |               |
| View->Window->Dockable->Markups                                           |               |
| View->Window->Dockable->Navigation                                        | F4            |
| View->Window->Dockable->Object Attributes                                 |               |
| View->Window->Dockable->Open Cells                                        | Shift+F7      |
| View->Window->Dockable->Probe                                             |               |
| View->Window->Dockable->Side Cells                                        |               |
| View->Window->Dockable->Task View                                         | F6            |
| View->Window->Dockable->Tree View                                         | F7            |
| View->Window->Status Bar                                                  |               |

<!-- image -->

## Limitations of Layout Files

This appendix describes the maximum limits of layout elements for GDSII and OASIS files in the application.

This topic is available:

- Maximum Limits of GDSII and OASIS Files

## Maximum Limits of GDSII and OASIS Files

Table 46 defines the supported maximum limits of the GDSII and OASIS formats in the application.

| Limitation                                                        | OASIS                                                                                                       | GDSII                                                                    |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Range of layer and datatype numbers                               | 0 to 2 31 - 1                                                                                               | 0 to 65,535                                                              |
| Maximum number of layer:datatype combinations supported           | 2 31                                                                                                        | 2 31                                                                     |
| Maximum length of cell name                                       | 2 31 - 1                                                                                                    | 65,533                                                                   |
| Maximum number of total cells                                     | 2 32                                                                                                        | 2 32                                                                     |
| Maximum number of vertices for a polygon or path                  | Above 65,530 vertices shapes are not filled                                                                 | 8191 with the last vertex coordinates being the same as the first vertex |
| Maximum coordinate space numbers                                  | Limited to the range of -2 31 to 2 31 DBU for OASIS32 Limited to the range of -2 45 to 2 45 DBU for OASIS64 | -2 31 to 2 31                                                            |
| Maximum dimension of array references                             | 2 31 - 1 x 2 31 - 1                                                                                         | 65,535 x 65,535                                                          |
| Maximum dimension of repetitions (path, polygon, rectangle, text) | 2 31 - 1                                                                                                    | N/A                                                                      |

Table 46 Maximum limits of layout files

<!-- image -->

| Limitation                                  | OASIS                                             | GDSII   |
|---------------------------------------------|---------------------------------------------------|---------|
| General OASIS integers (signed or unsigned) | OASIS32: 32-bit integers OASIS64: 64-bit integers | N/A     |

Table 46 Maximum limits of layout files (Continued)

<!-- image -->

## OASIS Files Compliance Checking

This appendix describes the standalone oasis\_info utility used to check the compliance of OASIS files or to print records in the OASIS files from the terminal window.

This topic is available:

- The oasis\_info Utility

## The oasis\_info Utility

This utility returns statistics if the input OASIS file is compliant with the OASIS specification. The utility can also print partial or all records in the given OASIS file based on the arguments you specify. The utility is available in the ICVWB\_INSTALL\_DIR/bin directory and must be run from the terminal window.

## Syntax

```
oasis_info oasis_file [-checksum | -file_props | -cblock_offset_dump] oasis_info oasis_file -all [-short [ num_points ]] [-beautify] oasis_info oasis_file [-cblock offset ] [-offset begin [ end ]] [-short [ num_points ]] [-beautify] oasis_info oasis_file -brief oasis_info oasis_file -cell cell_name [-short [ num_points ]] [-beautify]
```

## Returns

If you do not specify any arguments, then the utility reports whether the OASIS file complies with the OASIS specification. If you specify arguments, then the utility returns additional information about the OASIS file.

## Arguments

```
oasis_file Specifies the input OASIS file.
```

<!-- image -->

```
-all
```

Specifies to return all records in the file.

```
-beautify
```

Specifies to break the record into multiple lines if the point list is too long. If you do not specify this option, then the utility prints the record on one line.

## -brief

Specifies to return only the START and END records. This option does not validate the file.

```
-cblock_offset_dump
```

Specifies to print all CBLOCK records and offsets. Cannot combine with other options.

```
-cblock offset
```

Specifies to return the records in the CBLOCK record at file offset offset . If -offset offset is used with the -cblock argument, then only the records in the specified range within the CBLOCK are reported.

```
-cell cell_name
```

Specifies to return all records specified in the cell cell\_name .

```
-checksum
```

Specifies to run only a checksum calculation on OASIS files that have CRC32 or CHECKSUM32, and returns a pass or fail report. When specifying this option, the utility does NOT compute any other OASIS compliance checks.

```
-file_props
```

Returns file-level property records. With this option, oasis\_info does not perform deep validation.

```
-offset begin [end]
```

Specifies to return records in the file offset range specified with the begin and end values. When you specify begin and end , the tool returns all records between and including these points. If you do not specify end , then the utility returns the record at begin or immediately after begin only.

```
-short [ num_points ]
```

Specifies that the utility returns up to num\_points of each polygon, path, or random repetition point. If you do not specify num\_points , then the utility does not return any points. For num\_points , specify a non-negative integer.

<!-- image -->

## Description

Runs the OASIS compliance checking tool on your OASIS file in order to help diagnose any problems in your files.

## Examples

```
#To get a record at specified offset 28: oasis_info doc/fw/tut3/NAND.oasis -offset 28 ... 28     PROPERTY:28   ref 0  'OASIS_LIB_REVISION' cnt 1 pr:str(tp:14 ref:0) 'Synopsys OASIS Library R-2020.09-SP1.807894' ... #To get records in a range 13-40: oasis_info doc/fw/tut3/NAND.oasis -offset 13 40 ... 13    START       unit=1000.000000 table_offset at <END> record 28     PROPERTY:28   ref 0  'OASIS_LIB_REVISION' cnt 1 pr:str(tp:14 ref:0) 'Synopsys OASIS Library R-2020.09-SP1.807894' 33     PROPERTY:28   ref 1  'SYNOPSYS_SEG_FW' cnt 6 pr:str(tp:15 ref:1) 'version' pr:str(tp:14 ref:2) 'R-2020.09-SP1 (841427)' pr:str(tp:15 ref:3) 'layout_server_version' pr:str(tp:13 ref:2) 'R-2020.09-SP1 (841427)' pr:str(tp:15 ref:4) 'compression'  pr:uint 6 ... #To get all records in a CBLOCK at specified offset 50: oasis_info doc/fw/tut3/NAND.oasis -cblock 50 ... 50    CBLOCK:34      CBLOCK     comp-bytes 92 uncomp-bytes 118 rate=77.97% C:0    XYRELATIVE:16 C:1    PLACEMENT:17  x 480 y 1170 flp 0 mag 1.0 ang 0 ref 1  'ACONT' rep:3 y-dm:1 y-sp:120 C:11   PLACEMENT:17  x 240 y 1170 flp 0 mag 1.0 ang 0 ref 1  'ACONT' rep:3 y-dm:1 y-sp:120 C:16   PLACEMENT:17  x 720 y 1170 flp 0 mag 1.0 ang 0 ref 1  'ACONT' rep:3 y-dm:1 y-sp:120 ... #To get a record from a CBLOCK (offset 50) at specified offset 11: oasis_info doc/fw/tut3/NAND.oasis -cblock 50 -offset 11 ... 50    CBLOCK:34      CBLOCK     comp-bytes 92 uncomp-bytes 118 rate=77.97% C:11   PLACEMENT:17  x 240 y 1170 flp 0 mag 1.0 ang 0 ref 1  'ACONT' rep:3 y-dm:1 y-sp:120 ...
```

<!-- image -->

<!-- image -->

## Creating Standalone Cache Files with genCache

This appendix describes the application used to generate standalone cache files for GDSII, GDSII gzip files, OASIS, and OASIS gzip files.

These topics are available:

- runProg genCache
- Using the genCache DP Option

## runProg genCache

The genCache tool is available in the /ICVWB\_INSTALL\_DIR/bin directory. You can generate a cache file without starting a session using the runProg genCache ca he fil g n r t tool from the terminal window.

## Syntax

## For Linux:

```
runP og e Cach runProg genCache inputFileName directoryOfOutputCacheFile [-64][-f][-cores number ] [-dp host_file [-dp_workers workers_number ]] [-layout_oasis_strict on|off] [-reference_properties on|off] [-mode hicap|locap] [-max_warnings number |all][-progress] [-path_close_smooth on|off]
```

## For Windows:

```
genCach . x genCache.exe inputFileName directoryOfOutputCacheFile [-64] [-f][-cores number ] [-dp host_file [-dp_workers workers_number ]] [-layout_oasis_strict on|off] [-reference_properties on|off] [-mode hicap|locap] [-max_warnings number |all][-progress] [-path_close_smooth on|off]
```

## Arguments

inputFileName

Specifies the layout (OASIS or GDSII) file for which you want cache file information generated.

directoryOfOutputCacheFile

Specifies the directory where you want the output cache file located.

-64

Specifies to use the 64-bit server when parsing a 64-bit OASIS file. If you do not specify this argument, the tool uses the 32-bit server instead. Note that specifying this argument might cause the tool to use more memory at runtime.

-f Force to regenerate a new cache file. Overwrite a cache file if it exists.

```
-cores number
```

An integer between 1 and 32 specifying the number of cores to be used. If this optional parameter is not specified, the number of available cores are used (up to 32).

```
-dp host_file
```

Specifies using d genCach distr bu p o istributed processing with the servers listed in host\_file .

```
-dp_workers workers_number
```

Specifies the number of workers used during distributed processing. The number of workers should be less than or equal to the total number of slots provided by host\_file . The default is 4 .

```
-layout_oasis_strict on|off
```

Allow to generate cache for illegal strict OASIS file that is actually not-strict. If set as on , genCache prints a warning and continues generating cache. If set as off , the application errors-out according to the OASIS specification requirements. Default is on .

```
-reference_properties on|off
```

Specifies whether to read instance properties before loading the layout. A Boolean. The default is on .

```
-mode hicap|locap
```

Allowed values are locap and hicap . hicap configures command for high speed, but increases the load time and uses more memory. The default is hicap .

<!-- image -->

when creating a cache file. The default is on .

<!-- image -->

```
-max_warnings number |all Specifies the maximum allowed warnings. The default is 5. -progress Display the percentage of completion of the cache file generation at the terminal. -path_close_smooth on|off Creates a smooth connection between the start and end of a closed path outline
```

## Description

Cache files store information about the layout files, allowing the application to load them more quickly. This feature is especially useful when you previously opened a large layout file (that has not changed since the last run). Cache files can also be generated using distributed processing.

## Note:

No new cache file is generated if the up-to-date cache file exists in the output directory. You can override this by specifying the -f flag.

## Examples

Example 1 The following generates a cache file in your current working directory for the layout test.gds

runProg genCache test.gds

## Example 2 Using layout strict mode:

```
genCache inputFileName arg1 directoryOfOutputCacheFile arg2 -layout_oasis_strict on Same as: genCache inputFileName arg1 directoryOfOutputCacheFile arg2
```

## Using the genCache DP Option

You can set up a distributed job for OASIS files by using the genCach DP opti s u d r b j genCache Distributed Processing (DP) option. DP cache generation enables you to generate cache files more quickly in cases where the file is located on a network server and many host machines are available.

A distributed run requires interfacing to multiple hosts/nodes to launch Workers from a single Master application. The host machines for the Worker and Master should be dedicated and all hosts should have access to the layout file located on the network server.

<!-- image -->

## The Host File

A host file is used to provide host information to genCache. The following example demonstrates the formatting for a distr bu e p oc ngh f l xam host file in RSH mode:

```
# HOSTS INFORMATION FILE (RSH) # Each valid host definition occupies an entire line. # Line with '#' as the first character is a comment line. # Format of each line: # # enabled| hostname| #slots| tmpDir| mode| command 1| teralab-x | 1 | /tmp| RSH | rsh 1| teralab-y | 1 | /tmp| RSH | rsh
```

Table 47 contains detailed information about the host file.

Table 47 genCache Host File Information

| Hosts Information File Details Field   | Value                                  | Purpose                                                                                                                                                         |
|----------------------------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1                                      | An integer - can be 0 or 1             | A 0 signifies that the host cannot be used. a 1 denotes a usable Worker machine.                                                                                |
| teralab-x                              | A string - a valid hostname            | This is the hostname of a valid Worker machine. For SGE, LSF this field is empty.                                                                               |
| 1                                      | An integer - any valid integer         | This number is used to denote the number of worker slots on this host (rsh and ssh) or farm (lsf and sge). -1 indicates unlimited. For genCache it should be 1. |
| /tmp                                   | A string - a valid, writable directory | This directory is used for local data storage for an application. GenCache is not using this.                                                                   |
| RSH                                    | A string - command mode                | The string signifies the command mode used to connect to the Worker machine. Valid entries are RSH, SSH, LSF, and SGE.                                          |
| rsh                                    | A string - the connection command      | The given string denotes the remote command used to connect to the Worker machine.                                                                              |

## The Log File

genCache generates several log files in DP mode. These logs are informative and useful for understanding the interaction between the genCache master and workers.

<!-- image -->

The following log files are created for the genCache application run in DP mode:

- master.&lt;hostname&gt;.&lt;pid&gt;.log
- worker.&lt;hostname&gt;.&lt;pid&gt;.log

The number of Worker log files is equal to the number of Workers that ran during the DP loading. Use the -dp\_no\_worker\_logging command line option to disable Log files for Workers.

The location of log files is affected by setting the CDPL\_LOGDIR environment variable. If this variable is not defined, the current working directory is used.

The Number of Workers

You should specify the number of workers to be used during DP genCache. The number of workers should be less than or equal to the total number of slots provided by the host information file. genCache uses 4 workers by default. You can specify the number of workers by using the -dp\_workers option.

## Examples

```
genCache inputFileName directoryOfOutputCacheFile [-64] [-cores number] [-dp host_file [-dp_cmd worker_cmd] [-dp_workers workers_number] [-dp_no_worker_logging]]
```

To set up a distributed job:

## 1. Create the host file.

The host file should be formatted as shown in the following example:

```
# host file sample containing 2 worker machines \ (my_server_1 and my_server_2) # and specifying rsh as connection mode 1 | my_server_1 | 1 | /tmp | RSH | rsh 1 | my_server_2 | 1 | /tmp | RSH | rsh
```

## 2. Define the log directory.

This step is optional.

## Note:

The log directory should be visible from all workers, that is, it should be network-visible. If you don't specify the log directory, then the current directory is used as the log directory. In this case, the current directory also should be network-visible.

## 3. Run the genCache command:

```
runProg genCache test_layout.oasis cache_directory \ -dp host_file -dp_workers 2
```

<!-- image -->

## E

## Layout Format Conversion

These topics are available:

- Converting GDS and OASIS to Optimized OASIS
- Converting GDS and OASIS to Optimized OASIS in DP mode
- Converting OASIS to GDS

## Converting GDS and OASIS to Optimized OASIS

gds2oa i  ut l y The gds2oasis converter is a command-line utility that generates Optimized OASIS. Optimized OASIS is a legal OASIS-spec compliant OASIS file that any OASIS-compliant reader can read. Synopsys tools can load the Optimized OASIS instantly even when opening the layout for the first time (as if it had a cache file). Also, Optimized OASIS has better performance because of optimizations while converting the input layout. The gds2oasis utility is available in the /ICVWB\_INSTALL\_DIR/bin directory and needs to be run from the terminal window.

## Syntax

## For Linux

gds2oa i ut l y gds2oasis parameters\_value input\_filename output\_filename

## For Windows

gds2oasis.exe parameters\_value input\_filename output\_filename

## Returns

1 on syntax/input error and 0 otherwise.

## Arguments

parameters\_value

Specifies a list of paired parameters and values, for example, {parameter1 value1 parameter2 value2 …}.

<!-- image -->

```
-dp host_file
```

Specifies using distributed processing with the servers listed in host\_file .

```
-dp_workers workers_number
```

Specifies the number of workers used during distributed processing. The number of workers should be less than or equal to the total number of slots provided by host\_file . The default is 4.

```
-dp_no_worker_logging
```

Log file Workers can be disabled by using the -dp\_no\_worker\_logging command. For more information about using the Optimized OASIS DP options please see #unique\_364.

## Note:

The Windows platform does not support DP options.

```
-cores number
```

Specifies the number of cores to be used during sorting and compaction. This argument accepts positive integers. If it is not specified, the number of cores is determined automatically.

```
-cacheDir dir_name
```

Specifies cache file directory for the layout servers used to open the input file. If this argument is not specified, the cache is switched off.

```
-compress level
```

Indicates the OASIS compression level. It accepts numbers from 0 to 9. 0 means no compression and no CBLOCKs are generated in this case. The default is 6.

```
-omit_fig_properties
```

If this argument is provided, properties of shapes and instances are not converted into the output OASIS OPT file. Otherwise, all shapes and instances properties are converted into the output file.

```
-remove_duplicate_refs boolean
```

When set to 1 , duplicate references are removed during the conversion of GDS and OASIS layouts to Optimized OASIS.

```
-round_end_seg_count number
```

Provides the number of vertices that should be used while converting round ends of paths to polygons. The default is 8. This argument accepts integers greater than or equal to 8.

<!-- image -->

```
-load_gdsii_boxes
```

When the value is true, GDSII boxes are loaded as polygons and converted to a Optimized OASIS file. The default is false.

```
-round_path
```

Controls the rounding of corners for circular paths. When the value is true, the path corners are rounded along with the path ends. The default is false.

```
-wind_path
```

Specifies path winding. For a more detailed description, see the default windpath command in the IC Validator WorkBench Command Manual . The default is false.

```
-path_close_smooth on|off
```

Creates a smooth connection between the start and end of a closed path outline when converting GDS files to Optimized OASIS files.

```
-progress
```

Display at the terminal the completion percentage of the optimized layout file generation.

```
input_filename
```

Indicates the input layout file. It accepts all layout types supported by the applications.

```
output_filename
```

Indicates the output layout file, which is a spatially sorted valid OASIS file. No autocomplete for the file extension is applied.

```
-nooptimize
```

When the -nooptimize mode is used, a regular OASIS file is generated. In this mode, distributed processing is not available.

## Description

Takes the input file and converts it to an optimized and spatially organized OASIS OPT file, which is a valid OASIS file with increased search performance.

## Converting GDS and OASIS to Optimized OASIS in DP mode

The gds2oasis converter includes a DP option for GDSII files. This enables you to speed up Optimized OASIS conversion in cases where the file is located on a network server and many host machines are available.

<!-- image -->

The Host File

Host machines for the Master and Workers should be dedicated. All hosts should have access to the layout file located on the network server. Then the host information file should be created.

The Log File

Optimized OASIS generates several log files in DP mode; this is similar to the Log File that generates the genCache in DP mode. For additional information, see Using the genCache DP Option.

The Number of Workers

You should specify the number of Workers to be used during DP Optimized OASIS conversion. The number of Workers should be less than or equal to the total number of slots provided by the host information file. Optimized OASIS uses four workers by default. You can specify the number of workers by using Optimized OASIS's -dp\_workers command line option.

Additionally, you can pass regular gds2oasis options such as -compress or other private options.

## Converting OASIS to GDS

The oasis2gds is a command-line script that is available in the /ICVWB\_INSTALL\_DIR/bin directory and performs OASIS to GDS conversions up to 40% faster when compared to opening and then saving the layout, and consumes up to 5% lesser memory. The syntax for the script is as follows:

oasis2gds &lt;input\_filename&gt; &lt;output\_filename&gt;

To use the oasis2gds script:

1. Go to the ICVWB\_INSTALL\_DIR/bin directory.
2. Run the oasis2gds script from the Windows or Linux command-line. For example:

```
ICVWB_INSTALL_DIR is the installation directory.
```

```
◦ Windows: oasis2gds.bat layout1.oas layout2.gds ◦ Linux: oasis2gds layout1.oas layout2.gds
```

<!-- image -->

## F

## Using Python With the Application

This appendix describes the using Python to script the application and using the iLayout Python module for working with layouts.

These topics are available:

- Python Scripting
- iLayout Python Module
- Boolean Operations on snps.ilayout Objects
- Creating Python GUI Widgets

## Python Scripting

To start scripting ICVWB in Python, you need to first import snps.wb . All commands described in the ICVWB Command Manual-with the exception of those that explicitly require Tcl callbacks or objects, such as cell data , find init -data , bop commandsare available as functions.

The function names follow a simple rule: spaces in the command name are replaced with underscores. For example, layout root cells -&gt; layout\_root\_cells() .

Here are some examples of working with the ICVWB application using Python:

```
import snps.wb as wb wb.layout_new("a") wb.cell_object_add({'type':'rectangle','coords':[0,0,200,50]}) wb.layout_open("layouts/4bit.oas") [cell for cell in wb.layout_cells()] #-> ['1bit', '4bit'] bboxes=[wb.cell_bbox(cell=cell) for cell in wb.layout_cells()] bboxes[0] #-> [-15000000.0, -59000000.0, 83000000.0, 20000000.0]
```

You can access Python script custom arguments (excluding the application-specific predefined arguments) using sys.argv , or access the full list of all arguments using snps.wb.argv .

<!-- image -->

## Note:

```
It is recommended to avoid known ICVWB parameters like -nodisplay , -cores , -help , and so on for your_script_args . These parameters are processed by ICVWB itself and might not be passed to your Python script in sys.argv .
```

You can also use the Python Pane to access snps.ilayout : the iLayout Python module. The iLayout module is a simple yet powerful API for reading or writing layout files. See iLayout Python Module for more information.

## iLayout Python Module

The snps.ilayout Python module provides a simple API for reading and writing layout data. The module currently supports GDSII, GDSII.gz, OASIS, and OASIS\_OPT formats. The implementation scales to very large layouts: it can read and write full-chip designs. There is no Python package for snps.ilayout . The module is included with IC Validator WorkBench and can be used from its Python Pane.

## Print basic information about an OASIS layout

```
import snps.ilayout as il lout = il.open('/path/to/layout.oas') print(lout.dbu) print(lout.properties) print([cell.name for cell in lout])
```

## API Overview

The module exports two main functions: open() and save() .

snps.ilayout.open() loads a layout and returns a snps.ilayout.Layout object. The latter provides a cell iterator and each cell provides an iterator of elements.

snps.ilayout.save() saves any object with expected attributes; sub-classing snps.ilayout.Layout is not needed (and not supported).

## Cell elements are of either of the following types:

- snps.ilayout.Poly
- snps.ilayout.Path
- snps.ilayout.Ref
- snps.ilayout.Text

<!-- image -->

<!-- image -->

All snps.ilayout objects (including Layout and Cell) are immutable. Modification is only done by creating a new object. The following example illustrates this. The example normalizes text elements by setting the magnification to 1.

## Normalize text element magnification

```
import snps.ilayout as il def elem_normalized(elem): """ Normalizing the scales of il.Text objects by dropping the scale, i.e., default 1 is applied""" if type (elem) == il.Text: return il.Text(string=elem.string, location=elem.location, layer=elem.layer, dt=elem.dt, properties=elem.properties) return elem class cell_normalized: """ Cell with a given cell. """ def __init__(self, cell): self.cell = cell self.name = cell.name self.properties = cell.properties def __iter__(self): return (elem_normalized(elem) for elem in self.cell) class lout_normalized: """ Layout with a given layout. """ def __init__(self, layout): """ Builds a layout with the given layout. """ self.layout = layout self.properties = layout.properties self.dbu = layout.dbu def __iter__(self): """ Cell iterator """ return (cell_normalized(cell) for cell in self.layout) lout = il. open ('/path/to/layout.gds') il.save(lout_normalized(lout), 'normalize_text_mag.gds', format ='gds', dbu=lout.dbu)
```

snps.ilayout.children() returns cell children as iterable objects of strings. snps.ilayout.bbox() returns a tuple of minimum and maximum points of given object. snps.ilayout.filter() returns cell objects as iterable objects.

## Print the cell's children, bbox, and filtered layers

```
import os import sys import snps.ilayout as il def parent_child(lout): """Generates (parent, child) pairs of cell names for the layout passed as argument.""" for cell in lout: for child in il.children(cell): yield (cell.name, child) def cells_bbox(lout): """Generates (cell_name, bbox) pairs of cell names for the layout passed as argument.""" for cell in lout: yield(cell.name, il.bbox(cell, lout)); def filter_layers(lout): """Generate layer iterator of given cell""" mylist = ((10,0),(11,0),(12,0),(13,0),(14,0)) yield(il.filter(il.filter.layer_dt(mylist), cell)) print("# Print every cell hierarchy for a1248.gds") file = f'/path/to/a1248.gds' layout = il.open(file) all_hier = parent_child(layout) for hier in all_hier: print(hier) all_bbox = cells_bbox(layout) for bbox in all_bbox: print(bbox) cell = next(iter(layout)) layers = filter_layers(cell) for layer in layers: print(layer) sys.exit()
```

## Reference

## snps.ilayout.Layout class - representation of a layout file Data descriptors:

```
dbu: double - layout DBU in SI units ( meters) properties: List[snps.ilayout.Property] - file-level layout properties
```

<!-- image -->

## Methods:

```
__iter__(self: snps.ilayout.Layout) -> snps.ilayout.layout iterator Iterator for a layout file __repr__(self: snps.ilayout.Layout)
```

Returns a string containing a printable representation of the snps.ilayout.Layout object.

## Example:

```
lout = il.open('/path/to/layout.oas') print(lout.dbu) print(lout.properties) print([cell.name for cell in lout]) repr(lout)
```

## Output:

```
1e-09 [] ['1bit', '4bit'] 'snps.ilayout.open(/path/to/layout.gds)'
```

## snps.ilayout.Cell class - representation of a cell

## Data descriptors:

```
name: str - cell name properties: List[snps.ilayout.Property] - cell-level properties Methods: __iter__(self: snps.ilayout.Cell) -> snps.ilayout.cell iterator Iterator for cell contents __repr__(self: snps.ilayout.Layout)
```

Returns a string containing a printable representation of the snps.ilayout.Layout object.

## Example:

```
lout = il.open('/path/to/layout.oas') #Taking the first cell of the layout cell = next(iter(lout)) print(cell.name) print(cell.properties) print([elem for elem in cell])
```

<!-- image -->

## Output:

```
rep-1 [Property(name='cell_pro', value_list=['1 2.2 "str 1" "str 2" "rep-1"'])] [Poly(boundary=[(0, 0), (90, 30), (380, 30), (400, 0)], layer=23, dt= 0, properties=[Property(name='prop1', value_list=['"HTRAP" 1 2.2 "str 1" "str 2" "rep-1"'])]), Poly(boundary=[(0, 5500), (90, 5530), (380, 5530), (400, 5500)], layer=23, dt= 0, properties=[Property(name='prop1', value_list=['"HTRAP" 1 2.2 "str 1" "str 2" "rep-1"'])]), … ]
```

## snps.ilayout.Property class - representation of an OASIS-style property

## Data descriptors:

```
name: unicode - property name
```

```
value_list: List[object] - property value list Methods: __init__(self: snps.ilayout.Property, name: unicode, value_list: List[object]=[]) Builds the snps.ilayout.Property object with the given name: string and value_list: list of objects. name and value_list are keyword arguments. value_list has a default argument empty list [] . __repr__(self: snps.ilayout.Property)
```

Returns a string containing a printable representation of the snps.ilayout.Property object.

## Example:

```
prop = il.Property(name='a', value_list=['"HTRAP26" 1 2.2  "str 1" "str 2" "a"']), il.Property(name='b', value_list=['"PATH" 1 2.2 "str 1" "str 2" "a"']), il.Property(name='c', value_list=['"Reference" "property:" "ref" "a" "type"11']), il.Property(name='d', value_list=['"TEXT" 1 2.2 "str 1" "str 2" "a"'])
```

## snps.ilayout.Poly class - representation of a polygon

## Data descriptors:

```
Boundary: List[Tuple[int, int]] - polygon boundary (vector of points) layer: int - polygon layer dt: int - polygon data type properties: List[snps.ilayout.Property] - polygon properties
```

<!-- image -->

## Methods:

```
__init__(self: snps.ilayout.Poly, boundary: List[Tuple[int, int]], layer: int=0, dt: int=0, properties: List[snps.ilayout.Property]=[] Builds the snps.ilayout.Poly object, with the given keyword arguments: boundary , layer , dt and properties . layer and dt have default set to 0. properties also has default set to [] . __repr__(self: snps.ilayout.Poly) Returns a string containing a printable representation of the snps.ilayout.Poly object. Example: poly=il.Poly(boundary=[(0,0), (0,100), (100, 100), (100,0)], layer = 0,
```

```
properties=[prop[0]])
```

## snps.ilayout.Path class - representation of a path; derived from Poly

## Data descriptors:

```
centerline: List[Tuple[int, int]] - path center line (vector of points) width: int - path width start_ext: int - path start extension end_ext: int - path end extension Data descriptors inherited from Poly: boundary: List[Tuple[int, int]] - path boundary (vector of points) layer: int - path layer dt: int - path data type properties: List[snps.ilayout.Property] - path properties Methods: __init__(self: snps.ilayout.Path, centerline: List[Tuple[int, int]], start_ext: int=0, end_ext: int=0, width: int, layer: int=0, dt: int=0, properties: List[snps.ilayout.Property]=[]) Builds the snps.ilayout.Path object with given keyword arguments: centerline , start_ext , end_ext , width , layer , dt and properties . The start_ext , end_ext , layer, and dt have defaults set to 0. properties has a default set to [] . __repr__(self: snps.ilayout.Path)
```

<!-- image -->

```
location: Tuple[int, int] scale: double - text scale (GDSII-only) layer: int - text layer
```

<!-- image -->

```
Returns a string containing a printable representation of the snps.ilayout.Path object. Example: path = il.Path(centerline=[(225, 115), (85,115), (85, 165)], start_ext=10, end_ext=10, width=20, properties=[prop[1]]) snps.ilayout.Ref class - representation of a reference Data descriptors: cell: unicode - target cell location: Tuple[int, int] - reference location angle: float - reference angle flip: bool - mirror through the X-axis mag: float - reference magnification properties: List[snps.ilayout.Property] - reference properties Methods: __init__(self: snps.ilayout.Ref, cell: unicode, location: Tuple[int, int], angle: float=0, flip: bool=False, mag: float=1, properties: List[snps.ilayout.Property]=[]) Builds the snps.ilayout.Ref object with given keyword arguments cell , location , angle , flip , mag and properties . angle has default set to 0, flip has default set to False, mag has default set to 1, and properties has a default set to [] . __repr__(self: snps.ilayout.Ref) Returns a string containing a printable representation of the snps.ilayout.Ref object. Example: ref=il.Ref(cell='1', location=(0,0), angle=50, flip=1, mag=10, properties=[prop[2]]) snps.ilayout.Text class - representation of a text Data descriptors: string: str - text string - text location
```

<!-- image -->

```
dt: int - text data type properties: List[snps.ilayout.Property] - text properties Methods: __init__(self: snps.ilayout.Text, string: str, location: Tuple[int, int], layer: int=0, dt: int=0, properties: List[snps.ilayout.Property]=[]) Builds the snps.ilayout.Text object with given keyword arguments string , location , layer (default is set to 0), dt (default is set to 0) and properties (default is set to [] ). __repr__(self: snps.ilayout.Text) Returns a string containing a printable representation of the snps.ilayout.Text object. Example: text=il.Text(string='text', location=(200,200), layer=0, dt=0, properties=[prop[3]])
```

## snps.ilayout.open (arg0: str, **kwargs) -&gt; snps.ilayout.Layout

Loads a layout (in GDSII, OASIS, OASIS\_OPT and GDSII.GZ formats) from the given file\_path and returns a Python object of type snps.ilayout.Layout . The first argument is the file\_path of the loaded layout; it is a string. The **kwargs are optional keyword arguments.

The optional keyword arguments are:

- cache\_dir: str

Specifies the path of the directory for saving/reading the layout cache file. This argument accepts a ':' separated list of paths. When setting the cache directories with default layout\_cache\_dir or from Options &gt; Layout &gt; Cache in the graphic user interface, the application checks that there is a writable directory available in the cache paths, otherwise issues an error message. The first writable cache-directory is used for writing the cache-files. For more details, see the default layout\_cache\_dir command in the IC Validator WorkBench Command Manual .

If you do not specify an argument, no cache file is created.

- cores: int

Specifies the maximal allowed layout load concurrency. You can specify an integer from one through the maximum of 256. If you specify more cores than the machine has, then the machine's core count is used instead. If you do not specify an argument the number of available cores is used. For more details, see the default layout\_oasis\_cores command in the IC Validator WorkBench Command Manual .

## Example:

```
lout = il.open('/path/to/layout.gds', cache_dir= '/tmp/', cores=8)
```

## snps.ilayout.save (arg0: object, arg1: str, **kwargs)

Writes any Python object with expected attributes as a file in the requested format (in GDSII, OASIS and OASIS\_OPT formats).

## Arguments

```
arg0: object
```

As a first argument, it receives any Python object, which will have dbu and properties (the last one is optional) and return the cell iterator. The cell will have the name and properties (optional) and return an iterator of elements. The elements are of the

following types: snps.ilayout.Poly , snps.ilayout.Path , snps.ilayout.Ref and snps.ilayout.Text .

```
arg1: str
```

As a second argument, it receives a string which is a path of the new created file.

The required keyword arguments are:

- format: str - it can be gds , oasis or oasis\_opt .
- dbu: double - layout DBU, in SI units (meters).

## Example:

```
il.save(lout, 'new_4bit.gds', format='gds', dbu=lout.dbu)
```

## snps.ilayout.children (cell)

Returns iterable object of strings.

## Arguments

cell

Indicates a cell-like object of which you want to get the children.

## Example:

```
lout = il.open('/path/to/4bit.gds', cache_dir= '/tmp/', cores=8) cell = next(iter(lout)) print(cell.name) for child in il.children(cell): print(child)
```

<!-- image -->

<!-- image -->

## snps.ilayout.bbox (cell: object, layout: object) ) -&gt; Tuple[int, int, int, int]

Returns the bounding box of the cell (or cell-like object), including all referenced cells (child cells).

## Arguments

```
cell: object
```

Indicates the specific cell.

```
layout: object
```

Use the layout argument for finding the child cells.

## Example:

```
import snps.ilayout as il lout = il.open('/path/to/4bit.oas') for cell in lout: cell_bbox = il.bbox(cell, lout) print(cell.name) print(cell_bbox)
```

## Layout Creation Example

The following example shows a simple case of creating and saving a new layout.

## Simple layout creation

```
import snps.ilayout as il class layout: """ Layout with a given list of cells. """ def __init__(self, cells): """ Builds a layout with the given cell list. """ self.dbu = 1e-9 self.properties = [] self.cells = cells def __iter__(self): """ Cell iterator """ return iter(self.cells) class cell: """ Cell with a given list of elements. """ def __init__(self, name, elems): """ Builds a cell with a given element list. """ self.elems = elems self.name = name def __iter__(self): """ Cell contents iterator""" return iter (self.elems) # Create a list of elements. elements = [il.Poly(boundary=[(0,0), (0,100), (100,100), (100,0)]), il.Poly(boundary=[(200,200), (200,300), (300, 300), (300,200)])] elements.append(il.Text(string='text', location=(250, 100), layer=5, dt=0)) # Create a cell with the above list of elements. new_cell = cell('a', elements) # Create a layout with new_cell. new_layout = layout([new_cell]) # Save new_layout in gds format. il.save(new_layout, 'new_created_layout.gds', dbu=new_layout.dbu, format='gds')
```

## Boolean Operations on snps.ilayout Objects

The snps.pytbool module can be used to perform Boolean operations on snps.ilayout objects. The iLayout Python module is implemented with efficient layer/datatype filtering and cell flattening methods to support Boolean operations.

- Functional Description
- Layer/datatype Filtering
- Flattening Cells

<!-- image -->

## Functional Description

Boolean operations take one or more iterables, which yield il.Poly objects, and the result is a similar iterable object. For example, snps.ilayout.Cell objects can be directly passed to pytBool operators.

## Note:

When passing snps.ilayout.Cell objects to a pytbool operation, polygons from subcells are not part of the Boolean operation . If you want to perform the operation on the cell including polygons from placements, the cell should be flattened first, using, for example, snps.wb.layout\_extrac('-flat', ...) .

## The following Boolean operations are available:

```
· snps.pytbool.and_(iterable1, iterable2) · snps.pytbool.or_(iterable1, iterable2) · snps.pytbool.xor_(iterable1, iterable2) · snps.pytbool.not_(iterable1, iterable2)
```

## Layer/datatype Filtering

To restrict the Boolean operation to certain layers/datatypes, the following approach is recommended:

```
iterable = il.filter(il.filter.layer_dt((10, 10)), cell)
```

The following functions are implemented in the snps.ilayout module:

## Syntax

```
snps.ilayout.filter.layer_dt()
```

## This takes either:

- a Tuple[int, int]- a (layer, datatype) pair, or
- a List[Tuple[int, int]]- a list of layer/datatypes

And produces a predicate object.

## Syntax

```
snps.ilayout.filter()
```

This takes a predicate object returned by snps.ilayout.filter.layer\_dt() and a Cell object. And returns a Cell object, which only iterates elements on the specified layers.

<!-- image -->

## Example

```
from snps import ilayout as il, pytbool as pb # Open a flat layout, get the (single) cell. lout = il.open('flat_lout.oas') cell = next(iter(lout)) # Filter layer/dt 1:0 and 2:0. lyr1 = il.filter(il.filter.layer_dt((1, 0)),  cell) lyr2 = il.filter(il.filter.layer_dt((2, 0)),  cell) # XOR lyr1 and lyr2. diff = pb.xor_(lyr1, lyr2) # Name the diff and save it. named_diff = name_cell(diff, 'XOR') il.save([named_diff], 'xor.oas', dbu=lout.dbu, format='oasis') class name_cell: """ Renames the orig cell with new name """ def __init__(self, orig, name): self.name = name self.orig = orig def __iter__(self): """ Cell contents iterator""" return iter(self.orig)
```

## Flattening Cells

You can flatten cells using the iLayout Python feature. The snps.ilayout.flatten() method takes as arguments a cell-like object and a layout-like object and returns a flattened cell object.

## Syntax

```
snps.ilayout.flatten(cell, layout) Arguments cell A cell-like object. layout A layout-like object. Example """ Function to drop all references to the cells """ def drop_refs (elem):
```

<!-- image -->

```
if type(elem) != il.Ref: return elem class layout: def __init__(self, cells): self.dbu = 1e-9 self.properties = [] self.cells = cells def __iter__(self): return iter(self.cells) class cell: def __init__(self, name, elems): self.elems = elems self.name = name def __iter__(self): return (drop_refs(elem) for elem in self.elems) import snps.ilayout as il import snps.pytbool as pb lout = il.open('/path/to/layout.oasis') my_cell=[c for c in lout if c.name == 'my_cell_name'][0] flat_cell = il.flatten(my_cell, layout=lout) newLayout = layout([cell("my_cell_name_flat", flat_cell)]) il.save(newLayout, 'flat.oas', dbu=1e-9, format='oasis')
```

## Creating Python GUI Widgets

You can create custom QWidgets in the IC Validator WorkBench application by using the PySide2 Python module.

To use PySide2, you need to install it by running the following command

```
icvwb -nodisplay -python -m pip install PySide2 Examples from PySide2.QtWidgets import * import snps.wb as wb """ Construct the widget """ wnd = QMainWindow() widget = QWidget(wnd) wnd.setCentralWidget(widget) layout = QVBoxLayout(widget) menu = QMenuBar() layout.addWidget(menu)
```

<!-- image -->

```
fileMenu = QMenu('File') menu.addMenu(fileMenu) open = fileMenu.addAction('Open') exit = fileMenu.addAction('Exit') actMenu = QMenu('Actions') menu.addMenu(actMenu) dbu = actMenu.addAction('Show dbu') names = actMenu.addAction('Cell names') """ Define the actions to perform for each button """ def layoutDBU(): wb.layout_dbu() def layoutOpen(): wb.layout_open("/path/to/layout.oas", "?") def cellNames(): wb.layout_cells() """ Connect the buttons to the functions """ open.triggered.connect(lambda : layoutOpen()) exit.triggered.connect(wnd.close) dbu.triggered.connect(layoutDBU) names.triggered.connect(cellNames) """ Show the widget """ wnd.show()
```

<!-- image -->