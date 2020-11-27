# class glob:
# Globals module

# file handles
logger_main = 0
logger_sql = 0

# system
system_version = "v2.0.2"
system_build = "23"
system_sql = "v001"
current_open_db = ""

# runtime
scriptpath = ""
mainpath = ""
localespath = ""
language = 0

# configuration
slide_horizontal = 0
slide_vertical = 0
loc_database = ""
loc_scans = ""
loc_orders = ""
loc_logs = ""
loc_backups = ""
radio1_language = 0
radio2_language = 0

# screen settings
screen_width = 0
screen_height = 0
screen_width_calc = 0
screen_height_calc = 0
screen_width_setup = 0
screen_height_setup = 0
screen_top = 0
screen_left = 0

# SQL connection
conn = 0

# root TK
root = 0

# menu
menu = 0
filemenu = 0
tablemenu = 0
datamenu = 0
sysmenu = 0
helpmenu = 0

# buttons
button_add = 0
button_copy = 0
button_del = 0
button_nl = 0
button_en = 0

# frames
filterframe = 0
buttonframe = 0
sqlframe = 0
photoframe = 0
messageframe = 0

filter_frame = 0
button_frame = 0
sql_frame = 0
photo_frame = 0
message_frame = 0
message_text = ""

# sysconfig edit screen
top = 0
edit_edit_frame = 0
edit_button_frame = 0
button_edit_cancel = 0
button_edit_save = 0

button_filter_apply = 0
filter_label_country = 0
combo_country = 0
filter_label_denomination = 0
combo_denomination = 0

right_front_frame = 0
right_front_canvas = 0
right_rear_frame = 0
right_rear_canvas = 0
right_value_frame = 0
right_value_canvas = 0

mainlog = ""
radio1_mainlog = 0
radio2_mainlog = 0
radio3_mainlog = 0

sqllog = ""
radio1_sqllog = 0
radio2_sqllog = 0
radio3_sqllog = 0

# journal files
main_journal = ""
sql_journal = ""

# Actual data lists
coin_data = []
country_data = []

# sql treeview
treecolumns = ("#0", "#01", "#02", "#03", "#04", "#05", "#06", "#07", "#08")
treeheaders = [(0, "id"), (1, "SQL RecNo"), (2, "Private index"), (3, "Index"), (4, "Krause"), (5, "denomination"),
               (6, "valuta"), (7, "country"), (8, "year")]
style = ""