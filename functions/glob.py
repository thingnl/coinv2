# class glob:
# Globals module

# file handles
logger_main = 0
logger_sql = 0

# system
system_version = "v2.0.2"
system_build = "23"
system_sql = "v001"

# runtime
scriptpath = ""
mainpath = ""
localespath = ""
language = 0
open_filename = ""                          # Currently opened file
current_open_db = ""                        # Currently opened file incl path

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
cur = 0

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
databaseframe = 0

filter_frame = 0
button_frame = 0
sql_frame = 0
photo_frame = 0
message_frame = 0
database_frame = 0
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

# sql treeview scrollbars
scrollh = 0
scrollv = 0


# Column radio buttons
radio_private_index = "Show"
radio_index = "Show"
radio_krause_index = "Show"
radio_denomination = "Show"
radio_valuta = "Show"
radio_country = "Show"
radio_year = "Show"
radio_mmt = "Show"
radio_quality = "Show"
radio_remark = "Show"
radio_coinage = "Show"
radio_diameter = "Show"
radio_edge = "Show"
radio_edgetext = "Show"
radio_stiketype = "Show"
radio_weight = "Show"
radio_designer = "Show"
radio_frontside = "Show"
radio_rearside = "Show"
radio_material = "Show"
radio_rarity = "Show"
radio_frontjpg = "Show"
radio_rearjpg = "Show"
radio_serie = "Show"
radio_storage = "Show"
radio_have = "Show"
radio_want = "Show"
radio_ordered = "Show"
radio_sale = "Show"
radio_other = "Show"
radio_supplier = "Show"
radio_order = "Show"
radio_price = "Show"
radio_mint = "Show"
radio_mintmaster = "Show"
radio_ruler = "Show"
