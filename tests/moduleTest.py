# -*- coding:UTF-8 -*-

# region 引入必要依赖
from src.GpsAndMap.MapModule import *

# endregion

地图 = 地图类().添加瓦片.高德地图().智图GeoQ().地图

地图.保存html(目标路径='.')
