### Gen Collector Menu Documentation

Collector's Menu Generation Documentation

Required Files:

## gen/gen_menu_functions.py

Imports functions and definitions for menu creation. Need to define home
folder , the this module creates all required paths and filenames

Actual structure:

| Folder                    | Description                       | KEY                |
| ------------------------- | -----------                       | ---                |
| **HOME**                  |   Root System Structure           | **HOME**           |
| **HOME**/collector/tools  |   Tools Folder                    | **TOOLS**          |
| **TOOLS**/gen             |   Auto Code Generation Module     |                    |
| **TOOLS**/code            |   Code Folder                     | **CODE**           |
| **CODE**/auto             |   Auto generated files            | **AUTO**           |
| **AUTO**/views            |   Auto generated endpoint views   | **AUTO_VIEWS**     |
| **AUTO**/templates        |   Auto generated jinja templates  | **AUTO_TEMPLATES** |
|                           |       **/base.html**              |                    |
| **AUTO**/models           |   Auto generated ORM DB classes   | **AUTO_MODELS**    |
| **AUTO**/forms            |   Auto generated table forms      | **AUTO_FORMS**     |
| **AUTO**/includes         |   Auto generated include files    | **AUTO_INCLUDES**  |
|                           |       /collector_style.css        |                    |
|                           |       **/collector_navbar.html**  |                    |
|                           |       /menu.html                  |                    |
| **CODE**/src              |   Source Folder                   | **SRC**            |
|                           |       base_header.html            |                    |
| **SRC**/include           |   Files to be included            | **SRC_INCLUDE**    |
| **CODE**/output           |   Output folder                   | **OUTPUT**         |
                    
## Module functions

| Function                          | Description                               |
| --------                          | -----------                               |
| **Include_File** (file_name, f)   | Includes a file in specific output stream |
| **Comment** (comment, f)          | Includes a comment in output file         |
| **Gen_SubOption** (suboption, f)  | Generates a Menu sub-option               |
| **Gen_Option** (option, f)        | Generates a menu option                   |
| **Gen_Menu** (Menu, ACCOUNT)      | Generates full Menu                       |
| **Doc_bottom** (f)                | Generates document bottom                 |
| **Doc_head** (f)                  | Generates document header                 |
| **Style** ()                      | Generates Global Style Sheet file         |
| **Header** (f)                    | Generats Header                           |
| **Gen_Doc** ()                    | Generates Document                        |
| **Option** (name, url='/')        | Creates a new Option object               |
| **Sub_Option**
(name, url='/under_construction', 
hr=False, header=None)              | Creates a new sub-option object           |

## Main Program

### gen_collector_menu.py

Generates System Menu depending on actual in-code configuration.
Options and suboptions should be defined, then this program will create:

* **collector_navbar.html** 
    
    Systems Navigation Bar, including all options 
    and suboptions and roles handling. saved in:
    **AUTO_INCLUDES** folder (see below)
                            
* **base.html**
    
    Base Jinja HTML template, all other templates will inherit from this file
    For auto generation of this file it requires (and will include):
    
    * **SRC**/base_header.html  source file. should be edited in order to implement global base template definitions
    
    * **AUTO_INCLUDES**/collector_navbar.html   auto-Generated, (see above)
