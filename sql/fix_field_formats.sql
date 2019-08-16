USE collector;
UPDATE Dev_Forms SET Field_Format = "{:,d}" WHERE Type="int(11)";
UPDATE Dev_Forms SET Field_Format = "{:10s}" WHERE Type="date";
UPDATE Dev_Forms SET Field_Format = "{:10s}" WHERE Type="time";
UPDATE Dev_Forms SET Field_Format = "{:,.6f}" WHERE Type="decimal(20,6)";
UPDATE Dev_Forms SET Field_Format = "{:s}" WHERE Type="tinyint(4)";
UPDATE Dev_Forms SET Field_Format = "{:21s}" WHERE Type="datetime";
UPDATE Dev_Forms SET Field_Format = "{:s}" WHERE Type LIKE "varchar%";




