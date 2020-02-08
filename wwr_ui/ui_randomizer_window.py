# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'randomizer_window.ui',
# licensing of 'randomizer_window.ui' applies.
#
# Created: Sat Feb  8 13:16:48 2020
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 670)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 837, 559))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.seed = QtWidgets.QLineEdit(self.tab)
        self.seed.setObjectName("seed")
        self.gridLayout.addWidget(self.seed, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.clean_iso_path = QtWidgets.QLineEdit(self.tab)
        self.clean_iso_path.setObjectName("clean_iso_path")
        self.gridLayout.addWidget(self.clean_iso_path, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.output_folder = QtWidgets.QLineEdit(self.tab)
        self.output_folder.setObjectName("output_folder")
        self.gridLayout.addWidget(self.output_folder, 1, 1, 1, 1)
        self.output_folder_browse_button = QtWidgets.QPushButton(self.tab)
        self.output_folder_browse_button.setObjectName("output_folder_browse_button")
        self.gridLayout.addWidget(self.output_folder_browse_button, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.generate_seed_button = QtWidgets.QPushButton(self.tab)
        self.generate_seed_button.setObjectName("generate_seed_button")
        self.gridLayout.addWidget(self.generate_seed_button, 2, 2, 1, 1)
        self.clean_iso_path_browse_button = QtWidgets.QPushButton(self.tab)
        self.clean_iso_path_browse_button.setObjectName("clean_iso_path_browse_button")
        self.gridLayout.addWidget(self.clean_iso_path_browse_button, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progression_platforms_rafts = QtWidgets.QCheckBox(self.groupBox)
        self.progression_platforms_rafts.setObjectName("progression_platforms_rafts")
        self.gridLayout_2.addWidget(self.progression_platforms_rafts, 5, 0, 1, 1)
        self.progression_dungeons = QtWidgets.QCheckBox(self.groupBox)
        self.progression_dungeons.setChecked(True)
        self.progression_dungeons.setObjectName("progression_dungeons")
        self.gridLayout_2.addWidget(self.progression_dungeons, 0, 0, 1, 1)
        self.progression_long_sidequests = QtWidgets.QCheckBox(self.groupBox)
        self.progression_long_sidequests.setObjectName("progression_long_sidequests")
        self.gridLayout_2.addWidget(self.progression_long_sidequests, 2, 1, 1, 1)
        self.progression_short_sidequests = QtWidgets.QCheckBox(self.groupBox)
        self.progression_short_sidequests.setObjectName("progression_short_sidequests")
        self.gridLayout_2.addWidget(self.progression_short_sidequests, 2, 0, 1, 1)
        self.progression_treasure_charts = QtWidgets.QCheckBox(self.groupBox)
        self.progression_treasure_charts.setObjectName("progression_treasure_charts")
        self.gridLayout_2.addWidget(self.progression_treasure_charts, 7, 1, 1, 1)
        self.progression_submarines = QtWidgets.QCheckBox(self.groupBox)
        self.progression_submarines.setChecked(False)
        self.progression_submarines.setObjectName("progression_submarines")
        self.gridLayout_2.addWidget(self.progression_submarines, 5, 1, 1, 1)
        self.progression_triforce_charts = QtWidgets.QCheckBox(self.groupBox)
        self.progression_triforce_charts.setObjectName("progression_triforce_charts")
        self.gridLayout_2.addWidget(self.progression_triforce_charts, 7, 0, 1, 1)
        self.progression_great_fairies = QtWidgets.QCheckBox(self.groupBox)
        self.progression_great_fairies.setChecked(True)
        self.progression_great_fairies.setObjectName("progression_great_fairies")
        self.gridLayout_2.addWidget(self.progression_great_fairies, 3, 0, 1, 1)
        self.progression_spoils_trading = QtWidgets.QCheckBox(self.groupBox)
        self.progression_spoils_trading.setObjectName("progression_spoils_trading")
        self.gridLayout_2.addWidget(self.progression_spoils_trading, 2, 2, 1, 1)
        self.progression_misc = QtWidgets.QCheckBox(self.groupBox)
        self.progression_misc.setChecked(True)
        self.progression_misc.setObjectName("progression_misc")
        self.gridLayout_2.addWidget(self.progression_misc, 3, 2, 1, 1)
        self.progression_minigames = QtWidgets.QCheckBox(self.groupBox)
        self.progression_minigames.setObjectName("progression_minigames")
        self.gridLayout_2.addWidget(self.progression_minigames, 4, 0, 1, 1)
        self.progression_free_gifts = QtWidgets.QCheckBox(self.groupBox)
        self.progression_free_gifts.setChecked(True)
        self.progression_free_gifts.setObjectName("progression_free_gifts")
        self.gridLayout_2.addWidget(self.progression_free_gifts, 3, 1, 1, 1)
        self.progression_eye_reef_chests = QtWidgets.QCheckBox(self.groupBox)
        self.progression_eye_reef_chests.setObjectName("progression_eye_reef_chests")
        self.gridLayout_2.addWidget(self.progression_eye_reef_chests, 7, 2, 1, 1)
        self.progression_big_octos_gunboats = QtWidgets.QCheckBox(self.groupBox)
        self.progression_big_octos_gunboats.setObjectName("progression_big_octos_gunboats")
        self.gridLayout_2.addWidget(self.progression_big_octos_gunboats, 5, 2, 1, 1)
        self.progression_battlesquid = QtWidgets.QCheckBox(self.groupBox)
        self.progression_battlesquid.setObjectName("progression_battlesquid")
        self.gridLayout_2.addWidget(self.progression_battlesquid, 4, 1, 1, 1)
        self.progression_expensive_purchases = QtWidgets.QCheckBox(self.groupBox)
        self.progression_expensive_purchases.setChecked(True)
        self.progression_expensive_purchases.setObjectName("progression_expensive_purchases")
        self.gridLayout_2.addWidget(self.progression_expensive_purchases, 4, 2, 1, 1)
        self.progression_savage_labyrinth = QtWidgets.QCheckBox(self.groupBox)
        self.progression_savage_labyrinth.setObjectName("progression_savage_labyrinth")
        self.gridLayout_2.addWidget(self.progression_savage_labyrinth, 1, 2, 1, 1)
        self.progression_combat_secret_caves = QtWidgets.QCheckBox(self.groupBox)
        self.progression_combat_secret_caves.setObjectName("progression_combat_secret_caves")
        self.gridLayout_2.addWidget(self.progression_combat_secret_caves, 1, 1, 1, 1)
        self.progression_puzzle_secret_caves = QtWidgets.QCheckBox(self.groupBox)
        self.progression_puzzle_secret_caves.setChecked(True)
        self.progression_puzzle_secret_caves.setObjectName("progression_puzzle_secret_caves")
        self.gridLayout_2.addWidget(self.progression_puzzle_secret_caves, 1, 0, 1, 1)
        self.progression_tingle_chests = QtWidgets.QCheckBox(self.groupBox)
        self.progression_tingle_chests.setObjectName("progression_tingle_chests")
        self.gridLayout_2.addWidget(self.progression_tingle_chests, 0, 1, 1, 1)
        self.progression_mail = QtWidgets.QCheckBox(self.groupBox)
        self.progression_mail.setObjectName("progression_mail")
        self.gridLayout_2.addWidget(self.progression_mail, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.race_mode = QtWidgets.QCheckBox(self.groupBox_3)
        self.race_mode.setObjectName("race_mode")
        self.gridLayout_3.addWidget(self.race_mode, 1, 0, 1, 1)
        self.keylunacy = QtWidgets.QCheckBox(self.groupBox_3)
        self.keylunacy.setObjectName("keylunacy")
        self.gridLayout_3.addWidget(self.keylunacy, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_for_num_starting_triforce_shards = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_for_num_starting_triforce_shards.sizePolicy().hasHeightForWidth())
        self.label_for_num_starting_triforce_shards.setSizePolicy(sizePolicy)
        self.label_for_num_starting_triforce_shards.setObjectName("label_for_num_starting_triforce_shards")
        self.horizontalLayout_2.addWidget(self.label_for_num_starting_triforce_shards)
        self.num_starting_triforce_shards = QtWidgets.QComboBox(self.groupBox_3)
        self.num_starting_triforce_shards.setMaximumSize(QtCore.QSize(40, 16777215))
        self.num_starting_triforce_shards.setObjectName("num_starting_triforce_shards")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.horizontalLayout_2.addWidget(self.num_starting_triforce_shards)
        self.widget = QtWidgets.QWidget(self.groupBox_3)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_for_sword_mode = QtWidgets.QLabel(self.groupBox_3)
        self.label_for_sword_mode.setObjectName("label_for_sword_mode")
        self.horizontalLayout_5.addWidget(self.label_for_sword_mode)
        self.sword_mode = QtWidgets.QComboBox(self.groupBox_3)
        self.sword_mode.setObjectName("sword_mode")
        self.sword_mode.addItem("")
        self.sword_mode.addItem("")
        self.sword_mode.addItem("")
        self.horizontalLayout_5.addWidget(self.sword_mode)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_for_randomize_entrances = QtWidgets.QLabel(self.groupBox_3)
        self.label_for_randomize_entrances.setObjectName("label_for_randomize_entrances")
        self.horizontalLayout_8.addWidget(self.label_for_randomize_entrances)
        self.randomize_entrances = QtWidgets.QComboBox(self.groupBox_3)
        self.randomize_entrances.setObjectName("randomize_entrances")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.horizontalLayout_8.addWidget(self.randomize_entrances)
        self.widget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_8.addWidget(self.widget_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 1, 1, 1, 2)
        self.randomize_starting_island = QtWidgets.QCheckBox(self.groupBox_3)
        self.randomize_starting_island.setObjectName("randomize_starting_island")
        self.gridLayout_3.addWidget(self.randomize_starting_island, 2, 1, 1, 1)
        self.randomize_charts = QtWidgets.QCheckBox(self.groupBox_3)
        self.randomize_charts.setObjectName("randomize_charts")
        self.gridLayout_3.addWidget(self.randomize_charts, 2, 0, 1, 1)
        self.randomize_bgm = QtWidgets.QCheckBox(self.groupBox_3)
        self.randomize_bgm.setObjectName("randomize_bgm")
        self.gridLayout_3.addWidget(self.randomize_bgm, 3, 0, 1, 1)
        self.randomize_enemy_palettes = QtWidgets.QCheckBox(self.groupBox_3)
        self.randomize_enemy_palettes.setObjectName("randomize_enemy_palettes")
        self.gridLayout_3.addWidget(self.randomize_enemy_palettes, 2, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.instant_text_boxes = QtWidgets.QCheckBox(self.groupBox_2)
        self.instant_text_boxes.setChecked(True)
        self.instant_text_boxes.setObjectName("instant_text_boxes")
        self.gridLayout_4.addWidget(self.instant_text_boxes, 0, 1, 1, 1)
        self.generate_spoiler_log = QtWidgets.QCheckBox(self.groupBox_2)
        self.generate_spoiler_log.setChecked(True)
        self.generate_spoiler_log.setObjectName("generate_spoiler_log")
        self.gridLayout_4.addWidget(self.generate_spoiler_log, 1, 2, 1, 1)
        self.skip_rematch_bosses = QtWidgets.QCheckBox(self.groupBox_2)
        self.skip_rematch_bosses.setChecked(True)
        self.skip_rematch_bosses.setObjectName("skip_rematch_bosses")
        self.gridLayout_4.addWidget(self.skip_rematch_bosses, 1, 0, 1, 1)
        self.swift_sail = QtWidgets.QCheckBox(self.groupBox_2)
        self.swift_sail.setChecked(True)
        self.swift_sail.setObjectName("swift_sail")
        self.gridLayout_4.addWidget(self.swift_sail, 0, 0, 1, 1)
        self.invert_camera_x_axis = QtWidgets.QCheckBox(self.groupBox_2)
        self.invert_camera_x_axis.setObjectName("invert_camera_x_axis")
        self.gridLayout_4.addWidget(self.invert_camera_x_axis, 2, 0, 1, 1)
        self.add_shortcut_warps_between_dungeons = QtWidgets.QCheckBox(self.groupBox_2)
        self.add_shortcut_warps_between_dungeons.setObjectName("add_shortcut_warps_between_dungeons")
        self.gridLayout_4.addWidget(self.add_shortcut_warps_between_dungeons, 1, 1, 1, 1)
        self.reveal_full_sea_chart = QtWidgets.QCheckBox(self.groupBox_2)
        self.reveal_full_sea_chart.setChecked(True)
        self.reveal_full_sea_chart.setObjectName("reveal_full_sea_chart")
        self.gridLayout_4.addWidget(self.reveal_full_sea_chart, 0, 2, 1, 1)
        self.disable_tingle_chests_with_tingle_bombs = QtWidgets.QCheckBox(self.groupBox_2)
        self.disable_tingle_chests_with_tingle_bombs.setObjectName("disable_tingle_chests_with_tingle_bombs")
        self.gridLayout_4.addWidget(self.disable_tingle_chests_with_tingle_bombs, 2, 1, 1, 1)
        self.remove_title_and_ending_videos = QtWidgets.QCheckBox(self.groupBox_2)
        self.remove_title_and_ending_videos.setChecked(True)
        self.remove_title_and_ending_videos.setObjectName("remove_title_and_ending_videos")
        self.gridLayout_4.addWidget(self.remove_title_and_ending_videos, 2, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(True)
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_for_randomized_gear = QtWidgets.QLabel(self.tab_3)
        self.label_for_randomized_gear.setObjectName("label_for_randomized_gear")
        self.verticalLayout_8.addWidget(self.label_for_randomized_gear)
        self.randomized_gear = QtWidgets.QListView(self.tab_3)
        self.randomized_gear.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.randomized_gear.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.randomized_gear.setObjectName("randomized_gear")
        self.verticalLayout_8.addWidget(self.randomized_gear)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.remove_gear = QtWidgets.QPushButton(self.tab_3)
        self.remove_gear.setMinimumSize(QtCore.QSize(0, 80))
        self.remove_gear.setObjectName("remove_gear")
        self.verticalLayout_7.addWidget(self.remove_gear)
        self.add_gear = QtWidgets.QPushButton(self.tab_3)
        self.add_gear.setMinimumSize(QtCore.QSize(0, 80))
        self.add_gear.setObjectName("add_gear")
        self.verticalLayout_7.addWidget(self.add_gear)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_9.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_for_starting_gear = QtWidgets.QLabel(self.tab_3)
        self.label_for_starting_gear.setObjectName("label_for_starting_gear")
        self.verticalLayout_9.addWidget(self.label_for_starting_gear)
        self.starting_gear = QtWidgets.QListView(self.tab_3)
        self.starting_gear.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.starting_gear.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.starting_gear.setObjectName("starting_gear")
        self.verticalLayout_9.addWidget(self.starting_gear)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.starting_hcs = QtWidgets.QSpinBox(self.tab_3)
        self.starting_hcs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.starting_hcs.setMaximum(6)
        self.starting_hcs.setProperty("value", 0)
        self.starting_hcs.setProperty("displayIntegerBase", 10)
        self.starting_hcs.setObjectName("starting_hcs")
        self.horizontalLayout_10.addWidget(self.starting_hcs)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.starting_pohs = QtWidgets.QSpinBox(self.tab_3)
        self.starting_pohs.setMaximum(44)
        self.starting_pohs.setProperty("value", 0)
        self.starting_pohs.setProperty("displayIntegerBase", 10)
        self.starting_pohs.setObjectName("starting_pohs")
        self.horizontalLayout_10.addWidget(self.starting_pohs)
        self.current_health = QtWidgets.QLabel(self.tab_3)
        self.current_health.setObjectName("current_health")
        self.horizontalLayout_10.addWidget(self.current_health)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.randomize_all_custom_colors_together = QtWidgets.QPushButton(self.tab_2)
        self.randomize_all_custom_colors_together.setObjectName("randomize_all_custom_colors_together")
        self.horizontalLayout_11.addWidget(self.randomize_all_custom_colors_together)
        self.randomize_all_custom_colors_separately = QtWidgets.QPushButton(self.tab_2)
        self.randomize_all_custom_colors_separately.setObjectName("randomize_all_custom_colors_separately")
        self.horizontalLayout_11.addWidget(self.randomize_all_custom_colors_separately)
        self.gridLayout_5.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_for_custom_player_model = QtWidgets.QLabel(self.tab_2)
        self.label_for_custom_player_model.setObjectName("label_for_custom_player_model")
        self.horizontalLayout_3.addWidget(self.label_for_custom_player_model)
        self.custom_player_model = QtWidgets.QComboBox(self.tab_2)
        self.custom_player_model.setObjectName("custom_player_model")
        self.horizontalLayout_3.addWidget(self.custom_player_model)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.player_in_casual_clothes = QtWidgets.QCheckBox(self.tab_2)
        self.player_in_casual_clothes.setObjectName("player_in_casual_clothes")
        self.horizontalLayout_7.addWidget(self.player_in_casual_clothes)
        self.disable_custom_player_voice = QtWidgets.QCheckBox(self.tab_2)
        self.disable_custom_player_voice.setObjectName("disable_custom_player_voice")
        self.horizontalLayout_7.addWidget(self.disable_custom_player_voice)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_5)
        self.custom_model_comment = QtWidgets.QLabel(self.tab_2)
        self.custom_model_comment.setMaximumSize(QtCore.QSize(810, 16777215))
        self.custom_model_comment.setText("")
        self.custom_model_comment.setWordWrap(True)
        self.custom_model_comment.setObjectName("custom_model_comment")
        self.verticalLayout_3.addWidget(self.custom_model_comment)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.custom_colors_layout = QtWidgets.QVBoxLayout()
        self.custom_colors_layout.setObjectName("custom_colors_layout")
        self.verticalLayout_5.addLayout(self.custom_colors_layout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.custom_model_preview_label = QtWidgets.QLabel(self.tab_2)
        self.custom_model_preview_label.setText("")
        self.custom_model_preview_label.setObjectName("custom_model_preview_label")
        self.verticalLayout_6.addWidget(self.custom_model_preview_label)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea)
        self.option_description = QtWidgets.QLabel(self.centralwidget)
        self.option_description.setMinimumSize(QtCore.QSize(0, 32))
        self.option_description.setText("")
        self.option_description.setWordWrap(True)
        self.option_description.setObjectName("option_description")
        self.verticalLayout.addWidget(self.option_description)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.permalink = QtWidgets.QLineEdit(self.centralwidget)
        self.permalink.setObjectName("permalink")
        self.horizontalLayout_4.addWidget(self.permalink)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.update_checker_label = QtWidgets.QLabel(self.centralwidget)
        self.update_checker_label.setOpenExternalLinks(True)
        self.update_checker_label.setObjectName("update_checker_label")
        self.verticalLayout.addWidget(self.update_checker_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setObjectName("about_button")
        self.horizontalLayout.addWidget(self.about_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.reset_settings_to_default = QtWidgets.QPushButton(self.centralwidget)
        self.reset_settings_to_default.setMinimumSize(QtCore.QSize(180, 0))
        self.reset_settings_to_default.setObjectName("reset_settings_to_default")
        self.horizontalLayout.addWidget(self.reset_settings_to_default)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.randomize_button = QtWidgets.QPushButton(self.centralwidget)
        self.randomize_button.setObjectName("randomize_button")
        self.horizontalLayout.addWidget(self.randomize_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Wind Waker Randomizer", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Clean WW ISO", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Output Folder", None, -1))
        self.output_folder_browse_button.setText(QtWidgets.QApplication.translate("MainWindow", "Browse", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Seed (optional)", None, -1))
        self.generate_seed_button.setText(QtWidgets.QApplication.translate("MainWindow", "New seed", None, -1))
        self.clean_iso_path_browse_button.setText(QtWidgets.QApplication.translate("MainWindow", "Browse", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Where Should Progress Items Appear?", None, -1))
        self.progression_platforms_rafts.setText(QtWidgets.QApplication.translate("MainWindow", "Lookout Platforms and Rafts", None, -1))
        self.progression_dungeons.setText(QtWidgets.QApplication.translate("MainWindow", "Dungeons", None, -1))
        self.progression_long_sidequests.setText(QtWidgets.QApplication.translate("MainWindow", "Long Sidequests", None, -1))
        self.progression_short_sidequests.setText(QtWidgets.QApplication.translate("MainWindow", "Short Sidequests", None, -1))
        self.progression_treasure_charts.setText(QtWidgets.QApplication.translate("MainWindow", "Sunken Treasure (From Treasure Charts)", None, -1))
        self.progression_submarines.setText(QtWidgets.QApplication.translate("MainWindow", "Submarines", None, -1))
        self.progression_triforce_charts.setText(QtWidgets.QApplication.translate("MainWindow", "Sunken Treasure (From Triforce Charts)", None, -1))
        self.progression_great_fairies.setText(QtWidgets.QApplication.translate("MainWindow", "Great Fairies", None, -1))
        self.progression_spoils_trading.setText(QtWidgets.QApplication.translate("MainWindow", "Spoils Trading", None, -1))
        self.progression_misc.setText(QtWidgets.QApplication.translate("MainWindow", "Miscellaneous", None, -1))
        self.progression_minigames.setText(QtWidgets.QApplication.translate("MainWindow", "Minigames", None, -1))
        self.progression_free_gifts.setText(QtWidgets.QApplication.translate("MainWindow", "Free Gifts", None, -1))
        self.progression_eye_reef_chests.setText(QtWidgets.QApplication.translate("MainWindow", "Eye Reef Chests", None, -1))
        self.progression_big_octos_gunboats.setText(QtWidgets.QApplication.translate("MainWindow", "Big Octos and Gunboats", None, -1))
        self.progression_battlesquid.setText(QtWidgets.QApplication.translate("MainWindow", "Battlesquid Minigame", None, -1))
        self.progression_expensive_purchases.setText(QtWidgets.QApplication.translate("MainWindow", "Expensive Purchases", None, -1))
        self.progression_savage_labyrinth.setText(QtWidgets.QApplication.translate("MainWindow", "Savage Labyrinth", None, -1))
        self.progression_combat_secret_caves.setText(QtWidgets.QApplication.translate("MainWindow", "Combat Secret Caves", None, -1))
        self.progression_puzzle_secret_caves.setText(QtWidgets.QApplication.translate("MainWindow", "Puzzle Secret Caves", None, -1))
        self.progression_tingle_chests.setText(QtWidgets.QApplication.translate("MainWindow", "Tingle Chests", None, -1))
        self.progression_mail.setText(QtWidgets.QApplication.translate("MainWindow", "Mail", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Additional Randomization Options", None, -1))
        self.race_mode.setText(QtWidgets.QApplication.translate("MainWindow", "Race Mode", None, -1))
        self.keylunacy.setText(QtWidgets.QApplication.translate("MainWindow", "Key-Lunacy", None, -1))
        self.label_for_num_starting_triforce_shards.setText(QtWidgets.QApplication.translate("MainWindow", "Triforce Shards to Start With", None, -1))
        self.num_starting_triforce_shards.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.num_starting_triforce_shards.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.num_starting_triforce_shards.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.num_starting_triforce_shards.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.num_starting_triforce_shards.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "4", None, -1))
        self.num_starting_triforce_shards.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "5", None, -1))
        self.num_starting_triforce_shards.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "6", None, -1))
        self.num_starting_triforce_shards.setItemText(7, QtWidgets.QApplication.translate("MainWindow", "7", None, -1))
        self.num_starting_triforce_shards.setItemText(8, QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.label_for_sword_mode.setText(QtWidgets.QApplication.translate("MainWindow", "Sword Mode", None, -1))
        self.sword_mode.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Start with Sword", None, -1))
        self.sword_mode.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Randomized Sword", None, -1))
        self.sword_mode.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Swordless", None, -1))
        self.label_for_randomize_entrances.setText(QtWidgets.QApplication.translate("MainWindow", "Randomize Entrances", None, -1))
        self.randomize_entrances.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Disabled", None, -1))
        self.randomize_entrances.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Dungeons", None, -1))
        self.randomize_entrances.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Secret Caves", None, -1))
        self.randomize_entrances.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Dungeons & Secret Caves (Separately)", None, -1))
        self.randomize_entrances.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "Dungeons & Secret Caves (Together)", None, -1))
        self.randomize_starting_island.setText(QtWidgets.QApplication.translate("MainWindow", "Randomize Starting Island", None, -1))
        self.randomize_charts.setText(QtWidgets.QApplication.translate("MainWindow", "Randomize Charts", None, -1))
        self.randomize_bgm.setText(QtWidgets.QApplication.translate("MainWindow", "Randomize Background Music", None, -1))
        self.randomize_enemy_palettes.setText(QtWidgets.QApplication.translate("MainWindow", "Randomize Enemy Palettes", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Convenience Tweaks", None, -1))
        self.instant_text_boxes.setText(QtWidgets.QApplication.translate("MainWindow", "Instant Text Boxes", None, -1))
        self.generate_spoiler_log.setText(QtWidgets.QApplication.translate("MainWindow", "Generate Spoiler Log", None, -1))
        self.skip_rematch_bosses.setText(QtWidgets.QApplication.translate("MainWindow", "Skip Boss Rematches", None, -1))
        self.swift_sail.setText(QtWidgets.QApplication.translate("MainWindow", "Swift Sail", None, -1))
        self.invert_camera_x_axis.setText(QtWidgets.QApplication.translate("MainWindow", "Invert Camera X-Axis", None, -1))
        self.add_shortcut_warps_between_dungeons.setText(QtWidgets.QApplication.translate("MainWindow", "Add Shortcut Warps Between Dungeons", None, -1))
        self.reveal_full_sea_chart.setText(QtWidgets.QApplication.translate("MainWindow", "Reveal Full Sea Chart", None, -1))
        self.disable_tingle_chests_with_tingle_bombs.setText(QtWidgets.QApplication.translate("MainWindow", "Tingle Chests Require Non-Tingle Bombs", None, -1))
        self.remove_title_and_ending_videos.setText(QtWidgets.QApplication.translate("MainWindow", "Remove Title and Ending Videos", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Randomizer Settings", None, -1))
        self.label_for_randomized_gear.setText(QtWidgets.QApplication.translate("MainWindow", "Randomized Gear", None, -1))
        self.remove_gear.setText(QtWidgets.QApplication.translate("MainWindow", "<-", None, -1))
        self.add_gear.setText(QtWidgets.QApplication.translate("MainWindow", "->", None, -1))
        self.label_for_starting_gear.setText(QtWidgets.QApplication.translate("MainWindow", "Starting Gear", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Heart Containers", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Heart Pieces", None, -1))
        self.current_health.setText(QtWidgets.QApplication.translate("MainWindow", "Current Starting Health: 3 hearts", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "Starting Items", None, -1))
        self.randomize_all_custom_colors_together.setText(QtWidgets.QApplication.translate("MainWindow", "Randomize Colors Orderly", None, -1))
        self.randomize_all_custom_colors_separately.setText(QtWidgets.QApplication.translate("MainWindow", "Randomize Colors Chaotically", None, -1))
        self.label_for_custom_player_model.setText(QtWidgets.QApplication.translate("MainWindow", "Player Model", None, -1))
        self.player_in_casual_clothes.setText(QtWidgets.QApplication.translate("MainWindow", "Casual Clothes", None, -1))
        self.disable_custom_player_voice.setText(QtWidgets.QApplication.translate("MainWindow", "Disable Custom Voice", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Cosmetic", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Permalink (copy paste to share your settings):", None, -1))
        self.update_checker_label.setText(QtWidgets.QApplication.translate("MainWindow", "Checking for updates to the randomizer...", None, -1))
        self.about_button.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.reset_settings_to_default.setText(QtWidgets.QApplication.translate("MainWindow", "Reset All Settings to Default", None, -1))
        self.randomize_button.setText(QtWidgets.QApplication.translate("MainWindow", "Randomize", None, -1))

