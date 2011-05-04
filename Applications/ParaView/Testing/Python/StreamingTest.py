#/usr/bin/env python

import QtTesting
import QtTestingImage

#load streaming view plugin on client and server sides
object1 = 'pqClientMainWindow/menubar'
QtTesting.playCommand(object1, 'activate', 'menuTools')
object2 = 'pqClientMainWindow/menubar/menuTools'
QtTesting.playCommand(object2, 'activate', 'actionManage_Plugins')
object3 = 'pqClientMainWindow/PluginManagerDialog/localGroup/localPlugins'
QtTesting.playCommand(object3, 'setCurrent', 'MantaView')
QtTesting.playCommand(object3, 'setCurrent', 'StreamingView')
object4 = 'pqClientMainWindow/PluginManagerDialog/localGroup'
QtTesting.playCommand(object4, 'mousePress', '1,1,0,152,504')
QtTesting.playCommand(object4, 'mouseRelease', '1,0,0,152,504')
object5 = 'pqClientMainWindow/PluginManagerDialog/localGroup/loadSelected_Local'
QtTesting.playCommand(object5, 'activate', '')
object6 = 'pqClientMainWindow/PluginManagerDialog/buttonBox/1QPushButton0'
QtTesting.playCommand(object6, 'activate', '')

# Test the iterating view by rendering the first 7 pieces
object7 = 'pqClientMainWindow/centralwidget/MultiViewManager/SplitterFrame/MultiViewSplitter/0/MultiViewFrameMenu/CloseAction'
QtTesting.playCommand(object7, 'activate', '')
object8 = 'pqClientMainWindow/centralwidget/MultiViewManager/SplitterFrame/MultiViewSplitter/0/1QWidget0/1QScrollArea0/qt_scrollarea_viewport/EmptyView/ConvertActionsFrame/Iterating View'
QtTesting.playCommand(object8, 'activate', '')
object9 = 'pqClientMainWindow/pqStreamingControls/dockWidgetContents/scrollArea/qt_scrollarea_viewport/scrollAreaWidgetContents/streaming_controls/cache_size'
QtTesting.playCommand(object9, 'set_string', 'no')
object9_5 = 'pqClientMainWindow/pqStreamingControls/dockWidgetContents/scrollArea/qt_scrollarea_viewport/scrollAreaWidgetContents/streaming_controls/number_of_passes'
QtTesting.playCommand(object9_5, 'set_int', '32')
object10 = 'pqClientMainWindow/pqStreamingControls/dockWidgetContents/scrollArea/qt_scrollarea_viewport/scrollAreaWidgetContents/streaming_controls/last_pass'
QtTesting.playCommand(object10, 'set_int', '7')
QtTesting.playCommand(object1, 'activate', 'menuSources')
object11 = 'pqClientMainWindow/menubar/menuSources'
QtTesting.playCommand(object11, 'activate', 'StreamingSource')
object12 = 'pqClientMainWindow/proxyTabDock/proxyTabWidget/qt_tabwidget_stackedwidget/objectInspector/Accept'
QtTesting.playCommand(object12, 'activate', '')
QtTesting.playCommand(object1, 'activate', 'menuFilters')
object13 = 'pqClientMainWindow/menubar/menuFilters/Alphabetical'
QtTesting.playCommand(object13, 'activate', 'DataSetSurfaceFilter')
QtTesting.playCommand(object12, 'activate', '')
object20 = 'pqClientMainWindow/cameraToolbar/actionPositiveZ'
QtTesting.playCommand(object20, 'activate', '')
object21 = 'pqClientMainWindow/centralwidget/MultiViewManager/SplitterFrame/MultiViewSplitter/0/Viewport'
QtTesting.playCommand(object21, 'mousePress', '(0.529061,0.519763,1,1,0)')
QtTesting.playCommand(object21, 'mouseMove', '(0.71237,0.632411,1,0,0)')
QtTesting.playCommand(object21, 'mouseRelease', '(0.71237,0.632411,1,0,0)')
snapshotWidget = 'pqClientMainWindow/centralwidget/MultiViewManager/SplitterFrame/MultiViewSplitter/0/Viewport'
QtTestingImage.compareImage(snapshotWidget, 'IteratingImage.png', 300, 300);

# Test the prioritizing view by making sure the 7 pieces rendered are always nearest camera
QtTesting.playCommand(object7, 'activate', '')
object15 = 'pqClientMainWindow/centralwidget/MultiViewManager/SplitterFrame/MultiViewSplitter/0/1QWidget0/1QScrollArea0/qt_scrollarea_viewport/EmptyView/ConvertActionsFrame/Prioritizing View'
QtTesting.playCommand(object15, 'activate', '')
QtTesting.playCommand(object9, 'set_string', 'no')
QtTesting.playCommand(object9_5, 'set_int', '32')
QtTesting.playCommand(object10, 'set_int', '7')
object16 = 'pqClientMainWindow/pipelineBrowserDock/pipelineBrowser'
QtTesting.playCommand(object16, 'mousePress', '1,1,0,12,13,/0:0/0:0/0:1')
QtTesting.playCommand(object16, 'mouseRelease', '1,0,0,12,13,/0:0/0:0/0:1')
object17 = 'pqClientMainWindow/cameraToolbar/actionNegativeX'
QtTesting.playCommand(object17, 'activate', '')
object18 = 'pqClientMainWindow/cameraToolbar/actionPositiveY'
QtTesting.playCommand(object18, 'activate', '')
object19 = 'pqClientMainWindow/cameraToolbar/actionNegativeY'
QtTesting.playCommand(object19, 'activate', '')
object20 = 'pqClientMainWindow/cameraToolbar/actionPositiveZ'
QtTesting.playCommand(object20, 'activate', '')
object21 = 'pqClientMainWindow/centralwidget/MultiViewManager/SplitterFrame/MultiViewSplitter/0/Viewport'
QtTesting.playCommand(object21, 'mousePress', '(0.529061,0.519763,1,1,0)')
QtTesting.playCommand(object21, 'mouseMove', '(0.71237,0.632411,1,0,0)')
QtTesting.playCommand(object21, 'mouseRelease', '(0.71237,0.632411,1,0,0)')
QtTestingImage.compareImage(snapshotWidget, 'PrioritizingImage.png', 300, 300);

# Test the refining view by refining and coarsening
QtTesting.playCommand(object7, 'activate', '')
object27 = 'pqClientMainWindow/centralwidget/MultiViewManager/SplitterFrame/MultiViewSplitter/0/1QWidget0/1QScrollArea0/qt_scrollarea_viewport/EmptyView/ConvertActionsFrame/Refining View'
QtTesting.playCommand(object27, 'activate', '')
object28 = 'pqClientMainWindow/pqStreamingControls/dockWidgetContents/scrollArea/qt_scrollarea_viewport/scrollAreaWidgetContents/streaming_controls/cache_size'
QtTesting.playCommand(object28, 'set_string', 'no')
object29 = 'pqClientMainWindow/pqStreamingControls/dockWidgetContents/scrollArea/qt_scrollarea_vcontainer/1QScrollBar0'
QtTesting.playCommand(object29, 'mousePress', '1,1,0,7,35')
QtTesting.playCommand(object29, 'mouseMove', '1,0,0,4,88')
QtTesting.playCommand(object29, 'mouseRelease', '1,0,0,4,88')
object30 = 'pqClientMainWindow/pqStreamingControls/dockWidgetContents/scrollArea/qt_scrollarea_viewport/scrollAreaWidgetContents/refinement_controls/refinement_depth'
QtTesting.playCommand(object30, 'set_string', '3')
QtTesting.playCommand(object16, 'mousePress', '1,1,0,12,13,/0:0/0:0/0:1')
QtTesting.playCommand(object16, 'mouseRelease', '1,0,0,12,13,/0:0/0:0/0:1')
object34 = 'pqClientMainWindow/cameraToolbar/actionPositiveZ'
QtTesting.playCommand(object34, 'activate', '')
object35 = 'pqClientMainWindow/centralwidget/MultiViewManager/SplitterFrame/MultiViewSplitter/0/Viewport'
QtTesting.playCommand(object35, 'mousePress', '(0.298063,0.367589,1,1,0)')
QtTesting.playCommand(object35, 'mouseMove', '(0.374069,0.436759,1,0,0)')
QtTesting.playCommand(object35, 'mouseRelease', '(0.374069,0.436759,1,0,0)')
object36 = 'pqClientMainWindow/pqStreamingControls/dockWidgetContents/scrollArea/qt_scrollarea_viewport/scrollAreaWidgetContents/refinement_controls'
QtTesting.playCommand(object36, 'mousePress', '1,1,0,240,52')
QtTesting.playCommand(object36, 'mouseMove', '1,0,0,243,71')
QtTesting.playCommand(object36, 'mouseRelease', '1,0,0,243,71')
QtTesting.playCommand(object29, 'mousePress', '1,1,0,6,94')
QtTesting.playCommand(object29, 'mouseMove', '1,0,0,7,115')
QtTesting.playCommand(object29, 'mouseRelease', '1,0,0,7,115')
object37 = 'pqClientMainWindow/pqStreamingControls/dockWidgetContents/scrollArea/qt_scrollarea_viewport/scrollAreaWidgetContents/refinement_controls/refine'
QtTesting.playCommand(object37, 'activate', '')
QtTesting.playCommand(object37, 'activate', '')
object38 = 'pqClientMainWindow/pqStreamingControls/dockWidgetContents/scrollArea/qt_scrollarea_viewport/scrollAreaWidgetContents/refinement_controls/coarsen'
QtTesting.playCommand(object38, 'activate', '')
QtTesting.playCommand(object37, 'activate', '')
QtTestingImage.compareImage(snapshotWidget, 'RefiningImage.png', 300, 300);
